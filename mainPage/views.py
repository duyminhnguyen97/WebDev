from django.db.models import Q
from django.shortcuts import render
from .models import drug


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def product(request):
    drug_list = {
        'drug_info': drug.objects.order_by('drug_name')
    }
    return render(request, 'Products.html', drug_list)


def detail(request, pk):
    this_drug = drug.objects.get(id=pk)
    return render(request, 'Products-detail.html', {'this_drug': this_drug})


def search(request):
    query = request.GET.get('q')
    if query is None:
        query = ''
    results = drug.objects.filter(Q(drug_name__icontains=query)).order_by('drug_name')
    if not results:
        results = None
    return render(request, 'searchProducts.html', {'results': results, 'query': query})