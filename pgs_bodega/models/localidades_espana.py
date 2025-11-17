from odoo import models, fields, api

class LocalidadesEspana(models.Model):
    _name = "localidades_espana"
    _description = "Localidades de España"
    _rec_name = "NOMBRE"

    CODAUTO = fields.Char()
    CPRO = fields.Char()
    CMUN = fields.Char()
    DC = fields.Char()
    NOMBRE = fields.Char()
    CODPROV = fields.Char()


