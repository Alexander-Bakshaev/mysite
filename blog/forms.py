from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.PasswordInput(attrs={'placeholder': 'Email'}),
            'body': forms.Textarea(attrs={'placeholder': 'Текст комментария'}),
        }


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск')