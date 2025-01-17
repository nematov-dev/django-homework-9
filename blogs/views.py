from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from blogs.forms import CommentModelForm,BlogContactForm
from blogs.models import BlogModel, BlogCategoryModel, BlogTagModel, BlogCommentModel


def blog_list_view(request):
    if request.method == "POST":
        form = BlogContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:list')


    else:
        blogs = BlogModel.objects.all()
        categories = request.GET.get('categories')
        tags = request.GET.get('tags')

        if categories:
            blogs = blogs.filter(categories=categories)
        if tags:
            blogs = blogs.filter(tags=tags)

        latest_blogs = BlogModel.objects.all().order_by('-create_at')[:4]
        categories = BlogCategoryModel.objects.all()
        tags = BlogTagModel.objects.all()
        context = {
            "blogs": blogs,
            "latest_blogs": latest_blogs,
            "categories": categories,
            "tags": tags
        }
        return render(request, 'blogs/blog_list.html', context)


def blog_detail_view(request, pk):
    try:
        blog = BlogModel.objects.get(id=pk)
        blogs = BlogModel.objects.all()
        categories_filter = request.GET.get('categories')
        tags_filter = request.GET.get('tags')

        if categories_filter:
            blogs = blogs.filter(categories=categories_filter)
        if tags_filter:
            blogs = blogs.filter(tags=tags_filter)

        # Ushbu ma'lumotlarni har doim aniqlash
        latest_blogs = BlogModel.objects.all().order_by('-create_at')[:4]
        categories = BlogCategoryModel.objects.all()
        tags = BlogTagModel.objects.all()

    except BlogModel.DoesNotExist:
        return render(request, 'pages/404.html')

    context = {
        "blog": blog,
        "latest_blogs": latest_blogs,
        "categories": categories,
        "tags": tags
    }
    return render(request, 'blogs/blog_detail.html', context)



@login_required(login_url="users/login/")
def blog_comment_view(request, pk):
    try:
        blog = BlogModel.objects.get(id=pk)
    except BlogModel.DoesNotExist:
        return render(request, 'pages/404.html')
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            BlogCommentModel.objects.create(
                comment=request.POST['comment'],
                user=request.user,
                blog=blog
            )
            redirect_url = reverse('blogs:detail', kwargs={'pk': pk})
            return redirect(f"{redirect_url}#comments")
        else:
            return redirect(f'blogs/{pk}#comments')