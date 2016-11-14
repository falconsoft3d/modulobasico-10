# -*- coding: utf-8 -*-
from odoo import http

# class Modulobasico(http.Controller):
#     @http.route('/modulobasico/modulobasico/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulobasico/modulobasico/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulobasico.listing', {
#             'root': '/modulobasico/modulobasico',
#             'objects': http.request.env['modulobasico.modulobasico'].search([]),
#         })

#     @http.route('/modulobasico/modulobasico/objects/<model("modulobasico.modulobasico"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulobasico.object', {
#             'object': obj
#         })