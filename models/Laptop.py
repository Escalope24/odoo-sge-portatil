from odoo import models, fields, api

class Laptop(models.Model):
    _name = 'laptop.model'
    _description = 'Modelo de portátiles'
    product_id=fields.Many2one('product.template',string='Producto', requiered=True)
    name = fields.Char(string='Nombre', required=True, index=True)
    brand = fields.Char(string='Marca', required=True)
    brand_id = fields.Many2one(comodel_name='brand', string='Marca')
    model = fields.Char(string='Modelo', required=True)
    price = fields.Float(string='Precio', required=True)
    year = fields.Integer(string='Año')
    description = fields.Text(string='Descripción')
    sold = fields.Boolean(string='Vendido', default=False)
    seller_id = fields.Integer(string='ID del vendedor', default=lambda self: self.env['ir.sequence'].next_by_code('portatil.seller.sequence'), help='ID único del vendedor', required=True, readonly=True, copy=False, index=True, unique=True)
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