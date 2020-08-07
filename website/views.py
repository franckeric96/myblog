from django.shortcuts import render
from .models import SocialAccount, Gallerie,  Presentation
from blog.models import Tag, Article, CategorieArticle

# Create your views here.


def home(request):


    tag = Tag.objects.filter(status=True)
    sociaux = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[:1].get()
    gallerie = Gallerie.objects.filter(status=True)[:4]
    articles = Article.objects.filter(status=True)[:2]
    article_order = Article.objects.order_by('date_add')[:4]
    categorie = CategorieArticle.objects.filter(status=True)[:2]
    recent = Article.objects.order_by('date_add')[:3]




    datas = {

        'tag':tag,
        'sociaux':sociaux,
        'presentation':presentation,
        'gallerie':gallerie,
        #'articles':articles,
        #'order':article_order,
        'categorie':categorie,
        'recent': recent

    }

    return render(request, 'pages/index.html', datas)