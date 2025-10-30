# -*- coding: utf-8 -*-
# from odoo import http


# class PgsBodega(http.Controller):
#     @http.route('/pgs_bodega/pgs_bodega', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pgs_bodega/pgs_bodega/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pgs_bodega.listing', {
#             'root': '/pgs_bodega/pgs_bodega',
#             'objects': http.request.env['pgs_bodega.pgs_bodega'].search([]),
#         })

#     @http.route('/pgs_bodega/pgs_bodega/objects/<model("pgs_bodega.pgs_bodega"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pgs_bodega.object', {
#             'object': obj
#         })

