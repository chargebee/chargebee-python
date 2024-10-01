from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import enums


class Card:
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

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get", request.uri_path("cards", id), None, env, headers, RetrieveResponse
        )

    @staticmethod
    def update_card_for_customer(
        id, params: UpdateCardForCustomerParams, env=None, headers=None
    ) -> UpdateCardForCustomerResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "credit_card"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateCardForCustomerResponse,
        )

    @staticmethod
    def switch_gateway_for_customer(
        id, params: SwitchGatewayForCustomerParams, env=None, headers=None
    ) -> SwitchGatewayForCustomerResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "switch_gateway"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            SwitchGatewayForCustomerResponse,
        )

    @staticmethod
    def copy_card_for_customer(
        id, params: CopyCardForCustomerParams, env=None, headers=None
    ) -> CopyCardForCustomerResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "copy_card"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CopyCardForCustomerResponse,
        )

    @staticmethod
    def delete_card_for_customer(
        id, env=None, headers=None
    ) -> DeleteCardForCustomerResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "delete_card"),
            None,
            env,
            headers,
            DeleteCardForCustomerResponse,
        )
