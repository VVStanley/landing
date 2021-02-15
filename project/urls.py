from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from home.views import HomeView, SendEmail


urlpatterns = [
    path('manatee/', admin.site.urls),
    path('sendEmail/', SendEmail.as_view()),
    path('', HomeView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
