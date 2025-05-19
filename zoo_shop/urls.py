from django.urls import path
from .views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name = 'home'),
	path('about/', about, name ='about'),
	path('aboutShop/', aboutShop, name ='aboutShop'),
	path("spec/", spec, name="spec_list"),
    path("spec/<int:q_id>", specs, name="spec_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)