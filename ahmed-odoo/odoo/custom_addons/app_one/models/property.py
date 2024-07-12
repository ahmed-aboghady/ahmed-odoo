from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = "property"
    _description = "property record"
    _inherit = ["mail.thread","mail.activity.mixin"]

    name = fields.Char(required=True, size=15)
    descrabtion = fields.Text(default="flat",tracking=1)
    postcode = fields.Char(required=True)
    date_availability = fields.Date(tracking=1)
    selling_price = fields.Float()
    expicted_price = fields.Float(digits=(0, 6))
    diff = fields.Float(compute='_compute_diff')
    badroms = fields.Integer(required=True, size=1)
    living_erea = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], default="north")

    owner_id = fields.Many2one('owner')
    owner_phone = fields.Char(related='owner_id.phone')  #create related fields
    owner_address = fields.Char(related='owner_id.address' , readonly=0)

    # _______________ set state field _____________________
    state=fields.Selection([
        ('draft' ,'Draft'),
        ('pending' , 'Pending'),
        ('sold' , 'Sold')],default="draft" )

    # _______________ set state Btns _____________________
    def draft_action(self):     #btn draft method
        for rec in self:
            rec.state = "draft"
    def pending_action(self):     #btn draft method
        for rec in self:
            rec.state = "pending"
    def sold_action(self):      #btn draft method
        for rec in self:
            rec.state = "sold"

    # _______________ compute method_____________________
    @api.depends('expicted_price','selling_price')  #    @api.depends
    def _compute_diff(self):
        for rec in self:
            print("iam from her")
            rec.diff = rec.expicted_price - rec.selling_price

#_______________________________
    @api.onchange('expicted_price', 'selling_price')    #    @on change
    def _compute_diff(self):
        for rec in self:
            print("iam from onchange")
            rec.diff = rec.expicted_price - rec.selling_price


    # _______________ heigh level constrain using db tair_____________________
    _sql_constraints = [
        ('unique_name', 'unique("name")', 'this not unique name!')
    ]

    # _______________ mudim level constrain using logic tair  level2 _____________________
    @api.constrains("badroms")
    def check_if_bedrooms_greeter_zero(self):
        for rec in self:
            if rec.badroms == 0:
                raise ValidationError("the num of bedrooms not valid")

    # _______________ overwrite on create method _____________________
    @api.model_create_multi
    def create(self,vals):
        res = super(Property,self).create(vals)
        print("hi iam create method ")
        return res

        # _______________ overwrite on read method _____________________
    @api.model
    def _search(self, domain,offset=0,limit=None,order=None,access_rights_uid=None):
        res = super(Property, self)._search(domain,offset=0,limit=None,order=None,access_rights_uid=None)
        print("hi iam read method")
        return res

       # _______________ overwrite on update method _____________________
    def write(self,vals):
        res = super(Property, self).write(vals)
        print("hi iam update method")
        return res
        # _______________ overwrite on delete method _____________________
    def unlink(self):
        res = super(Property, self).unlink()
        print("hi iam delete method")
        return res