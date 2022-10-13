import json

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from api import user
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

from ..billing.models import BillingProfile
from ..cart.models import Cart
from ..product.models import Product

from .models import Order
from .serializers import OrderSerializer, DetailedOrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    # Operations to be performed
    queryset = Order.objects.all().order_by('id')
    # Class responsible for serializing the data
    serializer_class = OrderSerializer

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def cancel(self, request, pk):
        item = self.get_object()
        serializer = OrderSerializer(data=request.data)
        item.mark_cancel()
        #return Response({'status': 'status changed'})
        return Response({
            "order": OrderSerializer(item, context={'request': request}).data
        })
class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        profile_id = request.GET.get("profile_id", 1)

        if profile_id == None:
            return Response({'error': 'Profile Id Not Found'}, status=400)

        profiles = BillingProfile.objects.filter(id=profile_id)

        if not profiles.count() == 1:
            return Response({'error': 'Profile Doesn\'t exist'}, status=400)

        cart_obj, _ = Cart.objects.get_existing_or_new(request)

        if cart_obj.total_cart_products == 0:
            return Response({'error': 'Cart Is Empty'}, status=400)

        order_obj = Order.objects.get_order(profiles.first())

        return Response({
            "order": DetailedOrderSerializer(order_obj, context={'request': request}).data
        })

    def post(self, request, *args, **kwargs):

        profile_id = request.data.get("profile_id")

        if profile_id == None:
            # return Response({'error': 'Profile Id Not Found'}, status=400)
            profiles = BillingProfile.objects.filter(user=request.user)
        else:
            profiles = BillingProfile.objects.filter(id=profile_id)

        if not profiles.count() == 1:
            return Response({'error': 'Profile Doesn\'t exist'}, status=400)

        order_obj = Order.objects.get_order(profiles.first())

        return Response(DetailedOrderSerializer(order_obj).data)


