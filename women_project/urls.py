from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page
from women.views import pageNotFound, authNeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
    path('', include('authvery.urls')),
    path('captcha/', include('captcha.urls')),
]

handler404 = pageNotFound  # Обработчик Хэндлеров, дебюг в false
handler403 = authNeed

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Чтобы из статики картинки добавлялись в юрл для показа

''' для разворачивания в инете, статика чтобы загружалась. импорт двух библиотек а дальше копипаста в if  
    from django.views.static import serve as mediaserve
from django.conf.urls import url
 
if settings.DEBUG:
    import debug_toolbar
 
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
else:
    urlpatterns += [
        url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': settings.MEDIA_ROOT}),
        url(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': settings.STATIC_ROOT}),
    ]
  '''
