from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Sale
from .serializers import ProductSerializer, SaleSerializer
from django.db.models import Q

class ProductSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        products = Product.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__icontains=query) |
            Q(tag__icontains=query)
        )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetailView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)
        return Response(serializer.data)

class AddSaleView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        sale = Sale(product=product)
        sale.save()

        return Response({'success': True}, status=status.HTTP_201_CREATED)

class SaleListView(APIView):
    def get(self, request):
        sales = Sale.objects.all()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)