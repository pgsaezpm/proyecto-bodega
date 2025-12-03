from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Trabajo(models.Model):
    _name = 'pgs_bodega.trabajo'
    _description = 'Bodega (Tipo de Trabajo)'

    id_trabajo = fields.Char (string='ID de trabajo', required=True)
    descripcion = fields.Text(string='Descripcion del trabajo', required=True)
    tipo_trabajo = fields.Selection([
        ('campo','Campo'),
        ('bodega','Bodega'),
        ('produccion','Produccion'),
    ], string="Tipo de trabajo")
    movimiento = fields.One2many('pgs_bodega.movimientos','trabajo',String='Movimiento')

    _sql_constraints = [('id_trabajo','unique(id_trabajo)','El id de trabajo ya existe')]

    @api.depends('descripcion','tipo_trabajo')
    def _compute_display_name(self):
        for record in self:
            if record.descripcion and record.tipo_trabajo:
                record.display_name = f"{record.descripcion}, ({record.tipo_trabajo})"
            else:
                record.display_name = 'Sin nombre'