from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


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


class Cards(TypedDict):
    payment_source_id: Required[str]
    status: Required[Status]
    gateway: Required[enums.Gateway]
    gateway_account_id: NotRequired[str]
    ref_tx_id: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    iin: Required[str]
    last4: Required[str]
    card_type: NotRequired[CardType]
    funding_type: Required[FundingType]
    expiry_month: Required[int]
    expiry_year: Required[int]
    issuing_country: NotRequired[str]
    billing_addr1: NotRequired[str]
    billing_addr2: NotRequired[str]
    billing_city: NotRequired[str]
    billing_state_code: NotRequired[str]
    billing_state: NotRequired[str]
    billing_country: NotRequired[str]
    billing_zip: NotRequired[str]
    created_at: Required[int]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    ip_address: NotRequired[str]
    powered_by: NotRequired[PoweredBy]
    customer_id: Required[str]
    masked_number: NotRequired[str]


class UpdateCardForCustomerCustomerParams(TypedDict):
    vat_number: NotRequired[str]
