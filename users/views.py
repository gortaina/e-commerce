from django.shortcuts import render

# Create your views here.

def is_ajax(request):
    if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        return True

    if request.content_type == "application/json":
        return True
    return False