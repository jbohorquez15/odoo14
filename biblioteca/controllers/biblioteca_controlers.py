# -*- coding: utf-8 -*-

from odoo import http


class Biblioteca(http.Controller):
    @http.route('/biblioteca/', auth='public', website=True)
    def index(self, **kw):
        return "Hello, world"

    @http.route('/biblioteca/libros/', auth='public', website=True)
    def list(self, **kw):
        libros = http.request.env['biblioteca.libros'].search([])
        return http.request.render('biblioteca.libros_website', {
             'libros': libros,
         })
    @http.route('/biblioteca/<model("biblioteca.libros_lecturas"):lecturas>/', auth='public')
    def list(self,lecturas):
         return http.request.render('biblioteca.lecturas_website', {
             'lecturas': lecturas,
         })
        
#         return http.request.render('biblioteca.listing', {
#             'root': '/biblioteca/biblioteca',
#             'objects': http.request.env['biblioteca.biblioteca'].search([]),
#         })

#     @http.route('/biblioteca/biblioteca/objects/<model("biblioteca.biblioteca"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('biblioteca.object', {
#             'object': obj
#         })
