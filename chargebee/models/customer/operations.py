from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums, payment_intent, card


@dataclass
class Customer:

    env: environment.Environment

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
        status: Required["Customer.PaymentMethodStatus"]
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
            "Customer.ParentAccountAccessPortalEditChildSubscriptions"
        ]
        portal_download_child_invoices: NotRequired[
            "Customer.ParentAccountAccessPortalDownloadChildInvoices"
        ]
        send_subscription_emails: Required[bool]
        send_invoice_emails: Required[bool]
        send_payment_emails: Required[bool]

    class ChildAccountAccess(TypedDict):
        portal_edit_subscriptions: NotRequired[
            "Customer.ChildAccountAccessPortalEditSubscriptions"
        ]
        portal_download_invoices: NotRequired[
            "Customer.ChildAccountAccessPortalDownloadInvoices"
        ]
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
        preferred_scheme: NotRequired["card.Card.PreferredScheme"]
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
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
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
        parent_id: NotRequired[Filters.StringFilter]
        payment_owner_id: NotRequired[Filters.StringFilter]
        invoice_owner_id: NotRequired[Filters.StringFilter]

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
        preferred_scheme: NotRequired["card.Card.PreferredScheme"]
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
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
        gw_payment_method_id: NotRequired[str]
        reference_id: NotRequired[str]
        additional_information: NotRequired[Dict[Any, Any]]

    class RelationshipsParentAccountAccessParams(TypedDict):
        portal_edit_child_subscriptions: NotRequired[
            "Customer.ParentAccountAccessPortalEditChildSubscriptions"
        ]
        portal_download_child_invoices: NotRequired[
            "Customer.ParentAccountAccessPortalDownloadChildInvoices"
        ]
        send_subscription_emails: NotRequired[bool]
        send_payment_emails: NotRequired[bool]
        send_invoice_emails: NotRequired[bool]

    class RelationshipsChildAccountAccessParams(TypedDict):
        portal_edit_subscriptions: NotRequired[
            "Customer.ChildAccountAccessPortalEditSubscriptions"
        ]
        portal_download_invoices: NotRequired[
            "Customer.ChildAccountAccessPortalDownloadInvoices"
        ]
        send_subscription_emails: NotRequired[bool]
        send_payment_emails: NotRequired[bool]
        send_invoice_emails: NotRequired[bool]

    class UpdateHierarchySettingsParentAccountAccessParams(TypedDict):
        portal_edit_child_subscriptions: NotRequired[
            "Customer.ParentAccountAccessPortalEditChildSubscriptions"
        ]
        portal_download_child_invoices: NotRequired[
            "Customer.ParentAccountAccessPortalDownloadChildInvoices"
        ]
        send_subscription_emails: NotRequired[bool]
        send_payment_emails: NotRequired[bool]
        send_invoice_emails: NotRequired[bool]

    class UpdateHierarchySettingsChildAccountAccessParams(TypedDict):
        portal_edit_subscriptions: NotRequired[
            "Customer.ChildAccountAccessPortalEditSubscriptions"
        ]
        portal_download_invoices: NotRequired[
            "Customer.ChildAccountAccessPortalDownloadInvoices"
        ]
        send_subscription_emails: NotRequired[bool]
        send_payment_emails: NotRequired[bool]
        send_invoice_emails: NotRequired[bool]

    class CreateParams(TypedDict):
        id: NotRequired[str]
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        email: NotRequired[str]
        preferred_currency_code: NotRequired[str]
        phone: NotRequired[str]
        company: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        net_term_days: NotRequired[int]
        allow_direct_debit: NotRequired[bool]
        vat_number: NotRequired[str]
        vat_number_prefix: NotRequired[str]
        entity_identifier_scheme: NotRequired[str]
        entity_identifier_standard: NotRequired[str]
        registered_for_gst: NotRequired[bool]
        is_einvoice_enabled: NotRequired[bool]
        einvoicing_method: NotRequired[enums.EinvoicingMethod]
        taxability: NotRequired[enums.Taxability]
        exemption_details: NotRequired[List[Dict[Any, Any]]]
        customer_type: NotRequired[enums.CustomerType]
        client_profile_id: NotRequired[str]
        taxjar_exemption_category: NotRequired[enums.TaxjarExemptionCategory]
        business_customer_without_vat_number: NotRequired[bool]
        locale: NotRequired[str]
        entity_code: NotRequired[enums.EntityCode]
        exempt_number: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
        auto_close_invoices: NotRequired[bool]
        consolidated_invoicing: NotRequired[bool]
        card: NotRequired["Customer.CreateCardParams"]
        bank_account: NotRequired["Customer.CreateBankAccountParams"]
        token_id: NotRequired[str]
        payment_method: NotRequired["Customer.CreatePaymentMethodParams"]
        payment_intent: NotRequired["Customer.CreatePaymentIntentParams"]
        billing_address: NotRequired["Customer.CreateBillingAddressParams"]
        entity_identifiers: NotRequired[List["Customer.CreateEntityIdentifierParams"]]
        business_entity_id: NotRequired[str]
        tax_providers_fields: NotRequired[
            List["Customer.CreateTaxProvidersFieldParams"]
        ]
        created_from_ip: NotRequired[str]
        invoice_notes: NotRequired[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        relationship: NotRequired["Customer.ListRelationshipParams"]
        include_deleted: NotRequired[bool]
        id: NotRequired[Filters.StringFilter]
        first_name: NotRequired[Filters.StringFilter]
        last_name: NotRequired[Filters.StringFilter]
        email: NotRequired[Filters.StringFilter]
        company: NotRequired[Filters.StringFilter]
        phone: NotRequired[Filters.StringFilter]
        auto_collection: NotRequired[Filters.EnumFilter]
        taxability: NotRequired[Filters.EnumFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        offline_payment_method: NotRequired[Filters.EnumFilter]
        auto_close_invoices: NotRequired[Filters.BooleanFilter]
        channel: NotRequired[Filters.EnumFilter]
        business_entity_id: NotRequired[Filters.StringFilter]
        sort_by: NotRequired[Filters.SortFilter]

    class UpdateParams(TypedDict):
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        email: NotRequired[str]
        preferred_currency_code: NotRequired[str]
        phone: NotRequired[str]
        company: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        allow_direct_debit: NotRequired[bool]
        net_term_days: NotRequired[int]
        taxability: NotRequired[enums.Taxability]
        exemption_details: NotRequired[List[Dict[Any, Any]]]
        customer_type: NotRequired[enums.CustomerType]
        client_profile_id: NotRequired[str]
        taxjar_exemption_category: NotRequired[enums.TaxjarExemptionCategory]
        locale: NotRequired[str]
        entity_code: NotRequired[enums.EntityCode]
        exempt_number: NotRequired[str]
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
        invoice_notes: NotRequired[str]
        auto_close_invoices: NotRequired[bool]
        meta_data: NotRequired[Dict[Any, Any]]
        fraud_flag: NotRequired["Customer.FraudFlag"]
        consolidated_invoicing: NotRequired[bool]
        tax_providers_fields: NotRequired[
            List["Customer.UpdateTaxProvidersFieldParams"]
        ]

    class UpdatePaymentMethodParams(TypedDict):
        payment_method: Required["Customer.UpdatePaymentMethodPaymentMethodParams"]

    class UpdateBillingInfoParams(TypedDict):
        billing_address: NotRequired["Customer.UpdateBillingInfoBillingAddressParams"]
        entity_identifiers: NotRequired[
            List["Customer.UpdateBillingInfoEntityIdentifierParams"]
        ]
        vat_number: NotRequired[str]
        vat_number_prefix: NotRequired[str]
        entity_identifier_scheme: NotRequired[str]
        entity_identifier_standard: NotRequired[str]
        registered_for_gst: NotRequired[bool]
        business_customer_without_vat_number: NotRequired[bool]
        is_einvoice_enabled: NotRequired[bool]
        einvoicing_method: NotRequired[enums.EinvoicingMethod]
        tax_providers_fields: NotRequired[
            List["Customer.UpdateBillingInfoTaxProvidersFieldParams"]
        ]

    class ContactsForCustomerParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class AssignPaymentRoleParams(TypedDict):
        payment_source_id: Required[str]
        role: Required[enums.Role]

    class AddContactParams(TypedDict):
        contact: Required["Customer.AddContactContactParams"]

    class UpdateContactParams(TypedDict):
        contact: Required["Customer.UpdateContactContactParams"]

    class DeleteContactParams(TypedDict):
        contact: Required["Customer.DeleteContactContactParams"]

    class AddPromotionalCreditsParams(TypedDict):
        amount: Required[int]
        currency_code: NotRequired[str]
        description: Required[str]
        credit_type: NotRequired[enums.CreditType]
        reference: NotRequired[str]

    class DeductPromotionalCreditsParams(TypedDict):
        amount: Required[int]
        currency_code: NotRequired[str]
        description: Required[str]
        credit_type: NotRequired[enums.CreditType]
        reference: NotRequired[str]

    class SetPromotionalCreditsParams(TypedDict):
        amount: Required[int]
        currency_code: NotRequired[str]
        description: Required[str]
        credit_type: NotRequired[enums.CreditType]
        reference: NotRequired[str]

    class RecordExcessPaymentParams(TypedDict):
        transaction: Required["Customer.RecordExcessPaymentTransactionParams"]
        comment: NotRequired[str]

    class CollectPaymentParams(TypedDict):
        amount: NotRequired[int]
        invoice_allocations: Required[
            List["Customer.CollectPaymentInvoiceAllocationParams"]
        ]
        payment_source_id: NotRequired[str]
        token_id: NotRequired[str]
        payment_method: NotRequired["Customer.CollectPaymentPaymentMethodParams"]
        card: NotRequired["Customer.CollectPaymentCardParams"]
        payment_intent: NotRequired["Customer.CollectPaymentPaymentIntentParams"]
        replace_primary_payment_source: NotRequired[bool]
        retain_payment_source: NotRequired[bool]
        payment_initiator: NotRequired[enums.PaymentInitiator]

    class DeleteParams(TypedDict):
        delete_payment_method: NotRequired[bool]

    class MoveParams(TypedDict):
        id_at_from_site: Required[str]
        from_site: Required[str]

    class ChangeBillingDateParams(TypedDict):
        billing_date: NotRequired[int]
        billing_month: NotRequired[int]
        billing_date_mode: NotRequired[enums.BillingDateMode]
        billing_day_of_week: NotRequired["Customer.BillingDayOfWeek"]
        billing_day_of_week_mode: NotRequired[enums.BillingDayOfWeekMode]

    class MergeParams(TypedDict):
        from_customer_id: Required[str]
        to_customer_id: Required[str]

    class RelationshipsParams(TypedDict):
        parent_id: NotRequired[str]
        payment_owner_id: NotRequired[str]
        invoice_owner_id: NotRequired[str]
        use_default_hierarchy_settings: NotRequired[bool]
        parent_account_access: NotRequired[
            "Customer.RelationshipsParentAccountAccessParams"
        ]
        child_account_access: NotRequired[
            "Customer.RelationshipsChildAccountAccessParams"
        ]

    class HierarchyParams(TypedDict):
        hierarchy_operation_type: Required[enums.HierarchyOperationType]

    class UpdateHierarchySettingsParams(TypedDict):
        use_default_hierarchy_settings: NotRequired[bool]
        parent_account_access: NotRequired[
            "Customer.UpdateHierarchySettingsParentAccountAccessParams"
        ]
        child_account_access: NotRequired[
            "Customer.UpdateHierarchySettingsChildAccountAccessParams"
        ]

    def create(self, params: CreateParams = None, headers=None) -> CreateResponse:
        jsonKeys = {
            "exemption_details": 0,
            "meta_data": 0,
            "additional_information": 1,
            "billing_address": 1,
        }
        return request.send(
            "post",
            request.uri_path("customers"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        return request.send_list_request(
            "get",
            request.uri_path("customers"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("customers", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
        )

    def update(self, id, params: UpdateParams = None, headers=None) -> UpdateResponse:
        jsonKeys = {
            "exemption_details": 0,
            "meta_data": 0,
        }
        return request.send(
            "post",
            request.uri_path("customers", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
        )

    def update_payment_method(
        self, id, params: UpdatePaymentMethodParams, headers=None
    ) -> UpdatePaymentMethodResponse:
        jsonKeys = {
            "additional_information": 1,
        }
        return request.send(
            "post",
            request.uri_path("customers", id, "update_payment_method"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdatePaymentMethodResponse,
            None,
            False,
            jsonKeys,
        )

    def update_billing_info(
        self, id, params: UpdateBillingInfoParams = None, headers=None
    ) -> UpdateBillingInfoResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "update_billing_info"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateBillingInfoResponse,
            None,
            False,
            jsonKeys,
        )

    def contacts_for_customer(
        self, id, params: ContactsForCustomerParams = None, headers=None
    ) -> ContactsForCustomerResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("customers", id, "contacts"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ContactsForCustomerResponse,
            None,
            False,
            jsonKeys,
        )

    def assign_payment_role(
        self, id, params: AssignPaymentRoleParams, headers=None
    ) -> AssignPaymentRoleResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "assign_payment_role"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AssignPaymentRoleResponse,
            None,
            False,
            jsonKeys,
        )

    def add_contact(
        self, id, params: AddContactParams, headers=None
    ) -> AddContactResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "add_contact"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AddContactResponse,
            None,
            False,
            jsonKeys,
        )

    def update_contact(
        self, id, params: UpdateContactParams, headers=None
    ) -> UpdateContactResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "update_contact"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateContactResponse,
            None,
            False,
            jsonKeys,
        )

    def delete_contact(
        self, id, params: DeleteContactParams, headers=None
    ) -> DeleteContactResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "delete_contact"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeleteContactResponse,
            None,
            False,
            jsonKeys,
        )

    def add_promotional_credits(
        self, id, params: AddPromotionalCreditsParams, headers=None
    ) -> AddPromotionalCreditsResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "add_promotional_credits"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AddPromotionalCreditsResponse,
            None,
            False,
            jsonKeys,
        )

    def deduct_promotional_credits(
        self, id, params: DeductPromotionalCreditsParams, headers=None
    ) -> DeductPromotionalCreditsResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "deduct_promotional_credits"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeductPromotionalCreditsResponse,
            None,
            False,
            jsonKeys,
        )

    def set_promotional_credits(
        self, id, params: SetPromotionalCreditsParams, headers=None
    ) -> SetPromotionalCreditsResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "set_promotional_credits"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            SetPromotionalCreditsResponse,
            None,
            False,
            jsonKeys,
        )

    def record_excess_payment(
        self, id, params: RecordExcessPaymentParams, headers=None
    ) -> RecordExcessPaymentResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "record_excess_payment"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RecordExcessPaymentResponse,
            None,
            False,
            jsonKeys,
        )

    def collect_payment(
        self, id, params: CollectPaymentParams, headers=None
    ) -> CollectPaymentResponse:
        jsonKeys = {
            "additional_information": 1,
        }
        return request.send(
            "post",
            request.uri_path("customers", id, "collect_payment"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CollectPaymentResponse,
            None,
            False,
            jsonKeys,
        )

    def delete(self, id, params: DeleteParams = None, headers=None) -> DeleteResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "delete"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
        )

    def move(self, params: MoveParams, headers=None) -> MoveResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", "move"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            MoveResponse,
            None,
            False,
            jsonKeys,
        )

    def change_billing_date(
        self, id, params: ChangeBillingDateParams = None, headers=None
    ) -> ChangeBillingDateResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "change_billing_date"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ChangeBillingDateResponse,
            None,
            False,
            jsonKeys,
        )

    def merge(self, params: MergeParams, headers=None) -> MergeResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", "merge"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            MergeResponse,
            None,
            False,
            jsonKeys,
        )

    def clear_personal_data(self, id, headers=None) -> ClearPersonalDataResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "clear_personal_data"),
            self.env,
            None,
            headers,
            ClearPersonalDataResponse,
            None,
            False,
            jsonKeys,
        )

    def relationships(
        self, id, params: RelationshipsParams = None, headers=None
    ) -> RelationshipsResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "relationships"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RelationshipsResponse,
            None,
            False,
            jsonKeys,
        )

    def delete_relationship(self, id, headers=None) -> DeleteRelationshipResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "delete_relationship"),
            self.env,
            None,
            headers,
            DeleteRelationshipResponse,
            None,
            False,
            jsonKeys,
        )

    def hierarchy(self, id, params: HierarchyParams, headers=None) -> HierarchyResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("customers", id, "hierarchy"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            HierarchyResponse,
            None,
            False,
            jsonKeys,
        )

    def update_hierarchy_settings(
        self, id, params: UpdateHierarchySettingsParams = None, headers=None
    ) -> UpdateHierarchySettingsResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "update_hierarchy_settings"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateHierarchySettingsResponse,
            None,
            False,
            jsonKeys,
        )
