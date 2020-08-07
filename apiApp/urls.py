from .blog.apiviews import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('categorie', CategorieArticleViewset)
router.register('tag', TagViewset)
router.register('article', ArticleViewset)
router.register('commentaire', CommentaireViewset)

app_name = 'api'

urlpatterns = [
    

]

urlpatterns += router.urls