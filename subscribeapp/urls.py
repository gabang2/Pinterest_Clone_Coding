from django.urls import path

from subscribeapp.views import SubscriptionView, SubscriptionListView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscription/', SubscriptionView.as_view(), name='subscription'),
    path('list/', SubscriptionListView.as_view(), name='list')
]