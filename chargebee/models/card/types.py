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


class UpdateCardForCustomerCustomerParams(TypedDict):
    vat_number: NotRequired[str]
