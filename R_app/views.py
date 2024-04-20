from django.shortcuts import render, redirect, HttpResponse
from R_app.models import Author, Recipe
from R_app.forms import AuthorForm, RecipeForm
from django.contrib import messages
# Create your views here.


# Function to check if the user is logged in
def is_user_authenticated(request):
    return 'member_id' in request.session


# Decorator to enforce login requirement
def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not is_user_authenticated(request):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


def home(request):
    return render(request, 'home.html')


def register(request):
    try:
        if request.method == "POST":
            form = AuthorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(login)
        else:
            form = AuthorForm()
            return render(request, 'register.html', {'Form': form})
    except ValueError:
        HttpResponse("Value Error Guys!!")
        return redirect(home)


def login(request):
    if request.method == "POST":
        try:
            username = request.POST.get('UNAME')
            password = request.POST.get('PASSWD')
            author = Author.objects.get(USERNAME=username)
            if author.PASSWORD == password:
                request.session["member_id"] = author.id
                return redirect(display)
            else:
                return HttpResponse("Incorrect Password!!")
        except Author.DoesNotExist:
            return HttpResponse("Invalid Username!!")
        except Exception as e:
            return HttpResponse("An error occurred: {}".format(str(e)))
    else:
        return render(request, 'login.html')


@login_required
def display(request):
    recipes = Recipe.objects.all()
    return render(request, 'display.html', {"Recipes": recipes})


@login_required
def detail(request, r_id):
    try:
        recipe = Recipe.objects.get(id=r_id)
        return render(request, 'detail.html', {"Recipe": recipe})
    except Recipe.DoesNotExist:
        return HttpResponse("No such recipe")
        #return redirect('display')


@login_required
def add_recipe(request):
    if request.method == "POST":
        try:
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                recipe = form.save(commit=False)
                recipe.save()
                return redirect(display)
            else:
                return render(request, 'add_recipe.html', {"Form": form})
        except Exception as e:
            return HttpResponse(str(e))
    else:
        form = RecipeForm()
        return render(request, 'add_recipe.html', {"Form": form})


@login_required
def edit_recipe(request, r_id):
    try:
        recipe = Recipe.objects.get(id=r_id)
    except Recipe.DoesNotExist:
        return HttpResponse("Recipe not found")

    if request.method == "POST":
        try:
            form = RecipeForm(request.POST or None, request.FILES, instance=recipe)
            if form.is_valid():
                form.save()
                return redirect(display)
            else:
                return render(request, 'add_recipe.html', {"Form": form})
        except Exception as e:
            return HttpResponse(str(e))
    else:
        form = RecipeForm(instance=recipe)
        return render(request, 'add_recipe.html', {"Form": form})


@login_required
def delete_recipe(request, r_id):
    try:
        recipe = Recipe.objects.filter(id=r_id)
        recipe.delete()
        messages.info(request, 'Recipe Removed!!')
        return redirect(display)
    except Exception:
        messages.info(request, 'Error in deleting the recipe!!')
        return redirect(display)


def logout(request):
    try:
        del request.session["member_id"]
    except KeyError:
        pass
    return redirect(login)
