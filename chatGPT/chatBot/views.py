from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == "POST":
        question = request.POST.get('question', '')  # Safely get 'question', default to empty string if not present
        return render(request, 'home.html', {"question": question})

    return render(request, 'home.html', {})



