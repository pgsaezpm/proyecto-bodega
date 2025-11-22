from odoo import models, fields, api
from odoo.exceptions import ValidationError

class VariedadUva(models.Model):
    _name = 'pgs_bodega.variedad_uva'
    _description = 'Módulo (Variedad uva)'

    id_variedad = fields.Char (string='Id variedad', required=True)
    nombre_variedad = fields.Selection([
        ('tempranillo','Tempranillo'),
        ('albillo','Albillo'),
        ('godello','Godello'),
        ('mencia','Mencía'),
    ], string="Nombre de variedad")
    denominacion_origen = fields.Many2many('pgs_bodega.denominacion_origen',string='Denominacion origen')
    rendimiento_denominacion_origen = fields.Integer(string='Rendimiento denominacion de origen')
    #Domain para que filtre y solo muestre los productos que sean del tipo adecuado
    producto_inicial1 = fields.Many2one('product.product',string='Producto uva',domain=[('product_tmpl_id.tipo_producto', '=', 'uva')])
    producto_sig_inicial2 = fields.Many2one('product.product',string='Producto pasta',domain=[('product_tmpl_id.tipo_producto', '=', 'pasta')])
    producto_sig3 = fields.Many2one('product.product',string='Producto mosto',domain=[('product_tmpl_id.tipo_producto', '=', 'mosto')])
    parcela = fields.One2many('pgs_bodega.parcela','variedad_uva',string='Parcela')
    grado_brix = fields.Float(string='Grado brix')
    grado_probable = fields.Float(string='Grado probable de alcohol',compute='_calcular_grado_probable')
    registro_albaran = fields.Many2many('pgs_bodega.registro_albaran',string="Parcelas asignadas")
    

    _sql_constraints = [('id_variedad_uniq','unique(id_variedad)','El id de variedad ya existe')]

    @api.constrains('producto_inicial1')
    def _check_productos(self):
        for record in self:
            if not record.producto_inicial1 or not record.producto_sig_inicial2 or not record.producto_sig3:
                raise ValidationError("Todos los productos deben estar definidos.")

    @api.constrains('nombre_variedad')
    def _check_nombre_variedad(self):
        for record in self:
            if not record.nombre_variedad:
                raise ValidationError("Debes rellenar el campo nombre")

    @api.depends('grado_brix')
    def _calcular_grado_probable(self):
        for record in self:
            record.grado_probable = 0.6757 * record.grado_brix - 2.0839

    #Cambiar el campo titulo del modulo
    @api.depends('id_variedad','nombre_variedad')
    def _compute_display_name(self):
        for record in self:
            if record.id_variedad and record.nombre_variedad:
                record.display_name = f"{record.id_variedad}, ({record.nombre_variedad})"
            else:
                record.display_name = 'Sin nombre'