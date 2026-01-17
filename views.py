from django.shortcuts import render
from django.http import HttpResponse, Http404 ,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


app_course= {
    "python": "This is Python course",
    "java": "This is Java course",
    "swift": "This is Swift course",
    "django": "This is Django course",
}

def index(request):
    return HttpResponse("This is first Django project, first index")

def course(request, item):
    try:
        course = app_course[item]
        return HttpResponse(course)
    except:
        return HttpResponseNotFound("Item not found")
        #raise Http404("Item not found in the server")

    #return HttpResponse(app_course.get(item, "Item not found"))

def calculator(request, num1 , num2):
    return HttpResponse(f"Num1 * Num2 = {num1 * num2}")


def course_number_view(request, num1):  #yusufaliokcu.com/first_app/10 -> yusufaliokcu.com/first_app/swift
    course_list = list(app_course.keys())
    try:
        course = course_list[num1]
        page_to_go = reverse("course", args=[course])
        return HttpResponseRedirect(page_to_go)
    except:
        return HttpResponseNotFound("Course not found")