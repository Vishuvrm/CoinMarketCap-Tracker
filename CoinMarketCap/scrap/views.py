from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from .serializers import ScrappedDataSerializer
from .models import ScrappedData


class PutData(generics.ListCreateAPIView):
    serializer_class = ScrappedDataSerializer

    def post(self, request, *args, **kwargs):
        request_data = request.data
        # validate the request data
        # instance = ScrappedData.objects.filter(pk=request_data["name"])
        request_serializer = self.serializer_class(data=request_data, many=True)
        if request_serializer.is_valid(raise_exception=True):
            ScrappedData.create_or_update(request_data)
            # request_serializer.save()
            # ScrappedData.objects.update_or_create(request_data)
            return Response({"Success": "Inserted successfully into database"}, status=status.HTTP_201_CREATED)
        return Response(request_serializer.errors, status=status.HTTP_403_FORBIDDEN)
# Create your views here.
class FetchData(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        response_obj = ScrappedData.objects.all()
        response = []
        for res in response_obj:
            "name", "price", "perc_1h", "perc_24h", "perc_7d", "market_cap", "volume_24h", "circulating_supply"
            r = {
                "name": res.name,
                "price": res.price,
                "perc_1h": res.perc_1h,
                "perc_24h": res.perc_24h,
                "perc_7d": res.perc_7d,
                "market_cap": res.market_cap,
                "volume_24h": res.volume_24h,
                "circulating_supply": res.circulating_supply
            }
        
            response.append(r)
        response.pop(0)
    
        return Response(response, status=status.HTTP_200_OK)