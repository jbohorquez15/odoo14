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
    precio_base = fields.Float (string="Precio Base", default=0.00)
    tarifa_adicional = fields.Float (string="Tarifa Adicional", default=10.00)
    precio_total = fields.Float (string="Total Precio", readonly=True)
    
    lectores_ids = fields.Many2many(
        comodel_name = 'res.partner',
        relation ='libros_partner_rel',
        column1  ='libros_id',
        column2  ='partner_id',
        string   ='Lectores',
    )
    
    @api.onchange('precio_base','tarifa_adicional')
    def _onchange_precio_total(self):
        if self.precio_base<0.00:
            raise UserError('Precio Base no puede ser Negativo')
        self.precio_total=self.precio_base + self.tarifa_adicional
    
    @api.constrains('tarifa_adicional')
    def _check_precio_adicional(self):
        for record in self:
            if record.tarifa_adicional<10.00:
                 raise ValidationError('Tarifa Adicional no puede ser mayor que 10:%s' %record.tarifa_adicional)
                
    