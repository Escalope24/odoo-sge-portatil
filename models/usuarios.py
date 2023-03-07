from odoo import models, fields, api

class Usuarios(models.Model):
    _name = "usuarios"
    _rec_name = "nombre"
    _description = "usuarios"

    dni = fields.Char(string="DNI", size=9, required=True)
    nombre = fields.Char(string="Nombre", required=True)
    imagen = fields.Image()
    telefono = fields.Integer(string="Número de telefono", size=9, required=True)
    email = fields.Char(string="Correo", required=True)
    portatiles = fields.One2many("portatiles", "vendedor", string="Portátiles a la venta")
    ventas = fields.One2many("ventas", "vendedor", string="Ventas")
    vendedor = fields.Boolean(string="Vendedor", compute='_vendedor')
    compras = fields.One2many("ventas", "comprador", string="Compras")
    
    @api.depends('portatiles')
    def _vendedor(self):
        for record in self:
            if len(record.portatiles) > 0:
                record.vendedor = True
            else:
                record.vendedor = False

    @api.onchange('dni')
    def _onchange_dni(self):
        if self.dni:
            try:
                if len(self.dni) != 9:
                    raise ValueError("El DNI debe tener 9 caracteres")
            except:
                return {
                    'warning': {
                        'title': "Error",
                        'message': "El DNI debe tener 9 caracteres",
                    }
                }
