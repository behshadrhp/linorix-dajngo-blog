from .models import Essay, Tag
from django.core.paginator import Paginator
from django.db.models import Q


def SearchEngin(request):

    searchbar = ''

    if request.GET.get('search'):
        searchbar = request.GET.get('search')
        
        tag = Tag.objects.filter(label__iexact=searchbar)
        essay = Essay.objects.distinct().filter(
        Q(title__icontains=searchbar)|
        Q(description__icontains=searchbar)|
        Q(tag__in=tag)
        )

    else:
        essay = Essay.objects.all()

    # pagination 
    paginator = Paginator(essay, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj, searchbar