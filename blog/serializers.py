from rest_framework import serializers
from . import models


class CategorieArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategorieArticle
        fields = '__all__'



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'





class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'
        depth = 1



class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Commentaire
        fields = '__all__'
        depth = 1

