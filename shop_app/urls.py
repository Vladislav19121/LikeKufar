from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('activation/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('registration/', views.registration, name='registration'),
    path('user_page/<int:id>', views.user_page, name='user_page'),
    path('category/<int:id>/', views.open_category, name='category_products'),
    path('add_product/<int:id>/', views.add_product, name='add_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('cart/', views.cart, name='cart'),
    path('add_product_in_cart/<int:id>', views.add_product_in_cart, name='add_product_in_cart'),
    path('remove_from_cart/<int:cart_product_id>', views.remove_form_cart, name='remove_from_cart'),
    path('search/', views.search_results, name='search_results'),
    path('add_category', views.add_category, name='add_category'),
    path('delete_category/<int:id>/', views.delete_category, name='delete_category'),
    path('add-discount/<int:id>/', views.add_discount, name='add_discount'),
    path('delete-discount/<int:id>/', views.delete_discount, name='delete_discount')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)