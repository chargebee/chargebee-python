from enum import Enum


class AccountHolderType(Enum):
    INDIVIDUAL = "individual"
    COMPANY = "company"

    def __str__(self):
        return self.value


class AccountReceivablesHandling(Enum):
    NO_ACTION = "no_action"
    SCHEDULE_PAYMENT_COLLECTION = "schedule_payment_collection"
    WRITE_OFF = "write_off"

    def __str__(self):
        return self.value


class AccountType(Enum):
    CHECKING = "checking"
    SAVINGS = "savings"
    BUSINESS_CHECKING = "business_checking"
    CURRENT = "current"

    def __str__(self):
        return self.value


class Action(Enum):
    UPSERT = "upsert"
    REMOVE = "remove"

    def __str__(self):
        return self.value


class ApiVersion(Enum):
    V1 = "v1"
    V2 = "v2"

    def __str__(self):
        return self.value


class ApplyOn(Enum):
    INVOICE_AMOUNT = "invoice_amount"
    SPECIFIC_ITEM_PRICE = "specific_item_price"

    def __str__(self):
        return self.value


class AutoCollection(Enum):
    ON = "on"
    OFF = "off"

    def __str__(self):
        return self.value


class AvalaraSaleType(Enum):
    WHOLESALE = "wholesale"
    RETAIL = "retail"
    CONSUMED = "consumed"
    VENDOR_USE = "vendor_use"

    def __str__(self):
        return self.value


class BillingAlignmentMode(Enum):
    IMMEDIATE = "immediate"
    DELAYED = "delayed"

    def __str__(self):
        return self.value


class BillingDateMode(Enum):
    USING_DEFAULTS = "using_defaults"
    MANUALLY_SET = "manually_set"

    def __str__(self):
        return self.value


class BillingDayOfWeekMode(Enum):
    USING_DEFAULTS = "using_defaults"
    MANUALLY_SET = "manually_set"

    def __str__(self):
        return self.value


