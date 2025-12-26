from odoo import models, fields


class HotelService(models.Model):
    _name = 'hotel.service'
    _description = 'Hotel Service'

    name = fields.Char(string='Service Name', required=True)
    price = fields.Integer(string='Price')
