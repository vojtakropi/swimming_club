# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    birthdate = fields.Date(string='Birthdate')
    swimming_level = fields.Selection(
        selection=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
            ('competitive', 'Competitive'),
        ],
        string='Swimming Level',
    )
    gdpr_consent = fields.Boolean(string='GDPR Consent')
    is_landlord = fields.Boolean(
        string='Landlord',
        help="Company that rents a swimming pool to the club. "
             "Landlords are not club members and are excluded from the Parents filter.",
    )

    _SWIMMING_CLUB_PARENT_FIELDS = ['email', 'phone']

    @api.model
    def _commercial_fields(self):
        return super()._commercial_fields() + self._SWIMMING_CLUB_PARENT_FIELDS
