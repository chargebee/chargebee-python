from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import (
    payment_intent,
    card,
    card,
    payment_source,
    resource_migration,
    hierarchy,
    contact,
    transaction,
)


@dataclass
class BillingAddressResponse(Model):
    raw_data: Dict[Any, Any] = None
    first_name: str = None
    last_name: str = None
    email: str = None
    company: str = None
    phone: str = None
    line1: str = None
    line2: str = None
    line3: str = None
    city: str = None
    state_code: str = None
    state: str = None
    country: str = None
    zip: str = None
    validation_status: str = None


@dataclass
class ReferralUrlResponse(Model):
    raw_data: Dict[Any, Any] = None
    external_customer_id: str = None
    referral_sharing_url: str = None
    created_at: int = None
    updated_at: int = None
    referral_campaign_id: str = None
    referral_account_id: str = None
    referral_external_campaign_id: str = None
    referral_system: str = None


@dataclass
class ContactResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    label: str = None
    enabled: bool = None
    send_account_email: bool = None
    send_billing_email: bool = None


@dataclass
class PaymentMethodResponse(Model):
    raw_data: Dict[Any, Any] = None
    type: str = None
    gateway: str = None
    gateway_account_id: str = None
    status: str = None
    reference_id: str = None


@dataclass
class BalanceResponse(Model):
    raw_data: Dict[Any, Any] = None
    promotional_credits: int = None
    excess_payments: int = None
    refundable_credits: int = None
    unbilled_charges: int = None
    currency_code: str = None
    balance_currency_code: str = None


@dataclass
class EntityIdentifierResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    value: str = None
    scheme: str = None
    standard: str = None


@dataclass
class TaxProvidersFieldResponse(Model):
    raw_data: Dict[Any, Any] = None
    provider_name: str = None
    field_id: str = None
    field_value: str = None


@dataclass
class RelationshipResponse(Model):
    raw_data: Dict[Any, Any] = None
    parent_id: str = None
    payment_owner_id: str = None
    invoice_owner_id: str = None


@dataclass
class ParentAccountAccessResponse(Model):
    raw_data: Dict[Any, Any] = None
    portal_edit_child_subscriptions: str = None
    portal_download_child_invoices: str = None
    send_subscription_emails: bool = None
    send_invoice_emails: bool = None
    send_payment_emails: bool = None


@dataclass
class ChildAccountAccessResponse(Model):
    raw_data: Dict[Any, Any] = None
    portal_edit_subscriptions: str = None
    portal_download_invoices: str = None
    send_subscription_emails: bool = None
    send_invoice_emails: bool = None
    send_payment_emails: bool = None


@dataclass
class CustomerResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    company: str = None
    vat_number: str = None
    auto_collection: str = None
    offline_payment_method: str = None
    net_term_days: int = None
    vat_number_validated_time: int = None
    vat_number_status: str = None
    allow_direct_debit: bool = None
    is_location_valid: bool = None
    created_at: int = None
    created_from_ip: str = None
    exemption_details: List[Dict[Any, Any]] = None
    taxability: str = None
    entity_code: str = None
    exempt_number: str = None
    resource_version: int = None
    updated_at: int = None
    locale: str = None
    billing_date: int = None
    billing_month: int = None
    billing_date_mode: str = None
    billing_day_of_week: str = None
    billing_day_of_week_mode: str = None
    pii_cleared: str = None
    auto_close_invoices: bool = None
    channel: str = None
    active_id: str = None
    card_status: str = None
    fraud_flag: str = None
    primary_payment_source_id: str = None
    backup_payment_source_id: str = None
    billing_address: BillingAddressResponse = None
    referral_urls: List[ReferralUrlResponse] = None
    contacts: List[ContactResponse] = None
    payment_method: PaymentMethodResponse = None
    invoice_notes: str = None
    business_entity_id: str = None
    preferred_currency_code: str = None
    promotional_credits: int = None
    unbilled_charges: int = None
    refundable_credits: int = None
    excess_payments: int = None
    balances: List[BalanceResponse] = None
    entity_identifiers: List[EntityIdentifierResponse] = None
    tax_providers_fields: List[TaxProvidersFieldResponse] = None
    is_einvoice_enabled: bool = None
    einvoicing_method: str = None
    meta_data: Dict[Any, Any] = None
    deleted: bool = None
    registered_for_gst: bool = None
    consolidated_invoicing: bool = None
    customer_type: str = None
    business_customer_without_vat_number: bool = None
    client_profile_id: str = None
    relationship: RelationshipResponse = None
    use_default_hierarchy_settings: bool = None
    parent_account_access: ParentAccountAccessResponse = None
    child_account_access: ChildAccountAccessResponse = None
    vat_number_prefix: str = None
    entity_identifier_scheme: str = None
    entity_identifier_standard: str = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse
    card: "card.CardResponse" = None


@dataclass
class ListCustomerResponse:
    customer: CustomerResponse
    card: "card.CardResponse" = None


@dataclass
class ListResponse(Response):

    list: List[ListCustomerResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):

    customer: CustomerResponse
    card: "card.CardResponse" = None


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse
    card: "card.CardResponse" = None


@dataclass
class UpdatePaymentMethodResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse
    card: "card.CardResponse" = None


@dataclass
class UpdateBillingInfoResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse
    card: "card.CardResponse" = None


@dataclass
class ContactsForCustomerCustomerResponse:
    contact: "contact.ContactResponse"


@dataclass
class ContactsForCustomerResponse(Response):

    list: List[ContactsForCustomerCustomerResponse]
    next_offset: str = None


@dataclass
class AssignPaymentRoleResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse
    payment_source: "payment_source.PaymentSourceResponse"


@dataclass
class AddContactResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse
    card: "card.CardResponse" = None


@dataclass
class UpdateContactResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse
    card: "card.CardResponse" = None


@dataclass
class DeleteContactResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse
    card: "card.CardResponse" = None


@dataclass
class AddPromotionalCreditsResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse


@dataclass
class DeductPromotionalCreditsResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse


@dataclass
class SetPromotionalCreditsResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse


@dataclass
class RecordExcessPaymentResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse
    transaction: "transaction.TransactionResponse"


@dataclass
class CollectPaymentResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse
    transaction: "transaction.TransactionResponse"


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse
    card: "card.CardResponse" = None


@dataclass
class MoveResponse(Response):
    is_idempotency_replayed: bool
    resource_migration: "resource_migration.ResourceMigrationResponse"


@dataclass
class ChangeBillingDateResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse


@dataclass
class MergeResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse


@dataclass
class ClearPersonalDataResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse


@dataclass
class RelationshipsResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse


@dataclass
class DeleteRelationshipResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse


@dataclass
class HierarchyResponse(Response):

    hierarchies: List["hierarchy.HierarchyResponse"]


@dataclass
class UpdateHierarchySettingsResponse(Response):
    is_idempotency_replayed: bool
    customer: CustomerResponse
