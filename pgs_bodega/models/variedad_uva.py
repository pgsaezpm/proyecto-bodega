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
    denominacion_origen = fields.One2many('pgs_bodega.denominacion_origen','variedad_uva',string='Denominacion origen')
    rendimiento_denominacion_origen = fields.Integer(string='Rendimiento denominacion de origen')
    #Domain para que filtre y solo muestre los productos que sean del tipo adecuado
    producto_inicial1 = fields.Many2one('product.product',string='Producto uva',domain=[('product_tmpl_id.tipo_producto', '=', 'uva')])
    producto_sig_inicial2 = fields.Many2one('product.product',string='Producto pasta',domain=[('product_tmpl_id.tipo_producto', '=', 'pasta')])
    producto_sig3 = fields.Many2one('product.product',string='Producto mosto',domain=[('product_tmpl_id.tipo_producto', '=', 'mosto')])

    _sql_constraints = [('id_variedad_uniq','unique(id_variedad)','El id de variedad ya existe')]

    @api.constrains('producto_inicial1')
    def _check_productos(self):
        for record in self:
            if not record.producto_inicial1 or not record.producto_sig_inicial2 or not record.producto_sig3:
                raise ValidationError("Todos los productos deben estar definidos.")

#     class HrRecruitmentStage(models.Model):
#     _name = 'hr.recruitment.stage'
#     job_id = fields.Many2one('hr.job', compute='compute_stage', inverse='stage_inverse')
#     stage_ids = fields.One2many('hr.job', 'stage_id')

#     @api.depends('stage_ids')
#     def compute_stage(self):
#         if len(self.stage_ids) > 0:
#             self.job_id = self.stage_ids[0]

#     def stage_inverse(self):
#         if len(self.stage_ids) > 0:
#             # delete previous reference
#             stage = self.env['hr.job'].browse(self.stage_ids[0].id)
#             asset.stage_id = False
#         # set new reference
#         self.job_id.stage_id = self


# class HrJob(models.Model):
#     _name = 'hr.job'
#     stage_id = fields.Many2one('hr.recruitment.stage', string='Stage')