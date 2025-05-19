from django.urls import path
from .views import * 

urlpatterns = [
    path('', home, name = 'home'),
	path('about/', about, name ='about'),
	path('aboutShop/', aboutShop, name ='aboutShop'),
	path("spec/", spec, name="spec_list"),
    path("spec/<int:q_id>", specs, name="spec_detail"),
]