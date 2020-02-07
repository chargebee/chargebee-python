from chargebee.compat import json
from chargebee.models import *


class Result(object):

    def __init__(self, response):
        self._response = response
        self._response_obj = {}

    @property
    def subscription(self):
        subscription = self._get('subscription', Subscription)
        return subscription;

    @property
    def customer(self):
        customer = self._get('customer', Customer)
        return customer;

    @property
    def hierarchy(self):
        hierarchy = self._get('hierarchy', Hierarchy);
        return hierarchy;

    @property
    def contact(self):
        contact = self._get('contact', Contact);
        return contact;

    @property
    def token(self):
        token = self._get('token', Token);
        return token;

    @property
    def payment_source(self):
        payment_source = self._get('payment_source', PaymentSource)
        return payment_source;

    @property
    def third_party_payment_method(self):
        third_party_payment_method = self._get('third_party_payment_method', ThirdPartyPaymentMethod)
        return third_party_payment_method;

    @property
    def virtual_bank_account(self):
        virtual_bank_account = self._get('virtual_bank_account', VirtualBankAccount);
        return virtual_bank_account;

    @property
    def card(self):
        card = self._get('card', Card)
        return card;

    @property
    def promotional_credit(self):
        promotional_credit = self._get('promotional_credit', PromotionalCredit)
        return promotional_credit;

    @property
    def invoice(self):
        invoice = self._get('invoice', Invoice)
        return invoice;

    @property
    def credit_note(self):
        credit_note = self._get('credit_note', CreditNote)
        return credit_note;

    @property
    def unbilled_charge(self):
        unbilled_charge = self._get('unbilled_charge', UnbilledCharge)
        return unbilled_charge;

    @property
    def order(self):
        order = self._get('order', Order)
        return order;

    @property
    def gift(self):
        gift = self._get('gift', Gift)
        return gift;

    @property
    def transaction(self):
        transaction = self._get('transaction', Transaction)
        return transaction;

    @property
    def hosted_page(self):
        hosted_page = self._get('hosted_page', HostedPage)
        return hosted_page;

    @property
    def estimate(self):
        estimate = self._get('estimate', Estimate)
        return estimate;

    @property
    def quote(self):
        quote = self._get('quote', Quote)
        return quote;

    @property
    def plan(self):
        plan = self._get('plan', Plan)
        return plan;

    @property
    def addon(self):
        addon = self._get('addon', Addon)
        return addon;

    @property
    def coupon(self):
        coupon = self._get('coupon', Coupon)
        return coupon;

    @property
    def coupon_set(self):
        coupon_set = self._get('coupon_set', CouponSet)
        return coupon_set;

    @property
    def coupon_code(self):
        coupon_code = self._get('coupon_code', CouponCode)
        return coupon_code;

    @property
    def address(self):
        address = self._get('address', Address)
        return address;

    @property
    def event(self):
        event = self._get('event', Event)
        return event;

    @property
    def comment(self):
        comment = self._get('comment', Comment)
        return comment;

    @property
    def download(self):
        download = self._get('download', Download)
        return download;

    @property
    def portal_session(self):
        portal_session = self._get('portal_session', PortalSession)
        return portal_session;

    @property
    def site_migration_detail(self):
        site_migration_detail = self._get('site_migration_detail', SiteMigrationDetail)
        return site_migration_detail;

    @property
    def resource_migration(self):
        resource_migration = self._get('resource_migration', ResourceMigration)
        return resource_migration;

    @property
    def time_machine(self):
        time_machine = self._get('time_machine', TimeMachine)
        return time_machine;

    @property
    def export(self):
        export = self._get('export', Export)
        return export;

    @property
    def payment_intent(self):
        payment_intent = self._get('payment_intent', PaymentIntent)
        return payment_intent;

    @property
    def unbilled_charges(self):
        unbilled_charges = self._get_list('unbilled_charges', UnbilledCharge)
        return unbilled_charges;

    @property
    def credit_notes(self):
        credit_notes = self._get_list('credit_notes', CreditNote)
        return credit_notes;

    @property
    def hierarchies(self):
        hierarchies = self._get_list('hierarchies', Hierarchy)
        return hierarchies;

    @property
    def invoices(self):
        invoices = self._get_list('invoices', Invoice)
        return invoices;

    def _get_list(self, type, cls):
        if not type in self._response:
            return None

        set_val = []
        for obj in self._response[type]:
            if isinstance(obj, dict):
                model = cls.construct(obj)
                set_val.append(model)

        self._response_obj[type] = set_val
        return self._response_obj[type]

    def _get(self, type, cls):
        if not type in self._response:
            return None

        if not type in self._response_obj:
            self._response_obj[type] = cls.construct(self._response[type])

        return self._response_obj[type]

    def __str__(self):
        return json.dumps(self._response, indent=4)

    def __repr__(self):
        return "<chargebee.Result: {}>".format(";".join(self._response.keys()))


class Content(Result):
    pass
