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
class ProductTemplate(models.Model):
    _inherit = 'product.template'
    is_lectura_product = fields.Boolean(string="Usar Lector como Producto", 
                                        help="Indica si las Lecturas son Productos",
                                       default=False)
    
    