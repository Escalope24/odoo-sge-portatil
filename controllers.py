from odoo import http
from odoo.http import request

class PortalController(http.Controller):
    @http.route('/laptops', auth='public', website=True)
    def laptops(self, **kw):
        laptops = request.env['portatil.portatil'].search([])
        return http.request.render('nombre_del_modulo.laptops', {
            'laptops': laptops
        })

    @http.route('/about', auth='public', website=True)
    def about(self, **kw):
        return http.request.render('nombre_del_modulo.about')