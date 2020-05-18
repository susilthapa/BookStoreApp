from django.urls import path
from .views import OrdersPageView, OrderSuccessView, OrderFailureView


urlpatterns = [
    path('', OrdersPageView.as_view(), name='orders'),
    path('esewa_payment_success/', OrderSuccessView.as_view(), name='payment-success'),
    path('esewa_payment_failure/', OrderFailureView.as_view(), name='payment-failure')
]
