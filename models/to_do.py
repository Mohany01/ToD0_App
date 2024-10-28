from email.policy import default

from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError

class ToDo(models.Model):
    _name = 'todo.task'
    _description = 'TO DO TASK'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Task Name' , default='New', requierd=1, track_visibility='always')
    description = fields.Text(string='Description')
    partner_id = fields.Many2one('res.partner', string='Assign To', required=1, track_visibility='always' )
    date = fields.Date(string='Due Date', track_visibility='always')
    status = fields.Selection([
        ('new', 'New'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed')
    ],default='new', track_visibility='always')
    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This Task is Already  Exist'),]


    def set_to_new(self):
        for rec in self:
            rec.status = "new"


    def set_to_progress(self):
        for rec in self:
            rec.status = "in progress"


    def set_to_completed(self):
        for rec in self:
            rec.status = "completed"


