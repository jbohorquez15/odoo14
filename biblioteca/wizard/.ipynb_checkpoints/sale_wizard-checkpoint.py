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
        requiered = True,
        default = _default_lecturas )
    
    lectores_lecturas_ids = fields.Many2many(
        comodel_name = 'res.partner',
        string   ='Lectores',
        related  ='lecturas_id.libros_ids',
        help = 'Lectores Activos'
    )
    lectores_facturas_ids = fields.Many2many(
        comodel_name = 'res.partner',
        string   ='Lectores para la Factura'
    )
    
    def create_sale_order(self):
        lecturas_productos_id = self.env['product.product'].search([('is_lectura_product','=',True)], limit=1)
        if lecturas_productos_id:
            for lectores in self.lectores_facturas_ids:
                order_id = self.env['sale.orer'].create({
                    'partner_id':lectores.id,
                    'lectura_id':self.lecturas_id,
                    'order_line':[(0,0,{'product_id':lecturas_productos_id.id,'price_unit':lecturas_id.total_precio})]
                })