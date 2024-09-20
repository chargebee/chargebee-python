from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums, payment_intent


class VatNumberStatus(Enum):
    VALID = "valid"
    INVALID = "invalid"
    NOT_VALIDATED = "not_validated"
    UNDETERMINED = "undetermined"

    def __str__(self):
        return self.value


class BillingDayOfWeek(Enum):
    SUNDAY = "sunday"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"

    def __str__(self):
        return self.value


class PiiCleared(Enum):
    ACTIVE = "active"
    SCHEDULED_FOR_CLEAR = "scheduled_for_clear"
    CLEARED = "cleared"

    def __str__(self):
        return self.value


class CardStatus(Enum):
    NO_CARD = "no_card"
    VALID = "valid"
    EXPIRING = "expiring"
    EXPIRED = "expired"
    PENDING_VERIFICATION = "pending_verification"
    INVALID = "invalid"

    def __str__(self):
        return self.value


class FraudFlag(Enum):
    SAFE = "safe"
    SUSPICIOUS = "suspicious"
    FRAUDULENT = "fraudulent"

    def __str__(self):
        return self.value


class PaymentMethodStatus(Enum):
    VALID = "valid"
    EXPIRING = "expiring"
    EXPIRED = "expired"
    INVALID = "invalid"
    PENDING_VERIFICATION = "pending_verification"

    def __str__(self):
        return self.value


class ParentAccountAccessPortalEditChildSubscriptions(Enum):
    YES = "yes"
    VIEW_ONLY = "view_only"
    NO = "no"

    def __str__(self):
        return self.value


class ParentAccountAccessPortalDownloadChildInvoices(Enum):
    YES = "yes"
    VIEW_ONLY = "view_only"
    NO = "no"

    def __str__(self):
        return self.value


class ChildAccountAccessPortalEditSubscriptions(Enum):
    YES = "yes"
    VIEW_ONLY = "view_only"

    def __str__(self):
        return self.value


class ChildAccountAccessPortalDownloadInvoices(Enum):
    YES = "yes"
    VIEW_ONLY = "view_only"
    NO = "no"

    def __str__(self):
        return self.value


