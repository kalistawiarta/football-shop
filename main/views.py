from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        "app_title" : "Football Shop",
        "student_name" : "Kalista Wiarta",
        "student_class" : "PBP F"
    }
    return render(request, "home.html", context)                                                                                