from odoo import models, fields, api
from odoo.exceptions import ValidationError

class DenominacionOrigen(models.Model):
    _name = 'pgs_bodega.denominacion_origen'
    _description = 'Bodega (Denominación Origen)'

    id_denominacion = fields.Char (string='ID denominacion de origen', required=True)
    nombre = fields.Char(string='Nombre denominacion origen', required=True)
    variedad_uva = fields.Many2many('pgs_bodega.variedad_uva',string='Variedad de uva')

    _sql_constraints = [('id_denominacion_uniq','unique(id_denominacion)','El id de denominación de origen ya existe')]

    #Cambiar el campo titulo del modulo
    @api.depends('nombre')
    def _compute_display_name(self):
        for record in self:
            if record.nombre:
                record.display_name = f"{record.nombre}"
            else:
                record.display_name = 'Sin nombre'