# Copyright 2021 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class AccountFinancialReportColumn(models.Model):
    _name = "account.financial.report.column"
    _description = "Manage column options in financial reports"
    _order = "sequence, id"

    res_model = fields.Char()
    sequence = fields.Integer()
    name = fields.Char(required=True)
    expression_label = fields.Char(required=True)
    is_visible = fields.Boolean(default=True)
    # user_id = fields.Many2one(comodel_name="res.users")
