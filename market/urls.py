from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.index ,name="index"),
    path('marketplace/',views.market ,name="market"),
    path('item/<int:pk>/',views.details ,name="item"),
    path('cart/<int:pk>',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('login/', LoginView.as_view(template_name='market/login.html'), name="login"),
    path('logout/',LogoutView.as_view(template_name='market/logout.html'),name="logout"),
    path('accounts/profile/',views.profile,name="profile"),
    path('signup/',views.register,name="register"),
    path('checkout/delete/<int:pk>',views.delete_cart,name="delete_cart"),
    path('search/',views.search,name="search"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)