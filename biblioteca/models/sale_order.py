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
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    lecturas_id=fields.Many2one(comodel_name='biblioteca.libros_lecturas',
                               string='Libros en Lecturas',
                               ondelete='set null')
    
    lector_id=fields.Many2one(related='lecturas_id.partner_id',
                               string='Lector',
                               ondelete='set null')
    
    libros_ids = fields.Many2many(
        string = 'Libros',
        related ='lecturas_id.libros_ids',
    )
    