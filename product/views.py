from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import CategoryListSerializer, CategoryDetailSerializer
from . serializers import ProductListSerializer, ProductDetailSerializer
from .serializers import ReviewListSerializer, ReviewDetailSerializer


@api_view(['GET'])
def category_detail_api_view(reguest, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = CategoryDetailSerializer(category, many=False).data
    return Response(data=data)



@api_view(['GET'])
def category_list_api_view(request):
    #1 queryset
    categories = Category.objects.all()
    #2 reformat serializer 
    category_list = CategoryListSerializer(categories, many=True).data
    #3 return response
    return Response(data=category_list, status=status.HTTP_200_OK)


@api_view(['GET'])
def  product_detail_api_view(reguest, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product, many=False).data
    return Response(data=data)


@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all() 
    product_list = ProductListSerializer(products, many=True).data
    return Response(data=product_list, status=status.HTTP_200_OK)





@api_view(['GET'])
def review_detail_api_view(reguest, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(review, many=False).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all() 
    review_list = ReviewListSerializer(reviews, many=True).data
    return Response(data=review_list, status=status.HTTP_200_OK)
