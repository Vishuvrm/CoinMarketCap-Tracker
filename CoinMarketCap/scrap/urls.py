from scrap.views import PutData, FetchData
from django.urls import path

urlpatterns = [
    path('put-data', PutData.as_view(), name='data'),
    path('fetch-data', FetchData.as_view(), name='fetch')
]