class BillingPeriodUnit(Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

    def __str__(self):
        return self.value


class BillingStartOption(Enum):
    IMMEDIATELY = "immediately"
    ON_SPECIFIC_DATE = "on_specific_date"

    def __str__(self):
        return self.value


class CancelOption(Enum):
    IMMEDIATELY = "immediately"
    END_OF_TERM = "end_of_term"
    SPECIFIC_DATE = "specific_date"
    END_OF_BILLING_TERM = "end_of_billing_term"

    def __str__(self):
        return self.value


class Category(Enum):
    INTRODUCTORY = "introductory"
    PROMOTIONAL = "promotional"
    DEVELOPER_DETERMINED = "developer_determined"

    def __str__(self):
        return self.value


class ChangeOption(Enum):
    IMMEDIATELY = "immediately"
    END_OF_TERM = "end_of_term"
    SPECIFIC_DATE = "specific_date"

    def __str__(self):
        return self.value


class Channel(Enum):
    WEB = "web"
    APP_STORE = "app_store"
    PLAY_STORE = "play_store"

    def __str__(self):
        return self.value


class ChargeModel(Enum):
    FULL_CHARGE = "full_charge"
    PRORATE = "prorate"

    def __str__(self):
        return self.value


class ChargeOn(Enum):
    IMMEDIATELY = "immediately"
    ON_EVENT = "on_event"

    def __str__(self):
        return self.value


class ChargeOnEvent(Enum):
    SUBSCRIPTION_CREATION = "subscription_creation"
    SUBSCRIPTION_TRIAL_START = "subscription_trial_start"
    PLAN_ACTIVATION = "plan_activation"
    SUBSCRIPTION_ACTIVATION = "subscription_activation"
    CONTRACT_TERMINATION = "contract_termination"
    ON_DEMAND = "on_demand"

    def __str__(self):
        return self.value


class ChargeOnOption(Enum):
    IMMEDIATELY = "immediately"
    ON_EVENT = "on_event"

    def __str__(self):
        return self.value


class ChargebeeResponseSchemaType(Enum):
    PLANS_ADDONS = "plans_addons"
    ITEMS = "items"
    COMPAT = "compat"

    def __str__(self):
        return self.value


class ChargesHandling(Enum):
    INVOICE_IMMEDIATELY = "invoice_immediately"
    ADD_TO_UNBILLED_CHARGES = "add_to_unbilled_charges"

    def __str__(self):
        return self.value


class ContractTermCancelOption(Enum):
    TERMINATE_IMMEDIATELY = "terminate_immediately"
    END_OF_CONTRACT_TERM = "end_of_contract_term"
    SPECIFIC_DATE = "specific_date"
    END_OF_SUBSCRIPTION_BILLING_TERM = "end_of_subscription_billing_term"

    def __str__(self):
        return self.value


class CreditOptionForCurrentTermCharges(Enum):
    NONE = "none"
    PRORATE = "prorate"
    FULL = "full"

    def __str__(self):
        return self.value


class CreditType(Enum):
    LOYALTY_CREDITS = "loyalty_credits"
    REFERRAL_REWARDS = "referral_rewards"
    GENERAL = "general"

    def __str__(self):
        return self.value


class CustomerType(Enum):
    RESIDENTIAL = "residential"
    BUSINESS = "business"
    SENIOR_CITIZEN = "senior_citizen"
    INDUSTRIAL = "industrial"

    def __str__(self):
        return self.value


class DedupeOption(Enum):
    SKIP = "skip"
    UPDATE_EXISTING = "update_existing"

    def __str__(self):
        return self.value


class DirectDebitScheme(Enum):
    ACH = "ach"
    BACS = "bacs"
    SEPA_CORE = "sepa_core"
    AUTOGIRO = "autogiro"
    BECS = "becs"
    BECS_NZ = "becs_nz"
    PAD = "pad"
    NOT_APPLICABLE = "not_applicable"

    def __str__(self):
        return self.value


class DiscountType(Enum):
    FIXED_AMOUNT = "fixed_amount"
    PERCENTAGE = "percentage"
    PRICE = "price"

    def __str__(self):
        return self.value


class DispositionType(Enum):
    ATTACHMENT = "attachment"
    INLINE = "inline"

    def __str__(self):
        return self.value


class DunningType(Enum):
    AUTO_COLLECT = "auto_collect"
    OFFLINE = "offline"
    DIRECT_DEBIT = "direct_debit"

    def __str__(self):
        return self.value


class DurationType(Enum):
    ONE_TIME = "one_time"
    FOREVER = "forever"
    LIMITED_PERIOD = "limited_period"

    def __str__(self):
        return self.value


class EcheckType(Enum):
    WEB = "web"
    PPD = "ppd"
    CCD = "ccd"

    def __str__(self):
        return self.value


class EinvoicingMethod(Enum):
    AUTOMATIC = "automatic"
    MANUAL = "manual"
    SITE_DEFAULT = "site_default"

    def __str__(self):
        return self.value


class EndScheduleOn(Enum):
    AFTER_NUMBER_OF_INTERVALS = "after_number_of_intervals"
    SPECIFIC_DATE = "specific_date"
    SUBSCRIPTION_END = "subscription_end"

    def __str__(self):
        return self.value


class EntityCode(Enum):
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"
    F = "f"
    G = "g"
    H = "h"
    I = "i"
    J = "j"
    K = "k"
    L = "l"
    M = "m"
    N = "n"
    P = "p"
    Q = "q"
    R = "r"
    MED1 = "med1"
    MED2 = "med2"

    def __str__(self):
        return self.value


class EntityType(Enum):
    CUSTOMER = "customer"
    SUBSCRIPTION = "subscription"
    COUPON = "coupon"
    PLAN_ITEM_PRICE = "plan_item_price"
    ADDON_ITEM_PRICE = "addon_item_price"
    CHARGE_ITEM_PRICE = "charge_item_price"
    INVOICE = "invoice"
    QUOTE = "quote"
    CREDIT_NOTE = "credit_note"
    TRANSACTION = "transaction"
    PLAN = "plan"
    ADDON = "addon"
    ORDER = "order"
    ITEM_FAMILY = "item_family"
    ITEM = "item"
    ITEM_PRICE = "item_price"
    PLAN_ITEM = "plan_item"
    ADDON_ITEM = "addon_item"
    CHARGE_ITEM = "charge_item"
    PLAN_PRICE = "plan_price"
    ADDON_PRICE = "addon_price"
    CHARGE_PRICE = "charge_price"
    DIFFERENTIAL_PRICE = "differential_price"
    ATTACHED_ITEM = "attached_item"
    FEATURE = "feature"
    SUBSCRIPTION_ENTITLEMENT = "subscription_entitlement"
    ITEM_ENTITLEMENT = "item_entitlement"
    BUSINESS_ENTITY = "business_entity"
    PRICE_VARIANT = "price_variant"
    OMNICHANNEL_SUBSCRIPTION = "omnichannel_subscription"
    OMNICHANNEL_SUBSCRIPTION_ITEM = "omnichannel_subscription_item"
    OMNICHANNEL_TRANSACTION = "omnichannel_transaction"
    RECORDED_PURCHASE = "recorded_purchase"
    OMNICHANNEL_SUBSCRIPTION_ITEM_SCHEDULED_CHANGE = (
        "omnichannel_subscription_item_scheduled_change"
    )
    SALES_ORDER = "sales_order"
    OMNICHANNEL_ONE_TIME_ORDER = "omnichannel_one_time_order"
    OMNICHANNEL_ONE_TIME_ORDER_ITEM = "omnichannel_one_time_order_item"
    USAGE_FILE = "usage_file"
    BUSINESS_RULE = "business_rule"
    RULESET = "ruleset"

    def __str__(self):
        return self.value


class EventName(Enum):
    CANCELLATION_PAGE_LOADED = "cancellation_page_loaded"

    def __str__(self):
        return self.value


class EventType(Enum):
    COUPON_CREATED = "coupon_created"
    COUPON_UPDATED = "coupon_updated"
    COUPON_DELETED = "coupon_deleted"
    COUPON_SET_CREATED = "coupon_set_created"
    COUPON_SET_UPDATED = "coupon_set_updated"
    COUPON_SET_DELETED = "coupon_set_deleted"
    COUPON_CODES_ADDED = "coupon_codes_added"
    COUPON_CODES_DELETED = "coupon_codes_deleted"
    COUPON_CODES_UPDATED = "coupon_codes_updated"
    CUSTOMER_CREATED = "customer_created"
    CUSTOMER_CHANGED = "customer_changed"
    CUSTOMER_DELETED = "customer_deleted"
    CUSTOMER_MOVED_OUT = "customer_moved_out"
    CUSTOMER_MOVED_IN = "customer_moved_in"
    PROMOTIONAL_CREDITS_ADDED = "promotional_credits_added"
    PROMOTIONAL_CREDITS_DEDUCTED = "promotional_credits_deducted"
    SUBSCRIPTION_CREATED = "subscription_created"
    SUBSCRIPTION_CREATED_WITH_BACKDATING = "subscription_created_with_backdating"
    SUBSCRIPTION_STARTED = "subscription_started"
    SUBSCRIPTION_TRIAL_END_REMINDER = "subscription_trial_end_reminder"
    SUBSCRIPTION_ACTIVATED = "subscription_activated"
    SUBSCRIPTION_ACTIVATED_WITH_BACKDATING = "subscription_activated_with_backdating"
    SUBSCRIPTION_CHANGED = "subscription_changed"
    SUBSCRIPTION_TRIAL_EXTENDED = "subscription_trial_extended"
    MRR_UPDATED = "mrr_updated"
    SUBSCRIPTION_CHANGED_WITH_BACKDATING = "subscription_changed_with_backdating"
    SUBSCRIPTION_CANCELLATION_SCHEDULED = "subscription_cancellation_scheduled"
    SUBSCRIPTION_CANCELLATION_REMINDER = "subscription_cancellation_reminder"
    SUBSCRIPTION_CANCELLED = "subscription_cancelled"
    SUBSCRIPTION_CANCELED_WITH_BACKDATING = "subscription_canceled_with_backdating"
    SUBSCRIPTION_REACTIVATED = "subscription_reactivated"
    SUBSCRIPTION_REACTIVATED_WITH_BACKDATING = (
        "subscription_reactivated_with_backdating"
    )
    SUBSCRIPTION_RENEWED = "subscription_renewed"
    SUBSCRIPTION_ITEMS_RENEWED = "subscription_items_renewed"
    SUBSCRIPTION_SCHEDULED_CANCELLATION_REMOVED = (
        "subscription_scheduled_cancellation_removed"
    )
    SUBSCRIPTION_CHANGES_SCHEDULED = "subscription_changes_scheduled"
    SUBSCRIPTION_SCHEDULED_CHANGES_REMOVED = "subscription_scheduled_changes_removed"
    SUBSCRIPTION_SHIPPING_ADDRESS_UPDATED = "subscription_shipping_address_updated"
    SUBSCRIPTION_DELETED = "subscription_deleted"
    SUBSCRIPTION_PAUSED = "subscription_paused"
    SUBSCRIPTION_PAUSE_SCHEDULED = "subscription_pause_scheduled"
    SUBSCRIPTION_SCHEDULED_PAUSE_REMOVED = "subscription_scheduled_pause_removed"
    SUBSCRIPTION_RESUMED = "subscription_resumed"
    SUBSCRIPTION_RESUMPTION_SCHEDULED = "subscription_resumption_scheduled"
    SUBSCRIPTION_SCHEDULED_RESUMPTION_REMOVED = (
        "subscription_scheduled_resumption_removed"
    )
    SUBSCRIPTION_ADVANCE_INVOICE_SCHEDULE_ADDED = (
        "subscription_advance_invoice_schedule_added"
    )
    SUBSCRIPTION_ADVANCE_INVOICE_SCHEDULE_UPDATED = (
        "subscription_advance_invoice_schedule_updated"
    )
    SUBSCRIPTION_ADVANCE_INVOICE_SCHEDULE_REMOVED = (
        "subscription_advance_invoice_schedule_removed"
    )
    PENDING_INVOICE_CREATED = "pending_invoice_created"
    PENDING_INVOICE_UPDATED = "pending_invoice_updated"
    INVOICE_GENERATED = "invoice_generated"
    INVOICE_GENERATED_WITH_BACKDATING = "invoice_generated_with_backdating"
    INVOICE_UPDATED = "invoice_updated"
    INVOICE_DELETED = "invoice_deleted"
    CREDIT_NOTE_CREATED = "credit_note_created"
    CREDIT_NOTE_CREATED_WITH_BACKDATING = "credit_note_created_with_backdating"
    CREDIT_NOTE_UPDATED = "credit_note_updated"
    CREDIT_NOTE_DELETED = "credit_note_deleted"
    PAYMENT_SCHEDULES_CREATED = "payment_schedules_created"
    PAYMENT_SCHEDULES_UPDATED = "payment_schedules_updated"
    PAYMENT_SCHEDULE_SCHEME_CREATED = "payment_schedule_scheme_created"
    PAYMENT_SCHEDULE_SCHEME_DELETED = "payment_schedule_scheme_deleted"
    SUBSCRIPTION_RENEWAL_REMINDER = "subscription_renewal_reminder"
    ADD_USAGES_REMINDER = "add_usages_reminder"
    TRANSACTION_CREATED = "transaction_created"
    TRANSACTION_UPDATED = "transaction_updated"
    TRANSACTION_DELETED = "transaction_deleted"
    PAYMENT_SUCCEEDED = "payment_succeeded"
    PAYMENT_FAILED = "payment_failed"
    DUNNING_UPDATED = "dunning_updated"
    PAYMENT_REFUNDED = "payment_refunded"
    PAYMENT_INITIATED = "payment_initiated"
    REFUND_INITIATED = "refund_initiated"
    AUTHORIZATION_SUCCEEDED = "authorization_succeeded"
    AUTHORIZATION_VOIDED = "authorization_voided"
    CARD_ADDED = "card_added"
    CARD_UPDATED = "card_updated"
    CARD_EXPIRY_REMINDER = "card_expiry_reminder"
    CARD_EXPIRED = "card_expired"
    CARD_DELETED = "card_deleted"
    PAYMENT_SOURCE_ADDED = "payment_source_added"
    PAYMENT_SOURCE_UPDATED = "payment_source_updated"
    PAYMENT_SOURCE_DELETED = "payment_source_deleted"
    PAYMENT_SOURCE_EXPIRING = "payment_source_expiring"
    PAYMENT_SOURCE_EXPIRED = "payment_source_expired"
    PAYMENT_SOURCE_LOCALLY_DELETED = "payment_source_locally_deleted"
    VIRTUAL_BANK_ACCOUNT_ADDED = "virtual_bank_account_added"
    VIRTUAL_BANK_ACCOUNT_UPDATED = "virtual_bank_account_updated"
    VIRTUAL_BANK_ACCOUNT_DELETED = "virtual_bank_account_deleted"
    TOKEN_CREATED = "token_created"
    TOKEN_CONSUMED = "token_consumed"
    TOKEN_EXPIRED = "token_expired"
    UNBILLED_CHARGES_CREATED = "unbilled_charges_created"
    UNBILLED_CHARGES_VOIDED = "unbilled_charges_voided"
    UNBILLED_CHARGES_DELETED = "unbilled_charges_deleted"
    UNBILLED_CHARGES_INVOICED = "unbilled_charges_invoiced"
    ORDER_CREATED = "order_created"
    ORDER_UPDATED = "order_updated"
    ORDER_CANCELLED = "order_cancelled"
    ORDER_DELIVERED = "order_delivered"
    ORDER_RETURNED = "order_returned"
    ORDER_READY_TO_PROCESS = "order_ready_to_process"
    ORDER_READY_TO_SHIP = "order_ready_to_ship"
    ORDER_DELETED = "order_deleted"
    ORDER_RESENT = "order_resent"
    QUOTE_CREATED = "quote_created"
    QUOTE_UPDATED = "quote_updated"
    QUOTE_DELETED = "quote_deleted"
    TAX_WITHHELD_RECORDED = "tax_withheld_recorded"
    TAX_WITHHELD_DELETED = "tax_withheld_deleted"
    TAX_WITHHELD_REFUNDED = "tax_withheld_refunded"
    GIFT_SCHEDULED = "gift_scheduled"
    GIFT_UNCLAIMED = "gift_unclaimed"
    GIFT_CLAIMED = "gift_claimed"
    GIFT_EXPIRED = "gift_expired"
    GIFT_CANCELLED = "gift_cancelled"
    GIFT_UPDATED = "gift_updated"
    HIERARCHY_CREATED = "hierarchy_created"
    HIERARCHY_DELETED = "hierarchy_deleted"
    PAYMENT_INTENT_CREATED = "payment_intent_created"
    PAYMENT_INTENT_UPDATED = "payment_intent_updated"
    CONTRACT_TERM_CREATED = "contract_term_created"
    CONTRACT_TERM_RENEWED = "contract_term_renewed"
    CONTRACT_TERM_TERMINATED = "contract_term_terminated"
    CONTRACT_TERM_COMPLETED = "contract_term_completed"
    CONTRACT_TERM_CANCELLED = "contract_term_cancelled"
    ITEM_FAMILY_CREATED = "item_family_created"
    ITEM_FAMILY_UPDATED = "item_family_updated"
    ITEM_FAMILY_DELETED = "item_family_deleted"
    ITEM_CREATED = "item_created"
    ITEM_UPDATED = "item_updated"
    ITEM_DELETED = "item_deleted"
    ITEM_PRICE_CREATED = "item_price_created"
    ITEM_PRICE_UPDATED = "item_price_updated"
    ITEM_PRICE_DELETED = "item_price_deleted"
    ATTACHED_ITEM_CREATED = "attached_item_created"
    ATTACHED_ITEM_UPDATED = "attached_item_updated"
    ATTACHED_ITEM_DELETED = "attached_item_deleted"
    DIFFERENTIAL_PRICE_CREATED = "differential_price_created"
    DIFFERENTIAL_PRICE_UPDATED = "differential_price_updated"
    DIFFERENTIAL_PRICE_DELETED = "differential_price_deleted"
    FEATURE_CREATED = "feature_created"
    FEATURE_UPDATED = "feature_updated"
    FEATURE_DELETED = "feature_deleted"
    FEATURE_ACTIVATED = "feature_activated"
    FEATURE_REACTIVATED = "feature_reactivated"
    FEATURE_ARCHIVED = "feature_archived"
    ITEM_ENTITLEMENTS_UPDATED = "item_entitlements_updated"
    ENTITLEMENT_OVERRIDES_UPDATED = "entitlement_overrides_updated"
    ENTITLEMENT_OVERRIDES_REMOVED = "entitlement_overrides_removed"
    ITEM_ENTITLEMENTS_REMOVED = "item_entitlements_removed"
    ENTITLEMENT_OVERRIDES_AUTO_REMOVED = "entitlement_overrides_auto_removed"
    SUBSCRIPTION_ENTITLEMENTS_CREATED = "subscription_entitlements_created"
    SUBSCRIPTION_ENTITLEMENTS_UPDATED = "subscription_entitlements_updated"
    BUSINESS_ENTITY_CREATED = "business_entity_created"
    BUSINESS_ENTITY_UPDATED = "business_entity_updated"
    BUSINESS_ENTITY_DELETED = "business_entity_deleted"
    CUSTOMER_BUSINESS_ENTITY_CHANGED = "customer_business_entity_changed"
    SUBSCRIPTION_BUSINESS_ENTITY_CHANGED = "subscription_business_entity_changed"
    PURCHASE_CREATED = "purchase_created"
    VOUCHER_CREATED = "voucher_created"
    VOUCHER_EXPIRED = "voucher_expired"
    VOUCHER_CREATE_FAILED = "voucher_create_failed"
    ITEM_PRICE_ENTITLEMENTS_UPDATED = "item_price_entitlements_updated"
    ITEM_PRICE_ENTITLEMENTS_REMOVED = "item_price_entitlements_removed"
    SUBSCRIPTION_RAMP_CREATED = "subscription_ramp_created"
    SUBSCRIPTION_RAMP_DELETED = "subscription_ramp_deleted"
    SUBSCRIPTION_RAMP_APPLIED = "subscription_ramp_applied"
    SUBSCRIPTION_RAMP_DRAFTED = "subscription_ramp_drafted"
    SUBSCRIPTION_RAMP_UPDATED = "subscription_ramp_updated"
    PRICE_VARIANT_CREATED = "price_variant_created"
    PRICE_VARIANT_UPDATED = "price_variant_updated"
    PRICE_VARIANT_DELETED = "price_variant_deleted"
    CUSTOMER_ENTITLEMENTS_UPDATED = "customer_entitlements_updated"
    SUBSCRIPTION_MOVED_IN = "subscription_moved_in"
    SUBSCRIPTION_MOVED_OUT = "subscription_moved_out"
    SUBSCRIPTION_MOVEMENT_FAILED = "subscription_movement_failed"
    OMNICHANNEL_SUBSCRIPTION_CREATED = "omnichannel_subscription_created"
    OMNICHANNEL_SUBSCRIPTION_ITEM_RENEWED = "omnichannel_subscription_item_renewed"
    OMNICHANNEL_SUBSCRIPTION_ITEM_DOWNGRADED = (
        "omnichannel_subscription_item_downgraded"
    )
    OMNICHANNEL_SUBSCRIPTION_ITEM_EXPIRED = "omnichannel_subscription_item_expired"
    OMNICHANNEL_SUBSCRIPTION_ITEM_CANCELLATION_SCHEDULED = (
        "omnichannel_subscription_item_cancellation_scheduled"
    )
    OMNICHANNEL_SUBSCRIPTION_ITEM_SCHEDULED_CANCELLATION_REMOVED = (
        "omnichannel_subscription_item_scheduled_cancellation_removed"
    )
    OMNICHANNEL_SUBSCRIPTION_ITEM_RESUBSCRIBED = (
        "omnichannel_subscription_item_resubscribed"
    )
    OMNICHANNEL_SUBSCRIPTION_ITEM_UPGRADED = "omnichannel_subscription_item_upgraded"
    OMNICHANNEL_SUBSCRIPTION_ITEM_CANCELLED = "omnichannel_subscription_item_cancelled"
    OMNICHANNEL_SUBSCRIPTION_IMPORTED = "omnichannel_subscription_imported"
    OMNICHANNEL_SUBSCRIPTION_ITEM_GRACE_PERIOD_STARTED = (
        "omnichannel_subscription_item_grace_period_started"
    )
    OMNICHANNEL_SUBSCRIPTION_ITEM_GRACE_PERIOD_EXPIRED = (
        "omnichannel_subscription_item_grace_period_expired"
    )
    OMNICHANNEL_SUBSCRIPTION_ITEM_DUNNING_STARTED = (
        "omnichannel_subscription_item_dunning_started"
    )
    OMNICHANNEL_SUBSCRIPTION_ITEM_DUNNING_EXPIRED = (
        "omnichannel_subscription_item_dunning_expired"
    )
    RULE_CREATED = "rule_created"
    RULE_UPDATED = "rule_updated"
    RULE_DELETED = "rule_deleted"
    RECORD_PURCHASE_FAILED = "record_purchase_failed"
    OMNICHANNEL_SUBSCRIPTION_ITEM_CHANGE_SCHEDULED = (
        "omnichannel_subscription_item_change_scheduled"
    )
    OMNICHANNEL_SUBSCRIPTION_ITEM_SCHEDULED_CHANGE_REMOVED = (
        "omnichannel_subscription_item_scheduled_change_removed"
    )
    OMNICHANNEL_SUBSCRIPTION_ITEM_REACTIVATED = (
        "omnichannel_subscription_item_reactivated"
    )
    SALES_ORDER_CREATED = "sales_order_created"
    SALES_ORDER_UPDATED = "sales_order_updated"
    OMNICHANNEL_SUBSCRIPTION_ITEM_CHANGED = "omnichannel_subscription_item_changed"
    OMNICHANNEL_SUBSCRIPTION_ITEM_PAUSED = "omnichannel_subscription_item_paused"
    OMNICHANNEL_SUBSCRIPTION_ITEM_RESUMED = "omnichannel_subscription_item_resumed"
    OMNICHANNEL_ONE_TIME_ORDER_CREATED = "omnichannel_one_time_order_created"
    OMNICHANNEL_ONE_TIME_ORDER_ITEM_CANCELLED = (
        "omnichannel_one_time_order_item_cancelled"
    )
    USAGE_FILE_INGESTED = "usage_file_ingested"
    OMNICHANNEL_SUBSCRIPTION_ITEM_PAUSE_SCHEDULED = (
        "omnichannel_subscription_item_pause_scheduled"
    )
    OMNICHANNEL_SUBSCRIPTION_MOVED_IN = "omnichannel_subscription_moved_in"
    OMNICHANNEL_TRANSACTION_CREATED = "omnichannel_transaction_created"
    PLAN_CREATED = "plan_created"
    PLAN_UPDATED = "plan_updated"
    PLAN_DELETED = "plan_deleted"
    ADDON_CREATED = "addon_created"
    ADDON_UPDATED = "addon_updated"
    ADDON_DELETED = "addon_deleted"

    def __str__(self):
        return self.value


class ExcludeTaxType(Enum):
    EXCLUSIVE = "exclusive"
    NONE = "none"

    def __str__(self):
        return self.value


class ExportType(Enum):
    DATA = "data"
    IMPORT_FRIENDLY_DATA = "import_friendly_data"

    def __str__(self):
        return self.value


class FreePeriodUnit(Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

    def __str__(self):
        return self.value


class FriendOfferType(Enum):
    NONE = "none"
    COUPON = "coupon"
    COUPON_CODE = "coupon_code"

    def __str__(self):
        return self.value


class Gateway(Enum):
    CHARGEBEE = "chargebee"
    CHARGEBEE_PAYMENTS = "chargebee_payments"
    ADYEN = "adyen"
    STRIPE = "stripe"
    WEPAY = "wepay"
    BRAINTREE = "braintree"
    AUTHORIZE_NET = "authorize_net"
    PAYPAL_PRO = "paypal_pro"
    PIN = "pin"
    EWAY = "eway"
    EWAY_RAPID = "eway_rapid"
    WORLDPAY = "worldpay"
    BALANCED_PAYMENTS = "balanced_payments"
    BEANSTREAM = "beanstream"
    BLUEPAY = "bluepay"
    ELAVON = "elavon"
    FIRST_DATA_GLOBAL = "first_data_global"
    HDFC = "hdfc"
    MIGS = "migs"
    NMI = "nmi"
    OGONE = "ogone"
    PAYMILL = "paymill"
    PAYPAL_PAYFLOW_PRO = "paypal_payflow_pro"
    SAGE_PAY = "sage_pay"
    TCO = "tco"
    WIRECARD = "wirecard"
    AMAZON_PAYMENTS = "amazon_payments"
    PAYPAL_EXPRESS_CHECKOUT = "paypal_express_checkout"
    ORBITAL = "orbital"
    MONERIS_US = "moneris_us"
    MONERIS = "moneris"
    BLUESNAP = "bluesnap"
    CYBERSOURCE = "cybersource"
    VANTIV = "vantiv"
    CHECKOUT_COM = "checkout_com"
    PAYPAL = "paypal"
    INGENICO_DIRECT = "ingenico_direct"
    EXACT = "exact"
    MOLLIE = "mollie"
    QUICKBOOKS = "quickbooks"
    RAZORPAY = "razorpay"
    GLOBAL_PAYMENTS = "global_payments"
    BANK_OF_AMERICA = "bank_of_america"
    ECENTRIC = "ecentric"
    METRICS_GLOBAL = "metrics_global"
    WINDCAVE = "windcave"
    PAY_COM = "pay_com"
    EBANX = "ebanx"
    DLOCAL = "dlocal"
    NUVEI = "nuvei"
    SOLIDGATE = "solidgate"
    PAYSTACK = "paystack"
    JP_MORGAN = "jp_morgan"
    DEUTSCHE_BANK = "deutsche_bank"
    EZIDEBIT = "ezidebit"
    GOCARDLESS = "gocardless"
    NOT_APPLICABLE = "not_applicable"

    def __str__(self):
        return self.value


class HierarchyOperationType(Enum):
    COMPLETE_HIERARCHY = "complete_hierarchy"
    SUBORDINATES = "subordinates"
    PATH_TO_ROOT = "path_to_root"

    def __str__(self):
        return self.value


class InvoiceDunningHandling(Enum):
    CONTINUE = "continue"
    STOP = "stop"

    def __str__(self):
        return self.value


class ItemType(Enum):
    PLAN = "plan"
    ADDON = "addon"
    CHARGE = "charge"

    def __str__(self):
        return self.value


class Layout(Enum):
    IN_APP = "in_app"
    FULL_PAGE = "full_page"

    def __str__(self):
        return self.value


class NotifyReferralSystem(Enum):
    NONE = "none"
    FIRST_PAID_CONVERSION = "first_paid_conversion"
    ALL_INVOICES = "all_invoices"

    def __str__(self):
        return self.value


class OfflinePaymentMethod(Enum):
    NO_PREFERENCE = "no_preference"
    CASH = "cash"
    CHECK = "check"
    BANK_TRANSFER = "bank_transfer"
    ACH_CREDIT = "ach_credit"
    SEPA_CREDIT = "sepa_credit"
    BOLETO = "boleto"
    US_AUTOMATED_BANK_TRANSFER = "us_automated_bank_transfer"
    EU_AUTOMATED_BANK_TRANSFER = "eu_automated_bank_transfer"
    UK_AUTOMATED_BANK_TRANSFER = "uk_automated_bank_transfer"
    JP_AUTOMATED_BANK_TRANSFER = "jp_automated_bank_transfer"
    MX_AUTOMATED_BANK_TRANSFER = "mx_automated_bank_transfer"
    CUSTOM = "custom"

    def __str__(self):
        return self.value


class OnEvent(Enum):
    SUBSCRIPTION_CREATION = "subscription_creation"
    SUBSCRIPTION_TRIAL_START = "subscription_trial_start"
    PLAN_ACTIVATION = "plan_activation"
    SUBSCRIPTION_ACTIVATION = "subscription_activation"
    CONTRACT_TERMINATION = "contract_termination"

    def __str__(self):
        return self.value


class Operation(Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"

    def __str__(self):
        return self.value


class OperationType(Enum):
    ADD = "add"
    REMOVE = "remove"

    def __str__(self):
        return self.value


class PauseOption(Enum):
    IMMEDIATELY = "immediately"
    END_OF_TERM = "end_of_term"
    SPECIFIC_DATE = "specific_date"
    BILLING_CYCLES = "billing_cycles"

    def __str__(self):
        return self.value


class PaymentInitiator(Enum):
    CUSTOMER = "customer"
    MERCHANT = "merchant"

    def __str__(self):
        return self.value


class PaymentMethod(Enum):
    CASH = "cash"
    CHECK = "check"
    BANK_TRANSFER = "bank_transfer"
    OTHER = "other"
    CUSTOM = "custom"
    CHARGEBACK = "chargeback"
    CARD = "card"
    AMAZON_PAYMENTS = "amazon_payments"
    PAYPAL_EXPRESS_CHECKOUT = "paypal_express_checkout"
    DIRECT_DEBIT = "direct_debit"
    ALIPAY = "alipay"
    UNIONPAY = "unionpay"
    APPLE_PAY = "apple_pay"
    WECHAT_PAY = "wechat_pay"
    ACH_CREDIT = "ach_credit"
    SEPA_CREDIT = "sepa_credit"
    IDEAL = "ideal"
    GOOGLE_PAY = "google_pay"
    SOFORT = "sofort"
    BANCONTACT = "bancontact"
    GIROPAY = "giropay"
    DOTPAY = "dotpay"
    UPI = "upi"
    NETBANKING_EMANDATES = "netbanking_emandates"
    BOLETO = "boleto"
    VENMO = "venmo"
    PAY_TO = "pay_to"
    FASTER_PAYMENTS = "faster_payments"
    SEPA_INSTANT_TRANSFER = "sepa_instant_transfer"
    AUTOMATED_BANK_TRANSFER = "automated_bank_transfer"
    KLARNA_PAY_NOW = "klarna_pay_now"
    ONLINE_BANKING_POLAND = "online_banking_poland"
    PAYCONIQ_BY_BANCONTACT = "payconiq_by_bancontact"
    ELECTRONIC_PAYMENT_STANDARD = "electronic_payment_standard"
    KBC_PAYMENT_BUTTON = "kbc_payment_button"
    PAY_BY_BANK = "pay_by_bank"
    TRUSTLY = "trustly"
    STABLECOIN = "stablecoin"

    def __str__(self):
        return self.value


class PaymentMethodType(Enum):
    CARD = "card"
    PAYPAL_EXPRESS_CHECKOUT = "paypal_express_checkout"
    AMAZON_PAYMENTS = "amazon_payments"
    DIRECT_DEBIT = "direct_debit"
    GENERIC = "generic"
    ALIPAY = "alipay"
    UNIONPAY = "unionpay"
    APPLE_PAY = "apple_pay"
    WECHAT_PAY = "wechat_pay"
    IDEAL = "ideal"
    GOOGLE_PAY = "google_pay"
    SOFORT = "sofort"
    BANCONTACT = "bancontact"
    GIROPAY = "giropay"
    DOTPAY = "dotpay"
    UPI = "upi"
    NETBANKING_EMANDATES = "netbanking_emandates"
    VENMO = "venmo"
    PAY_TO = "pay_to"
    FASTER_PAYMENTS = "faster_payments"
    SEPA_INSTANT_TRANSFER = "sepa_instant_transfer"
    AUTOMATED_BANK_TRANSFER = "automated_bank_transfer"
    KLARNA_PAY_NOW = "klarna_pay_now"
    ONLINE_BANKING_POLAND = "online_banking_poland"
    PAYCONIQ_BY_BANCONTACT = "payconiq_by_bancontact"
    ELECTRONIC_PAYMENT_STANDARD = "electronic_payment_standard"
    KBC_PAYMENT_BUTTON = "kbc_payment_button"
    PAY_BY_BANK = "pay_by_bank"
    TRUSTLY = "trustly"
    STABLECOIN = "stablecoin"

    def __str__(self):
        return self.value


class PaymentVoucherType(Enum):
    BOLETO = "boleto"

    def __str__(self):
        return self.value


class PeriodUnit(Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

    def __str__(self):
        return self.value


class PriceType(Enum):
    TAX_EXCLUSIVE = "tax_exclusive"
    TAX_INCLUSIVE = "tax_inclusive"

    def __str__(self):
        return self.value


class PricingModel(Enum):
    FLAT_FEE = "flat_fee"
    PER_UNIT = "per_unit"
    TIERED = "tiered"
    VOLUME = "volume"
    STAIRSTEP = "stairstep"

    def __str__(self):
        return self.value


class PricingType(Enum):
    PER_UNIT = "per_unit"
    FLAT_FEE = "flat_fee"
    PACKAGE = "package"

    def __str__(self):
        return self.value


class ProductCatalogVersion(Enum):
    V1 = "v1"
    V2 = "v2"

    def __str__(self):
        return self.value


class ProrationType(Enum):
    FULL_TERM = "full_term"
    PARTIAL_TERM = "partial_term"
    NONE = "none"

    def __str__(self):
        return self.value


class ReferralSystem(Enum):
    REFERRAL_CANDY = "referral_candy"
    REFERRAL_SAASQUATCH = "referral_saasquatch"
    FRIENDBUY = "friendbuy"

    def __str__(self):
        return self.value


class ReferrerRewardType(Enum):
    NONE = "none"
    REFERRAL_DIRECT_REWARD = "referral_direct_reward"
    CUSTOM_PROMOTIONAL_CREDIT = "custom_promotional_credit"
    CUSTOM_REVENUE_PERCENT_BASED = "custom_revenue_percent_based"

    def __str__(self):
        return self.value


class RefundableCreditsHandling(Enum):
    NO_ACTION = "no_action"
    SCHEDULE_REFUND = "schedule_refund"

    def __str__(self):
        return self.value


class ReportBy(Enum):
    CUSTOMER = "customer"
    INVOICE = "invoice"
    PRODUCT = "product"
    SUBSCRIPTION = "subscription"

    def __str__(self):
        return self.value


class ResumeOption(Enum):
    IMMEDIATELY = "immediately"
    SPECIFIC_DATE = "specific_date"

    def __str__(self):
        return self.value


class RetryEngine(Enum):
    CHARGEBEE = "chargebee"
    FLEXPAY = "flexpay"
    SUCCESSPLUS = "successplus"

    def __str__(self):
        return self.value


class Role(Enum):
    PRIMARY = "primary"
    BACKUP = "backup"
    NONE = "none"

    def __str__(self):
        return self.value


class ScheduleType(Enum):
    IMMEDIATE = "immediate"
    SPECIFIC_DATES = "specific_dates"
    FIXED_INTERVALS = "fixed_intervals"

    def __str__(self):
        return self.value


class Source(Enum):
    ADMIN_CONSOLE = "admin_console"
    API = "api"
    BULK_OPERATION = "bulk_operation"
    SCHEDULED_JOB = "scheduled_job"
    HOSTED_PAGE = "hosted_page"
    PORTAL = "portal"
    SYSTEM = "system"
    NONE = "none"
    JS_API = "js_api"
    MIGRATION = "migration"
    EXTERNAL_SERVICE = "external_service"

    def __str__(self):
        return self.value


class TaxExemptReason(Enum):
    TAX_NOT_CONFIGURED = "tax_not_configured"
    REGION_NON_TAXABLE = "region_non_taxable"
    EXPORT = "export"
    CUSTOMER_EXEMPT = "customer_exempt"
    PRODUCT_EXEMPT = "product_exempt"
    ZERO_RATED = "zero_rated"
    REVERSE_CHARGE = "reverse_charge"
    HIGH_VALUE_PHYSICAL_GOODS = "high_value_physical_goods"
    ZERO_VALUE_ITEM = "zero_value_item"
    TAX_NOT_CONFIGURED_EXTERNAL_PROVIDER = "tax_not_configured_external_provider"

    def __str__(self):
        return self.value


class TaxJurisType(Enum):
    COUNTRY = "country"
    FEDERAL = "federal"
    STATE = "state"
    COUNTY = "county"
    CITY = "city"
    SPECIAL = "special"
    UNINCORPORATED = "unincorporated"
    OTHER = "other"

    def __str__(self):
        return self.value


class TaxOverrideReason(Enum):
    ID_EXEMPT = "id_exempt"
    CUSTOMER_EXEMPT = "customer_exempt"
    EXPORT = "export"

    def __str__(self):
        return self.value


class Taxability(Enum):
    TAXABLE = "taxable"
    EXEMPT = "exempt"

    def __str__(self):
        return self.value


class TaxjarExemptionCategory(Enum):
    WHOLESALE = "wholesale"
    GOVERNMENT = "government"
    OTHER = "other"

    def __str__(self):
        return self.value


class TrialEndAction(Enum):
    SITE_DEFAULT = "site_default"
    PLAN_DEFAULT = "plan_default"
    ACTIVATE_SUBSCRIPTION = "activate_subscription"
    CANCEL_SUBSCRIPTION = "cancel_subscription"

    def __str__(self):
        return self.value


class Type(Enum):
    CARD = "card"
    PAYPAL_EXPRESS_CHECKOUT = "paypal_express_checkout"
    AMAZON_PAYMENTS = "amazon_payments"
    DIRECT_DEBIT = "direct_debit"
    GENERIC = "generic"
    ALIPAY = "alipay"
    UNIONPAY = "unionpay"
    APPLE_PAY = "apple_pay"
    WECHAT_PAY = "wechat_pay"
    IDEAL = "ideal"
    GOOGLE_PAY = "google_pay"
    SOFORT = "sofort"
    BANCONTACT = "bancontact"
    GIROPAY = "giropay"
    DOTPAY = "dotpay"
    UPI = "upi"
    NETBANKING_EMANDATES = "netbanking_emandates"
    VENMO = "venmo"
    PAY_TO = "pay_to"
    FASTER_PAYMENTS = "faster_payments"
    SEPA_INSTANT_TRANSFER = "sepa_instant_transfer"
    AUTOMATED_BANK_TRANSFER = "automated_bank_transfer"
    KLARNA_PAY_NOW = "klarna_pay_now"
    ONLINE_BANKING_POLAND = "online_banking_poland"
    PAYCONIQ_BY_BANCONTACT = "payconiq_by_bancontact"
    ELECTRONIC_PAYMENT_STANDARD = "electronic_payment_standard"
    KBC_PAYMENT_BUTTON = "kbc_payment_button"
    PAY_BY_BANK = "pay_by_bank"
    TRUSTLY = "trustly"
    STABLECOIN = "stablecoin"
    FREE_TRIAL = "free_trial"
    PAY_UP_FRONT = "pay_up_front"
    PAY_AS_YOU_GO = "pay_as_you_go"

    def __str__(self):
        return self.value


class UnbilledChargesHandling(Enum):
    NO_ACTION = "no_action"
    INVOICE = "invoice"

    def __str__(self):
        return self.value


class UnbilledChargesOption(Enum):
    INVOICE = "invoice"
    DELETE = "delete"

    def __str__(self):
        return self.value


class UnpaidInvoicesHandling(Enum):
    NO_ACTION = "no_action"
    SCHEDULE_PAYMENT_COLLECTION = "schedule_payment_collection"

    def __str__(self):
        return self.value


class UsageAccumulationResetFrequency(Enum):
    NEVER = "never"
    SUBSCRIPTION_BILLING_FREQUENCY = "subscription_billing_frequency"

    def __str__(self):
        return self.value


class ValidationStatus(Enum):
    NOT_VALIDATED = "not_validated"
    VALID = "valid"
    PARTIALLY_VALID = "partially_valid"
    INVALID = "invalid"

    def __str__(self):
        return self.value


class VoucherType(Enum):
    BOLETO = "boleto"

    def __str__(self):
        return self.value
