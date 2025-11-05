from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include(('catalog.urls', 'catalog'), namespace='catalog')),
    path('blogs/', include(('blogs.urls', 'blogs'), namespace='blogs')),
    path('', RedirectView.as_view(pattern_name='blogs:post_list', permanent=False), name='home'),  # ← добавили name='home'
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
