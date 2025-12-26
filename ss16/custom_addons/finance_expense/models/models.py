# -*- coding: utf-8 -*-

from odoo import models, fields, api


class finance_expense(models.Model):
    _name = 'finance.expense'
    _description = 'Finance Expense'

    name = fields.Char(
        string='Nội dung chi tiêu',
        required=True
    )

    expense_type = fields.Selection(
        [
            ('travel', 'Di chuyển'),
            ('food', 'Ăn uống'),
            ('other', 'Khác')
        ],
        string='Loại chi phí',
        default='travel'
    )

    amount = fields.Float(
        string='Số tiền'
    )

    expense_date = fields.Date(
        string='Ngày chi tiêu'
    )

    is_paid = fields.Boolean(
        string='Đã thanh toán',
        default=False
    )

    approval_note = fields.Text(
        string='Ghi chú duyệt chi',
        groups='finance_expense.group_finance_manager'
    )

    active = fields.Boolean(string='Active', default=True)
    # def name_get(self):
    #     result = []
    #     for record in self:
    #         name = f"{record.name} - {record.amount} VND"
    #         result.append((record.id, name))
    #     return result
