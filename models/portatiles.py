from odoo import models, fields, api


class Portatiles(models.Model):
    
    _name = 'portatil'
    _rec_name = 'modelo'
    _description = 'portatil'
    
    modelo = fields.Char(string='Modelo', required=True)
    marca = fields.Many2one('marca', required=True)
    imagen = fields.Image()
    resolucion = fields.Char(string='Resolución', required=True)
    frecuencia = fields.Integer(string='Frecuencia', required=True)
    tamaño = fields.Char(string='Tamaño', required=True)
    peso = fields.Float(string='Peso', required=True)
    RAM = fields.Integer(string='RAM', required=True)
    HDD = fields.Integer(string='HDD', required=True)
    SSD = fields.Integer(string='SSD', required=True)
    grafica = fields.Char(string='Tarjeta gráfica', required=True)
    placa_base = fields.Char(string='Placa base', required=True)