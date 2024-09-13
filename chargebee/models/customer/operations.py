from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any


class Customer:

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
        card: NotRequired[CreateCardParams]
        bank_account: NotRequired[CreateBankAccountParams]
        token_id: NotRequired[str]
        payment_method: NotRequired[CreatePaymentMethodParams]
        payment_intent: NotRequired[CreatePaymentIntentParams]
        billing_address: NotRequired[CreateBillingAddressParams]
        entity_identifiers: NotRequired[List[CreateEntityIdentifierParams]]
        business_entity_id: NotRequired[str]
        tax_providers_fields: NotRequired[List[CreateTaxProvidersFieldParams]]
        created_from_ip: NotRequired[str]
        invoice_notes: NotRequired[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        relationship: NotRequired[ListRelationshipParams]
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
        fraud_flag: NotRequired[FraudFlag]
        consolidated_invoicing: NotRequired[bool]
        tax_providers_fields: NotRequired[List[UpdateTaxProvidersFieldParams]]

    class UpdatePaymentMethodParams(TypedDict):
        payment_method: Required[UpdatePaymentMethodPaymentMethodParams]

    class UpdateBillingInfoParams(TypedDict):
        billing_address: NotRequired[UpdateBillingInfoBillingAddressParams]
        entity_identifiers: NotRequired[List[UpdateBillingInfoEntityIdentifierParams]]
        vat_number: NotRequired[str]
        vat_number_prefix: NotRequired[str]
        entity_identifier_scheme: NotRequired[str]
        entity_identifier_standard: NotRequired[str]
        registered_for_gst: NotRequired[bool]
        business_customer_without_vat_number: NotRequired[bool]
        is_einvoice_enabled: NotRequired[bool]
        einvoicing_method: NotRequired[enums.EinvoicingMethod]
        tax_providers_fields: NotRequired[
            List[UpdateBillingInfoTaxProvidersFieldParams]
        ]

    class ContactsForCustomerParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class AssignPaymentRoleParams(TypedDict):
        payment_source_id: Required[str]
        role: Required[enums.Role]

    class AddContactParams(TypedDict):
        contact: Required[AddContactContactParams]

    class UpdateContactParams(TypedDict):
        contact: Required[UpdateContactContactParams]

    class DeleteContactParams(TypedDict):
        contact: Required[DeleteContactContactParams]

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
        transaction: Required[RecordExcessPaymentTransactionParams]
        comment: NotRequired[str]

    class CollectPaymentParams(TypedDict):
        amount: NotRequired[int]
        invoice_allocations: Required[List[CollectPaymentInvoiceAllocationParams]]
        payment_source_id: NotRequired[str]
        token_id: NotRequired[str]
        payment_method: NotRequired[CollectPaymentPaymentMethodParams]
        card: NotRequired[CollectPaymentCardParams]
        payment_intent: NotRequired[CollectPaymentPaymentIntentParams]
        replace_primary_payment_source: NotRequired[bool]
        retain_payment_source: NotRequired[bool]
        payment_initiator: NotRequired[enums.PaymentInitiator]

    class DeleteParams(TypedDict):
        delete_payment_method: NotRequired[bool]

    class MoveParams(TypedDict):
        id_at_from_site: Required[str]
        from_site: Required[str]
        tax_providers_fields: NotRequired[List[MoveTaxProvidersFieldParams]]

    class ChangeBillingDateParams(TypedDict):
        billing_date: NotRequired[int]
        billing_month: NotRequired[int]
        billing_date_mode: NotRequired[enums.BillingDateMode]
        billing_day_of_week: NotRequired[BillingDayOfWeek]
        billing_day_of_week_mode: NotRequired[enums.BillingDayOfWeekMode]

    class MergeParams(TypedDict):
        from_customer_id: Required[str]
        to_customer_id: Required[str]
        tax_providers_fields: NotRequired[List[MergeTaxProvidersFieldParams]]

    class RelationshipsParams(TypedDict):
        parent_id: NotRequired[str]
        payment_owner_id: NotRequired[str]
        invoice_owner_id: NotRequired[str]
        use_default_hierarchy_settings: NotRequired[bool]
        parent_account_access: NotRequired[RelationshipsParentAccountAccessParams]
        child_account_access: NotRequired[RelationshipsChildAccountAccessParams]

    class HierarchyParams(TypedDict):
        hierarchy_operation_type: Required[enums.HierarchyOperationType]

    class UpdateHierarchySettingsParams(TypedDict):
        use_default_hierarchy_settings: NotRequired[bool]
        parent_account_access: NotRequired[
            UpdateHierarchySettingsParentAccountAccessParams
        ]
        child_account_access: NotRequired[
            UpdateHierarchySettingsChildAccountAccessParams
        ]

    @staticmethod
    def create(params: CreateParams = None, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("customers"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("customers"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("customers", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def update(
        id, params: UpdateParams = None, env=None, headers=None
    ) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("customers", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def update_payment_method(
        id, params: UpdatePaymentMethodParams, env=None, headers=None
    ) -> UpdatePaymentMethodResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "update_payment_method"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdatePaymentMethodResponse,
        )

    @staticmethod
    def update_billing_info(
        id, params: UpdateBillingInfoParams = None, env=None, headers=None
    ) -> UpdateBillingInfoResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "update_billing_info"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateBillingInfoResponse,
        )

    @staticmethod
    def contacts_for_customer(
        id, params: ContactsForCustomerParams = None, env=None, headers=None
    ) -> ContactsForCustomerResponse:
        return request.send(
            "get",
            request.uri_path("customers", id, "contacts"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ContactsForCustomerResponse,
        )

    @staticmethod
    def assign_payment_role(
        id, params: AssignPaymentRoleParams, env=None, headers=None
    ) -> AssignPaymentRoleResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "assign_payment_role"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AssignPaymentRoleResponse,
        )

    @staticmethod
    def add_contact(
        id, params: AddContactParams, env=None, headers=None
    ) -> AddContactResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "add_contact"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AddContactResponse,
        )

    @staticmethod
    def update_contact(
        id, params: UpdateContactParams, env=None, headers=None
    ) -> UpdateContactResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "update_contact"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateContactResponse,
        )

    @staticmethod
    def delete_contact(
        id, params: DeleteContactParams, env=None, headers=None
    ) -> DeleteContactResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "delete_contact"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            DeleteContactResponse,
        )

    @staticmethod
    def add_promotional_credits(
        id, params: AddPromotionalCreditsParams, env=None, headers=None
    ) -> AddPromotionalCreditsResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "add_promotional_credits"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AddPromotionalCreditsResponse,
        )

    @staticmethod
    def deduct_promotional_credits(
        id, params: DeductPromotionalCreditsParams, env=None, headers=None
    ) -> DeductPromotionalCreditsResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "deduct_promotional_credits"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            DeductPromotionalCreditsResponse,
        )

    @staticmethod
    def set_promotional_credits(
        id, params: SetPromotionalCreditsParams, env=None, headers=None
    ) -> SetPromotionalCreditsResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "set_promotional_credits"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            SetPromotionalCreditsResponse,
        )

    @staticmethod
    def record_excess_payment(
        id, params: RecordExcessPaymentParams, env=None, headers=None
    ) -> RecordExcessPaymentResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "record_excess_payment"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RecordExcessPaymentResponse,
        )

    @staticmethod
    def collect_payment(
        id, params: CollectPaymentParams, env=None, headers=None
    ) -> CollectPaymentResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "collect_payment"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CollectPaymentResponse,
        )

    @staticmethod
    def delete(
        id, params: DeleteParams = None, env=None, headers=None
    ) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "delete"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def move(params: MoveParams, env=None, headers=None) -> MoveResponse:
        return request.send(
            "post",
            request.uri_path("customers", "move"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            MoveResponse,
        )

    @staticmethod
    def change_billing_date(
        id, params: ChangeBillingDateParams = None, env=None, headers=None
    ) -> ChangeBillingDateResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "change_billing_date"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ChangeBillingDateResponse,
        )

    @staticmethod
    def merge(params: MergeParams, env=None, headers=None) -> MergeResponse:
        return request.send(
            "post",
            request.uri_path("customers", "merge"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            MergeResponse,
        )

    @staticmethod
    def clear_personal_data(id, env=None, headers=None) -> ClearPersonalDataResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "clear_personal_data"),
            None,
            env,
            headers,
            ClearPersonalDataResponse,
        )

    @staticmethod
    def relationships(
        id, params: RelationshipsParams = None, env=None, headers=None
    ) -> RelationshipsResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "relationships"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RelationshipsResponse,
        )

    @staticmethod
    def delete_relationship(id, env=None, headers=None) -> DeleteRelationshipResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "delete_relationship"),
            None,
            env,
            headers,
            DeleteRelationshipResponse,
        )

    @staticmethod
    def hierarchy(
        id, params: HierarchyParams, env=None, headers=None
    ) -> HierarchyResponse:
        return request.send(
            "get",
            request.uri_path("customers", id, "hierarchy"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            HierarchyResponse,
        )

    @staticmethod
    def update_hierarchy_settings(
        id, params: UpdateHierarchySettingsParams = None, env=None, headers=None
    ) -> UpdateHierarchySettingsResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "update_hierarchy_settings"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateHierarchySettingsResponse,
        )
