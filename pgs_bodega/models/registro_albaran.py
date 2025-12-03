from odoo import models, fields, api
from odoo.exceptions import ValidationError


class RegistroAlbaran(models.Model):
    _name = 'pgs_bodega.registro_albaran'
    _description = 'Módulo (Registros Albaran)'

    id_registro = fields.Char (string='Id', required=True)
    viticultor_propietario = fields.Many2many('res.partner',string='Viticultor propietario',domain=[('es_viticultor', '=', True)])
    hora_registro = fields.Datetime(string='Hora y fecha de creacion del registro',default=fields.Datetime.now)
    parcela = fields.Many2many('pgs_bodega.parcela',string='Parcela')
    variedad_uva = fields.Many2many('pgs_bodega.variedad_uva',string='Variedad de uva')
    tipo_recogida = fields.Selection([
        ('manual_remolque','Manual remolque'),
        ('manual_cajas','Manual cajas'),
        ('mecanizado','Mecanizado'),
    ], string="Tipo de recogida", default='manual_remolque')
    tara = fields.Float(string='Tara')
    peso_bruto = fields.Float(string='Peso bruto')
    peso_neto = fields.Float(string='Peso neto (Calculado)', compute='_calcular_peso_neto',store=True)
    calidad_uva = fields.Selection([
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ], string="Calidad de uva",default='1')
    
    _sql_constraints = [('id_uniq','unique(id)','El id ya existe')]

    @api.constrains('tara')
    def _check_tara(self):
        for record in self:
            if not record.tara > 0:
                raise ValidationError("Introduzca una tara valida")

    @api.constrains('peso_bruto')
    def _check_peso_bruto(self):
        for record in self:
            if not record.peso_bruto > record.tara:
                raise ValidationError("Introduzca un peso bruto valido, recuerda que el peso bruto no puede ser menor a la tara")

    @api.depends('tara','peso_bruto')
    def _calcular_peso_neto(self):
        for record in self:
            if record.tara and record.peso_bruto:
                record.peso_neto = record.peso_bruto - record.tara
            else:
                record.peso_neto = 0

    #Cambiar el campo titulo del modulo
    @api.depends('id_registro','hora_registro')
    def _compute_display_name(self):   
        for record in self:
            if record.id_registro and record.hora_registro:
                record.display_name = f"{record.id_registro}, ({record.hora_registro})"
            else:
                record.display_name = 'Sin nombre'

    #Crear el registro inicial en movimientos cuando se cree en este modelo un registro
    @api.model
    def create(self, vals):

        record = super(RegistroAlbaran, self).create(vals)

        # Obtener producto_uva (tu campo es Many2many)
        producto_uva = record.variedad_uva[:1].producto_inicial1.id if record.variedad_uva else None
        
        id_primer_mov = f"000{str(record.id_registro).zfill(3)}"

        # Crear el movimiento inicial
        self.env['pgs_bodega.movimientos'].create({
            'secuencia_grupo': 000,
            'id_registro': record.id_registro,
            'id_origen': 0,
            'id_mov': id_primer_mov,
            'cantidad': record.peso_neto,  
            'es_entrada': True,
            'producto_movido': producto_uva,
            'id_mov_anterior': False,
        }) 

        return record
