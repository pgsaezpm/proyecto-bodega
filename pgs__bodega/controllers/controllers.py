# -*- coding: utf-8 -*-
# from odoo import http


# class PgsBodega(http.Controller):
#     @http.route('/pgs__bodega/pgs__bodega', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pgs__bodega/pgs__bodega/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pgs__bodega.listing', {
#             'root': '/pgs__bodega/pgs__bodega',
#             'objects': http.request.env['pgs__bodega.pgs__bodega'].search([]),
#         })

#     @http.route('/pgs__bodega/pgs__bodega/objects/<model("pgs__bodega.pgs__bodega"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pgs__bodega.object', {
#             'object': obj
#         })

