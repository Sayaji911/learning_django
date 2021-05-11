from django.shortcuts import render
import json

booksData = open(r'C:\Users\SayajiChavan\Desktop\LearningDjango\bookstore-project\books.json').read()

data = json.loads(booksData)


def index(request):
    context = {'books': data}
    return render(request, "books/index.html", context)
