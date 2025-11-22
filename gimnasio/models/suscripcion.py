# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Suscripcion(models.Model):
    _name = 'gimnasio.suscripcion'
    _description = 'Gimnasio (Suscripcion)'

    nombre = fields.Char(string="Nombre del plan", required='True')
    precio = fields.Monetary(string="Precio", required='True',currency_field="moneda")
    moneda = fields.Many2one('res.currency',string="Moneda")
    duracion = fields.Integer(string="Duración", required='True')
    # clientes = fields.One2many('gimnasio.suscripcion',string="Clientes")
    
    campo_calculado = fields.Float(string="Campo calculado", compute="_calcular_campo_decimal")

    _sql_constraints = [('unico_nombre','UNIQUE(nombre)','El nombre debe ser unico')]

    @api.depends('nombre')
    def _compute_display_name (self):
        for record in self:
            record.display_name = record.nombre or "Sin nombre"

    @api.constrains('precio')
    def _check_precio(self):
        for record in self:
            if record.precio <= 0:
                raise ValidationError('El precio debe ser mayor a 0')

    @api.constrains('duracion')
    def _check_duracion(self):
        for record in self:
            if record.duracion < 1:
                raise ValidationError('La duración debe de ser al menos 1 mes')        

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
    #         datos = self.env['gimnasio.suscripcion'].search(domain=domain, limit=100) # Búsqueda al suscripcion según las condiciones del domain
    #         numero_datos = len(datos)