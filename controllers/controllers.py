# -*- coding: utf-8 -*-
from odoo import http

# class SimkopSyariah(http.Controller):
#     @http.route('/simkop_syariah/simkop_syariah/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simkop_syariah/simkop_syariah/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('simkop_syariah.listing', {
#             'root': '/simkop_syariah/simkop_syariah',
#             'objects': http.request.env['simkop_syariah.simkop_syariah'].search([]),
#         })

#     @http.route('/simkop_syariah/simkop_syariah/objects/<model("simkop_syariah.simkop_syariah"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simkop_syariah.object', {
#             'object': obj
#         })