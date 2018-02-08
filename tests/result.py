import unittest

from chargebee import Customer, Estimate
from chargebee.models.invoice_estimate import InvoiceEstimate


class ResultTest(unittest.TestCase):
    def test_construct(self):
        values = {
            "id": "XpbGElGQgEIrbF77",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@test.com",
            "auto_collection": "on",
            "net_term_days": 0,
            "allow_direct_debit": False,
            "created_at": 1515495068,
            "taxability": "taxable",
            "updated_at": 1515495068,
            "locale": "fr-CA",
            "resource_version": 1515495068000,
            "deleted": False,
            "object": "customer",
            "billing_address": {
                "first_name": "John",
                "last_name": "Doe",
                "line1": "PO Box 9999",
                "city": "Walnut",
                "state_code": "CA",
                "state": "California",
                "country": "US",
                "zip": "91789",
                "validation_status": "not_validated",
                "object": "billing_address"
            },
            "contacts": [
                {
                    "id": "ty68op521m",
                    "first_name": "Michel",
                    "last_name": "Ross",
                    "email": "Mike@test.com",
                    "label": "Mike",
                    "enabled": True,
                    "send_account_email": True,
                    "send_billing_email": False,
                    "object": "contact"
                },
            ],
            "card_status": "no_card",
            "promotional_credits": 0,
            "refundable_credits": 0,
            "excess_payments": 0,
            "unbilled_charges": 0,
            "preferred_currency_code": "USD"
        }

        cust = Customer.construct(values)

        self.assertIsInstance(cust, Customer)
        self.assertIsInstance(cust.billing_address, Customer.BillingAddress)
        self.assertEqual(cust.billing_address.zip, "91789")

        self.assertIsNone(cust.payment_method)

        self.assertIsInstance(cust.contacts, list)
        self.assertIsInstance(cust.contacts[0], Customer.Contact)
        self.assertEqual(cust.contacts[0].id, "ty68op521m")

    def test_dependent_sub_types(self):
        values = {
            "created_at": 1515494922,
            "object": "estimate",
            "invoice_estimates": [
                {
                    "recurring": True,
                    "price_type": "tax_exclusive",
                    "sub_total": 2000,
                    "total": 2000,
                    "credits_applied": 0,
                    "amount_paid": 0,
                    "amount_due": 2000,
                    "object": "invoice_estimate",
                    "line_items": [
                        {
                            "id": "li_XpbGElGQgEIDTu2k",
                            "date_from": 1515494914,
                            "date_to": 1518173314,
                            "unit_amount": 1000,
                            "quantity": 1,
                            "is_taxed": False,
                            "tax_amount": 0,
                            "object": "line_item",
                            "subscription_id": "addams",
                            "amount": 1000,
                            "description": "No Trial",
                            "entity_type": "plan",
                            "entity_id": "no_trial",
                            "discount_amount": 0,
                            "item_level_discount_amount": 0
                        },
                    ],
                    "taxes": [],
                    "line_item_taxes": [],
                    "currency_code": "USD",
                    "line_item_discounts": []
                },
            ]
        }
        estimate = Estimate.construct(values)

        self.assertIsInstance(estimate, Estimate)
        self.assertIsInstance(estimate.invoice_estimates, list)

        inv_estimate = estimate.invoice_estimates[0]
        self.assertIsInstance(inv_estimate, InvoiceEstimate)
        self.assertEqual(inv_estimate.currency_code, "USD")

        self.assertIsInstance(inv_estimate.line_items, list)
        self.assertIsInstance(inv_estimate.line_items[0], InvoiceEstimate.LineItem)
        self.assertEqual(inv_estimate.line_items[0].id, "li_XpbGElGQgEIDTu2k")
