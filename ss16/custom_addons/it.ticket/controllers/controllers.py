# -*- coding: utf-8 -*-
# from odoo import http


# class It.ticket(http.Controller):
#     @http.route('/it.ticket/it.ticket', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/it.ticket/it.ticket/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('it.ticket.listing', {
#             'root': '/it.ticket/it.ticket',
#             'objects': http.request.env['it.ticket.it.ticket'].search([]),
#         })

#     @http.route('/it.ticket/it.ticket/objects/<model("it.ticket.it.ticket"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('it.ticket.object', {
#             'object': obj
#         })

