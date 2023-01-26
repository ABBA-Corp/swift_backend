from django.urls import path
from .views import PaymentView, checkout_view


urlpatterns = [
    path('pay/', PaymentView.as_view()),
    path('checkout/', checkout_view),
]