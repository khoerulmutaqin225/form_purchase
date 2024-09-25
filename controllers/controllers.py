from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError
class MaterialController(http.Controller):

    @http.route('/materials', type='http', auth='user', website=True)
    def list_materials(self, **kwargs):
        materials = request.env['material.record'].search([])
        return request.render('form_purchase.material_list', {'materials': materials})

    @http.route('/materials/update/<int:id>', type='http', auth='user', methods=['POST'])
    def update_material(self, id, **kwargs):
        material = request.env['material.record'].browse(id)
        if material:
            material.write({
                'material_code': kwargs.get('material_code'),
                'material_name': kwargs.get('material_name'),
                'material_type': kwargs.get('material_type'),
                'material_buy_price': kwargs.get('material_buy_price'),
                'related_supplier_id': kwargs.get('related_supplier_id'),
            })
        return http.redirect('/materials')

    @http.route('/materials/delete/<int:id>', type='http', auth='user', methods=['POST'])
    def delete_material(self, id):
        material = request.env['material.record'].browse(id)
        if material:
            material.unlink()
        return http.redirect('/materials')
