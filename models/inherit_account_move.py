from odoo import models, api,fields
from odoo.http import request
import requests
import logging
_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    ip_address = fields.Char(string="IP Address")
    geo_city = fields.Char(string="City")
    geo_region = fields.Char(string="Region")
    geo_country = fields.Char(string="Country")
    geo_latitude = fields.Float(string="Latitude")
    geo_longitude = fields.Float(string="Longitude")

    @api.model_create_multi
    def create(self, vals_list):
        # Get IP address from request
        ip = None
        # Default location
        geo_data = {'city': '', 'region': '', 'country': '',
            'latitude': 0.0, 'longitude': 0.0 }


        if request and request.httprequest:
            ip = request.httprequest.headers.get('X-Forwarded-For', request.httprequest.remote_addr)
            _logger.info(f"Detected IP: {ip}")
            try:
                # You can use a free IP geolocation API
                response = requests.get(f'https://ipapi.co/{ip}/json/')

                if response.status_code == 200:
                    data = response.json()
                    geo_data.update({
                        'city': data.get('city', ''),
                        'region': data.get('region', ''),
                        'country': data.get('country_name', ''),
                        'latitude': data.get('latitude') or 0.0,
                        'longitude': data.get('longitude') or 0.0,
                    })
                   
            except Exception as e:
                    _logger.warning(f"Geo IP lookup failed: {e}")

        # Update values
        for vals in vals_list:
            vals.update({
                'ip_address': ip,
                'geo_city': geo_data['city'],
                'geo_region': geo_data['region'],
                'geo_country': geo_data['country'],
                'geo_latitude': geo_data['latitude'],
                'geo_longitude': geo_data['longitude'],
            })
        return super(AccountMove, self).create(vals)
