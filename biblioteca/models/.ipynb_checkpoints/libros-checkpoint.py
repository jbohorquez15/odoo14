# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class biblioteca(models.Model):
#     _name = 'biblioteca.biblioteca'
#     _description = 'biblioteca.biblioteca'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api
class libros(models.Model):
    _name = 'biblioteca.libros'
    _description = 'Libros Disponibles' 
    name = fields.Char(string ='Nombre', required=True)
    descripcion = fields.Text(string='Descripcion del Libro')
    categoria = fields.Selection(string='Categoria',
                                selection =[
                                    ('ciencias','Ciencias'),
                                    ('matematicas','Matematicas'),
                                    ('geografia','Geografia'),
                                    ('fisica','Fisica')
                                ], copy=False )
    active = fields.Boolean (string='Activo', default=True)
    