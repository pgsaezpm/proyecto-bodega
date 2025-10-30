from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProveedorViticultor(models.Model):
    _inherit = 'res.partner'

    es_viticultor = fields.Boolean(string='Es viticultor')
    # parcelas = fields.Many2one('pgs_bodega.parcela',string='Es viticultor')
