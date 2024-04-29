from django.urls import path
from .views import StripeCancelView, StripeCheckoutView, StripeSuccessView

urlpatterns = [
    path('create-checkout-session/<int:pk>', StripeCheckoutView.as_view()),
    path('success/', StripeSuccessView.as_view(), name='stripe_success'),
    path('cancel/', StripeCancelView.as_view(), name='stripe_cancel'),
]