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
from odoo.exceptions import UserError, ValidationError
class ResPartner(models.Model):
    _inherit = 'res.partner'
   
    libros_ids = fields.Many2many(
        comodel_name = 'biblioteca.libros',
        relation ='libros_partner_rel',
        column1  ='partner_id',
        column2  ='libros_id',
        string   ='Libros',     
    )
    