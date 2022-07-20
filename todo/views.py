from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from todo.models import Importance, Status, Todo


def index_view(request):

    importances = Importance.objects.all()
    status = Status.objects.all()
    todos = Todo.objects.all()

    return render(request, "todo-templates/index_todo.html", {
            "todos": todos,
            "importances": importances
    })


def signup_view(request):
    error = ""
    if request.method == 'POST':
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("todo:index")
        else:
            error = form.errors
            print(error)
    else:
        form = UserCreationForm()
    return render(request, "../templates/sign_up.html", {
        "form": form,
        "errormsg": error
    })


def signin_view(request):
    error = ""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, user=form.get_user())
            return redirect("todo:index")
    else:
        form = AuthenticationForm()
    return render(request, "../templates/sign_up.html", {
        "form": form,
        "errormsg": error
    })


def logout_view(request):
    logout(request)
    return redirect('todo:index')


def new_todo_view(request):
    if request.method == "POST":
        user = request.user

        if user.is_superuser:
            todo_name = request.POST.get("todo")
            importance_request = request.POST.get("importance")

            importance = Importance.objects.get(importance__exact=importance_request)

            status = Status.objects.get(status__contains="Offen")

            new_todo = Todo(user=user, todo=todo_name, importance=importance, status=status)
            new_todo.save()


            messages.success(request, 'added successfully')
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/?error=not_authenticated')

    else:
        return HttpResponseRedirect('/')


def edit_todo(request, todo_pk):
   todo = get_object_or_404(Todo, pk=todo_pk)

   if request.method != 'POST':
       # form = TodoForm(instance=todo, user=request.user)
       # return HttpResponse(form.as_p())
       pass


def get_all(request):
    if(request.method == "POST"):
        print("yeeeet")
    else:
        print("noooo")
    return JsonResponse({'foo': 'bar'})
