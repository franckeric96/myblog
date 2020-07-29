from . import models
from rest_framework import viewsets
from . import serializers
from . import models



class CategorieArticleViewSet(viewsets.ModelViewSet):
    queryset = models.CategorieArticle.objects.filter(status=True)
    serializer_class = serializers.CategorieArticleSerializer



class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.filter(status=True)
    serializer_class = serializers.TagSerializer



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.filter(status=True)
    serializer_class = serializers.ArticleSerializer



class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = models.Commentaire.objects.filter(status=True)
    serializer_class = serializers.CommentaireSerializer
