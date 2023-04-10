from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Review


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=10)

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'postCategory',
            'upload',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")
        if title == text:
            raise ValidationError(
                "The description should not be identical to the text."
            )

        return cleaned_data


class ReviewPostForm(forms.ModelForm):
    text = forms.CharField(min_length=10)

    class Meta:
        model = Review
        fields = [
            'text',
            'reviewUser',
            'reviewPost',
        ]
