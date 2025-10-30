from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductoUva(models.Model):
    _inherit = 'product.template'

    es_producto_uva = fields.Boolean(string='Producto de uva')
    tipo_producto = fields.Selection([
        ('uva','Uva'),
        ('pasta','Pasta'),
        ('mosto','Mosto'),
    ], string="Tipo de producto de uva")
