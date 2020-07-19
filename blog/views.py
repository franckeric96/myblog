from django.shortcuts import render, get_object_or_404, redirect
from website.models import Presentation, SocialAccount, Gallerie
from blog.models import Tag, Article, CategorieArticle, Commentaire
from django.db.models import Q

# Create your views here.

def single(request,id):

    tag = Tag.objects.filter(status=True)
    sociaux = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[:1].get()
    gallerie = Gallerie.objects.filter(status=True)[:4]
    recent = Article.objects.order_by('date_add')[:3]
    gallerie = Gallerie.objects.filter(status=True)[:4]
    article_order = Article.objects.order_by('date_add')[:4]
    categorie = CategorieArticle.objects.filter(status=True)[:2]
    article_single = get_object_or_404(Article, id=id)


    if request.method == 'POST' and request.POST['comment']:
        if request.user.is_authenticated:
            new_comment = Commentaire.objects.create(
                commentaire=request.POST['comment'], 
                website=request.POST['website'],
                nom=request.POST['name'],
                email=request.POST['mail'],
                user=request.user,
                article=article_single
            )
            new_comment.save()
        else:
            return redirect('login')


    datas = {

        'tag':tag,
        'sociaux':sociaux,
        'presentation':presentation,
        'gallerie':gallerie,
        'recent': recent,
        'order':article_order,
        'gallerie':gallerie,
        'categorie':categorie,
        'single':article_single,

    }

    return render(request, 'pages/single-post.html', datas)


def category(request):
    
    tag = Tag.objects.filter(status=True)
    sociaux = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[:1].get()
    gallerie = Gallerie.objects.filter(status=True)[:4]
    articles = Article.objects.filter(status=True)[:2]
    article_order = Article.objects.order_by('date_add')[:4]
    categorie = CategorieArticle.objects.filter(status=True)[:2]
    recent = Article.objects.order_by('date_add')[:3]
    slide_categorie = Article.objects.filter(status=True)[2:]
    article_news = Article.objects.filter(status=True)[:4]



    datas = {

        'tag':tag,
        'sociaux':sociaux,
        'presentation':presentation,
        'gallerie':gallerie,
        'articles':articles,
        'order':article_order,
        'categorie':categorie,
        'recent': recent,
        'slide': slide_categorie,
        'new':article_news

    }




    return render(request, 'pages/fashion-category.html', datas)


def search(request):

    tag = Tag.objects.filter(status=True)
    sociaux = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[:1].get()
    gallerie = Gallerie.objects.filter(status=True)[:4]

    try:
        request.POST['search']
        assert len(request.POST['search']) >= 2
    except Exception:
        return redirect(request.META.get('HTTP_REFERER', '/'))

    q = request.POST['search']
    articles = Article.objects.filter(status=True)
    articles = articles.filter(Q(titre__icontains=q) | Q(description__icontains=q) | Q(contenu__icontains=q))


    datas = {
        'tag':tag,
        'sociaux':sociaux,
        'presentation':presentation,
        'gallerie':gallerie,
        'q': q,
        'articles': articles,
        'nombre_resultat': len(articles),
    }

    return render(request, 'pages/blog_search.html', datas)