from django import forms
from .models import Post, Category, Comment

# choices = [("Coding","Coding"), ("Sports","Sports"), ("Entertainment","Entertainment"), ("History","History")]
choices = Category.objects.all().values_list("name", "name")

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "header_image", "author", "category","snippet", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your title..."}),
            "title_tag": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your title..."}),
            "author": forms.TextInput(attrs={"class": "form-control", "value": "", "id":"elder", "type":"hidden"}),
            # "author": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(choices=choice_list, attrs={"class":"form-control"}),
            "snippet": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your intro..."}),
            "body": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter your text..."}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "snippet", "body" )

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your title..."}),
            "title_tag": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your title..."}),
            "snippet": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your intro..."}),
            "body": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter your text..."}),
        }

class Comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body" )

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }