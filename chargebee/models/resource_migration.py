import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class ResourceMigration(Model):

    fields = ["from_site", "entity_type", "entity_id", "status", "errors", "created_at", "updated_at"]


    @staticmethod
    def retrieve_latest(params, env=None, headers=None):
        return request.send('get', request.uri_path("resource_migrations","retrieve_latest"), params, env, headers)
