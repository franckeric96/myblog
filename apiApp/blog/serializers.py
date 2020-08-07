from rest_framework import serializers
from blog import models



class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:

        model = models.Commentaire
        fields = '__all__'



class ArticleSerializer(serializers.ModelSerializer):
    commentaire_article = CommentaireSerializer(many=True, required=False)

    class Meta:
        model = models.Article
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    tag_Article = ArticleSerializer(many=True, required=False)

    class Meta:

        model = models.Tag
        fields = '__all__'

class CategorieArticleSerializer(serializers.ModelSerializer):
    categorie_Article = ArticleSerializer(many=True, required=False)

    class Meta:

        model = models.CategorieArticle
        fields = '__all__'