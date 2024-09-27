from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class PosOrder(models.Model):
    _inherit = 'pos.order'
    
    # global send_repository_download_email
    def send_email_receipt(self ,mail_template=None, email_to=None):  
        email_to='Khoerulmutaqin225@gmail.com'
        domain = []  
        mail_template = self.env['mail.template'].search([('name','=','Email Template : Request Repository Download')])
        if mail_template:
            authorMail = self.env['res.users'].browse(2) # Id Administrator
            incoming_mail = self.env['fetchmail.server'].browse(2)
            incoming_mail_server = incoming_mail.user
            mail_template.model_id.env.user.email_formatted = f'{authorMail.name} <{incoming_mail_server}>' # Override Author email from OdooBot to Administrator 
            if email_to:
                mail_template.email_to = email_to
        mail_template.send_mail(self.id, force_send=True)