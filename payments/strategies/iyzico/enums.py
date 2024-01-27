import enum


class PaymentStatus(enum.StrEnum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    INIT_THREEDS = "INIT_THREEDS"
    CALLBACK_THREEDS = "CALLBACK_THREEDS"
    