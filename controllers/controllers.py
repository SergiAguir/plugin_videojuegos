# -*- coding: utf-8 -*-
# from odoo import http


# class PluginVideo(http.Controller):
#     @http.route('/plugin_video/plugin_video/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/plugin_video/plugin_video/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('plugin_video.listing', {
#             'root': '/plugin_video/plugin_video',
#             'objects': http.request.env['plugin_video.plugin_video'].search([]),
#         })

#     @http.route('/plugin_video/plugin_video/objects/<model("plugin_video.plugin_video"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('plugin_video.object', {
#             'object': obj
#         })
