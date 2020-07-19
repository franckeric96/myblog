from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from website.models import Presentation, SocialAccount, Gallerie
from blog.models import Tag, Article, CategorieArticle


# Create your views here.
def contact(request):
    
    
    tag = Tag.objects.filter(status=True)
    sociaux = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[:1].get()
    gallerie = Gallerie.objects.filter(status=True)[:4]
    recent = Article.objects.order_by('date_add')[:3]



    form = ContactForm(request.POST or None)
    if form.is_valid(): 
        form.save()
        form = ContactForm()
    
    datas ={

        'tag':tag,
        'sociaux':sociaux,
        'presentation':presentation,
        'gallerie':gallerie,
        'recent': recent,
        'form': form
       
        }


    return render(request, 'pages/contact.html', datas)