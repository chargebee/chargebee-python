from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.filters import Filters


class MimeType(Enum):
    PDF = "pdf"
    ZIP = "zip"

    def __str__(self):
        return self.value


class Status(Enum):
    IN_PROCESS = "in_process"
    COMPLETED = "completed"
    FAILED = "failed"

    def __str__(self):
        return self.value


class Download(TypedDict):
    download_url: Required[str]
    valid_till: Required[int]
    mime_type: NotRequired[str]


class RevenueRecognitionInvoiceParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    Recurring: NotRequired[Filters.BooleanFilter]
    Status: NotRequired[Filters.EnumFilter]
    PriceType: NotRequired[Filters.EnumFilter]
    Date: NotRequired[Filters.TimestampFilter]
    PaidAt: NotRequired[Filters.TimestampFilter]
    Total: NotRequired[Filters.NumberFilter]
    AmountPaid: NotRequired[Filters.NumberFilter]
    AmountAdjusted: NotRequired[Filters.NumberFilter]
    CreditsApplied: NotRequired[Filters.NumberFilter]
    AmountDue: NotRequired[Filters.NumberFilter]
    DunningStatus: NotRequired[Filters.EnumFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    Channel: NotRequired[Filters.EnumFilter]


class RevenueRecognitionSubscriptionParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    CustomerId: NotRequired[Filters.StringFilter]
    Status: NotRequired[Filters.EnumFilter]
    CancelReason: NotRequired[Filters.EnumFilter]
    RemainingBillingCycles: NotRequired[Filters.NumberFilter]
    CreatedAt: NotRequired[Filters.TimestampFilter]
    ActivatedAt: NotRequired[Filters.TimestampFilter]
    NextBillingAt: NotRequired[Filters.TimestampFilter]
    CancelledAt: NotRequired[Filters.TimestampFilter]
    HasScheduledChanges: NotRequired[Filters.BooleanFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    OfflinePaymentMethod: NotRequired[Filters.EnumFilter]
    AutoCloseInvoices: NotRequired[Filters.BooleanFilter]
    Channel: NotRequired[Filters.EnumFilter]
    PlanId: NotRequired[Filters.StringFilter]


class RevenueRecognitionCustomerParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    FirstName: NotRequired[Filters.StringFilter]
    LastName: NotRequired[Filters.StringFilter]
    Email: NotRequired[Filters.StringFilter]
    Company: NotRequired[Filters.StringFilter]
    Phone: NotRequired[Filters.StringFilter]
    AutoCollection: NotRequired[Filters.EnumFilter]
    Taxability: NotRequired[Filters.EnumFilter]
    CreatedAt: NotRequired[Filters.TimestampFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    OfflinePaymentMethod: NotRequired[Filters.EnumFilter]
    AutoCloseInvoices: NotRequired[Filters.BooleanFilter]
    Channel: NotRequired[Filters.EnumFilter]


class RevenueRecognitionRelationshipParams(TypedDict):
    ParentId: NotRequired[Filters.StringFilter]
    PaymentOwnerId: NotRequired[Filters.StringFilter]
    InvoiceOwnerId: NotRequired[Filters.StringFilter]


class DeferredRevenueInvoiceParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    Recurring: NotRequired[Filters.BooleanFilter]
    Status: NotRequired[Filters.EnumFilter]
    PriceType: NotRequired[Filters.EnumFilter]
    Date: NotRequired[Filters.TimestampFilter]
    PaidAt: NotRequired[Filters.TimestampFilter]
    Total: NotRequired[Filters.NumberFilter]
    AmountPaid: NotRequired[Filters.NumberFilter]
    AmountAdjusted: NotRequired[Filters.NumberFilter]
    CreditsApplied: NotRequired[Filters.NumberFilter]
    AmountDue: NotRequired[Filters.NumberFilter]
    DunningStatus: NotRequired[Filters.EnumFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    Channel: NotRequired[Filters.EnumFilter]


class DeferredRevenueSubscriptionParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    CustomerId: NotRequired[Filters.StringFilter]
    Status: NotRequired[Filters.EnumFilter]
    CancelReason: NotRequired[Filters.EnumFilter]
    RemainingBillingCycles: NotRequired[Filters.NumberFilter]
    CreatedAt: NotRequired[Filters.TimestampFilter]
    ActivatedAt: NotRequired[Filters.TimestampFilter]
    NextBillingAt: NotRequired[Filters.TimestampFilter]
    CancelledAt: NotRequired[Filters.TimestampFilter]
    HasScheduledChanges: NotRequired[Filters.BooleanFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    OfflinePaymentMethod: NotRequired[Filters.EnumFilter]
    AutoCloseInvoices: NotRequired[Filters.BooleanFilter]
    Channel: NotRequired[Filters.EnumFilter]
    PlanId: NotRequired[Filters.StringFilter]


class DeferredRevenueCustomerParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    FirstName: NotRequired[Filters.StringFilter]
    LastName: NotRequired[Filters.StringFilter]
    Email: NotRequired[Filters.StringFilter]
    Company: NotRequired[Filters.StringFilter]
    Phone: NotRequired[Filters.StringFilter]
    AutoCollection: NotRequired[Filters.EnumFilter]
    Taxability: NotRequired[Filters.EnumFilter]
    CreatedAt: NotRequired[Filters.TimestampFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    OfflinePaymentMethod: NotRequired[Filters.EnumFilter]
    AutoCloseInvoices: NotRequired[Filters.BooleanFilter]
    Channel: NotRequired[Filters.EnumFilter]


class DeferredRevenueRelationshipParams(TypedDict):
    ParentId: NotRequired[Filters.StringFilter]
    PaymentOwnerId: NotRequired[Filters.StringFilter]
    InvoiceOwnerId: NotRequired[Filters.StringFilter]


class PlansPlanParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    Name: NotRequired[Filters.StringFilter]
    Price: NotRequired[Filters.NumberFilter]
    Period: NotRequired[Filters.NumberFilter]
    PeriodUnit: NotRequired[Filters.EnumFilter]
    TrialPeriod: NotRequired[Filters.NumberFilter]
    TrialPeriodUnit: NotRequired[Filters.EnumFilter]
    AddonApplicability: NotRequired[Filters.EnumFilter]
    Giftable: NotRequired[Filters.BooleanFilter]
    Status: NotRequired[Filters.EnumFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    Channel: NotRequired[Filters.EnumFilter]


class AddonsAddonParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    Name: NotRequired[Filters.StringFilter]
    ChargeType: NotRequired[Filters.EnumFilter]
    Price: NotRequired[Filters.NumberFilter]
    Period: NotRequired[Filters.NumberFilter]
    PeriodUnit: NotRequired[Filters.EnumFilter]
    Status: NotRequired[Filters.EnumFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    Channel: NotRequired[Filters.EnumFilter]


class CouponsCouponParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    Name: NotRequired[Filters.StringFilter]
    DiscountType: NotRequired[Filters.EnumFilter]
    DurationType: NotRequired[Filters.EnumFilter]
    Status: NotRequired[Filters.EnumFilter]
    ApplyOn: NotRequired[Filters.EnumFilter]
    CreatedAt: NotRequired[Filters.TimestampFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]


class CustomersCustomerParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    FirstName: NotRequired[Filters.StringFilter]
    LastName: NotRequired[Filters.StringFilter]
    Email: NotRequired[Filters.StringFilter]
    Company: NotRequired[Filters.StringFilter]
    Phone: NotRequired[Filters.StringFilter]
    AutoCollection: NotRequired[Filters.EnumFilter]
    Taxability: NotRequired[Filters.EnumFilter]
    CreatedAt: NotRequired[Filters.TimestampFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    OfflinePaymentMethod: NotRequired[Filters.EnumFilter]
    AutoCloseInvoices: NotRequired[Filters.BooleanFilter]
    Channel: NotRequired[Filters.EnumFilter]


class CustomersRelationshipParams(TypedDict):
    ParentId: NotRequired[Filters.StringFilter]
    PaymentOwnerId: NotRequired[Filters.StringFilter]
    InvoiceOwnerId: NotRequired[Filters.StringFilter]


class SubscriptionsSubscriptionParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    CustomerId: NotRequired[Filters.StringFilter]
    Status: NotRequired[Filters.EnumFilter]
    CancelReason: NotRequired[Filters.EnumFilter]
    RemainingBillingCycles: NotRequired[Filters.NumberFilter]
    CreatedAt: NotRequired[Filters.TimestampFilter]
    ActivatedAt: NotRequired[Filters.TimestampFilter]
    NextBillingAt: NotRequired[Filters.TimestampFilter]
    CancelledAt: NotRequired[Filters.TimestampFilter]
    HasScheduledChanges: NotRequired[Filters.BooleanFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    OfflinePaymentMethod: NotRequired[Filters.EnumFilter]
    AutoCloseInvoices: NotRequired[Filters.BooleanFilter]
    Channel: NotRequired[Filters.EnumFilter]
    PlanId: NotRequired[Filters.StringFilter]


class InvoicesInvoiceParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    SubscriptionId: NotRequired[Filters.StringFilter]
    CustomerId: NotRequired[Filters.StringFilter]
    Recurring: NotRequired[Filters.BooleanFilter]
    Status: NotRequired[Filters.EnumFilter]
    PriceType: NotRequired[Filters.EnumFilter]
    Date: NotRequired[Filters.TimestampFilter]
    PaidAt: NotRequired[Filters.TimestampFilter]
    Total: NotRequired[Filters.NumberFilter]
    AmountPaid: NotRequired[Filters.NumberFilter]
    AmountAdjusted: NotRequired[Filters.NumberFilter]
    CreditsApplied: NotRequired[Filters.NumberFilter]
    AmountDue: NotRequired[Filters.NumberFilter]
    DunningStatus: NotRequired[Filters.EnumFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    Channel: NotRequired[Filters.EnumFilter]


class CreditNotesCreditNoteParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    CustomerId: NotRequired[Filters.StringFilter]
    SubscriptionId: NotRequired[Filters.StringFilter]
    ReferenceInvoiceId: NotRequired[Filters.StringFilter]
    Type: NotRequired[Filters.EnumFilter]
    ReasonCode: NotRequired[Filters.EnumFilter]
    CreateReasonCode: NotRequired[Filters.StringFilter]
    Status: NotRequired[Filters.EnumFilter]
    Date: NotRequired[Filters.TimestampFilter]
    Total: NotRequired[Filters.NumberFilter]
    PriceType: NotRequired[Filters.EnumFilter]
    AmountAllocated: NotRequired[Filters.NumberFilter]
    AmountRefunded: NotRequired[Filters.NumberFilter]
    AmountAvailable: NotRequired[Filters.NumberFilter]
    VoidedAt: NotRequired[Filters.TimestampFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    Channel: NotRequired[Filters.EnumFilter]


class TransactionsTransactionParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    CustomerId: NotRequired[Filters.StringFilter]
    SubscriptionId: NotRequired[Filters.StringFilter]
    PaymentSourceId: NotRequired[Filters.StringFilter]
    PaymentMethod: NotRequired[Filters.EnumFilter]
    Gateway: NotRequired[Filters.EnumFilter]
    GatewayAccountId: NotRequired[Filters.StringFilter]
    IdAtGateway: NotRequired[Filters.StringFilter]
    ReferenceNumber: NotRequired[Filters.StringFilter]
    Type: NotRequired[Filters.EnumFilter]
    Date: NotRequired[Filters.TimestampFilter]
    Amount: NotRequired[Filters.NumberFilter]
    AmountCapturable: NotRequired[Filters.NumberFilter]
    Status: NotRequired[Filters.EnumFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]


class OrdersOrderParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    SubscriptionId: NotRequired[Filters.StringFilter]
    CustomerId: NotRequired[Filters.StringFilter]
    Status: NotRequired[Filters.EnumFilter]
    PriceType: NotRequired[Filters.EnumFilter]
    OrderDate: NotRequired[Filters.TimestampFilter]
    ShippingDate: NotRequired[Filters.TimestampFilter]
    ShippedAt: NotRequired[Filters.TimestampFilter]
    DeliveredAt: NotRequired[Filters.TimestampFilter]
    CancelledAt: NotRequired[Filters.TimestampFilter]
    AmountPaid: NotRequired[Filters.NumberFilter]
    RefundableCredits: NotRequired[Filters.NumberFilter]
    RefundableCreditsIssued: NotRequired[Filters.NumberFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    ResentStatus: NotRequired[Filters.EnumFilter]
    IsResent: NotRequired[Filters.BooleanFilter]
    OriginalOrderId: NotRequired[Filters.StringFilter]


class ItemFamiliesItemFamilyParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    Name: NotRequired[Filters.StringFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]


class ItemsItemParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    ItemFamilyId: NotRequired[Filters.StringFilter]
    Type: NotRequired[Filters.EnumFilter]
    Name: NotRequired[Filters.StringFilter]
    ItemApplicability: NotRequired[Filters.EnumFilter]
    Status: NotRequired[Filters.EnumFilter]
    IsGiftable: NotRequired[Filters.BooleanFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    EnabledForCheckout: NotRequired[Filters.BooleanFilter]
    EnabledInPortal: NotRequired[Filters.BooleanFilter]
    Metered: NotRequired[Filters.BooleanFilter]
    UsageCalculation: NotRequired[Filters.EnumFilter]
    Channel: NotRequired[Filters.EnumFilter]


class ItemPricesItemPriceParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    Name: NotRequired[Filters.StringFilter]
    PricingModel: NotRequired[Filters.EnumFilter]
    ItemId: NotRequired[Filters.StringFilter]
    PriceVariantId: NotRequired[Filters.StringFilter]
    TrialPeriod: NotRequired[Filters.NumberFilter]
    TrialPeriodUnit: NotRequired[Filters.EnumFilter]
    Status: NotRequired[Filters.EnumFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    PeriodUnit: NotRequired[Filters.EnumFilter]
    Period: NotRequired[Filters.NumberFilter]
    Channel: NotRequired[Filters.EnumFilter]


class AttachedItemsAttachedItemParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    ItemId: NotRequired[Filters.StringFilter]
    Type: NotRequired[Filters.EnumFilter]
    ChargeOnEvent: NotRequired[Filters.EnumFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    ParentItemId: NotRequired[Filters.StringFilter]


class DifferentialPricesDifferentialPriceParams(TypedDict):
    ItemPriceId: NotRequired[Filters.StringFilter]
    Id: NotRequired[Filters.StringFilter]
    ParentItemId: NotRequired[Filters.StringFilter]


class PriceVariantsPriceVariantParams(TypedDict):
    Id: NotRequired[Filters.StringFilter]
    Name: NotRequired[Filters.StringFilter]
    Status: NotRequired[Filters.EnumFilter]
    UpdatedAt: NotRequired[Filters.TimestampFilter]
    CreatedAt: NotRequired[Filters.TimestampFilter]
