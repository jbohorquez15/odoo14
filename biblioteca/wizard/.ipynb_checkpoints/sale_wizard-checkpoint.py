# -*- coding: utf-8 -*-
from odoo import models, fields, api
class SaleWizard(models.TransientModel):
    _name='biblioteca.wizard'
    _description='Para Generar Ventas desde los Prestamos'
    def _default_lecturas(self):
        return self.env['biblioteca.libros_lecturas'].browse(self._context.get('active_id'))
    
    lecturas_id = fields.Many2one(
        comodel_name = 'biblioteca.libros_lecturas',
        string   ='Libros Prestados',
        required = True,
        default = _default_lecturas )
    
    libros_lecturas_ids = fields.Many2many(
        comodel_name = 'biblioteca.libros',
        string   ='Lectores',
        related  ='lecturas_id.libros_ids',
        help = 'Lectores Activos'
    )
    
    libros_ids = fields.Many2many(
        comodel_name = 'biblioteca.libros',
        string   ='Libros Disponibles'
    )
    
    
    lectores_facturas_ids = fields.One2many(
        comodel_name = 'res.partner',
        string   ='Lectores para la Factura',
        related  ='lecturas_id.partner_id',
    )
    
    
    
    
    def create_sale_order(self):
        lecturas_productos_id = self.env['product.product'].search([('is_lectura_product','=',True)], limit=1)
        if lecturas_productos_id:
            for libros in self.libros_lecturas_ids:
                order_id = self.env['sale.order'].create({
                    'partner_id':self.lectores_facturas_ids,
                    'lectura_id':self.lecturas_id,
                    'order_line':[(0,0,{'product_id':lecturas_productos_id.id,'price_unit':libros.precio_total})]
                })