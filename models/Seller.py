from odoo import models, fields, api

class Seller(models.Model):
    _name = 'seller.model'
    _description = 'Modelo de Vendedores'
    seller_id = fields.integer(string='ID Vendedor', required=True, index=True)
    name = fields.Char(string='Nombre', required=True, index=True)
    email = fields.Char(string='Correo Electrónico', required=True)
    phone = fields.Char(string='Teléfono', required=True)
    address = fields.Char(string='Dirección')
    is_active = fields.Boolean(string='Activo', default=True)

    laptop_ids = fields.One2many(comodel_name='laptop.model', inverse_name='seller_id', string='Portátiles Vendidos')

    @api.model
    def toggle_active(self):
        for seller in self:
            seller.is_active = not seller.is_active

    @api.model
    def view_laptops(self):
        action = self.env.ref('module_name.action_laptop_list')
        result = action.read()[0]
        result['domain'] = [('seller_id', '=', self.id)]
        return result
