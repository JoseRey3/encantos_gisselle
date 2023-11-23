from django.urls import path
from .views import home, about, product_detail, categoria_page

urlpatterns = [
    path('', home, name='home'),
    path('product_detail/<int:product_id>', product_detail, name='product_detail'),
    path('categoria_page/<int:categoria_id>', categoria_page, name='categoria_page'),
    path ('about/', about, name='about'),
]