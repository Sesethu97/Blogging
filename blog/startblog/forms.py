from multiprocessing.sharedctypes import Value
from secrets import choice
from django import forms
from .models import Post, Category


# choices_list =[("uncategorized", "uncategorized"),("sports", "sports"),("food&drinks", "food&drinks"),("entertainment", "entertainment"),("fashion", "fashion"),("photography&arts", "photography&arts"),("travels", "travels"),]
choices = Category.objects.all().values_list("name", "name")

choices_list = []

for item in choices:
    choices_list.append(item)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "category",
            "caption",
            "header_image",
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(
                choices=choices_list, attrs={"class": "form-control"}
            ),
            "caption": forms.Textarea(attrs={"class": "form-control"}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "caption",
        )

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "caption": forms.Textarea(attrs={"class": "form-control"}),
        }
