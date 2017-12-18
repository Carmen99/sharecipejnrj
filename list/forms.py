from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('image', 'prepare_time', 'portions', 'title', 'preview_text', 'ingredients', 'preperation')
