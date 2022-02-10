from django.urls import path

from subscribeapp.views import SubscriptionView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscription/', SubscriptionView.as_view(), name='subscription')
]