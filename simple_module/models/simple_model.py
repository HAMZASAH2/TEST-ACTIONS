# -*- coding: utf-8 -*-
from odoo import models, fields, _

class SimpleModel(models.Model):
    _name = 'simple.model'
    _description = 'Simple Model'

    name = fields.Char(required=True, help="The name of the record.")
    description = fields.Text(help="A description for the record.")
    active = fields.Boolean(default=True, help="Indicates if the record is active.")
    Text = fields.Text(string='Text Field', help="A simple text field for demonstration purposes.")