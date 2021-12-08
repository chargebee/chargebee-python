from chargebee.compat import json
from chargebee.models import *


class Result(object):

    def __init__(self, response):
        self._response = response
        self._response_obj = {}

    @property
    def subscription(self):
        subscription = self._get('subscription', Subscription,
        {'subscription_items' : Subscription.SubscriptionItem, 'item_tiers' : Subscription.ItemTier, 'charged_items' : Subscription.ChargedItem, 'addons' : Subscription.Addon, 'event_based_addons' : Subscription.EventBasedAddon, 'charged_event_based_addons' : Subscription.ChargedEventBasedAddon, 'coupons' : Subscription.Coupon, 'shipping_address' : Subscription.ShippingAddress, 'referral_info' : Subscription.ReferralInfo, 'contract_term' : Subscription.ContractTerm});
        return subscription;

    @property
    def contract_term(self):
        contract_term = self._get('contract_term', ContractTerm);
        return contract_term;

    @property
    def advance_invoice_schedule(self):
        advance_invoice_schedule = self._get('advance_invoice_schedule', AdvanceInvoiceSchedule,
        {'fixed_interval_schedule' : AdvanceInvoiceSchedule.FixedIntervalSchedule, 'specific_dates_schedule' : AdvanceInvoiceSchedule.SpecificDatesSchedule});
        return advance_invoice_schedule;

    @property
    def customer(self):
        customer = self._get('customer', Customer,
        {'billing_address' : Customer.BillingAddress, 'referral_urls' : Customer.ReferralUrl, 'contacts' : Customer.Contact, 'payment_method' : Customer.PaymentMethod, 'balances' : Customer.Balance, 'relationship' : Customer.Relationship, 'parent_account_access' : Customer.ParentAccountAccess, 'child_account_access' : Customer.ChildAccountAccess});
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
        payment_source = self._get('payment_source', PaymentSource,
        {'card' : PaymentSource.Card, 'bank_account' : PaymentSource.BankAccount, 'amazon_payment' : PaymentSource.AmazonPayment, 'paypal' : PaymentSource.Paypal});
        return payment_source;

    @property
    def third_party_payment_method(self):
        third_party_payment_method = self._get('third_party_payment_method', ThirdPartyPaymentMethod);
        return third_party_payment_method;

    @property
    def virtual_bank_account(self):
        virtual_bank_account = self._get('virtual_bank_account', VirtualBankAccount);
        return virtual_bank_account;

    @property
    def card(self):
        card = self._get('card', Card);
        return card;

    @property
    def promotional_credit(self):
        promotional_credit = self._get('promotional_credit', PromotionalCredit);
        return promotional_credit;

    @property
    def invoice(self):
        invoice = self._get('invoice', Invoice,
        {'line_items' : Invoice.LineItem, 'discounts' : Invoice.Discount, 'line_item_discounts' : Invoice.LineItemDiscount, 'taxes' : Invoice.Tax, 'line_item_taxes' : Invoice.LineItemTax, 'line_item_tiers' : Invoice.LineItemTier, 'linked_payments' : Invoice.LinkedPayment, 'dunning_attempts' : Invoice.DunningAttempt, 'applied_credits' : Invoice.AppliedCredit, 'adjustment_credit_notes' : Invoice.AdjustmentCreditNote, 'issued_credit_notes' : Invoice.IssuedCreditNote, 'linked_orders' : Invoice.LinkedOrder, 'notes' : Invoice.Note, 'shipping_address' : Invoice.ShippingAddress, 'billing_address' : Invoice.BillingAddress});
        return invoice;

    @property
    def tax_withheld(self):
        tax_withheld = self._get('tax_withheld', TaxWithheld);
        return tax_withheld;

    @property
    def credit_note(self):
        credit_note = self._get('credit_note', CreditNote,
        {'line_items' : CreditNote.LineItem, 'discounts' : CreditNote.Discount, 'line_item_discounts' : CreditNote.LineItemDiscount, 'line_item_tiers' : CreditNote.LineItemTier, 'taxes' : CreditNote.Tax, 'line_item_taxes' : CreditNote.LineItemTax, 'linked_refunds' : CreditNote.LinkedRefund, 'allocations' : CreditNote.Allocation});
        return credit_note;

    @property
    def unbilled_charge(self):
        unbilled_charge = self._get('unbilled_charge', UnbilledCharge,
        {'tiers' : UnbilledCharge.Tier});
        return unbilled_charge;

    @property
    def order(self):
        order = self._get('order', Order,
        {'order_line_items' : Order.OrderLineItem, 'shipping_address' : Order.ShippingAddress, 'billing_address' : Order.BillingAddress, 'line_item_taxes' : Order.LineItemTax, 'line_item_discounts' : Order.LineItemDiscount, 'linked_credit_notes' : Order.LinkedCreditNote, 'resent_orders' : Order.ResentOrder});
        return order;

    @property
    def gift(self):
        gift = self._get('gift', Gift,
        {'gifter' : Gift.Gifter, 'gift_receiver' : Gift.GiftReceiver, 'gift_timelines' : Gift.GiftTimeline});
        return gift;

    @property
    def transaction(self):
        transaction = self._get('transaction', Transaction,
        {'linked_invoices' : Transaction.LinkedInvoice, 'linked_credit_notes' : Transaction.LinkedCreditNote, 'linked_refunds' : Transaction.LinkedRefund, 'linked_payments' : Transaction.LinkedPayment});
        return transaction;

    @property
    def hosted_page(self):
        hosted_page = self._get('hosted_page', HostedPage);
        return hosted_page;

    @property
    def estimate(self):
        estimate = self._get('estimate', Estimate, {},
        {'subscription_estimate' : SubscriptionEstimate, 'invoice_estimate' : InvoiceEstimate, 'invoice_estimates' : InvoiceEstimate, 'next_invoice_estimate' : InvoiceEstimate, 'credit_note_estimates' : CreditNoteEstimate, 'unbilled_charge_estimates' : UnbilledCharge});
        estimate.init_dependant(self._response['estimate'], 'subscription_estimate',
        {'shipping_address' : SubscriptionEstimate.ShippingAddress, 'contract_term' : SubscriptionEstimate.ContractTerm});
        estimate.init_dependant(self._response['estimate'], 'invoice_estimate',
        {'line_items' : InvoiceEstimate.LineItem, 'discounts' : InvoiceEstimate.Discount, 'taxes' : InvoiceEstimate.Tax, 'line_item_taxes' : InvoiceEstimate.LineItemTax, 'line_item_tiers' : InvoiceEstimate.LineItemTier, 'line_item_discounts' : InvoiceEstimate.LineItemDiscount});
        estimate.init_dependant(self._response['estimate'], 'next_invoice_estimate',
        {'line_items' : InvoiceEstimate.LineItem, 'discounts' : InvoiceEstimate.Discount, 'taxes' : InvoiceEstimate.Tax, 'line_item_taxes' : InvoiceEstimate.LineItemTax, 'line_item_tiers' : InvoiceEstimate.LineItemTier, 'line_item_discounts' : InvoiceEstimate.LineItemDiscount});
        estimate.init_dependant_list(self._response['estimate'], 'invoice_estimates',
        {'line_items' : InvoiceEstimate.LineItem, 'discounts' : InvoiceEstimate.Discount, 'taxes' : InvoiceEstimate.Tax, 'line_item_taxes' : InvoiceEstimate.LineItemTax, 'line_item_tiers' : InvoiceEstimate.LineItemTier, 'line_item_discounts' : InvoiceEstimate.LineItemDiscount});
        estimate.init_dependant_list(self._response['estimate'], 'credit_note_estimates',
        {'line_items' : CreditNoteEstimate.LineItem, 'discounts' : CreditNoteEstimate.Discount, 'taxes' : CreditNoteEstimate.Tax, 'line_item_taxes' : CreditNoteEstimate.LineItemTax, 'line_item_discounts' : CreditNoteEstimate.LineItemDiscount, 'line_item_tiers' : CreditNoteEstimate.LineItemTier});
        estimate.init_dependant_list(self._response['estimate'], 'unbilled_charge_estimates',
        {'tiers' : UnbilledCharge.Tier});
        return estimate;

    @property
    def quote(self):
        quote = self._get('quote', Quote,
        {'line_items' : Quote.LineItem, 'discounts' : Quote.Discount, 'line_item_discounts' : Quote.LineItemDiscount, 'taxes' : Quote.Tax, 'line_item_taxes' : Quote.LineItemTax, 'line_item_tiers' : Quote.LineItemTier, 'shipping_address' : Quote.ShippingAddress, 'billing_address' : Quote.BillingAddress});
        return quote;

    @property
    def quoted_subscription(self):
        quoted_subscription = self._get('quoted_subscription', QuotedSubscription,
        {'addons' : QuotedSubscription.Addon, 'event_based_addons' : QuotedSubscription.EventBasedAddon, 'coupons' : QuotedSubscription.Coupon, 'subscription_items' : QuotedSubscription.SubscriptionItem, 'item_tiers' : QuotedSubscription.ItemTier, 'quoted_contract_term' : QuotedSubscription.QuotedContractTerm});
        return quoted_subscription;

    @property
    def quoted_charge(self):
        quoted_charge = self._get('quoted_charge', QuotedCharge,
        {'charges' : QuotedCharge.Charge, 'addons' : QuotedCharge.Addon, 'invoice_items' : QuotedCharge.InvoiceItem, 'item_tiers' : QuotedCharge.ItemTier, 'coupons' : QuotedCharge.Coupon});
        return quoted_charge;

    @property
    def quote_line_group(self):
        quote_line_group = self._get('quote_line_group', QuoteLineGroup,
        {'line_items' : QuoteLineGroup.LineItem, 'discounts' : QuoteLineGroup.Discount, 'line_item_discounts' : QuoteLineGroup.LineItemDiscount, 'taxes' : QuoteLineGroup.Tax, 'line_item_taxes' : QuoteLineGroup.LineItemTax});
        return quote_line_group;

    @property
    def plan(self):
        plan = self._get('plan', Plan,
        {'tiers' : Plan.Tier, 'applicable_addons' : Plan.ApplicableAddon, 'attached_addons' : Plan.AttachedAddon, 'event_based_addons' : Plan.EventBasedAddon});
        return plan;

    @property
    def addon(self):
        addon = self._get('addon', Addon,
        {'tiers' : Addon.Tier});
        return addon;

    @property
    def coupon(self):
        coupon = self._get('coupon', Coupon,
        {'item_constraints' : Coupon.ItemConstraint, 'item_constraint_criteria' : Coupon.ItemConstraintCriteria});
        return coupon;

    @property
    def coupon_set(self):
        coupon_set = self._get('coupon_set', CouponSet);
        return coupon_set;

    @property
    def coupon_code(self):
        coupon_code = self._get('coupon_code', CouponCode);
        return coupon_code;

    @property
    def address(self):
        address = self._get('address', Address);
        return address;

    @property
    def usage(self):
        usage = self._get('usage', Usage);
        return usage;

    @property
    def event(self):
        event = self._get('event', Event,
        {'webhooks' : Event.Webhook});
        return event;

    @property
    def comment(self):
        comment = self._get('comment', Comment);
        return comment;

    @property
    def download(self):
        download = self._get('download', Download);
        return download;

    @property
    def portal_session(self):
        portal_session = self._get('portal_session', PortalSession,
        {'linked_customers' : PortalSession.LinkedCustomer});
        return portal_session;

    @property
    def site_migration_detail(self):
        site_migration_detail = self._get('site_migration_detail', SiteMigrationDetail);
        return site_migration_detail;

    @property
    def resource_migration(self):
        resource_migration = self._get('resource_migration', ResourceMigration);
        return resource_migration;

    @property
    def time_machine(self):
        time_machine = self._get('time_machine', TimeMachine);
        return time_machine;

    @property
    def export(self):
        export = self._get('export', Export,
        {'download' : Export.Download});
        return export;

    @property
    def payment_intent(self):
        payment_intent = self._get('payment_intent', PaymentIntent,
        {'payment_attempt' : PaymentIntent.PaymentAttempt});
        return payment_intent;

    @property
    def item_family(self):
        item_family = self._get('item_family', ItemFamily);
        return item_family;

    @property
    def item(self):
        item = self._get('item', Item,
        {'applicable_items' : Item.ApplicableItem});
        return item;

    @property
    def item_price(self):
        item_price = self._get('item_price', ItemPrice,
        {'tiers' : ItemPrice.Tier, 'tax_detail' : ItemPrice.TaxDetail, 'accounting_detail' : ItemPrice.AccountingDetail});
        return item_price;

    @property
    def attached_item(self):
        attached_item = self._get('attached_item', AttachedItem);
        return attached_item;

    @property
    def differential_price(self):
        differential_price = self._get('differential_price', DifferentialPrice,
        {'tiers' : DifferentialPrice.Tier, 'parent_periods' : DifferentialPrice.ParentPeriod});
        return differential_price;


    @property
    def unbilled_charges(self):
        unbilled_charges = self._get_list('unbilled_charges', UnbilledCharge,
        {'tiers' : UnbilledCharge.Tier});
        return unbilled_charges;

    @property
    def credit_notes(self):
        credit_notes = self._get_list('credit_notes', CreditNote,
        {'line_items' : CreditNote.LineItem, 'discounts' : CreditNote.Discount, 'line_item_discounts' : CreditNote.LineItemDiscount, 'line_item_tiers' : CreditNote.LineItemTier, 'taxes' : CreditNote.Tax, 'line_item_taxes' : CreditNote.LineItemTax, 'linked_refunds' : CreditNote.LinkedRefund, 'allocations' : CreditNote.Allocation});
        return credit_notes;

    @property
    def advance_invoice_schedules(self):
        advance_invoice_schedules = self._get_list('advance_invoice_schedules', AdvanceInvoiceSchedule,
        {'fixed_interval_schedule' : AdvanceInvoiceSchedule.FixedIntervalSchedule, 'specific_dates_schedule' : AdvanceInvoiceSchedule.SpecificDatesSchedule});
        return advance_invoice_schedules;

    @property
    def hierarchies(self):
        hierarchies = self._get_list('hierarchies', Hierarchy,
        {});
        return hierarchies;

    @property
    def invoices(self):
        invoices = self._get_list('invoices', Invoice,
        {'line_items' : Invoice.LineItem, 'discounts' : Invoice.Discount, 'line_item_discounts' : Invoice.LineItemDiscount, 'taxes' : Invoice.Tax, 'line_item_taxes' : Invoice.LineItemTax, 'line_item_tiers' : Invoice.LineItemTier, 'linked_payments' : Invoice.LinkedPayment, 'dunning_attempts' : Invoice.DunningAttempt, 'applied_credits' : Invoice.AppliedCredit, 'adjustment_credit_notes' : Invoice.AdjustmentCreditNote, 'issued_credit_notes' : Invoice.IssuedCreditNote, 'linked_orders' : Invoice.LinkedOrder, 'notes' : Invoice.Note, 'shipping_address' : Invoice.ShippingAddress, 'billing_address' : Invoice.BillingAddress});
        return invoices;

    @property
    def differential_prices(self):
        differential_prices = self._get_list('differential_prices', DifferentialPrice,
        {'tiers' : DifferentialPrice.Tier, 'parent_periods' : DifferentialPrice.ParentPeriod});
        return differential_prices;


    def _get_list(self, type, cls, sub_types={}, dependant_types={}, dependant_sub_types={}):
        if not type in self._response:
            return None
        
        set_val = []
        for obj in self._response[type]:
            if isinstance(obj, dict):
                model = cls.construct(obj, sub_types, dependant_types)
                for k in dependant_sub_types:
                    model.init_dependant(obj, k, dependant_sub_types[k])
                set_val.append(model)

        self._response_obj[type] = set_val
        return self._response_obj[type]

    def _get(self, type, cls, sub_types=None, dependant_types=None):
        if not type in self._response:
            return None

        if not type in self._response_obj:
            self._response_obj[type] = cls.construct(self._response[type], sub_types, dependant_types)

        return self._response_obj[type]

    def __str__(self):
        return json.dumps(self._response, indent=4)


class Content(Result):
    pass
