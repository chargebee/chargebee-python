from chargebee.compat import json
from chargebee.models import *


class Result(object):

    IDEMPOTENCY_REPLAYED_HEADER = 'chargebee-idempotency-replayed'

    def __init__(self, response, response_header=None, http_status_code=None):
        self._response = response
        self._response_obj = {}
        self._response_header = response_header
        self._http_status_code = http_status_code

    @property
    def get_response_headers(self):
        return self._response_header

    @property
    def get_http_status_code(self):
        return self._http_status_code

    @property
    def is_idempotency_replayed(self):
        value = self._response_header.get(self.IDEMPOTENCY_REPLAYED_HEADER)
        if value is not None:
            return bool(value)
        else:
            return False

    @property
    def subscription(self):
        subscription = self._get('subscription', Subscription,
        {'subscription_items' : Subscription.SubscriptionItem, 'item_tiers' : Subscription.ItemTier, 'charged_items' : Subscription.ChargedItem, 'addons' : Subscription.Addon, 'event_based_addons' : Subscription.EventBasedAddon, 'charged_event_based_addons' : Subscription.ChargedEventBasedAddon, 'coupons' : Subscription.Coupon, 'shipping_address' : Subscription.ShippingAddress, 'referral_info' : Subscription.ReferralInfo, 'billing_override' : Subscription.BillingOverride, 'contract_term' : Subscription.ContractTerm, 'discounts' : Subscription.Discount});
        return subscription;

    @property
    def contract_term(self):
        contract_term = self._get('contract_term', ContractTerm);
        return contract_term;

    @property
    def discount(self):
        discount = self._get('discount', Discount);
        return discount;

    @property
    def advance_invoice_schedule(self):
        advance_invoice_schedule = self._get('advance_invoice_schedule', AdvanceInvoiceSchedule,
        {'fixed_interval_schedule' : AdvanceInvoiceSchedule.FixedIntervalSchedule, 'specific_dates_schedule' : AdvanceInvoiceSchedule.SpecificDatesSchedule});
        return advance_invoice_schedule;

    @property
    def customer(self):
        customer = self._get('customer', Customer,
        {'billing_address' : Customer.BillingAddress, 'referral_urls' : Customer.ReferralUrl, 'contacts' : Customer.Contact, 'payment_method' : Customer.PaymentMethod, 'balances' : Customer.Balance, 'entity_identifiers' : Customer.EntityIdentifier, 'tax_providers_fields' : Customer.TaxProvidersField, 'relationship' : Customer.Relationship, 'parent_account_access' : Customer.ParentAccountAccess, 'child_account_access' : Customer.ChildAccountAccess});
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
    def business_entity_transfer(self):
        business_entity_transfer = self._get('business_entity_transfer', BusinessEntityTransfer);
        return business_entity_transfer;

    @property
    def token(self):
        token = self._get('token', Token);
        return token;

    @property
    def payment_source(self):
        payment_source = self._get('payment_source', PaymentSource,
        {'card' : PaymentSource.Card, 'bank_account' : PaymentSource.BankAccount, 'cust_voucher_source' : PaymentSource.CustVoucherSource, 'billing_address' : PaymentSource.BillingAddress, 'amazon_payment' : PaymentSource.AmazonPayment, 'upi' : PaymentSource.Upi, 'paypal' : PaymentSource.Paypal, 'venmo' : PaymentSource.Venmo, 'klarna_pay_now' : PaymentSource.KlarnaPayNow, 'mandates' : PaymentSource.Mandate});
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
        {'line_items' : Invoice.LineItem, 'discounts' : Invoice.Discount, 'line_item_discounts' : Invoice.LineItemDiscount, 'taxes' : Invoice.Tax, 'line_item_taxes' : Invoice.LineItemTax, 'line_item_credits' : Invoice.LineItemCredit, 'line_item_tiers' : Invoice.LineItemTier, 'linked_payments' : Invoice.LinkedPayment, 'dunning_attempts' : Invoice.DunningAttempt, 'applied_credits' : Invoice.AppliedCredit, 'adjustment_credit_notes' : Invoice.AdjustmentCreditNote, 'issued_credit_notes' : Invoice.IssuedCreditNote, 'linked_orders' : Invoice.LinkedOrder, 'notes' : Invoice.Note, 'shipping_address' : Invoice.ShippingAddress, 'statement_descriptor' : Invoice.StatementDescriptor, 'billing_address' : Invoice.BillingAddress, 'einvoice' : Invoice.Einvoice, 'site_details_at_creation' : Invoice.SiteDetailsAtCreation, 'tax_origin' : Invoice.TaxOrigin, 'line_item_addresses' : Invoice.LineItemAddress});
        return invoice;

    @property
    def payment_reference_number(self):
        payment_reference_number = self._get('payment_reference_number', PaymentReferenceNumber);
        return payment_reference_number;

    @property
    def payment_schedule(self):
        payment_schedule = self._get('payment_schedule', PaymentSchedule,
        {'schedule_entries' : PaymentSchedule.ScheduleEntry});
        return payment_schedule;

    @property
    def tax_withheld(self):
        tax_withheld = self._get('tax_withheld', TaxWithheld);
        return tax_withheld;

    @property
    def credit_note(self):
        credit_note = self._get('credit_note', CreditNote,
        {'einvoice' : CreditNote.Einvoice, 'line_items' : CreditNote.LineItem, 'discounts' : CreditNote.Discount, 'line_item_discounts' : CreditNote.LineItemDiscount, 'line_item_tiers' : CreditNote.LineItemTier, 'taxes' : CreditNote.Tax, 'line_item_taxes' : CreditNote.LineItemTax, 'linked_refunds' : CreditNote.LinkedRefund, 'allocations' : CreditNote.Allocation, 'shipping_address' : CreditNote.ShippingAddress, 'billing_address' : CreditNote.BillingAddress, 'site_details_at_creation' : CreditNote.SiteDetailsAtCreation, 'tax_origin' : CreditNote.TaxOrigin, 'line_item_addresses' : CreditNote.LineItemAddress});
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
        {'linked_invoices' : Transaction.LinkedInvoice, 'linked_credit_notes' : Transaction.LinkedCreditNote, 'linked_refunds' : Transaction.LinkedRefund, 'linked_payments' : Transaction.LinkedPayment, 'gateway_error_detail' : Transaction.GatewayErrorDetail});
        return transaction;

    @property
    def hosted_page(self):
        hosted_page = self._get('hosted_page', HostedPage);
        return hosted_page;

    @property
    def estimate(self):
        estimate = self._get('estimate', Estimate, {},
        {'subscription_estimate' : SubscriptionEstimate, 'subscription_estimates' : SubscriptionEstimate, 'invoice_estimate' : InvoiceEstimate, 'invoice_estimates' : InvoiceEstimate, 'payment_schedule_estimates' : PaymentScheduleEstimate, 'next_invoice_estimate' : InvoiceEstimate, 'credit_note_estimates' : CreditNoteEstimate, 'unbilled_charge_estimates' : UnbilledCharge});
        estimate.init_dependant(self._response['estimate'], 'subscription_estimate',
        {'shipping_address' : SubscriptionEstimate.ShippingAddress, 'contract_term' : SubscriptionEstimate.ContractTerm});
        estimate.init_dependant(self._response['estimate'], 'invoice_estimate',
        {'line_items' : InvoiceEstimate.LineItem, 'discounts' : InvoiceEstimate.Discount, 'taxes' : InvoiceEstimate.Tax, 'line_item_taxes' : InvoiceEstimate.LineItemTax, 'line_item_tiers' : InvoiceEstimate.LineItemTier, 'line_item_credits' : InvoiceEstimate.LineItemCredit, 'line_item_discounts' : InvoiceEstimate.LineItemDiscount, 'line_item_addresses' : InvoiceEstimate.LineItemAddress});
        estimate.init_dependant(self._response['estimate'], 'next_invoice_estimate',
        {'line_items' : InvoiceEstimate.LineItem, 'discounts' : InvoiceEstimate.Discount, 'taxes' : InvoiceEstimate.Tax, 'line_item_taxes' : InvoiceEstimate.LineItemTax, 'line_item_tiers' : InvoiceEstimate.LineItemTier, 'line_item_credits' : InvoiceEstimate.LineItemCredit, 'line_item_discounts' : InvoiceEstimate.LineItemDiscount, 'line_item_addresses' : InvoiceEstimate.LineItemAddress});
        estimate.init_dependant_list(self._response['estimate'], 'subscription_estimates',
        {'shipping_address' : SubscriptionEstimate.ShippingAddress, 'contract_term' : SubscriptionEstimate.ContractTerm});
        estimate.init_dependant_list(self._response['estimate'], 'invoice_estimates',
        {'line_items' : InvoiceEstimate.LineItem, 'discounts' : InvoiceEstimate.Discount, 'taxes' : InvoiceEstimate.Tax, 'line_item_taxes' : InvoiceEstimate.LineItemTax, 'line_item_tiers' : InvoiceEstimate.LineItemTier, 'line_item_credits' : InvoiceEstimate.LineItemCredit, 'line_item_discounts' : InvoiceEstimate.LineItemDiscount, 'line_item_addresses' : InvoiceEstimate.LineItemAddress});
        estimate.init_dependant_list(self._response['estimate'], 'payment_schedule_estimates',
        {'schedule_entries' : PaymentScheduleEstimate.ScheduleEntry});
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
        {'tiers' : Plan.Tier, 'tax_providers_fields' : Plan.TaxProvidersField, 'applicable_addons' : Plan.ApplicableAddon, 'attached_addons' : Plan.AttachedAddon, 'event_based_addons' : Plan.EventBasedAddon});
        return plan;

    @property
    def addon(self):
        addon = self._get('addon', Addon,
        {'tiers' : Addon.Tier, 'tax_providers_fields' : Addon.TaxProvidersField});
        return addon;

    @property
    def coupon(self):
        coupon = self._get('coupon', Coupon,
        {'item_constraints' : Coupon.ItemConstraint, 'item_constraint_criteria' : Coupon.ItemConstraintCriteria, 'coupon_constraints' : Coupon.CouponConstraint});
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
    def gateway_error_detail(self):
        gateway_error_detail = self._get('gateway_error_detail', GatewayErrorDetail);
        return gateway_error_detail;

    @property
    def item_family(self):
        item_family = self._get('item_family', ItemFamily);
        return item_family;

    @property
    def item(self):
        item = self._get('item', Item,
        {'applicable_items' : Item.ApplicableItem, 'bundle_items' : Item.BundleItem, 'bundle_configuration' : Item.BundleConfiguration});
        return item;

    @property
    def price_variant(self):
        price_variant = self._get('price_variant', PriceVariant,
        {'attributes' : PriceVariant.Attribute});
        return price_variant;

    @property
    def attribute(self):
        attribute = self._get('attribute', Attribute);
        return attribute;

    @property
    def item_price(self):
        item_price = self._get('item_price', ItemPrice,
        {'tiers' : ItemPrice.Tier, 'tax_detail' : ItemPrice.TaxDetail, 'tax_providers_fields' : ItemPrice.TaxProvidersField, 'accounting_detail' : ItemPrice.AccountingDetail});
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
    def configuration(self):
        configuration = self._get('configuration', Configuration);
        return configuration;

    @property
    def feature(self):
        feature = self._get('feature', Feature,
        {'levels' : Feature.Level});
        return feature;

    @property
    def impacted_subscription(self):
        impacted_subscription = self._get('impacted_subscription', ImpactedSubscription,
        {'download' : ImpactedSubscription.Download});
        return impacted_subscription;

    @property
    def impacted_item(self):
        impacted_item = self._get('impacted_item', ImpactedItem,
        {'download' : ImpactedItem.Download});
        return impacted_item;

    @property
    def impacted_item_price(self):
        impacted_item_price = self._get('impacted_item_price', ImpactedItemPrice,
        {'download' : ImpactedItemPrice.Download});
        return impacted_item_price;

    @property
    def metadata(self):
        metadata = self._get('metadata', Metadata);
        return metadata;

    @property
    def subscription_entitlement(self):
        subscription_entitlement = self._get('subscription_entitlement', SubscriptionEntitlement,
        {'component' : SubscriptionEntitlement.Component});
        return subscription_entitlement;

    @property
    def customer_entitlement(self):
        customer_entitlement = self._get('customer_entitlement', CustomerEntitlement);
        return customer_entitlement;

    @property
    def item_entitlement(self):
        item_entitlement = self._get('item_entitlement', ItemEntitlement);
        return item_entitlement;

    @property
    def entitlement(self):
        entitlement = self._get('entitlement', Entitlement);
        return entitlement;

    @property
    def in_app_subscription(self):
        in_app_subscription = self._get('in_app_subscription', InAppSubscription);
        return in_app_subscription;

    @property
    def non_subscription(self):
        non_subscription = self._get('non_subscription', NonSubscription);
        return non_subscription;

    @property
    def entitlement_override(self):
        entitlement_override = self._get('entitlement_override', EntitlementOverride);
        return entitlement_override;

    @property
    def business_entity(self):
        business_entity = self._get('business_entity', BusinessEntity);
        return business_entity;

    @property
    def purchase(self):
        purchase = self._get('purchase', Purchase);
        return purchase;

    @property
    def payment_voucher(self):
        payment_voucher = self._get('payment_voucher', PaymentVoucher,
        {'linked_invoices' : PaymentVoucher.LinkedInvoice});
        return payment_voucher;

    @property
    def currency(self):
        currency = self._get('currency', Currency);
        return currency;

    @property
    def ramp(self):
        ramp = self._get('ramp', Ramp,
        {'items_to_add' : Ramp.ItemsToAdd, 'items_to_update' : Ramp.ItemsToUpdate, 'coupons_to_add' : Ramp.CouponsToAdd, 'discounts_to_add' : Ramp.DiscountsToAdd, 'item_tiers' : Ramp.ItemTier, 'status_transition_reason' : Ramp.StatusTransitionReason});
        return ramp;

    @property
    def payment_schedule_scheme(self):
        payment_schedule_scheme = self._get('payment_schedule_scheme', PaymentScheduleScheme,
        {'preferred_schedules' : PaymentScheduleScheme.PreferredSchedule});
        return payment_schedule_scheme;

    @property
    def pricing_page_session(self):
        pricing_page_session = self._get('pricing_page_session', PricingPageSession);
        return pricing_page_session;

    @property
    def omnichannel_subscription(self):
        omnichannel_subscription = self._get('omnichannel_subscription', OmnichannelSubscription, {},
        {'omnichannel_subscription_items' : OmnichannelSubscriptionItem});
        omnichannel_subscription.init_dependant_list(self._response['omnichannel_subscription'], 'omnichannel_subscription_items',
        {'upcoming_renewal' : OmnichannelSubscriptionItem.UpcomingRenewal});
        return omnichannel_subscription;

    @property
    def omnichannel_transaction(self):
        omnichannel_transaction = self._get('omnichannel_transaction', OmnichannelTransaction);
        return omnichannel_transaction;

    @property
    def omnichannel_subscription_item(self):
        omnichannel_subscription_item = self._get('omnichannel_subscription_item', OmnichannelSubscriptionItem,
        {'upcoming_renewal' : OmnichannelSubscriptionItem.UpcomingRenewal});
        return omnichannel_subscription_item;

    @property
    def recorded_purchase(self):
        recorded_purchase = self._get('recorded_purchase', RecordedPurchase,
        {'linked_omnichannel_subscriptions' : RecordedPurchase.LinkedOmnichannelSubscription, 'error_detail' : RecordedPurchase.ErrorDetail});
        return recorded_purchase;

    @property
    def rule(self):
        rule = self._get('rule', Rule);
        return rule;

    @property
    def usage_event(self):
        usage_event = self._get('usage_event', UsageEvent);
        return usage_event;

    @property
    def omnichannel_subscription_item_scheduled_change(self):
        omnichannel_subscription_item_scheduled_change = self._get('omnichannel_subscription_item_scheduled_change', OmnichannelSubscriptionItemScheduledChange,
        {'current_state' : OmnichannelSubscriptionItemScheduledChange.CurrentState, 'scheduled_state' : OmnichannelSubscriptionItemScheduledChange.ScheduledState});
        return omnichannel_subscription_item_scheduled_change;

    @property
    def usage_file(self):
        usage_file = self._get('usage_file', UsageFile,
        {'upload_detail' : UsageFile.UploadDetail});
        return usage_file;

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
        {'line_items' : Invoice.LineItem, 'discounts' : Invoice.Discount, 'line_item_discounts' : Invoice.LineItemDiscount, 'taxes' : Invoice.Tax, 'line_item_taxes' : Invoice.LineItemTax, 'line_item_credits' : Invoice.LineItemCredit, 'line_item_tiers' : Invoice.LineItemTier, 'linked_payments' : Invoice.LinkedPayment, 'dunning_attempts' : Invoice.DunningAttempt, 'applied_credits' : Invoice.AppliedCredit, 'adjustment_credit_notes' : Invoice.AdjustmentCreditNote, 'issued_credit_notes' : Invoice.IssuedCreditNote, 'linked_orders' : Invoice.LinkedOrder, 'notes' : Invoice.Note, 'shipping_address' : Invoice.ShippingAddress, 'statement_descriptor' : Invoice.StatementDescriptor, 'billing_address' : Invoice.BillingAddress, 'einvoice' : Invoice.Einvoice, 'site_details_at_creation' : Invoice.SiteDetailsAtCreation, 'tax_origin' : Invoice.TaxOrigin, 'line_item_addresses' : Invoice.LineItemAddress});
        return invoices;

    @property
    def differential_prices(self):
        differential_prices = self._get_list('differential_prices', DifferentialPrice,
        {'tiers' : DifferentialPrice.Tier, 'parent_periods' : DifferentialPrice.ParentPeriod});
        return differential_prices;

    @property
    def payment_schedules(self):
        payment_schedules = self._get_list('payment_schedules', PaymentSchedule,
        {'schedule_entries' : PaymentSchedule.ScheduleEntry});
        return payment_schedules;

    @property
    def credit_notes(self):
        credit_notes = self._get_list('credit_notes', CreditNote,
        {'einvoice' : CreditNote.Einvoice, 'line_items' : CreditNote.LineItem, 'discounts' : CreditNote.Discount, 'line_item_discounts' : CreditNote.LineItemDiscount, 'line_item_tiers' : CreditNote.LineItemTier, 'taxes' : CreditNote.Tax, 'line_item_taxes' : CreditNote.LineItemTax, 'linked_refunds' : CreditNote.LinkedRefund, 'allocations' : CreditNote.Allocation, 'shipping_address' : CreditNote.ShippingAddress, 'billing_address' : CreditNote.BillingAddress, 'site_details_at_creation' : CreditNote.SiteDetailsAtCreation, 'tax_origin' : CreditNote.TaxOrigin, 'line_item_addresses' : CreditNote.LineItemAddress});
        return credit_notes;

    @property
    def unbilled_charges(self):
        unbilled_charges = self._get_list('unbilled_charges', UnbilledCharge,
        {'tiers' : UnbilledCharge.Tier});
        return unbilled_charges;

    @property
    def downloads(self):
        downloads = self._get_list('downloads', Download,
        {});
        return downloads;

    @property
    def configurations(self):
        configurations = self._get_list('configurations', Configuration,
        {});
        return configurations;

    @property
    def in_app_subscriptions(self):
        in_app_subscriptions = self._get_list('in_app_subscriptions', InAppSubscription,
        {});
        return in_app_subscriptions;


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