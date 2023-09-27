from django.shortcuts import render
from ourapp.models import Product
from math import ceil
from django.core.paginator import Paginator

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
    #new trick to display category
    categories = Product.objects.values_list('product_category', flat=True).distinct() #distict() func will check no duplicate and give unique , value_list give tuples and flat=True argument means that the result will be a flat list of values, rather than a list of dictionaries or objects.
    #new trick to display all products in categorywise
    category_product_data = []
    for category in categories:
        products = Product.objects.filter(product_category=category)
        category_product_data.append({'category': category, 'products': products})
    #searching work
    if request.method == "POST":
        st=request.POST['searching']
        if st is not None:
            search=Product.objects.filter(product_name__icontains=st)
    data={
        'search':search,
        'categories':categories,
        'category_product_data': category_product_data
    }
    return render(request,"search.html",data)

def pagination(request):
    alldata=Product.objects.all().order_by('id')
    paginator=Paginator(alldata,2)    #shwoing only 2 out of all data
    page_num=request.GET.get('page')  #getting from url page value and then show accordingly
    limited_data=paginator.get_page(page_num) #it shows currentpage of totalpages
    total_pages=limited_data.paginator.num_pages  #return the number of pages
    # page_list=[n+1 for n in range(total_pages)] # it print the list of page numbers from 1 to total_pages (used for numbers but it will not increment and decrement the numbers)
    # Calculate the range of page numbers to display
    current_page = limited_data.number   #this line store the current page number...similar to page_num
    if total_pages <= 3:
        page_range = range(1, total_pages + 1)
    elif current_page <= 2:
        page_range = range(1, 4)
    elif current_page >= total_pages - 1:  #only execute if second last and last page
        page_range = range(total_pages - 2, total_pages + 1)
    else:
        page_range = range(current_page - 1, current_page + 2)
    data={
        # 'alldata':alldata,
        'total_pages':total_pages,
        # 'page_list':page_list,
        'limited_data':limited_data,
        'page_range': page_range
    }
    return render(request,"pagination.html",data)