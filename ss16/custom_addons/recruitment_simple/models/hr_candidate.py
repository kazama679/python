# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrCandidate(models.Model):
    _name = 'hr.candidate'
    _description = 'Hồ sơ ứng viên'
    _order = 'name asc'

    # Tên ứng viên (Bắt buộc)
    name = fields.Char(
        string='Tên ứng viên',
        required=True,
        help='Họ và tên đầy đủ của ứng viên'
    )

    # Giới tính
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác')
    ], string='Giới tính', help='Giới tính của ứng viên')

    # Ngày sinh
    birthday = fields.Date(
        string='Ngày sinh',
        help='Ngày tháng năm sinh của ứng viên'
    )

    # Nội dung CV tóm tắt
    cv_content = fields.Text(
        string='Nội dung CV',
        help='Tóm tắt nội dung CV và kinh nghiệm của ứng viên'
    )

    # Lương mong muốn
    expected_salary = fields.Integer(
        string='Lương mong muốn',
        help='Mức lương mà ứng viên mong muốn (VND)'
    )

    # Đã tuyển chưa?
    is_hired = fields.Boolean(
        string='Đã tuyển',
        default=False,
        help='Đánh dấu ứng viên đã được tuyển hay chưa'
    )

    # Trạng thái ứng viên
    state = fields.Selection([
        ('new', 'Ứng viên mới'),
        ('reviewing', 'Đang xem xét'),
        ('interviewed', 'Đã phỏng vấn'),
        ('hired', 'Đã tuyển'),
        ('rejected', 'Từ chối')
    ], string='Trạng thái', default='new', help='Trạng thái hiện tại của ứng viên')

    # Đánh giá của Sếp (Chỉ Manager mới thấy)
    manager_note = fields.Text(
        string='Đánh giá nội bộ',
        groups='recruitment_simple.group_hr_manager',
        help='Đánh giá nội bộ về ứng viên - chỉ Manager mới được xem'
    )

    # Thêm một số fields hệ thống hữu ích
    active = fields.Boolean(string='Active', default=True)

    def name_get(self):
        """Hiển thị tên ứng viên trong selection"""
        result = []
        for record in self:
            name = record.name
            if record.expected_salary:
                name += f' (Lương: {record.expected_salary:,} VND)'
            result.append((record.id, name))
        return result

    def action_hire(self):
        """Đánh dấu ứng viên đã được tuyển"""
        for record in self:
            record.is_hired = True
            record.state = 'hired'
        return True
