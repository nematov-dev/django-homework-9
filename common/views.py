from django.shortcuts import render



def recipies_page_views(request):
    return render(request,'recipies/recipe_with_sidebar.html')

def blog_page_views(request):
    return render(request,'blogs/blog_list.html')

def category_page_views(request):
    return render(request,'recipies/category.html')

def submit_page_views(request):
    return render(request,'recipies/submit_recipe.html')

def login_page_views(request):
    return render(request,'auth/login.html')