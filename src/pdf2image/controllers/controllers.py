# -*- coding: utf-8 -*-
# from odoo import http


# class Pdf2image(http.Controller):
#     @http.route('/pdf2image/pdf2image', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pdf2image/pdf2image/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pdf2image.listing', {
#             'root': '/pdf2image/pdf2image',
#             'objects': http.request.env['pdf2image.pdf2image'].search([]),
#         })

#     @http.route('/pdf2image/pdf2image/objects/<model("pdf2image.pdf2image"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pdf2image.object', {
#             'object': obj
#         })

