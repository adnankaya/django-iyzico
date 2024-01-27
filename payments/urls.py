from django.urls import path, include

from . import views

app_name = "payments"

urlpatterns = [
    path("", views.index, name="index"),
    path("callback/", views.callback, name="callback"),
    path("checkout/", views.CheckoutFormInitView.as_view(), name="checkout"),
    path("success/", views.SuccessView.as_view(), name="success"),
    path("failed/", views.FailedView.as_view(), name="failed"),
   
    
]
