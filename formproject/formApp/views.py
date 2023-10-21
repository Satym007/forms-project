from django.shortcuts import render
from .import forms

def form_name_views(request):
    form = forms.FormsName()
    
    if request.method == "POST":
        form = forms.FormsName(request.POST)

        if form.is_valid():

            print("Form validation successful ! see console for inforamtion")
            print("Name: "+form.cleaned_data['name'])
            print("Email:"+form.cleaned_data['email'])
            print("message:"+form.cleaned_data['text'])
    return render(request, 'home.html',{'form':form})            


# Create your views here.
