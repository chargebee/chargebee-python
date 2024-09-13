from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class PaymentSource:

    class CreateUsingTempTokenParams(TypedDict):
        customer_id: Required[str]
        gateway_account_id: NotRequired[str]
        type: Required[enums.Type]
        tmp_token: Required[str]
        issuing_country: NotRequired[str]
        replace_primary_payment_source: NotRequired[bool]
        additional_information: NotRequired[Dict[Any, Any]]

    class CreateUsingPermanentTokenParams(TypedDict):
        customer_id: Required[str]
        type: Required[enums.Type]
        gateway_account_id: NotRequired[str]
        reference_id: NotRequired[str]
        issuing_country: NotRequired[str]
        replace_primary_payment_source: NotRequired[bool]
        payment_method_token: NotRequired[str]
        customer_profile_token: NotRequired[str]
        network_transaction_id: NotRequired[str]
        mandate_id: NotRequired[str]
        skip_retrieval: NotRequired[bool]
        card: NotRequired[CreateUsingPermanentTokenCardParams]
        billing_address: NotRequired[CreateUsingPermanentTokenBillingAddressParams]
        additional_information: NotRequired[Dict[Any, Any]]

    class CreateUsingTokenParams(TypedDict):
        customer_id: Required[str]
        replace_primary_payment_source: NotRequired[bool]
        token_id: Required[str]

    class CreateUsingPaymentIntentParams(TypedDict):
        customer_id: Required[str]
        payment_intent: NotRequired[CreateUsingPaymentIntentPaymentIntentParams]
        replace_primary_payment_source: NotRequired[bool]

    class CreateVoucherPaymentSourceParams(TypedDict):
        customer_id: Required[str]
        voucher_payment_source: Required[
            CreateVoucherPaymentSourceVoucherPaymentSourceParams
        ]

    class CreateCardParams(TypedDict):
        customer_id: Required[str]
        card: Required[CreateCardCardParams]
        replace_primary_payment_source: NotRequired[bool]

    class CreateBankAccountParams(TypedDict):
        customer_id: Required[str]
        bank_account: NotRequired[CreateBankAccountBankAccountParams]
        issuing_country: NotRequired[str]
        replace_primary_payment_source: NotRequired[bool]

    class UpdateCardParams(TypedDict):
        card: NotRequired[UpdateCardCardParams]
        gateway_meta_data: NotRequired[Dict[Any, Any]]
        reference_transaction: NotRequired[str]

    class UpdateBankAccountParams(TypedDict):
        bank_account: NotRequired[UpdateBankAccountBankAccountParams]

    class VerifyBankAccountParams(TypedDict):
        amount1: Required[int]
        amount2: Required[int]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        subscription_id: NotRequired[str]
        customer_id: NotRequired[Filters.StringFilter]
        type: NotRequired[Filters.EnumFilter]
        status: NotRequired[Filters.EnumFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]

    class SwitchGatewayAccountParams(TypedDict):
        gateway_account_id: Required[str]

    class ExportPaymentSourceParams(TypedDict):
        gateway_account_id: Required[str]

    @staticmethod
    def create_using_temp_token(
        params: CreateUsingTempTokenParams, env=None, headers=None
    ) -> CreateUsingTempTokenResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_using_temp_token"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateUsingTempTokenResponse,
        )

    @staticmethod
    def create_using_permanent_token(
        params: CreateUsingPermanentTokenParams, env=None, headers=None
    ) -> CreateUsingPermanentTokenResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_using_permanent_token"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateUsingPermanentTokenResponse,
        )

    @staticmethod
    def create_using_token(
        params: CreateUsingTokenParams, env=None, headers=None
    ) -> CreateUsingTokenResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_using_token"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateUsingTokenResponse,
        )

    @staticmethod
    def create_using_payment_intent(
        params: CreateUsingPaymentIntentParams, env=None, headers=None
    ) -> CreateUsingPaymentIntentResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_using_payment_intent"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateUsingPaymentIntentResponse,
        )

    @staticmethod
    def create_voucher_payment_source(
        params: CreateVoucherPaymentSourceParams, env=None, headers=None
    ) -> CreateVoucherPaymentSourceResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_voucher_payment_source"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateVoucherPaymentSourceResponse,
        )

    @staticmethod
    def create_card(
        params: CreateCardParams, env=None, headers=None
    ) -> CreateCardResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_card"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateCardResponse,
        )

    @staticmethod
    def create_bank_account(
        params: CreateBankAccountParams, env=None, headers=None
    ) -> CreateBankAccountResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_bank_account"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateBankAccountResponse,
        )

    @staticmethod
    def update_card(
        id, params: UpdateCardParams = None, env=None, headers=None
    ) -> UpdateCardResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "update_card"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateCardResponse,
        )

    @staticmethod
    def update_bank_account(
        id, params: UpdateBankAccountParams = None, env=None, headers=None
    ) -> UpdateBankAccountResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "update_bank_account"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateBankAccountResponse,
        )

    @staticmethod
    def verify_bank_account(
        id, params: VerifyBankAccountParams, env=None, headers=None
    ) -> VerifyBankAccountResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "verify_bank_account"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            VerifyBankAccountResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("payment_sources", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("payment_sources"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def switch_gateway_account(
        id, params: SwitchGatewayAccountParams, env=None, headers=None
    ) -> SwitchGatewayAccountResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "switch_gateway_account"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            SwitchGatewayAccountResponse,
        )

    @staticmethod
    def export_payment_source(
        id, params: ExportPaymentSourceParams, env=None, headers=None
    ) -> ExportPaymentSourceResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "export_payment_source"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ExportPaymentSourceResponse,
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def delete_local(id, env=None, headers=None) -> DeleteLocalResponse:
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "delete_local"),
            None,
            env,
            headers,
            DeleteLocalResponse,
        )
