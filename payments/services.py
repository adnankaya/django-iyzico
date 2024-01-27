from payments.strategies.paypal import PayPalPaymentStrategy
from payments.strategies.creditcard import CreditCardPaymentStrategy
from payments.strategies.banktransfer import BankTransferPaymentStrategy
from payments.strategies.iyzico import IyzicoPaymentStrategy

from .models import PaymentMethod


class PaymentService:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        return self.strategy.process_payment(amount)

    def checkout_init(self, *args, **kwargs):
        return self.strategy.checkout_init(*args, **kwargs)

    def checkout_retrieve(self, *args, **kwargs):
        return self.strategy.checkout_retrieve(*args, **kwargs)


class PaymentStrategyFactory:
    @staticmethod
    def get_strategy(payment_method: str):
        if payment_method == PaymentMethod.PAYPAL.value:
            return PayPalPaymentStrategy()
        elif payment_method == PaymentMethod.IYZICO.value:
            return IyzicoPaymentStrategy()
        elif payment_method == PaymentMethod.CREDIT_CARD.value:
            return CreditCardPaymentStrategy()
        elif payment_method == PaymentMethod.BANK_TRANSFER.value:
            return BankTransferPaymentStrategy()
