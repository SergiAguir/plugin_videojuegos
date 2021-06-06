# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class plugin_video(models.Model):
#     _name = 'plugin_video.plugin_video'
#     _description = 'plugin_video.plugin_video'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
