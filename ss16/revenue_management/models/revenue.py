from odoo import models, fields, api


class Revenue(models.Model):
    _name = 'finance.revenue'
    _description = 'Revenue'

    date = fields.Date(string='Date', required=True)
    amount = fields.Float(string='Amount', required=True)
    description = fields.Text(string='Description')

    @api.model
    def total_by_date(self, date):
        records = self.search([('date', '=', date)])
        return sum(records.mapped('amount'))
