from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import logging


from payments.strategies.iyzico.exceptions import (
    CheckoutFormInitializeException,
    CheckoutFormRetrieveExeption,
)
from payments.models import PaymentMethod
from payments.services import PaymentService
from payments.services import PaymentStrategyFactory as Factory


logger = logging.getLogger(__name__)


def index(request):
    ctx = {"title": "payment index"}
    return render(request, "payments/index.html", ctx)


class CheckoutFormInitView(View):
    def post(self, request, *args, **kwargs):
        """If this view requested with POST then we will redirect to paymentPageUrl which is iyzico,
        then payment process will continue there.
        """
        try:
            strategy = Factory.get_strategy(PaymentMethod.IYZICO.value)
            res = PaymentService(strategy).checkout_init()
            return redirect(res["payment_url"])
        except CheckoutFormInitializeException as e:
            logger.exception(e)

    def get(self, request, *args, **kwargs):
        ctx = {"title": _("Checkout Page")}
        strategy = Factory.get_strategy(PaymentMethod.IYZICO.value)
        res = PaymentService(strategy).checkout_init()
        ctx.update(
            {
                "checkout_form_content": res["checkout_form_content"],
            }
        )
        return render(request, "payments/checkout.html", ctx)


@require_POST
@csrf_exempt
def callback(request):
    """The payment service will request to this view"""
    try:
        token = request.POST.get("token")
        strategy = Factory.get_strategy(PaymentMethod.IYZICO.value)
        response = PaymentService(strategy).checkout_retrieve(token)
        return HttpResponseRedirect(response["url"])
    except CheckoutFormRetrieveExeption as e:
        logger.exception(e)


class SuccessView(TemplateView):
    template_name = "payments/payment-success.html"


class FailedView(TemplateView):
    template_name = "payments/payment-failed.html"
