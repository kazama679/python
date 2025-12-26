# -*- coding: utf-8 -*-
{
    'name': "Simple Library - Quản lý Thư viện",

    'summary': "Module quản lý thư viện trường học: Sách, Tác giả, Thể loại và Lịch sử mượn trả",

    'description': """
        Module Quản lý Thư viện Trường học
        ====================================
        
        Tính năng chính:
        - Quản lý đầu sách (Tên, ISBN, Trạng thái, Độ mới)
        - Quản lý tác giả và thể loại sách
        - Theo dõi lịch sử mượn trả sách
        - Phân quyền: Student (Chỉ xem) và Librarian (Quản lý toàn bộ)
        - Bảo mật field-level: Giá nhập sách chỉ Librarian thấy
        
        Bài tập Odoo: Simple Library Management System
    """,

    'author': "Your Name",
    'website': "https://www.yourcompany.com",

    'category': 'Services',
    'version': '1.0',

    # Module phụ thuộc
    'depends': ['base'],

    # Dữ liệu luôn được load
    'data': [
        # Security
        'security/library_security.xml',
        'security/ir.model.access.csv',
        
        # Views
        'views/library_views.xml',
        'views/library_menu.xml',
    ],
    
    # Demo data (optional)
    'demo': [],
    
    # Cài đặt module
    'installable': True,
    'application': True,
    'auto_install': False,
}


