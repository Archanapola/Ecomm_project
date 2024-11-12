from django.urls import path, include
from accounts import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view
from .forms import LoginForm,PasswordResetForm,PasswordChangeForm,MySetPasswordForm
from django.contrib import admin
urlpatterns = [
    path('', views.home, name = 'homeUrl'),
    path('category/<slug:val>', views.CategoryView.as_view(), name="category"),
    path('category_title/<str:val>/', views.CategoryTitleView.as_view(), name="CategoryTitle"),
    path('product_details/<int:pk>', views.ProductDetailsView.as_view(), name="Product_Details"),

     path("search/", views.search, name = "search"),

    path('add_to_cart/<int:pk>/', views.add_to_cart, name="add_to_cart"),
    path('cart/', views.show_cart, name='showcart'),
     path('wishlist/', views.show_wishlist, name='show_wishlist'),


     path('checkout/', views.checkout.as_view(), name='checkout'),
     path('paymentdone/',views.payment_done , name="paymentdone"),
     path("orders/", views.orders, name = "orders"),

     path('pluscart/', views.plus_cart),
     path('minuscart/', views.minus_cart),
     path('removecart/', views.remove_cart),
    path('pluswishlist/', views.plus_wishlist, name="plus_wishlist"),
    path('minuswishlist/', views.minus_wishlist, name="minus_wishlist"),



    path('buy_now/<int:pk>', views.BuyNowView.as_view(), name="buy_now"),
    path('AboutUs>', views.AboutUsView.as_view(), name="AboutUs"),
    path('ContactUs>', views.ContactUsView.as_view(), name="ContactUs"),
    path('profile/', views.ProfileView.as_view(), name = "profile"),
    path('address/', views.AddressView, name="address"),
    path('update-address/<int:pk>', views.UpdatAddressView.as_view(), name="UpdateAddress"),


    path('register/', views.RegistrationView.as_view(), name='register'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form =LoginForm), name="login"),
    
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset_form.html', form_class =PasswordResetForm), 
         name="password_reset"),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/password_change.html', form_class =PasswordChangeForm,
                                                                   success_url='/passwordchange-done'), name="passwordchange"),
    path('passwordchange-done/', auth_view.PasswordChangeDoneView.as_view(template_name='app/password_change_done.html',
                                                                       ),name="passwordchange-done"), 
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    path('passwordreset/', 
         auth_view.PasswordResetView.as_view(template_name='app/password_reset_form.html', 
          form_class = PasswordResetForm), name='passwordreset'),
         
    path('password-reset/done/', 
         auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), 
         name='password_reset_done'),
         
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', 
         form_class = MySetPasswordForm), name='password_reset_confirm'),
         
    path('password-reset-complete/', 
         auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), 
         name='password_reset_complete'),




]
"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"""

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Archana Fashions"
admin.site.site_header = "Archana Fashions"
admin.site.site_header = "Welcome to Archana Fashions"