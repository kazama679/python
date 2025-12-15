from odoo import models, fields


class EstateCustomer(models.Model):
    _name = 'estate.customer'
    _description = 'Customer'

    name = fields.Char(string='Name', required=True)
    property_ids = fields.One2many(
        'estate.property', 'customer_id', string='Properties')
