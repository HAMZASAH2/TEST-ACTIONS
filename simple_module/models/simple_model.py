# -*- coding: utf-8 -*-
from odoo import models, fields, _

class SimpleModel(models.Model):
    _name = 'simple.model'
    _description = 'Simple Model'

    name = fields.Char(string='Name', required=True, help="The name of the record.")
    description = fields.Text(string='Description', help="A description for the record.")
