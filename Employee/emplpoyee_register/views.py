from django.shortcuts import render,redirect 
from.forms import Employee_form
from .models import create
# Create your views here.
def form_view(request,id=-1):
    if request.method=="POST":
        if id==-1 :
            form=Employee_form(request.POST or None)
        else :
            obj=create.objects.get(pk=id)
            form=Employee_form(request.POST ,instance=obj)
        if form.is_valid:
            form.save()
            form=Employee_form()
            return   redirect("/list")
        else :
            return render(request,'form.html',{"form":form})
    else:
        if id==-1:
            form=Employee_form()
        else :
            obj=create.objects.get(pk=id)
            form=Employee_form(instance=obj)
        return render(request,'form.html',{"form":form})
        
       
def list_view(request):
    obj=create.objects.all()
    return  render(request,'list.html',{"object":obj})

def delete_view(requset,id):
     obj=create.objects.get(pk=id)
     obj.delete()
     return redirect("/list")


        

    