class BillingAddress(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    state: NotRequired[str]
    country: NotRequired[str]
    zip: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class ReferralUrl(TypedDict):
    external_customer_id: NotRequired[str]
    referral_sharing_url: Required[str]
    created_at: Required[int]
    updated_at: Required[int]
    referral_campaign_id: Required[str]
    referral_account_id: Required[str]
    referral_external_campaign_id: NotRequired[str]
    referral_system: Required[enums.ReferralSystem]


class Contact(TypedDict):
    id: Required[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: Required[str]
    phone: NotRequired[str]
    label: NotRequired[str]
    enabled: Required[bool]
    send_account_email: Required[bool]
    send_billing_email: Required[bool]


class PaymentMethod(TypedDict):
    type: Required[enums.Type]
    gateway: Required[enums.Gateway]
    gateway_account_id: NotRequired[str]
    status: Required[PaymentMethodStatus]
    reference_id: Required[str]


class Balance(TypedDict):
    promotional_credits: Required[int]
    excess_payments: Required[int]
    refundable_credits: Required[int]
    unbilled_charges: Required[int]
    currency_code: Required[str]
    balance_currency_code: Required[str]


class EntityIdentifier(TypedDict):
    id: Required[str]
    value: NotRequired[str]
    scheme: Required[str]
    standard: NotRequired[str]


class TaxProvidersField(TypedDict):
    provider_name: Required[str]
    field_id: Required[str]
    field_value: Required[str]


class Relationship(TypedDict):
    parent_id: NotRequired[str]
    payment_owner_id: Required[str]
    invoice_owner_id: Required[str]


class ParentAccountAccess(TypedDict):
    portal_edit_child_subscriptions: NotRequired[
        ParentAccountAccessPortalEditChildSubscriptions
    ]
    portal_download_child_invoices: NotRequired[
        ParentAccountAccessPortalDownloadChildInvoices
    ]
    send_subscription_emails: Required[bool]
    send_invoice_emails: Required[bool]
    send_payment_emails: Required[bool]


class ChildAccountAccess(TypedDict):
    portal_edit_subscriptions: NotRequired[ChildAccountAccessPortalEditSubscriptions]
    portal_download_invoices: NotRequired[ChildAccountAccessPortalDownloadInvoices]
    send_subscription_emails: Required[bool]
    send_invoice_emails: Required[bool]
    send_payment_emails: Required[bool]


class CreateCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]
    tmp_token: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    number: NotRequired[str]
    expiry_month: NotRequired[int]
    expiry_year: NotRequired[int]
    cvv: NotRequired[str]
    billing_addr1: NotRequired[str]
    billing_addr2: NotRequired[str]
    billing_city: NotRequired[str]
    billing_state_code: NotRequired[str]
    billing_state: NotRequired[str]
    billing_zip: NotRequired[str]
    billing_country: NotRequired[str]
    ip_address: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class CreateBankAccountParams(TypedDict):
    gateway_account_id: NotRequired[str]
    iban: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    company: NotRequired[str]
    email: NotRequired[str]
    phone: NotRequired[str]
    bank_name: NotRequired[str]
    account_number: NotRequired[str]
    routing_number: NotRequired[str]
    bank_code: NotRequired[str]
    account_type: NotRequired[enums.AccountType]
    account_holder_type: NotRequired[enums.AccountHolderType]
    echeck_type: NotRequired[enums.EcheckType]
    issuing_country: NotRequired[str]
    swedish_identity_number: NotRequired[str]
    billing_address: NotRequired[Dict[Any, Any]]


class CreatePaymentMethodParams(TypedDict):
    type: NotRequired[enums.Type]
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]
    reference_id: NotRequired[str]
    tmp_token: NotRequired[str]
    issuing_country: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class CreatePaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    reference_id: NotRequired[str]
    gw_payment_method_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class CreateBillingAddressParams(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CreateEntityIdentifierParams(TypedDict):
    id: NotRequired[str]
    scheme: NotRequired[str]
    value: NotRequired[str]
    standard: NotRequired[str]


class CreateTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class ListRelationshipParams(TypedDict):
    ParentId: NotRequired[Filters.StringFilter]
    PaymentOwnerId: NotRequired[Filters.StringFilter]
    InvoiceOwnerId: NotRequired[Filters.StringFilter]


class UpdateTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class UpdatePaymentMethodPaymentMethodParams(TypedDict):
    type: Required[enums.Type]
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]
    reference_id: NotRequired[str]
    tmp_token: NotRequired[str]
    issuing_country: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class UpdateBillingInfoBillingAddressParams(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class UpdateBillingInfoEntityIdentifierParams(TypedDict):
    id: NotRequired[str]
    scheme: NotRequired[str]
    value: NotRequired[str]
    operation: NotRequired[enums.Operation]
    standard: NotRequired[str]


class UpdateBillingInfoTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class AddContactContactParams(TypedDict):
    id: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: Required[str]
    phone: NotRequired[str]
    label: NotRequired[str]
    enabled: NotRequired[bool]
    send_billing_email: NotRequired[bool]
    send_account_email: NotRequired[bool]


class UpdateContactContactParams(TypedDict):
    id: Required[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    phone: NotRequired[str]
    label: NotRequired[str]
    enabled: NotRequired[bool]
    send_billing_email: NotRequired[bool]
    send_account_email: NotRequired[bool]


class DeleteContactContactParams(TypedDict):
    id: Required[str]


class RecordExcessPaymentTransactionParams(TypedDict):
    amount: Required[int]
    currency_code: NotRequired[str]
    date: Required[int]
    payment_method: Required[enums.PaymentMethod]
    reference_number: NotRequired[str]
    custom_payment_method_id: NotRequired[str]


class CollectPaymentInvoiceAllocationParams(TypedDict):
    invoice_id: Required[str]
    allocation_amount: NotRequired[int]


class CollectPaymentPaymentMethodParams(TypedDict):
    type: NotRequired[enums.Type]
    gateway_account_id: NotRequired[str]
    reference_id: NotRequired[str]
    tmp_token: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class CollectPaymentCardParams(TypedDict):
    gateway_account_id: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    number: NotRequired[str]
    expiry_month: NotRequired[int]
    expiry_year: NotRequired[int]
    cvv: NotRequired[str]
    billing_addr1: NotRequired[str]
    billing_addr2: NotRequired[str]
    billing_city: NotRequired[str]
    billing_state_code: NotRequired[str]
    billing_state: NotRequired[str]
    billing_zip: NotRequired[str]
    billing_country: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class CollectPaymentPaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    gw_payment_method_id: NotRequired[str]
    reference_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class MoveTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class MergeTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class RelationshipsParentAccountAccessParams(TypedDict):
    portal_edit_child_subscriptions: NotRequired[
        ParentAccountAccessPortalEditChildSubscriptions
    ]
    portal_download_child_invoices: NotRequired[
        ParentAccountAccessPortalDownloadChildInvoices
    ]
    send_subscription_emails: NotRequired[bool]
    send_payment_emails: NotRequired[bool]
    send_invoice_emails: NotRequired[bool]


class RelationshipsChildAccountAccessParams(TypedDict):
    portal_edit_subscriptions: NotRequired[ChildAccountAccessPortalEditSubscriptions]
    portal_download_invoices: NotRequired[ChildAccountAccessPortalDownloadInvoices]
    send_subscription_emails: NotRequired[bool]
    send_payment_emails: NotRequired[bool]
    send_invoice_emails: NotRequired[bool]


class UpdateHierarchySettingsParentAccountAccessParams(TypedDict):
    portal_edit_child_subscriptions: NotRequired[
        ParentAccountAccessPortalEditChildSubscriptions
    ]
    portal_download_child_invoices: NotRequired[
        ParentAccountAccessPortalDownloadChildInvoices
    ]
    send_subscription_emails: NotRequired[bool]
    send_payment_emails: NotRequired[bool]
    send_invoice_emails: NotRequired[bool]


class UpdateHierarchySettingsChildAccountAccessParams(TypedDict):
    portal_edit_subscriptions: NotRequired[ChildAccountAccessPortalEditSubscriptions]
    portal_download_invoices: NotRequired[ChildAccountAccessPortalDownloadInvoices]
    send_subscription_emails: NotRequired[bool]
    send_payment_emails: NotRequired[bool]
    send_invoice_emails: NotRequired[bool]
