from django import forms

from blogs.models import BlogCommentModel,BlogContactModel


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = BlogCommentModel
        fields = ['comment']

class BlogContactForm(forms.ModelForm):
    class Meta:
        model = BlogContactModel
        fields = ['email']