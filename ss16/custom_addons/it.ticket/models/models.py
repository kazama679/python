# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class it.ticket(models.Model):
#     _name = 'it.ticket.it.ticket'
#     _description = 'it.ticket.it.ticket'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

