from odoo import models, fields, api
from odoo.exceptions import ValidationError


class client(models.Model):
    _name = "client"
    _inherit = "owner"
