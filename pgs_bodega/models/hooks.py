from odoo import api, SUPERUSER_ID

def proteger_registros(cr, registry):
    """
    Este hook marca los registros cargados desde XML como 'noupdate=1'
    después de la instalación.
    Así no se sobrescriben si el usuario los modifica.
    """
    env = api.Environment(cr, SUPERUSER_ID, {})

    # Busca el registro ir.model.data correspondiente
    imd = env['ir.model.data'].search([
        ('module', '=', 'pgs_bodega'),
        ('name', '=', 'deposito_0'),
    ])

    # Los marcamos como noupdate=1 para que Odoo no los toque más
    if imd:
        imd.noupdate = True
