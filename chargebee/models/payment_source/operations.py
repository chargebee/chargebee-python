from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums, payment_intent, card


@dataclass
class PaymentSource:
    env: environment.Environment

    class Status(Enum):
        VALID = "valid"
        EXPIRING = "expiring"
        EXPIRED = "expired"
        INVALID = "invalid"
        PENDING_VERIFICATION = "pending_verification"

        def __str__(self):
            return self.value

    class CardBrand(Enum):
        VISA = "visa"
        MASTERCARD = "mastercard"
        AMERICAN_EXPRESS = "american_express"
        DISCOVER = "discover"
        JCB = "jcb"
        DINERS_CLUB = "diners_club"
        OTHER = "other"
        BANCONTACT = "bancontact"
        CMR_FALABELLA = "cmr_falabella"
        TARJETA_NARANJA = "tarjeta_naranja"
        NATIVA = "nativa"
        CENCOSUD = "cencosud"
        CABAL = "cabal"
        ARGENCARD = "argencard"
        ELO = "elo"
        HIPERCARD = "hipercard"
        CARNET = "carnet"
        RUPAY = "rupay"
        MAESTRO = "maestro"
        DANKORT = "dankort"
        CARTES_BANCAIRES = "cartes_bancaires"
        NOT_APPLICABLE = "not_applicable"

        def __str__(self):
            return self.value

    class CardFundingType(Enum):
        CREDIT = "credit"
        DEBIT = "debit"
        PREPAID = "prepaid"
        NOT_KNOWN = "not_known"
        NOT_APPLICABLE = "not_applicable"

        def __str__(self):
            return self.value

    class Card(TypedDict):
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        iin: Required[str]
        last4: Required[str]
        brand: Required["PaymentSource.CardBrand"]
        funding_type: Required["PaymentSource.CardFundingType"]
        expiry_month: Required[int]
        expiry_year: Required[int]
        billing_addr1: NotRequired[str]
        billing_addr2: NotRequired[str]
        billing_city: NotRequired[str]
        billing_state_code: NotRequired[str]
        billing_state: NotRequired[str]
        billing_country: NotRequired[str]
        billing_zip: NotRequired[str]
        masked_number: NotRequired[str]

    class BankAccount(TypedDict):
        last4: Required[str]
        name_on_account: NotRequired[str]
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        direct_debit_scheme: NotRequired[enums.DirectDebitScheme]
        bank_name: NotRequired[str]
        mandate_id: NotRequired[str]
        account_type: NotRequired[enums.AccountType]
        echeck_type: NotRequired[enums.EcheckType]
        account_holder_type: NotRequired[enums.AccountHolderType]
        email: NotRequired[str]

    class CustVoucherSource(TypedDict):
        last4: Required[str]
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        email: NotRequired[str]

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

    class AmazonPayment(TypedDict):
        email: NotRequired[str]
        agreement_id: NotRequired[str]

    class Upi(TypedDict):
        vpa: NotRequired[str]

    class Paypal(TypedDict):
        email: NotRequired[str]
        agreement_id: NotRequired[str]

    class Venmo(TypedDict):
        user_name: NotRequired[str]

    class KlarnaPayNow(TypedDict):
        email: NotRequired[str]

    class Mandate(TypedDict):
        id: Required[str]
        subscription_id: Required[str]
        created_at: Required[int]

    class CreateUsingPermanentTokenCardParams(TypedDict):
        last4: NotRequired[str]
        iin: NotRequired[str]
        expiry_month: NotRequired[int]
        expiry_year: NotRequired[int]
        brand: NotRequired["PaymentSource.CardBrand"]
        funding_type: NotRequired["PaymentSource.CardFundingType"]

    class CreateUsingPermanentTokenBillingAddressParams(TypedDict):
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        email: NotRequired[str]
        line1: NotRequired[str]
        line2: NotRequired[str]
        line3: NotRequired[str]
        city: NotRequired[str]
        state_code: NotRequired[str]
        state: NotRequired[str]
        zip: NotRequired[str]
        country: NotRequired[str]

    class CreateUsingPaymentIntentPaymentIntentParams(TypedDict):
        id: NotRequired[str]
        gateway_account_id: NotRequired[str]
        gw_token: NotRequired[str]
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
        reference_id: NotRequired[str]
        gw_payment_method_id: NotRequired[str]
        additional_info: NotRequired[Dict[Any, Any]]
        additional_information: NotRequired[Dict[Any, Any]]

    class CreateVoucherPaymentSourceVoucherPaymentSourceParams(TypedDict):
        voucher_type: Required[enums.VoucherType]
        gateway_account_id: NotRequired[str]
        tax_id: NotRequired[str]
        billing_address: NotRequired[Dict[Any, Any]]

    class CreateCardCardParams(TypedDict):
        gateway_account_id: NotRequired[str]
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        number: Required[str]
        expiry_month: Required[int]
        expiry_year: Required[int]
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

    class CreateBankAccountBankAccountParams(TypedDict):
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
        swedish_identity_number: NotRequired[str]
        billing_address: NotRequired[Dict[Any, Any]]

    class UpdateCardCardParams(TypedDict):
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        expiry_month: NotRequired[int]
        expiry_year: NotRequired[int]
        billing_addr1: NotRequired[str]
        billing_addr2: NotRequired[str]
        billing_city: NotRequired[str]
        billing_zip: NotRequired[str]
        billing_state_code: NotRequired[str]
        billing_state: NotRequired[str]
        billing_country: NotRequired[str]
        additional_information: NotRequired[Dict[Any, Any]]

    class UpdateBankAccountBankAccountParams(TypedDict):
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        email: NotRequired[str]

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
        card: NotRequired["PaymentSource.CreateUsingPermanentTokenCardParams"]
        billing_address: NotRequired[
            "PaymentSource.CreateUsingPermanentTokenBillingAddressParams"
        ]
        additional_information: NotRequired[Dict[Any, Any]]

    class CreateUsingTokenParams(TypedDict):
        customer_id: Required[str]
        replace_primary_payment_source: NotRequired[bool]
        token_id: Required[str]

    class CreateUsingPaymentIntentParams(TypedDict):
        customer_id: Required[str]
        payment_intent: NotRequired[
            "PaymentSource.CreateUsingPaymentIntentPaymentIntentParams"
        ]
        replace_primary_payment_source: NotRequired[bool]

    class CreateVoucherPaymentSourceParams(TypedDict):
        customer_id: Required[str]
        voucher_payment_source: Required[
            "PaymentSource.CreateVoucherPaymentSourceVoucherPaymentSourceParams"
        ]

    class CreateCardParams(TypedDict):
        customer_id: Required[str]
        card: Required["PaymentSource.CreateCardCardParams"]
        replace_primary_payment_source: NotRequired[bool]

    class CreateBankAccountParams(TypedDict):
        customer_id: Required[str]
        bank_account: NotRequired["PaymentSource.CreateBankAccountBankAccountParams"]
        issuing_country: NotRequired[str]
        replace_primary_payment_source: NotRequired[bool]

    class UpdateCardParams(TypedDict):
        card: NotRequired["PaymentSource.UpdateCardCardParams"]
        gateway_meta_data: NotRequired[Dict[Any, Any]]
        reference_transaction: NotRequired[str]

    class UpdateBankAccountParams(TypedDict):
        bank_account: NotRequired["PaymentSource.UpdateBankAccountBankAccountParams"]

    class VerifyBankAccountParams(TypedDict):
        amount1: Required[int]
        amount2: Required[int]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        subscription_id: NotRequired[str]
        include_deleted: NotRequired[bool]
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

    def create_using_temp_token(
        self, params: CreateUsingTempTokenParams, headers=None
    ) -> CreateUsingTempTokenResponse:
        jsonKeys = {
            "additional_information": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_using_temp_token"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateUsingTempTokenResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_using_permanent_token(
        self, params: CreateUsingPermanentTokenParams, headers=None
    ) -> CreateUsingPermanentTokenResponse:
        jsonKeys = {
            "additional_information": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_using_permanent_token"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateUsingPermanentTokenResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_using_token(
        self, params: CreateUsingTokenParams, headers=None
    ) -> CreateUsingTokenResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_using_token"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateUsingTokenResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_using_payment_intent(
        self, params: CreateUsingPaymentIntentParams, headers=None
    ) -> CreateUsingPaymentIntentResponse:
        jsonKeys = {
            "additional_info": 1,
            "additional_information": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_using_payment_intent"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateUsingPaymentIntentResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_voucher_payment_source(
        self, params: CreateVoucherPaymentSourceParams, headers=None
    ) -> CreateVoucherPaymentSourceResponse:
        jsonKeys = {
            "billing_address": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_voucher_payment_source"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateVoucherPaymentSourceResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_card(self, params: CreateCardParams, headers=None) -> CreateCardResponse:
        jsonKeys = {
            "additional_information": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_card"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateCardResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_bank_account(
        self, params: CreateBankAccountParams, headers=None
    ) -> CreateBankAccountResponse:
        jsonKeys = {
            "billing_address": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", "create_bank_account"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateBankAccountResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update_card(
        self, id, params: UpdateCardParams = None, headers=None
    ) -> UpdateCardResponse:
        jsonKeys = {
            "gateway_meta_data": 0,
            "additional_information": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "update_card"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateCardResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update_bank_account(
        self, id, params: UpdateBankAccountParams = None, headers=None
    ) -> UpdateBankAccountResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "update_bank_account"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateBankAccountResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def verify_bank_account(
        self, id, params: VerifyBankAccountParams, headers=None
    ) -> VerifyBankAccountResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "verify_bank_account"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            VerifyBankAccountResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("payment_sources", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("payment_sources"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def switch_gateway_account(
        self, id, params: SwitchGatewayAccountParams, headers=None
    ) -> SwitchGatewayAccountResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "switch_gateway_account"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            SwitchGatewayAccountResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def export_payment_source(
        self, id, params: ExportPaymentSourceParams, headers=None
    ) -> ExportPaymentSourceResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "export_payment_source"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ExportPaymentSourceResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete_local(self, id, headers=None) -> DeleteLocalResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_sources", id, "delete_local"),
            self.env,
            None,
            headers,
            DeleteLocalResponse,
            None,
            False,
            jsonKeys,
            options,
        )
