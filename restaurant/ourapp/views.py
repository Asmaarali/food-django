from django.shortcuts import render
from ourapp.models import Product
from math import ceil

# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('product_category','id')
    # print(catprods)
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(product_category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds}
    return render(request,"index.html",params)

def productpage(request,slug):
    productdetail=Product.objects.get(product_slug=slug)
    # print(productpage)
    data={
        'productdetail':productdetail
    }
    return render(request,"productpage.html",data)

def searching(request):
    search=Product.objects.all()
    if request.method == "POST":
        st=request.POST['searching']
        if st is not None:
            search=Product.objects.filter(product_name__icontains=st)
    print(search)
    data={
        'search':search
    }
    return render(request,"search.html",data)