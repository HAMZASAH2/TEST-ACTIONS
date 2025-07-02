# -*- coding: utf-8 -*-
from odoo import models, fields, _

class SimpleModel(models.Model):
    _name = 'simple.model'
    _description = 'Simple Model'

    name = fields.Char(required=True, help="The name of the record.")
    description = fields.Text(help="A description for the record.")
    active = fields.Boolean(default=True, help="Indicates if the record is active.")
    test_field = fields.Char(string='Test Field', help="A test field for demonstration purposes.")
    test_integer = fields.Integer(string='Test Integer', help="An integer field for testing purposes.")
    # Add any additional fields or methods as needed
    # This model can be extended with more fields or methods as required
    # For example, you can add computed fields, constraints, or business logic methods
    # Example of a computed field
    # computed_field = fields.Char(string='Computed Field', compute='_compute_computed_field',
    #                               help="A computed field that does something.")
