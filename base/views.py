from django.shortcuts import render, redirect
from .serializers import UserSerializer, PlatformSerializer


def user_form_view(request):
    invalidMassage = ""
    
    if request.method == 'POST':
        form = request.POST

        serializer = UserSerializer(data={k: v for (k, v) in form.items()})
        if serializer.is_valid():
            serializer.save()
            return redirect("step2", owner=serializer.data['id'])
        else: 
            err = serializer.errors
            invalidMassage = err[next(iter(err))][0]
        
    return render(request, "base/step1.html", {"invalid_input_message": invalidMassage})


def platform_form_view(request, owner):
    invalidMassage = ""

    if request.method == 'POST':
        form = request.POST
        form_dict = {k: v for (k, v) in form.items()}
        form_dict['owner'] = owner

        serializer = PlatformSerializer(data=form_dict)
        if serializer.is_valid():
            serializer.save()
            return redirect("complete")
        else: 
            err = serializer.errors
            invalidMassage = err[next(iter(err))][0]

    return render(request, "base/step2.html", {"invalid_input_message": invalidMassage})


def complete_view(request):
    return render(request, "base/complete.html")

