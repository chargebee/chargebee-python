import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class InstallmentDetail(Model):
    class Installment(Model):
      fields = ["id", "invoice_id", "date", "amount", "status", "created_at", "resource_version", "updated_at"]
      pass

    fields = ["id", "invoice_id", "amount", "installments"]

