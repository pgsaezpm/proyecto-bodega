# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Clase(models.Model):
    _name = 'gimnasio.clase'
    _description = 'Gimnasio (Clase)'

    nombre = fields.Char(string="Nombre de la clase", required="True")
    capacidad_maxima = fields.Integer(string="Capacidad máxima", required="True")
    dia_semana = fields.Selection([
        ('lunes','Lunes'),
        ('martes','Martes'),
        ('miercoles','Miercoles'),
        ('jueves','Jueves'),
        ('viernes','Viernes'),
        ('sabado','Sábado'),
        ('domingo','Domingo'),
    ], string="Día de la semana",required="True")
    hora_inicio = fields.Float(string="Hora de inicio", required="True")
    hora_fin = fields.Float(string="Hora de finalización", compute="_calcular_hora_fin")
    duracion = fields.Float(string="Duración", required="True",default=1)
    entrenador = fields.Many2one('gimnasio.entrenador',string="Entrenador", required="True")

    @api.depends('nombre')
    def _compute_display_name (self):
        for record in self:
            if record.nombre:
                record.display_name = f"{record.nombre}"
            else:
                record.display_name = "Sin nombre"
    
    @api.depends('hora_inicio','duracion')
    def _calcular_hora_fin (self):
        for record in self:
            if record.hora_inicio and record.duracion:
                record.hora_fin = record.hora_inicio + record.duracion
            else:
                record.hora_fin = 0

    @api.constrains('duracion')
    def _check_duracion(self):
        for record in self:
            if record.duracion <= 0 :
                raise ValidationError("La duracion no es válida")
        
    # @api.model
    # def name_search(self, name='', args=None, operator='ilike', limit=100):
    #     args = args or [] # Nos aseguramos que tengamos args
    #     if not name: # Si no hay name (término de búsqueda)
    #         return super().name_search(name, args, operator, limit)

    #     domain = [] # Aquí añadimos las condiciones ('campo', operador, name)

    #     objetos = self.search(args + domain, limit=limit) # Hacemos la búsqueda
    #     return [(objeto.id, objeto.display_name) for objeto in objetos] # Devolvemos una lista de resultados


    # def _calcular_datos(self):
    #     for record in self:
    #         domain = [] # ('campo', operador, name)
    #         datos = self.env['gimnasio.clase'].search(domain=domain, limit=100) # Búsqueda al clase según las condiciones del domain
    #         numero_datos = len(datos)