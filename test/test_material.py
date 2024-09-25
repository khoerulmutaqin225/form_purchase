from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.Material = self.env['material.record']

    def test_create_material(self):
        material = self.Material.create({
            'material_code': 'M001',
            'material_name': 'Cotton Fabric',
            'material_type': 'cotton',
            'material_buy_price': 150.0,
            'related_supplier_id': self.env.ref('base.res_partner_1').id,
        })
        self.assertEqual(material.material_code, 'M001')

    def test_price_constraint(self):
        with self.assertRaises(ValidationError):
            self.Material.create({
                'material_code': 'M002',
                'material_name': 'Cheap Fabric',
                'material_type': 'fabric',
                'material_buy_price': 50.0,
                'related_supplier_id': self.env.ref('base.res_partner_1').id,
            })
