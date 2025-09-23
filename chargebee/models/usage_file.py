import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class UsageFile(Model):
    class UploadDetail(Model):
      fields = ["url", "expires_at"]
      pass

    fields = ["id", "name", "mime_type", "error_code", "error_reason", "status", "total_records_count", \
    "processed_records_count", "failed_records_count", "file_size_in_bytes", "processing_started_at", \
    "processing_completed_at", "uploaded_by", "uploaded_at", "error_file_path", "error_file_url", \
    "upload_details"]


    @staticmethod
    def upload_url(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("usage_files","upload_url"), params, env, headers, "file-ingest", False,json_keys)

    @staticmethod
    def processing_status(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("usage_files",id,"processing_status"), None, env, headers, "file-ingest", False,json_keys)
