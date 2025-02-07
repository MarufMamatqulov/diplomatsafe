from django.urls import path, include
from . import views  # Nuqtali import!
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'safes', views.SafeViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'models', views.ModelViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.category_list, name='category_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),  # Qidiruv uchun
    path('api/', include(router.urls)),  # API uchun
]
# Bu yerda static(...) kerak emas!