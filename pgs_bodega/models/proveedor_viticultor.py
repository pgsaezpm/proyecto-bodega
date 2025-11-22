from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProveedorViticultor(models.Model):
    _inherit = 'res.partner'

    es_viticultor = fields.Boolean(string='Es viticultor')
    parcelas = fields.One2many('pgs_bodega.parcela','viticultor_propietario',string="Parcelas asignadas")
    registro_albaran = fields.Many2many('pgs_bodega.registro_albaran',string="Parcelas asignadas")
