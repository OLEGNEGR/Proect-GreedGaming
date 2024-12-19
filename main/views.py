from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request) -> HttpResponse:

    context = {
        'title': 'GreedGaming - Главная',
        'content': "Магазин игр GreedGaming",
    }

    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
     context: dict[str, str] = {
        'title': 'GreedGaming - Про нас',
        'content': "Про нас",
        'text_on_page': "Текст про то почему мой магазин лучший."
    }
     return render(request, 'main/about.html', context)
    

# Create your views here.
