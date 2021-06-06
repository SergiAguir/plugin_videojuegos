# -*- coding: utf-8 -*-

from odoo import models, fields, api


class plugin_video(models.Model):
    _name = 'videojuegos.juego_model'
    _inherit = 'videojuegos.juego_model'

    pegi = fields.Integer(string="Pegi")