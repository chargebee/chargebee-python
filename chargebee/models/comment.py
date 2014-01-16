import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Comment(Model):

    fields = ["id", "entity_type", "added_by", "notes", "created_at", "type", "entity_id" ]


    @staticmethod
    def create(params, env=None):
        return request.send('post', '/comments', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/comments/%s' % id, None, env)

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/comments', params, env)

    @staticmethod
    def delete(id, env=None):
        return request.send('post', '/comments/%s/delete' % id, None, env)
