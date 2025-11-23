from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Deposito(models.Model):
    _name = 'pgs_bodega.deposito'
    _description = 'Bodega (Deposito)'

    id_deposito = fields.Char (string='ID deposito', required=True)
    nombre = fields.Char(string='Nombre deposito', required=True)
    capacidad = fields.Integer(string='Capacidad deposito en Kg')
    tipo_producto = fields.Selection([
        ('uva','Uva'),
        ('pasta','Pasta'),
        ('mosto','Mosto'),
    ], string="Tipo de producto que almacena")
    producto = fields.Many2one('product.product',string='Producto')

    _sql_constraints = [('id_deposito','unique(id_deposito)','El id de deposito ya existe')]

    #Cambiar el campo titulo del modulo
    @api.depends('nombre')
    def _compute_display_name(self):
        for record in self:
            if record.nombre:
                record.display_name = f"{record.nombre}"
            else:
                record.display_name = 'Sin nombre'