from django import forms
from .models import CustomUser, Article
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'phone', 'password1', 'password2')
        

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    
    class Meta:
        model = Article
        fields = ('title', 'content', 'author')
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 20})
        }