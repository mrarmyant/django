from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to display list of blogs"
    return HttpResponse(response)

def new(request):
    response = "Placeholder for New Blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, pk):
    response = "Placeholder to display blog " + pk
    print ("========================================")
    print (pk)
    return HttpResponse(response)

def edit(request, pk):
    response = "Placeholder to edit blog #" + pk
    return HttpResponse(response)

def destroy(request):
    return redirect('/')