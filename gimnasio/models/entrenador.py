# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Entrenador(models.Model):
    _name = 'gimnasio.entrenador'
    _description = 'Gimnasio (Entrenador)'

    nombre = fields.Char(string="Nombre", required="True")
    apellido_1 = fields.Char(string="Primer apellido", required="True")
    apellido_2 = fields.Char(string="Segundo apellido")
    dni = fields.Char(string="DNI", required="True")
    email = fields.Char(string="Correo electrónico")
    telefono = fields.Char(string="Teléfono", required="True")
    clases = fields.One2many('gimnasio.clase','entrenador',string="Clases que imparte")

    _sql_constraints = [('unico_dni','UNIQUE(dni)','El DNI debe ser unico')]
    _sql_constraints = [('unico_email','UNIQUE(email)','El email debe ser unico')]

    # @api.constrains('dni')
    # def _check_dni(self):
    #     for record in self:
    #         LETRAS_DNI = 'TRWAGMYFPDXBNJZSQVHLCKE'
    #         dni = record.dni[0:8]
    #         if record.dni != f"{dni}{LETRAS_DNI[int(dni) % 23]}":
    #             raise ValidationError("El DNI no es válido.")
              
    @api.depends('nombre','apellido_1','apellido_2')
    def _compute_display_name (self):
        for record in self:
            if record.nombre and record.apellido_1:
                record.display_name = f"{record.apellido_1} {record.apellido_2 or ""},{record.nombre}"
            else:
                record.display_name = "Sin nombre"

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
    #         datos = self.env['gimnasio.entrenador'].search(domain=domain, limit=100) # Búsqueda al entrenador según las condiciones del domain
    #         numero_datos = len(datos)