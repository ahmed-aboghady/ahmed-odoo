from odoo import models, fields, api
from odoo.exceptions import ValidationError


class owner(models.Model):
    _name = "owner"

    name = fields.Char(required=True, size=15)
    phone = fields.Char()
    address = fields.Char()
