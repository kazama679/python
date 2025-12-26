from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
from datetime import timedelta
from odoo.exceptions import ValidationError
from odoo import api

class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Hotel Booking'

    code = fields.Char(string='Booking Code')

    check_in = fields.Date(
        string='Check-in Date',
        default=fields.Date.today
    )

    check_out = fields.Date(string='Check-out Date')

    duration = fields.Integer(
        string='Duration (Nights)',
        compute='_compute_duration',
        store=True
    )

    total_amount = fields.Integer(
        string='Total Amount',
        compute='_compute_total_amount',
        store=True
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done')
        ],
        default='draft'
    )

    customer_id = fields.Many2one(
        'hotel.customer',
        string='Customer',
        required=True
    )

    room_id = fields.Many2one(
        'hotel.room',
        string='Room',
        required=True
    )

    service_ids = fields.Many2many(
        'hotel.service',
        string='Services'
    )

    @api.depends('check_in', 'check_out')
    def _compute_duration(self):
        for record in self:
            if record.check_in and record.check_out:
                days = (record.check_out - record.check_in).days
                record.duration = max(days, 0)
            else:
                record.duration = 0

    @api.depends('duration', 'room_id', 'service_ids')
    def _compute_total_amount(self):
        for record in self:
            room_cost = record.duration * record.room_id.price_per_night if record.room_id else 0
            service_cost = sum(record.service_ids.mapped('price'))
            record.total_amount = room_cost + service_cost

    @api.constrains('check_in', 'check_out')
    def _check_date_valid(self):
        for record in self:
            if record.check_in and record.check_out:
                if record.check_out <= record.check_in:
                    raise ValidationError(
                        'Check-out date must be after check-in date.')

    @api.depends('check_in', 'check_out')
    def _compute_duration(self):
        for record in self:
            if record.check_in and record.check_out:
                delta = (record.check_out - record.check_in).days
                record.duration = max(delta, 0)
            else:
                record.duration = 0

    @api.depends('duration', 'room_id', 'service_ids')
    def _compute_total_amount(self):
        for record in self:
            room_cost = record.duration * record.room_id.price_per_night if record.room_id else 0
            service_cost = sum(record.service_ids.mapped('price'))
            record.total_amount = room_cost + service_cost

    @api.onchange('room_id')
    def _onchange_room_id(self):
        if self.room_id and self.room_id.status == 'maintenance':
            return {
                'warning': {
                    'title': 'Warning',
                    'message': 'Phòng này đang bảo trì, vui lòng chọn phòng khác!'
                }
            }

    @api.onchange('check_in')
    def _onchange_check_in(self):
        if self.check_in:
            self.check_out = self.check_in + timedelta(days=1)


    @api.constrains('check_in', 'check_out')
    def _check_booking_dates(self):
        for record in self:
            if record.check_in and record.check_out:
                if record.check_out <= record.check_in:
                    raise ValidationError('Ngày trả phòng không hợp lệ!')

    @api.constrains('room_id')
    def _check_room_available(self):
        for record in self:
            if record.room_id and record.room_id.status == 'occupied':
                raise ValidationError('Phòng này đang có khách ở!')
