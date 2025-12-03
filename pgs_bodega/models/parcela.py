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
    variedad_uva = fields.Many2one('pgs_bodega.variedad_uva',string='Variedad de uva')
    registro_albaran = fields.Many2many('pgs_bodega.registro_albaran',string="Parcelas asignadas")
    numero_cepas = fields.Integer(string="Numero de cepas")
    poligono = fields.Char(string="Numero de polígono")
    info_catastral = fields.Char(string="Informacion catastral",compute='_calcular_info_catastral')

    _sql_constraints = [('id_parcela_unico','unique(id_parcela)','El id de la parcela ya existe')]

    #Cambiar el campo titulo del modulo
    @api.depends('id_parcela','poligono','localidad')
    def _calcular_info_catastral(self):
        for record in self:
            if record.id_parcela and record.localidad and record.poligono:
                record.info_catastral = f"{record.localidad.CPRO} {record.localidad.CMUN} {record.poligono} {record.id_parcela}"
            else:
                record.info_catastral = 0

    @api.depends('nombre','viticultor_propietario')
    def _compute_display_name(self):
        for record in self:
            if record.nombre and record.viticultor_propietario.display_name:
                record.display_name = f"{record.nombre}, ({record.viticultor_propietario.display_name})"
            else:
                record.display_name = 'Sin nombre'


    # @api.onchange('provincia')
    # @api.onchange('provincia')
    # def _onchange_provincia_set_domain(self):
    #     self.localidad = False
        
    #     if not self.provincia:
    #         return {'domain': {'localidad': []}}

    #     val = self.provincia.code
    #     print("FILTRANDO LOCALIDADES POR:", val)
        
    #     return {
    #         'domain': {
    #             'localidad': [('provcode', '=', val)]
    #         }
    #     }