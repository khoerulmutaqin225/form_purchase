from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class Material(models.Model):
    _name = 'material.record'
    _description = 'Material Record'

    material_code = fields.Char(string='Material Code', required=True)
    material_name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection(
        [('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')],
        string='Material Type', required=True)
    material_buy_price = fields.Float(string='Material Buy Price', required=True)

    related_supplier_id = fields.Many2one('res.partner', string='Related Supplier', required=True)

    @api.constrains('material_buy_price')
    def check_buy_price(self):
        for record in self:
            if record.material_buy_price < 100:
                raise ValidationError("Material Buy Price must be greater than or equal to 100.")
