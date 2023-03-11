from odoo import models, fields, api

class Devoluciones (models.Model):
    _name = "devoluciones"
    _rec_name = "nombre"
    _description = "devoluciones"

    nombre = fields.Char(string="Registro", compute='_dependecias')
    comprador = fields.Many2one('usuarios', required=True)
    vendedor = fields.Many2one('usuarios', required=True)
    portatil = fields.Many2one('portatiles', required=True)
    fecha_venta = fields.Date(string="Fecha de compra", required=True)
    fecha_devolucion = fields.Date(string="Fecha de devolucion", required=True)
    motivo=fields.Char(string="Motivo")

    @api.depends('comprador', 'vendedor', 'portatil', 'fecha_venta', 'fecha_devolucion')
    def _dependecias(self):
        for record in self:
            record.nombre = str(record.comprador.nombre) + ' devolvio el portatil ' + str(record.portatil.nombre) + ' de ' + str(record.vendedor.nombre) + 'comprado el dia ' + str(record.fecha_venta)  + 'y finalmente devuelto el dia ' + str(record.fecha_devolucion)+ 'por el motivo de que '+str(record.motivo)
   
   