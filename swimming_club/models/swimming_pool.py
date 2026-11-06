# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SwimmingPool(models.Model):
    _name = 'swimming.pool'
    _description = 'Swimming Pool'
    _order = 'name'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    partner_id = fields.Many2one(
        'res.partner', string='Landlord',
        domain=[('is_landlord', '=', True)],
        context={'default_is_landlord': True},
        help="Company the club pays the rent to. Use it as the vendor on vendor bills.",
    )
    street = fields.Char()
    zip = fields.Char()
    city = fields.Char()
    country_id = fields.Many2one('res.country', string='Country')

    lane_ids = fields.One2many('swimming.lane', 'pool_id', string='Lanes')
    lane_count = fields.Integer(string='Number of Lanes', compute='_compute_lane_count')

    @api.depends('lane_ids')
    def _compute_lane_count(self):
        for pool in self:
            pool.lane_count = len(pool.lane_ids)


class SwimmingLane(models.Model):
    _name = 'swimming.lane'
    _description = 'Swimming Lane'
    _order = 'pool_id, sequence, id'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    pool_id = fields.Many2one(
        'swimming.pool', string='Swimming Pool',
        required=True, ondelete='cascade', index=True,
    )

    _name_pool_uniq = models.Constraint(
        'unique(pool_id, name)',
        'A lane with this name already exists in this swimming pool.',
    )

    @api.depends('name', 'pool_id.name')
    def _compute_display_name(self):
        for lane in self:
            lane.display_name = f"{lane.pool_id.name} - {lane.name}" if lane.pool_id else lane.name
