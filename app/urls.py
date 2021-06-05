from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
# from .views import

schema_view = get_schema_view(title='Blog API')
router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # path('business/', BusinessListView.as_view(), name='business-info'),
    # path('business/<int:pk>/', BusinessDetailView.as_view(), name='business-data'),
    # path('orders/products/business/<int:pk>', BusinessOrderDetailView.as_view()),
    # path('user/business/<int:pk>', BusinessUserDetailView.as_view()),
    # path('business/bank/<int:pk>', BusinessBankDetailView.as_view()),

]