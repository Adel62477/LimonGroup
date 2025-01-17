from rest_framework import generics, viewsets
from django.db.models.query import QuerySet
from decimal import Decimal
from django.db.models import F, Sum

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import get_production

from .serializers import (OrderSerializer,
                          SewingModelSerializer,
                          DailyWorkSerializer,
                          NewOrderSerializer,
                          PriceSerializer,
                          FabricCuttingSerializer,
                          RawStuffSerializer,
                          StorageSerializer, DailyWorkDetailSerializer)
from .models import (Order, SewingModel, DailyWork,
                     NewOrder, Price, FabricCutting, RawStuff, Storage)


class PriceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


price_list_create = PriceListCreateAPIView.as_view()


class PriceRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


price_ret_update = PriceRetrieveUpdateAPIView.as_view()


class PriceRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


price_ret_destroy = PriceRetrieveDestroyAPIView.as_view()


class SewingModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = SewingModel.objects.all()
    serializer_class = SewingModelSerializer


sewingModel_list_create = SewingModelListCreateAPIView.as_view()


class SewingModelRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = SewingModel.objects.all()
    serializer_class = SewingModelSerializer


sewingModel_ret_update = SewingModelRetrieveUpdateAPIView.as_view()


class SewingModelRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = SewingModel.objects.all()
    serializer_class = SewingModelSerializer


sewingModel_ret_destroy = SewingModelRetrieveDestroyAPIView.as_view()


class DailyWorkListAPIView(generics.ListCreateAPIView):
class DailyWorkListAPIView(generics.ListAPIView):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkDetailSerializer


class DailyWorkCreateAPIView(generics.CreateAPIView):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkSerializer
    ordering_fields = ['id'] 
    


class DailyWorkCreateUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkDetailSerializer


class DailyWorkRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkSerializer


class NewOrderListAPIView(generics.ListCreateAPIView):
    queryset = NewOrder.objects.all()
    serializer_class = NewOrderSerializer


class NewOrderRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = NewOrder.objects.all()
    serializer_class = NewOrderSerializer


class NewOrderRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = NewOrder.objects.all()
    serializer_class = NewOrderSerializer


class FabricCuttingListCreateAPIView(generics.ListCreateAPIView):
    queryset = FabricCutting.objects.all()
    serializer_class = FabricCuttingSerializer


class FabricCuttingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = FabricCutting.objects.all()
    serializer_class = FabricCuttingSerializer


class FabricCuttingRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = NewOrder.objects.all()
    serializer_class = FabricCuttingSerializer


class RawStuffListCreateAPIView(generics.ListCreateAPIView):
    queryset = RawStuff.objects.all()
    serializer_class = RawStuffSerializer


class RawStuffRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = RawStuff.objects.all()
    serializer_class = RawStuffSerializer


class RawStuffRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = RawStuff.objects.all()
    serializer_class = FabricCuttingSerializer


class StorageListAPIView(generics.ListCreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class StorageRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class StorageRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)
    
class ProductionWork(APIView):
    def get(self, request):
        date = request.data.get('date')
        if not date:
            return Response({'error': 'Вы не указали дату'}, status=400)

        summary = get_production(date)

        return Response(summary)

class QuantityModelCreateView(generics.CreateAPIView):
    queryset = QuantityModel.objects.all()
    serializer_class = QuantityModelSerializer


class QuantityModelListView(generics.ListAPIView):
    queryset = QuantityModel.objects.all()
    serializer_class = QuantityModelSerializer


class QuantityUpdateModelView(generics.RetrieveUpdateAPIView):
    queryset = QuantityModel.objects.all()
    serializer_class = QuantityModelSerializer


class QuantityDestroyModelView(generics.RetrieveDestroyAPIView):
    queryset = QuantityModel.objects.all()
    serializer_class = QuantityModelSerializer

# class OrderCreateUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# class OrderListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

