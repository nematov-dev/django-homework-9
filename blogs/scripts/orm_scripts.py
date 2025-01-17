from blogs.models import BlogModel,BlogLikeModel

def run():
    blogs = BlogModel(title = 'Assalomu alaykum')
    blogs.save()

    

    