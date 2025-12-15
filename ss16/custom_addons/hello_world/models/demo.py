from odoo import models, fields


class Demo(models.Model):
    _name = 'demo.hello'
    _description = 'CSDL danh cho viec demo'

    name = fields.Char(string='Ten', required=True)
    description = fields.Text(string='Mo ta')
