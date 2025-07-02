# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase

class TestSimpleModel(TransactionCase):
    def test_create(self):
        rec = self.env['simple.model'].create({'name': 'Test', 'description': 'A test record.'})
        self.assertEqual(rec.name, 'Test')
        self.assertEqual(rec.description, 'A test record.')
