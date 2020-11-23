from rest_framework import serializers
from .models import Article


from rest_framework import serializers
from .models import Article, Item



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
#        fields = ['id', 'title', 'author']
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
