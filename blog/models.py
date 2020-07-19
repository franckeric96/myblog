from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.


class CategorieArticle(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/CategorieArticle")

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Categorie Article'
        verbose_name_plural = 'Categories Article'

    def __str__(self):
        return self.nom


class Tag(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    contenu = HTMLField()
    image = models.ImageField(upload_to="images/Article")
    tag = models.ManyToManyField(Tag, related_name='tag_Article')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_article')
    categorie = models.ForeignKey(CategorieArticle, on_delete=models.CASCADE, related_name='categorie_Article')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaire_article')
    nom = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    website = models.URLField(null=True)
    commentaire = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return self.user.username

class like(models.Model):
    """Model definition for like."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_article')
    is_like = models.BooleanField(default=False)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        """Meta definition for like."""

        verbose_name = 'like'
        verbose_name_plural = 'likes'

    def __str__(self):
        return self.user.username
        
