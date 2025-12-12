from odoo import models, fields


class ProductManagement(models.Model):
    _name = 'product.management'
    _description = 'Product Management'

    product_name = fields.Char(string='Product Name', required=True)
    product_price = fields.Float(string='Price', default=0.0)
    product_quantity = fields.Integer(string='Quantity', default=0)
