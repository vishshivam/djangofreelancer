from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('user.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # logout path
    path('logout/', auth_views.LogoutView.as_view(template_name="user/logout.html"), name="logout"),
    
    # reset and change password views
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='user/change_password.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordResetCompleteView.as_view(template_name='user/change_password_done.html'), name='password_change_done'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='user/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
