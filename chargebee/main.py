import os.path
from dataclasses import dataclass

import chargebee
from chargebee.environment import Environment


@dataclass
class Chargebee:
    env: Environment = None
    idempotency_header: str = "chargebee-idempotency-key"

    verify_ca_certs: bool = True
    ca_cert_path = os.path.join(os.path.dirname(__file__), "ssl", "ca-certs.crt")

    def __init__(
        self,
        api_key: str,
        site: str,
        chargebee_domain: str = None,
        protocol: str = None,
        connection_time_out: int = None,
        read_time_out: int = None,
        use_async_client: bool = False,
    ):
        self.env = Environment({"api_key": api_key, "site": site})
        if chargebee_domain is not None:
            self.update_chargebee_domain(chargebee_domain)
        if protocol is not None:
            self.update_protocol(protocol)
        if connection_time_out is not None:
            self.update_connect_timeout_secs(connection_time_out)
        if read_time_out is not None:
            self.update_read_timeout_secs(read_time_out)
        if use_async_client:
            self.env.use_async_client = True
        self.env.set_api_endpoint()

        self.Addon = chargebee.Addon(self.env)
        self.Address = chargebee.Address(self.env)
        self.AdvanceInvoiceSchedule = chargebee.AdvanceInvoiceSchedule(self.env)
        self.AttachedItem = chargebee.AttachedItem(self.env)
        self.Attribute = chargebee.Attribute(self.env)
        self.BillingConfiguration = chargebee.BillingConfiguration(self.env)
        self.Brand = chargebee.Brand(self.env)
        self.BusinessEntity = chargebee.BusinessEntity(self.env)
        self.BusinessEntityTransfer = chargebee.BusinessEntityTransfer(self.env)
        self.Card = chargebee.Card(self.env)
        self.Comment = chargebee.Comment(self.env)
        self.Configuration = chargebee.Configuration(self.env)
        self.Contact = chargebee.Contact(self.env)
        self.ContractTerm = chargebee.ContractTerm(self.env)
        self.Coupon = chargebee.Coupon(self.env)
        self.CouponCode = chargebee.CouponCode(self.env)
        self.CouponSet = chargebee.CouponSet(self.env)
        self.CreditNote = chargebee.CreditNote(self.env)
        self.CreditNoteEstimate = chargebee.CreditNoteEstimate(self.env)
        self.Currency = chargebee.Currency(self.env)
        self.Customer = chargebee.Customer(self.env)
        self.CustomerEntitlement = chargebee.CustomerEntitlement(self.env)
        self.DifferentialPrice = chargebee.DifferentialPrice(self.env)
        self.Discount = chargebee.Discount(self.env)
        self.Download = chargebee.Download(self.env)
        self.Einvoice = chargebee.Einvoice(self.env)
        self.Entitlement = chargebee.Entitlement(self.env)
        self.EntitlementOverride = chargebee.EntitlementOverride(self.env)
        self.Estimate = chargebee.Estimate(self.env)
        self.Event = chargebee.Event(self.env)
        self.Export = chargebee.Export(self.env)
        self.Feature = chargebee.Feature(self.env)
        self.GatewayErrorDetail = chargebee.GatewayErrorDetail(self.env)
        self.Gift = chargebee.Gift(self.env)
        self.Hierarchy = chargebee.Hierarchy(self.env)
        self.HostedPage = chargebee.HostedPage(self.env)
        self.ImpactedCustomer = chargebee.ImpactedCustomer(self.env)
        self.ImpactedItem = chargebee.ImpactedItem(self.env)
        self.ImpactedItemPrice = chargebee.ImpactedItemPrice(self.env)
        self.ImpactedSubscription = chargebee.ImpactedSubscription(self.env)
        self.InAppSubscription = chargebee.InAppSubscription(self.env)
        self.Invoice = chargebee.Invoice(self.env)
        self.InvoiceEstimate = chargebee.InvoiceEstimate(self.env)
        self.Item = chargebee.Item(self.env)
        self.ItemEntitlement = chargebee.ItemEntitlement(self.env)
        self.ItemFamily = chargebee.ItemFamily(self.env)
        self.ItemPrice = chargebee.ItemPrice(self.env)
        self.Metadata = chargebee.Metadata(self.env)
        self.OfferEvent = chargebee.OfferEvent(self.env)
        self.OfferFulfillment = chargebee.OfferFulfillment(self.env)
        self.OmnichannelOneTimeOrder = chargebee.OmnichannelOneTimeOrder(self.env)
        self.OmnichannelOneTimeOrderItem = chargebee.OmnichannelOneTimeOrderItem(
            self.env
        )
        self.OmnichannelSubscription = chargebee.OmnichannelSubscription(self.env)
        self.OmnichannelSubscriptionItem = chargebee.OmnichannelSubscriptionItem(
            self.env
        )
        self.OmnichannelSubscriptionItemOffer = (
            chargebee.OmnichannelSubscriptionItemOffer(self.env)
        )
        self.OmnichannelSubscriptionItemScheduledChange = (
            chargebee.OmnichannelSubscriptionItemScheduledChange(self.env)
        )
        self.OmnichannelTransaction = chargebee.OmnichannelTransaction(self.env)
        self.Order = chargebee.Order(self.env)
        self.PaymentIntent = chargebee.PaymentIntent(self.env)
        self.PaymentReferenceNumber = chargebee.PaymentReferenceNumber(self.env)
        self.PaymentSchedule = chargebee.PaymentSchedule(self.env)
        self.PaymentScheduleEstimate = chargebee.PaymentScheduleEstimate(self.env)
        self.PaymentScheduleScheme = chargebee.PaymentScheduleScheme(self.env)
        self.PaymentSource = chargebee.PaymentSource(self.env)
        self.PaymentVoucher = chargebee.PaymentVoucher(self.env)
        self.PersonalizedOffer = chargebee.PersonalizedOffer(self.env)
        self.Plan = chargebee.Plan(self.env)
        self.PortalSession = chargebee.PortalSession(self.env)
        self.PriceVariant = chargebee.PriceVariant(self.env)
        self.PricingPageSession = chargebee.PricingPageSession(self.env)
        self.PromotionalCredit = chargebee.PromotionalCredit(self.env)
        self.Purchase = chargebee.Purchase(self.env)
        self.Quote = chargebee.Quote(self.env)
        self.QuoteLineGroup = chargebee.QuoteLineGroup(self.env)
        self.QuotedCharge = chargebee.QuotedCharge(self.env)
        self.QuotedDeltaRamp = chargebee.QuotedDeltaRamp(self.env)
        self.QuotedRamp = chargebee.QuotedRamp(self.env)
        self.QuotedSubscription = chargebee.QuotedSubscription(self.env)
        self.Ramp = chargebee.Ramp(self.env)
        self.RecordedPurchase = chargebee.RecordedPurchase(self.env)
        self.ResourceMigration = chargebee.ResourceMigration(self.env)
        self.Rule = chargebee.Rule(self.env)
        self.SiteMigrationDetail = chargebee.SiteMigrationDetail(self.env)
        self.Subscription = chargebee.Subscription(self.env)
        self.SubscriptionEntitlement = chargebee.SubscriptionEntitlement(self.env)
        self.SubscriptionEntitlementsCreatedDetail = (
            chargebee.SubscriptionEntitlementsCreatedDetail(self.env)
        )
        self.SubscriptionEntitlementsUpdatedDetail = (
            chargebee.SubscriptionEntitlementsUpdatedDetail(self.env)
        )
        self.SubscriptionEstimate = chargebee.SubscriptionEstimate(self.env)
        self.TaxWithheld = chargebee.TaxWithheld(self.env)
        self.ThirdPartyPaymentMethod = chargebee.ThirdPartyPaymentMethod(self.env)
        self.TimeMachine = chargebee.TimeMachine(self.env)
        self.Token = chargebee.Token(self.env)
        self.Transaction = chargebee.Transaction(self.env)
        self.UnbilledCharge = chargebee.UnbilledCharge(self.env)
        self.Usage = chargebee.Usage(self.env)
        self.UsageEvent = chargebee.UsageEvent(self.env)
        self.UsageFile = chargebee.UsageFile(self.env)
        self.VirtualBankAccount = chargebee.VirtualBankAccount(self.env)
        self.WebhookEndpoint = chargebee.WebhookEndpoint(self.env)

    def update_connect_timeout_secs(self, connect_timeout):
        self.env.connect_timeout = connect_timeout

    def update_read_timeout_secs(self, read_timeout):
        self.env.read_timeout = read_timeout

    def update_chargebee_domain(self, domain):
        self.env.chargebee_domain = domain

    def update_protocol(self, protocol):
        if protocol == "http":
            self.verify_ca_certs = False
        self.env.protocol = protocol

    def update_export_retry_delay_ms(self, export_retry_delay_ms):
        self.env.export_retry_delay_ms = export_retry_delay_ms

    def update_time_travel_retry_delay_ms(self, time_travel_retry_delay_ms):
        self.env.time_travel_retry_delay_ms = time_travel_retry_delay_ms

    def update_retry_config(self, retry_config):
        self.env.retry_config = retry_config

    def update_enable_debug_logs(self, enable_debug_logs):
        self.env.enable_debug_logs = enable_debug_logs
