from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Movimientos(models.Model):
    _name = 'pgs_bodega.movimientos'
    _description = 'Bodega (Movimientos)'

    #Campos para asignar el id_mov
    secuencia_grupo = fields.Integer(string="Secuencia Grupo", default=0)
    id_registro = fields.Char(string='ID registro')

    id_mov = fields.Char (string='ID movimiento',readonly=True)
    id_origen = fields.Char (string='ID origen', required=True)
    cantidad = fields.Integer(string='Cantidad en Kg de producto movido')
    es_entrada = fields.Boolean(string='¿Es entrada?',default=True)
    producto_movido = fields.Many2one('product.product',string='Producto',required=True)
    id_mov_anterior = fields.Char (string='ID movimiento anteriror relacionado')

    @api.constrains('cantidad')
    def _check_cantidad(self):
        for record in self:
            if not record.cantidad > 0:
                raise ValidationError("La cantidad movida debe ser mayor a 0")

    @api.onchange('id_mov_anterior')
    def _onchange_id_mov_anterior(self):
        if self.id_mov_anterior:
            self.id_registro = self.id_mov_anterior[:3]

    #Comprobar que no se cambia de uva en un movimiento p.ej: una uva Tempranillo no puede pasar a pasta o mosto Godello. 
    @api.constrains('producto_movido', 'id_mov_anterior')
    def _check_variedad_uva(self):
        for record in self:
            if not record.id_mov_anterior:
                continue  # No hay movimiento previo

        # 1. Buscar movimiento anterior por id_mov
            mov_anterior = self.search([('id_mov', '=', record.id_mov_anterior)], limit=1)

            if not mov_anterior:
                raise ValidationError("El ID de movimiento anterior no existe.")

            producto_previo = mov_anterior.producto_movido

            if not producto_previo:
                continue  # nada que validar

        # 2. Buscar la variedad de uva relacionada con el producto del movimiento anterior
            variedad = self.env['pgs_bodega.variedad_uva'].search([
            '|',
            '|',
            ('producto_inicial1', '=', producto_previo.id),
            ('producto_sig_inicial2', '=', producto_previo.id),
            ('producto_sig3', '=', producto_previo.id),
            ], limit=1)

            if not variedad:
                raise ValidationError(
                f"El producto '{producto_previo.display_name}' no pertence a ninguna variedad de uva."
                )

        # 3. Verificar que el nuevo producto pertenece a la misma variedad
            prod_actual = record.producto_movido

            if prod_actual.id not in [
                variedad.producto_inicial1.id,
                variedad.producto_sig_inicial2.id,
                variedad.producto_sig3.id,
                ]:
                raise ValidationError(
                    f"El producto seleccionado ({prod_actual.display_name}) "
                    f"no pertenece a la misma variedad de uva que el producto previo "
                    f"({producto_previo.display_name})."
                )

    @api.model
    def create(self, vals):
        grupo = vals.get('id_registro')
        # Asegurar formato AAA
        grupo = str(grupo).zfill(3)
        vals['id_registro'] = grupo

        # obtener último movimiento del grupo
        ultimo = self.search([('id_registro', '=', grupo)],
                            order="secuencia_grupo desc",
                            limit=1)

        siguiente = (ultimo.secuencia_grupo or 0) + 1
        vals['secuencia_grupo'] = siguiente

        # generar ID AAA + BBB
        vals['id_mov'] = f"{str(grupo).zfill(3)}{str(siguiente).zfill(3)}"

        return super().create(vals)

    