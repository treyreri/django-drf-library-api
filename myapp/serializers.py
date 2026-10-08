from rest_framework import serializers
from .models import Country, Author, Book


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'code']


class AuthorSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    country_id = serializers.PrimaryKeyRelatedField( queryset=Country.objects.all(), source='country', write_only=True )

    class Meta:
        model = Author
        fields = [ 'id', 'name', 'age', 'country', 'country_id' ]


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField( queryset=Author.objects.all(), source='author', write_only=True)
    title_upper = serializers.SerializerMethodField()
    is_expensive = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'pages',
            'price',
            'author',
            'author_id',
            'title_upper',
            'is_expensive' ]

    def validate_title(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError( "Title must start with a capital letter " )
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError( "Price must be greater than 0" )
        return value

    def validate(self, attrs):
        pages = attrs.get('pages')
        price = attrs.get('price')
        if pages > 1000 and price < 200:
            raise serializers.ValidationError(
                "If pages are greater than 1000, "
                "price must be at least 200 " )
        return attrs

    def get_title_upper(self, obj):
        return obj.title.upper()

    def get_is_expensive(self, obj):
        return obj.price > 200

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['book_info'] = ( f"{instance.title} — {instance.pages} pages")
        return representation