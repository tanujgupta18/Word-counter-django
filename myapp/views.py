from django.shortcuts import render

# Create your views here.

def index(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request,'word-counter.html' , {'amount': amount_of_words})
