from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Property Name', required=True)
    address = fields.Char(string='Address')
    customer_id = fields.Many2one('estate.customer', string='Customer')
