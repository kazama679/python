from odoo import models, fields


class BookstoreBook(models.Model):
    _name = 'bookstore.book'
    _description = 'Book'

    title = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    price = fields.Float(string='Price', default=0.0)
    publish_date = fields.Date(string='Publish Date')
