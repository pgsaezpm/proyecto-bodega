from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Parcela(models.Model):
    _name = 'pgs_bodega.parcela'
    _description = 'Bodega (Parcela)'

    id_parcela = fields.Char (string='ID parcela', required=True)
    nombre = fields.Char(string='Nombre parcela', required=True)
    viticultor_propietario = fields.Many2one('res.partner',string='Viticultor propietario',domain=[('es_viticultor', '=', True)])
    provincia = fields.Many2one('res.country.state',string='Provincia',domain="[('country_id.code','=','ES')]")
    localidad = fields.Many2one('localidades_espana',string='Localidad')
    tamanio_hectareas = fields.Float(string='Tamaño hectáreas',digits=(10,2))
    variedad_uva = fields.Many2one('pgs_bodega.variedad_uva',string='Variedad de uva', required=True)

    _sql_constraints = [('id_parcela_unico','unique(id_parcela)','El id de la parcela ya existe')]

    #Cambiar el campo titulo del modulo
    # @api.depends('nombre')
    # def _compute_display_name(self):
    #     for record in self:
    #         record.display_name = f"{record.codigo} - {record.descripcion}"
    # 