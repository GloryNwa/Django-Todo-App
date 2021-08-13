from django.shortcuts import render,redirect 
from django.http import HttpResponse

from .models import Todo
 

# Create your views here.

def index(request):
      todos = Todo.objects.all().order_by("-created_at")[:10]
      context={
        'todos':todos
      }
      return render(request, 'add.html', context)
    
def details(request, id):
    todo = Todo.objects.get(id=id)
    context ={
     'todo':todo
   }
    return render(request, 'details.html', context)
  
  
def add(request):
    if(request.method == 'POST'):
       title = request.POST['title']
       text =request.POST['text']
       
       todo = Todo(title=title, text=text)
       todo.save()
       return redirect('/todos')
       
    else: 
        return render(request, 'add.html')
      
      
      
def delete(request, id):
         Todo.objects.get(id=id).delete()
         return redirect('/todos')


  # return HttpResponse('Hello World') template_name='helloworld.html'
