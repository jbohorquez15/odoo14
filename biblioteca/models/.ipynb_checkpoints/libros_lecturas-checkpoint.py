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
from datetime import timedelta

class libros_lecturas(models.Model):
    _name = 'biblioteca.libros_lecturas'
    _description = 'Libros que se estan Leyendo' 
    libros_ids=fields.One2many(comodel_name='biblioteca.libros',
                            inverse_name='lecturas_id',
                             string="Libros",
                              required=True
                             )
    
    name = fields.Text(string='Descripcion del Prestamo')
    #partner_id = fields.Many2one()
    
    partner_id = fields.Many2one(
        comodel_name = 'res.partner',
        string   ='Leector',
    )
    
    fecha_inicio=fields.Date(string='Fecha de Inicio', default=fields.Date.today)
    duracion = fields.Integer(string='Dias a Leer', default=1)
    fecha_fin=fields.Date(string='Fecha de de Terminacion',compute='_compute_fecha_fin', inverse='_inverse_fecha_fin', store=True)
    
    @api.depends('fecha_inicio', 'duracion')
    def _compute_fecha_fin(self):
        for record in self:
            if not (record.fecha_inicio and record.duracion):
                record.fecha_fin = record.fecha_inicio
            else:
                duracion=timedelta(days=record.duracion)
                record.fecha_fin=record.fecha_inicio+duracion
    def _inverse_fecha_fin (self):
        for record in self:
            if record.fecha_inicio and record.fecha_fin:
                record.duracion = (record.fecha_fin-record.fecha_inicio).days+1
            else:
                continue
                
                