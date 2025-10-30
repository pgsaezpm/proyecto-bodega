
# from odoo import models, fields, api

# class pgs__bodega(models.Model):
#     _name = 'pgs__bodega.pgs__bodega'
#     _description = 'pgs__bodega.pgs__bodega'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

