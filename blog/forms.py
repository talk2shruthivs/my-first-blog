from django import forms
from .models import Post, Comment
from directmessages.models import Message

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('recipient', 'content')
