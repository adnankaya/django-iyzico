from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class PaymentMethod(models.TextChoices):
    PENDING = "PENDING", _("PENDING")
    PAYPAL = "PAYPAL", _("PAYPAL")
    IYZICO = "IYZICO", _("IYZICO")
    CREDIT_CARD = "CREDIT CARD", _("CREDIT CARD")
    BANK_TRANSFER = "BANK TRANSFER", _("BANK TRANSFER")