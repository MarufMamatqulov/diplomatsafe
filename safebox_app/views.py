from django.shortcuts import render, get_object_or_404
from .models import Safe, Category, Model
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q  # Q object - murakkab so'rovlar uchun
from rest_framework import viewsets
from .serializers import SafeSerializer, CategorySerializer, ModelSerializer

from django.shortcuts import render, get_object_or_404
from .models import Safe, Category, Model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ReviewForm  # ReviewForm import qilingan
from django.http import HttpResponseRedirect, HttpResponseForbidden # import
from django.contrib.auth.decorators import login_required

def home(request):
    safes = Safe.objects.filter(is_available=True).order_by('-id') # Yangi qo'shilgan
    categories = Category.objects.all()

    # Paginatsiya
    paginator = Paginator(safes, 12)  # Sahifada 12 ta mahsulot
    page_number = request.GET.get('page')  # URLdan sahifa raqamini olish
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # Agar sahifa raqami butun son bo'lmasa, birinchi sahifani ko'rsatamiz
        page_obj = paginator.page(1)
    except EmptyPage:
        # Agar sahifa raqami mavjud bo'lmagan bo'lsa, oxirgi sahifani ko'rsatamiz
        page_obj = paginator.page(paginator.num_pages)
    context = {
        'page_obj': page_obj,'categories':categories
    }
    return render(request, 'safebox_app/home.html', context)

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    safes = Safe.objects.filter(category=category, is_available=True)
    categories = Category.objects.all()

    #Paginatsiya
    paginator = Paginator(safes,12)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'page_obj': page_obj,'categories':categories
    }
    return render(request, 'safebox_app/category_list.html', context)


def product_detail(request, slug):  # @login_required dekoratori olib tashlandi
    safe = get_object_or_404(Safe, slug=slug, is_available=True)
    reviews = safe.reviews.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        if request.user.is_authenticated: # user logindan otgan bolsa
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.safe = safe
                review.user = request.user
                review.save()
                return HttpResponseRedirect(request.path_info)  # Sahifani qayta yuklash
        else:
            return HttpResponseForbidden("Sharh qoldirish uchun tizimga kirishingiz kerak.")

    else:
        form = ReviewForm()

    context = {
        'safe': safe,
        'reviews': reviews,
        'form': form,
        'categories':categories
    }
    return render(request, 'safebox_app/product_detail.html', context)

from django.db.models import Q  # Q object - murakkab so'rovlar uchun

def search(request):
    query = request.GET.get('q')
    categories = Category.objects.all()
    if query:
        safes = Safe.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(model__name__icontains=query) |
            Q(model__brand__name__icontains=query),
            is_available=True
        )
         # Paginatsiya
        paginator = Paginator(safes, 12)  # Sahifada 12 ta mahsulot
        page_number = request.GET.get('page')  # URLdan sahifa raqamini olish
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            # Agar sahifa raqami butun son bo'lmasa, birinchi sahifani ko'rsatamiz
            page_obj = paginator.page(1)
        except EmptyPage:
            # Agar sahifa raqami mavjud bo'lmagan bo'lsa, oxirgi sahifani ko'rsatamiz
            page_obj = paginator.page(paginator.num_pages)

    else:
        page_obj = None
    context = {
        'query': query,
        'page_obj': page_obj, 'categories':categories
    }

    return render(request, 'safebox_app/search_results.html', context)
class SafeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Safe.objects.filter(is_available=True)
    serializer_class = SafeSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer