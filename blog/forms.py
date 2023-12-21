from django import forms
from .models import BlogPost
from .models import Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category',
                  'summary', 'content', 'is_draft']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
