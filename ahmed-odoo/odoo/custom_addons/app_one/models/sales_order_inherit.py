from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SalesOrderInherit(models.Model):
    _inherit = "sale.order"
    property_id=fields.Many2one('property')

    def action_confirm(self):
         res = super(SalesOrderInherit, self).action_confirm()
         print("hi iam in action_Confirm method")
         return res
