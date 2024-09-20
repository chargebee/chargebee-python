from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums, payment_intent


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
    brand: Required[CardBrand]
    funding_type: Required[CardFundingType]
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
    brand: NotRequired[CardBrand]
    funding_type: NotRequired[CardFundingType]


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
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
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
