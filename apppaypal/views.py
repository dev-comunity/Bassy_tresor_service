# import uuid 
# from django.shortcuts import render,redirect
# from django.urls import reverse
# from django.contrib import messages
# # from paypal.standard.forms import PayPalPaymentsForm
# from django.conf import settings

# Create your views here.
# def hom(request):
#     paypal_dict={
#         'business':settings.PAYPAL_RECEIVER_EMAIL,
#         'amount':'20.00',
#         'item_name': 'produits 1',
#         'invoice':str(uuid.uuid4()),
#         'currenty_code':'USD',
#         'notify_url':f'http:// {host}{reverse("paypal-ipn")}',
#         'return_url':f'http://{host}{reverse("paypal-return")}',
#         'cancel_url':f'http://{host}{reverse("paypal-cancel")}',
#     }
#     form=PayPalPaymentsForm(initial=paypal_dict)
#     content={
#             'form':form
#         }
#     return render(request,'paiement/formpay.html',content)

#fonction of paypal 
# def paypal_return(request):
#     messages.seccuss(request,'you\'ve succesfy made a paiement')
#     return redirect('home')

# def paypal_cancel(request):
#     messages.error(request,'your order has been cancelled')
#     return redirect('home')

