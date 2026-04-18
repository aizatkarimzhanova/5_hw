from rest_framework import serializers
from .models import Category, Product, Review
from rest_framework.exceptions import ValidationError

class CategoryListSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = 'id name products_count'.split()
    
    def get_products_count(self, obj):
        return obj.products.count()

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = 'id title reviews average_rating'.split()
        depth = 1     

    def get_average_rating(self, obj):
        ratings = [i.stars for i in obj.reviews.all() if i.stars is not None]
        if ratings:
            return sum(ratings) / len(ratings)
        return 0 

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=255)

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=255)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Director does not exist')
        return category_id

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=2, max_length=255)
    product_id = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError('Product does not exist')
        return product_id