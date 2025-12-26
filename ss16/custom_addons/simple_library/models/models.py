# -*- coding: utf-8 -*-

from odoo import models, fields, api


# ==================== MODEL VỆ TINH 1: THỂ LOẠI SÁCH ====================
class LibraryCategory(models.Model):
    _name = 'library.category'
    _description = 'Thể loại sách'

    name = fields.Char(string='Tên thể loại', required=True)


# ==================== MODEL VỆ TINH 2: TÁC GIẢ ====================
class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Tác giả'

    name = fields.Char(string='Tên tác giả', required=True)
    bio = fields.Text(string='Tiểu sử')


# ==================== MODEL VỆ TINH 3: LỊCH SỬ MƯỢN TRẢ ====================
class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Lịch sử mượn trả sách'

    borrower_name = fields.Char(string='Tên người mượn', required=True)
    borrow_date = fields.Date(
        string='Ngày mượn', default=fields.Date.today, required=True)
    return_date = fields.Date(string='Ngày trả')
    is_returned = fields.Boolean(string='Đã trả', default=False)
    book_id = fields.Many2one(
        'library.book', string='Sách', ondelete='cascade')


# ==================== MODEL CHÍNH: SÁCH ====================
class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Quản lý sách thư viện'

    # Thông tin cơ bản
    name = fields.Char(string='Tên sách', required=True)
    isbn = fields.Char(string='Mã ISBN')

    # Trạng thái và tình trạng sách
    state = fields.Selection([
        ('draft', 'Mới nhập'),
        ('available', 'Có sẵn'),
        ('borrowed', 'Đang mượn'),
        ('lost', 'Đã mất')
    ], string='Trạng thái', default='draft')

    condition = fields.Selection([
        ('0', 'Kém'),
        ('1', 'Trung bình'),
        ('2', 'Tốt'),
        ('3', 'Mới')
    ], string='Độ mới sách', default='2')

    # Thông tin mật (chỉ Librarian thấy)
    purchase_price = fields.Integer(
        string='Giá nhập sách',
        groups='simple_library.group_library_librarian'
    )

    # Relationships
    category_id = fields.Many2one('library.category', string='Thể loại')
    author_ids = fields.Many2many('library.author', string='Tác giả')
    loan_ids = fields.One2many(
        'library.loan', 'book_id', string='Lịch sử mượn trả')
