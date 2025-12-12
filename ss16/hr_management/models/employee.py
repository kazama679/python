from odoo import models, fields, api


class HRManagementEmployee(models.Model):
    _name = 'hr.management.employee'
    _description = 'Simple Employee'

    employee_name = fields.Char(string='Name', required=True)
    employee_status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string='Status', default='active', required=True)

    # extended fields from later requirement
    position = fields.Selection([
        ('staff', 'Staff'),
        ('manager', 'Manager'),
        ('intern', 'Intern')
    ], string='Position', default='staff')
    salary = fields.Float(string='Salary', default=1000.0)
    start_date = fields.Date(
        string='Start Date', default=fields.Date.context_today)
