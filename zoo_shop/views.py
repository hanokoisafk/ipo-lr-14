import json
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'zoo_shop/main.html',{'title':'Главная страница'})

def about(request):
	return render(request, 'zoo_shop/aboutAuthor.html',{'title':'Информация об авторе'})


def aboutShop(request):
	return render(request, 'zoo_shop/aboutShop.html',{'title':'Информация об магазине'})

def load_qualifications(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    qualifications = [
        {
            "id": item["pk"],
            "name": item["fields"]["title"],
        }
        for item in data if item.get("model") == "data.specialty"
    ]

    return qualifications

qualifications = load_qualifications("dump.json")

def get_qualification_by_id(q_id):
    for qualification in qualifications:
        if qualification.get("id") == q_id:
            return qualification
    return None

def spec(request):
    return render(request, "zoo_shop/spec_list.html", {"qualifications": qualifications,
      'title': 'Список квалификаций'})

def specs(request, q_id: int):
    qualification = get_qualification_by_id(q_id)
    return render(request, "zoo_shop/spec_detail.html", {"qualification": qualification,
    'title': f"Квалификация № {q_id}" }) if qualification else HttpResponse("Квалификация не найдена")