from django.urls import path, include
from . import views

from apiApp.blog.apiviews import*
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('categorie', CategorieArticleViewset)
router.register('tag', TagViewset)
router.register('article', ArticleViewset)
router.register('commentaire', CommentaireViewset)


urlpatterns = [
    
    path("single/<int:id>/", views.single, name="single"),
    path("category",views.category, name="category"),
    path('category/<int:limit>', views.category, name="category"),
    path('search/', views.search, name='search'),
    
]