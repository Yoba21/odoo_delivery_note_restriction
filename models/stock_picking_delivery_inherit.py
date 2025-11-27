from odoo import models, fields, api
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    print_count = fields.Integer(default=0, readonly=True)
    first_print_date = fields.Datetime(readonly=True)
    last_print_date = fields.Datetime(readonly=True)

    def action_print_delivery_with_count(self):
        if not self.env.user.has_group('delivery_note_restriction.group_store_manager'):
            raise UserError("Not authorized to print delivery notes!")


        for rec in self:
            rec.print_count += 1
            rec.last_print_date = fields.Datetime.now()
            if rec.print_count == 1:
                rec.first_print_date = rec.last_print_date

        # return the actual delivery slip report
        return self.env.ref("stock.action_report_delivery").report_action(self)
