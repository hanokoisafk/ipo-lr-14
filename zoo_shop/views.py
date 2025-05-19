from django.shortcuts import render

def home(request):
	return render(request, 'zoo_shop/main.html',{'title':'Главная страница'})

def about(request):
	return render(request, 'zoo_shop/aboutAuthor.html',{'title':'Информация об авторе'})


def aboutShop(request):
	return render(request, 'zoo_shop/aboutShop.html',{'title':'Информация об магазине'})
