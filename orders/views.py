from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import View
from .import paymentConf as config
from django.contrib.auth.models import Permission

import requests

class OrdersPageView(TemplateView):
  template_name = "orders/purchase.html"
  # def post(self, request, *args, **kwargs):
  #   url ="https://uat.esewa.com.np/epay/main"
  #   d = {
  #       'amt': 100,
  #         'pdc': 0,
  #         'psc': 0,
  #         'txAmt': 0,
  #         'tAmt': 100,
  #         'pid':'2c40d92www9d453',
  #         'scd':'epay_payment',
  #         'su':'http://127.0.0.1:8000/orders/esewa_payment_success/',
  #         'fu':'http://127.0.0.1:8000/orders/esewa_payment_failure/'
  #       }
  #   resp = requests.post(url, d)
  #   print(resp.text)

     

class OrderSuccessView(TemplateView):
  template_name = 'orders/success.html'

  def get(self, request, *args, **kwargs):
    permission = Permission.objects.get(codename='special_status')
    user = request.user
    user.user_permissions.add(permission)
    return redirect('book_list')

  # def get(self, request, *args, **kwargs):
  #   url ="https://uat.esewa.com.np/epay/transrec"
  #   d = {
  #       'amt': 100,
  #       'scd': 'epay_payment',
  #       'rid': request.GET['refId'],
  #       'pid':'mybook31q23123',
  #   }
  #   resp = requests.post(url, d)
  #   print(f"RESP = {resp.text}")
    
  #   if 'Success' in resp.text:
  #     permission = Permission.objects.get(codename='special_status')
  #     user = request.user
  #     user.user_permissions.add(permission)
  #     return redirect('payment-success')
  #   else:
  #     print('FAIL')
  #     return render(request, 'orders/failure.html')

    

class OrderFailureView(TemplateView):
  template_name = 'orders/failure.html'

