from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def send_email_receipt(self, order):
        if order.partner_id and order.partner_id.email:
            template = self.env.ref('form_purchase.email_template_receipt')
            template.send_mail(order.id, force_send=True)
            return "Email sudah dikirim / Email sent"
        else:
            raise UserError("Customer must have an email address.")

    def _get_order_fields(self):
        fields = super(PosOrder, self)._get_order_fields()
        fields.remove('price_total')  # Disable Price
        fields.remove('discount')  # Disable Discount
        return fields
    
    @api.model
    def send_email_receipt(self, order):
        if order.partner_id and order.partner_id.email:
            template = self.env.ref('form_purchase.email_template_receipt')
            template.send_mail(order.id, force_send=True)
            return "Email sudah dikirim / Email sent"
        else:
            raise UserError("Customer must have an email address.")


