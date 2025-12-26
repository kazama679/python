from odoo import models, fields

class HotelRoomType(models.Model):
    _name = 'hotel.room.type'
    _description = 'Hotel Room Type'

    name = fields.Char(string='Type Name', required=True)
    code = fields.Char(string='Code')
