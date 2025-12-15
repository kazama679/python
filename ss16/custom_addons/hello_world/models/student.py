from odoo import models, fields


class Student(models.Model):
    _name = 'student.management'
    _description = 'Quan ly sinh vien'

    name = fields.Char(string='Tên', required=True)
    age = fields.Integer(string='Tuổi')
    email = fields.Char(string='Email')
    is_active = fields.Boolean(string='Hoạt động', default=True)
