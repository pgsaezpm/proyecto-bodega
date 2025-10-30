from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Parcela(models.Model):
    _name = 'pgs_bodega.parcela'
    _description = 'Bodega (Parcela)'

    id_parcela = fields.Char (string='ID parcela', required=True)
    nombre = fields.Char(string='Nombre parcela')
    # viticultor_propietario = fields.One2many('pgs_bodega.proveedor_viticultor','parcelas',string='Id viticultor',domain=[('product_tmpl_id.tipo_producto', '=', 'uva')])
    provincia = fields.Many2one('res.country.state',string='Provincia',domain="[('country_id.code','=','ES')]")
    # localidad = fields.Many2one('res.country.state',string='Provincia',domain="[('country_id.code','=','ES')]")
    tamanio_hectareas = fields.Float(string='Tamaño hectáreas',digits=(10,2))
    # variedad_uva = fields.Many2one('pgs_bodega.variedad_uva',string='Variedad de uva')

    _sql_constraints = [('id_parcela_unico','unique(id_parcela)','El id de la parcela ya existe')]