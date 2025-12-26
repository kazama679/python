# -*- coding: utf-8 -*-
{
    'name': "Recruitment Simple",
    'summary': "Module quản lý hồ sơ ứng viên",
    'description': """
        Module Hồ sơ ứng viên
        ====================
        
        Quản lý danh sách ứng viên nộp đơn xin việc với các tính năng:
        * Lưu trữ thông tin ứng viên chi tiết
        * Phân quyền theo vai trò (Recruiter, Manager, Customer)
        * Bảo mật thông tin nhạy cảm
        
    """,
    'author': "Your Company",
    'website': "http://www.yourcompany.com",
    'category': 'Human Resources',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/hr_groups.xml',
        'security/hr_rules.xml',
        'security/ir.model.access.csv',
        'views/hr_candidate_views.xml',
        'views/hr_candidate_menu.xml',
    ],
    'installable': True,
    'application': True,
}
