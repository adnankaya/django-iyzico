import json
import logging
import iyzipay
from django.conf import settings
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


from payments.strategies.base import PaymentStrategy
from payments.strategies.iyzico.exceptions import (
    CheckoutFormInitializeException,
    CheckoutFormRetrieveExeption,
)
from .enums import PaymentStatus


# TODO use dynamic data instead this!
from payments.strategies.iyzico.dummy import request_data


logger = logging.getLogger(__name__)


class IyzicoPaymentStrategy(PaymentStrategy):
    options = {
        "api_key": settings.IYZICO_APIKEY,
        "secret_key": settings.IYZICO_SECRETKEY,
        "base_url": settings.IYZICO_API_URL,
    }
    domain = f"{settings.DOMAIN}:{settings.DOMAIN_PORT}"
    protocol = "http" if settings.DOMAIN in ["localhost", "127.0.0.1"] else "https"

    def get_callback_url(self):
        callback_path = reverse("payments:callback")
        return f"{self.protocol}://{self.domain}{callback_path}"

    def process_payment(self, amount):
        # Logic to process payment via Iyzico
        pass

    def checkout_init(self):
        try:
            request_data["callbackUrl"] = self.get_callback_url()
            res = iyzipay.CheckoutFormInitialize().create(request_data, self.options)
            result = res.read().decode("utf-8")
            json_res = json.loads(result)
            # NOTE you can store token in database to validate payment in the end.
            token = json_res["token"]
            paymentPageUrl = json_res["paymentPageUrl"]
            checkout_form_content = json_res["checkoutFormContent"]

            return {
                "payment_url": paymentPageUrl,
                "checkout_form_content": checkout_form_content,
            }
        except:
            raise CheckoutFormInitializeException(
                _("Could not initialize iyzico checkout form!")
            )

    def checkout_retrieve(self, token: str, *args, **kwargs):
        response = {"url": None}
        try:
            payload = {
                "locale": request_data["locale"],
                "conversationId": request_data["conversationId"],
                "token": token,
            }

            res = iyzipay.CheckoutForm().retrieve(payload, self.options)
            result = res.read().decode("utf-8")
            json_res = json.loads(result)
            if json_res["paymentStatus"] == PaymentStatus.SUCCESS.value:
                response["url"] = reverse("payments:success")
            else:
                response["url"] = reverse("payments:failed")
            return response
        except CheckoutFormRetrieveExeption as e:
            logger.exception(e)
