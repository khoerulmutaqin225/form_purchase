from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class PosOrder(models.Model):
    _inherit = 'pos.order'
    
    # global send_email_receipt
    def send_email_receipt(self, mail=False): 
        email_to = mail
        mail_template = self.env.ref('form_purchase.email_template_receipt')
        if mail_template and email_to:
            authorMail = self.env['res.users'].browse(2) or False# Id Administrator
            # incoming_mail = self.env['fetchmail.server'].browse(2) or False
            # incoming_mail_server = incoming_mail.user or False
            # mail_template.model_id.env.user.email_formatted = f'{authorMail.name} <{incoming_mail_server}>' # Override Author email from OdooBot to Administrator 
            mail_template.send_mail(self.id, force_send=True)
