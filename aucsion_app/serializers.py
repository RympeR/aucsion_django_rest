from datetime import datetime, timedelta

from aucsion.utils.customFields import TimestampField
from django.db.models import Count
from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Seller
        fields = '__all__'


class SellerBlackListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    seller = SellerSerializer()

    class Meta:
        model = SellerBlackList
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Buyer
        fields = '__all__'


class BuyerBlackListSerializer(serializers.ModelSerializer):
    buyer = BuyerSerializer()

    class Meta:
        model = BuyerBlackList
        fields = '__all__'


class AucsionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aucsion
        fields = '__all__'


class AucsionHistorySerializer(serializers.ModelSerializer):
    buyer = BuyerSerializer()
    aucsion = AucsionSerializer()

    class Meta:
        model = AucsionHistory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    seller = SellerSerializer()
    aucsion = AucsionSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    buyer = BuyerSerializer()

    class Meta:
        model = Purchase
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer()

    class Meta:
        model = Delivery
        fields = '__all__'


class ExpertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expert
        fields = '__all__'


class ExpertiseSerializer(serializers.ModelSerializer):
    expert = ExpertSerializer()
    product = ProductSerializer()

    class Meta:
        model = Expertise
        fields = '__all__'
