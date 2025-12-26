from odoo import models, fields

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'

    name = fields.Char(string='Room Number', required=True)
    floor = fields.Integer(string='Floor')
    price_per_night = fields.Integer(string='Price per Night')

    status = fields.Selection(
        [
            ('available', 'Available'),
            ('occupied', 'Occupied'),
            ('maintenance', 'Maintenance')
        ],
        string='Status',
        default='available'
    )

    type_id = fields.Many2one(
        'hotel.room.type',
        string='Room Type'
    )
    _sql_constraints = [
        ('unique_room_name', 'unique(name)', 'Tên phòng đã tồn tại!')
    ]
    _sql_constraints = [
        ('check_room_price_positive', 'CHECK(price_per_night > 0)', 'Giá phòng phải lớn hơn 0!')
    ]
    _sql_constraints = [
        ('check_service_price_positive', 'CHECK(price > 0)', 'Giá dịch vụ phải lớn hơn 0!')
    ]

