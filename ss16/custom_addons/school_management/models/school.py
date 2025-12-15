from odoo import models, fields


class School(models.Model):
    _name = 'school.school'
    _description = 'School'

    name = fields.Char(string='Name', required=True)
    location = fields.Char(string='Location')
    start_date = fields.Date(string='Start Date')
