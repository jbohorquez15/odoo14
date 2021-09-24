# -*- coding: utf-8 -*-
from odoo import api, models

class LecturasReport(models.AbstractModel):
    _name = 'report.bibioteca.report_lecturas_document'

    def _get_report_values(self, docids, data=None):
        report = self.env['ir.actions.report']._get_report_from_name('odoo_academy.report_session_document')
        docs = self.env[report.model].browse(docids)
        products = self.env['product.template'].search([('is_session_product', '=', True)])
        return {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': docs,
            'products': products,
        }