# -*- coding: utf-8 -*-
# from odoo import http


# class Biblioteca(http.Controller):
#     @http.route('/biblioteca/biblioteca/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/biblioteca/biblioteca/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('biblioteca.listing', {
#             'root': '/biblioteca/biblioteca',
#             'objects': http.request.env['biblioteca.biblioteca'].search([]),
#         })

#     @http.route('/biblioteca/biblioteca/objects/<model("biblioteca.biblioteca"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('biblioteca.object', {
#             'object': obj
#         })
