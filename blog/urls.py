from django.urls import path, include
from . import views

from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register('categorie_article',api.CategorieArticleViewSet)
router.register('tag',api.TagViewSet)
router.register('commentaire',api.CommentaireViewSet)
router.register('article',api.ArticleViewSet)





urlpatterns = [
    
    path("single/<int:id>/", views.single, name="single"),
    path("category",views.category, name="category"),
    path('category/<int:limit>', views.category, name="category"),
    path('search/', views.search, name='search'),
    path('api/', include(router.urls))

]