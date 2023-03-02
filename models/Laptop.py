from odoo import models, fields, api

class Laptop(models.Model):
    _name = 'laptop.model'
    _description = 'Modelo de portátiles'

    name = fields.Char(string='Nombre', required=True, index=True)
    brand = fields.Char(string='Marca', required=True)
    brand_id = fields.Many2one(comodel_name='brand', string='Marca')
    model = fields.Char(string='Modelo', required=True)
    price = fields.Float(string='Precio', required=True)
    year = fields.Integer(string='Año')
    description = fields.Text(string='Descripción')
    sold = fields.Boolean(string='Vendido', default=False)

    buyer_ids = fields.Many2many(comodel_name='user.model', string='Compradores')

    # Nuevos campos
    processor = fields.Char(string='Procesador')
    ram = fields.Char(string='RAM')
    storage = fields.Char(string='Almacenamiento')
    display_size = fields.Char(string='Tamaño de pantalla')
    graphics = fields.Char(string='Tarjeta gráfica')
    operating_system = fields.Char(string='Sistema operativo')

    @api.model
    def mark_as_sold(self):
        self.sold = True

    @api.model
    def add_buyer(self, buyer):
        self.buyer_ids |= buyer

class Brand(models.Model):
    _name = 'brand'
    _description = 'Modelo de Marca'

    name = fields.Char(string='Nombre', required=True)