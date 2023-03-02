from odoo import models, fields, api
from odoo.exceptions import UserError

class User(models.Model):
    _name = 'user.model'
    _description = 'Modelo de usuarios'

    name = fields.Char(string='Nombre')
    email = fields.Char(string='Correo electrónico', required=True, index=True)
    password = fields.Char(string='Contraseña')
    is_active = fields.Boolean(string='Activo', default=True)
    laptops_bought_ids = fields.Many2many(comodel_name='laptop.model', string='Portátiles comprados')

    @api.constrains('email')
    def _check_email(self):
        for user in self:
            existing_user = self.env['user.model'].search([('email', '=', user.email), ('id', '!=', user.id)])
            if existing_user:
                raise UserError('El correo electrónico ya está en uso por otro usuario.')