import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class SiteMigrationDetail(Model):

    fields = ["entity_id", "other_site_name", "entity_id_at_other_site", "migrated_at", "entity_type", \
    "status"]


    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("site_migration_details"), params, env, headers)
