from django.shortcuts import render
from camping.models import Camp
from django.db.models import Q

def searchResult(request):
    camp=None
    query=None
    if "q" in request.GET:
        query = request.GET.get("q")
        camps = Camp.objects.all().filter(Q(name__icontains=query)| Q(location__icontains=query) | Q(description__icontains=query)).distinct()
    return render(request, 'search.html',{"query": query,"camps":camps})


