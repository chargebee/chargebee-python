from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import enums


@dataclass
class Card:
    env: environment.Environment

    class PreferredScheme(Enum):
        CARTES_BANCAIRES = "cartes_bancaires"
        MASTERCARD = "mastercard"
        VISA = "visa"

        def __str__(self):
            return self.value

    class Status(Enum):
        VALID = "valid"
        EXPIRING = "expiring"
        EXPIRED = "expired"

        def __str__(self):
            return self.value

    class CardType(Enum):
        VISA = "visa"
        MASTERCARD = "mastercard"
        AMERICAN_EXPRESS = "american_express"
        DISCOVER = "discover"
        JCB = "jcb"
        DINERS_CLUB = "diners_club"
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
        OTHER = "other"
        NOT_APPLICABLE = "not_applicable"

        def __str__(self):
            return self.value

    class FundingType(Enum):
        CREDIT = "credit"
        DEBIT = "debit"
        PREPAID = "prepaid"
        NOT_KNOWN = "not_known"
        NOT_APPLICABLE = "not_applicable"

        def __str__(self):
            return self.value

    class PoweredBy(Enum):
        IDEAL = "ideal"
        SOFORT = "sofort"
        BANCONTACT = "bancontact"
        GIROPAY = "giropay"
        CARD = "card"
        LATAM_LOCAL_CARD = "latam_local_card"
        PAYCONIQ = "payconiq"
        NOT_APPLICABLE = "not_applicable"

        def __str__(self):
            return self.value

    class UpdateCardForCustomerCustomerParams(TypedDict):
        vat_number: NotRequired[str]

    class UpdateCardForCustomerParams(TypedDict):
        gateway: NotRequired[enums.Gateway]
        gateway_account_id: NotRequired[str]
        tmp_token: NotRequired[str]
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        number: Required[str]
        expiry_month: Required[int]
        expiry_year: Required[int]
        cvv: NotRequired[str]
        preferred_scheme: NotRequired["Card.PreferredScheme"]
        billing_addr1: NotRequired[str]
        billing_addr2: NotRequired[str]
        billing_city: NotRequired[str]
        billing_state_code: NotRequired[str]
        billing_state: NotRequired[str]
        billing_zip: NotRequired[str]
        billing_country: NotRequired[str]
        ip_address: NotRequired[str]
        customer: NotRequired["Card.UpdateCardForCustomerCustomerParams"]

    class SwitchGatewayForCustomerParams(TypedDict):
        gateway: NotRequired[enums.Gateway]
        gateway_account_id: Required[str]

    class CopyCardForCustomerParams(TypedDict):
        gateway_account_id: Required[str]

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("cards", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update_card_for_customer(
        self, id, params: UpdateCardForCustomerParams, headers=None
    ) -> UpdateCardForCustomerResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("customers", id, "credit_card"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateCardForCustomerResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def switch_gateway_for_customer(
        self, id, params: SwitchGatewayForCustomerParams, headers=None
    ) -> SwitchGatewayForCustomerResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("customers", id, "switch_gateway"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            SwitchGatewayForCustomerResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def copy_card_for_customer(
        self, id, params: CopyCardForCustomerParams, headers=None
    ) -> CopyCardForCustomerResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("customers", id, "copy_card"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CopyCardForCustomerResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete_card_for_customer(
        self, id, headers=None
    ) -> DeleteCardForCustomerResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("customers", id, "delete_card"),
            self.env,
            None,
            headers,
            DeleteCardForCustomerResponse,
            None,
            False,
            jsonKeys,
            options,
        )
