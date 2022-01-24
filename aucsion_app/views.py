from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SellerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerCreateView(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerBlackListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SellerBlackList.objects.all()
    serializer_class = SellerBlackListSerializer


class SellerBlackListCreateView(generics.ListCreateAPIView):
    queryset = SellerBlackList.objects.all()
    serializer_class = SellerBlackListSerializer


class BuyerBlackListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuyerBlackList.objects.all()
    serializer_class = BuyerBlackListSerializer


class BuyerBlackListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = BuyerBlackListSerializer


class BuyerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


class BuyerCreateView(generics.ListCreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


class AucsionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aucsion.objects.all()
    serializer_class = AucsionSerializer


class AucsionCreateView(generics.ListCreateAPIView):
    queryset = Aucsion.objects.all()
    serializer_class = AucsionSerializer


class AucsionHistoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AucsionHistory.objects.all()
    serializer_class = AucsionHistorySerializer


class AucsionHistoryCreateView(generics.ListCreateAPIView):
    queryset = AucsionHistory.objects.all()
    serializer_class = AucsionHistorySerializer


class ProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PurchaseView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseCreateView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class DeliveryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class DeliveryCreateView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class ExpertView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer


class ExpertCreateView(generics.ListCreateAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer


class ExpertiseView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerializer


class ExpertiseCreateView(generics.ListCreateAPIView):
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerializer


