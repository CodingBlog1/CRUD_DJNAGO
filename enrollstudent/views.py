from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentModel
from django.http import HttpResponseRedirect,HttpResponse
import bcrypt
from django.template import loader

# Create your views here

def home(request):
    db = StudentModel.objects.all()

    if request.method == "POST":
       
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address')

        StudentModel.objects.create(
            name=name,
            email=email,
            address=address
        )
        return redirect('home')
    return render(request,'form.html',{'form':db})

# def update(request, id):
#   mymember = StudentModel.objects.get(id=id)
#   template = loader.get_template('index.html')
#   context = {
#     'mymember': mymember,
#   }
#   return HttpResponse(template.render(context, request))

def delete(request, id):
    if request.method == 'POST':
        pi = StudentModel.objects.get(pk=id)
        if pi:
            pi.delete()
            return redirect('home')
    return render(request, 'home.html')
# def uploaddata(request):
#     if request.method == "POST":
#         name = request.POST.get('name','')
#         email = request.POST.get('email','')
#         password = request.POST.get('password','#')

#         StudentModel.objects.create(
#             name=name,
#             email=email,
#             password=password
#         )
#         return render(request,'home.html')
#     return HttpResponseRedirect("THis is get request")