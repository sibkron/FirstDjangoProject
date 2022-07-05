from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['some', 'hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'football'
        }
    }

    return render(request, 'mainApp/homePage.html', data)


def about(request):
    return render(request, 'mainApp/about.html')
