# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval


class ResPartner(models.Model):

    _inherit = 'res.partner'

    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('dead', 'Dead'),
        ('never_touch', 'Never Touch'),
        ('archived', 'Archived')],
        string='Customer Status', default='active')


    def write(self, vals):
        res = super().write(vals)
        for rec in self:
            if vals.get('status') and vals.get('email', rec.email):
                if vals.get('status') in ('dead', 'never_touch'):
                    self.env['mail.blacklist'].sudo()._add(rec.email)
                else:
                    self.env['mail.blacklist'].sudo()._remove(rec.email)
        return res
