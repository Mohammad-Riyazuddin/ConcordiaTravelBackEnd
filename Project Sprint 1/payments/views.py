
from django.http import HttpResponseRedirect
import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from api.models import Package
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeSuccessView(TemplateView):
    template_name = 'success.html'

class StripeCancelView(TemplateView):
    template_name = 'cancel.html'

class StripeCheckoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            package_id = self.kwargs['pk']
            package = Package.objects.get(id=package_id)
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'cad',
                            'unit_amount': int(round(package.total_cost * 100, 0)),
                            'product_data': {
                                'name': package.name,
                            },
                        },
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card'],
                mode='payment',
                success_url= settings.SITE_URL + '?success=true',
                cancel_url= settings.SITE_URL + '?cancel=true',
            )
            print(checkout_session.url)
            return redirect(checkout_session.url)
        except:
            return Response(
                {'error': 'Something went wrong when trying to create the checkout session'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )