# -*- coding: utf-8 -*-

from odoo import models, fields, api
# from odoo.exceptions import ValidationError

class Modelo(models.Model):
    _name = 'modulo.modelo'
    _description = 'Módulo (Modelo)'

    campo = fields.Integer(string="Campo")
    campo_calculado = fields.Float(string="Campo calculado", compute="_calcular_campo_decimal")

    _sql_constraints = []

    @api.depends('campo')
    def _calcular_campo_decimal(self):
        for record in self:
            record.campo_calculado = 0.0

    # @api.constrains('campo')
    # def _check_campo(self):
    #     for record in self:
    #         pass

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
    #         datos = self.env['modulo.modelo'].search(domain=domain, limit=100) # Búsqueda al modelo según las condiciones del domain
    #         numero_datos = len(datos)