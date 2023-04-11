from django.forms import DateInput
from django_filters import FilterSet, DateFilter, ModelChoiceFilter
from .models import Author, Post, Category, Review


class PostFilter(FilterSet):
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Author',
        empty_label='Select a author',
    )

    postCategory = ModelChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='Select a category',
    )

    creation_after = DateFilter(
        field_name='dateCreation',
        label='Date Creation',
        lookup_expr='gt',
        widget=DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }


class ReviewFilter(FilterSet):
    reviewUser = ModelChoiceFilter(
        field_name='reviewUser',
        queryset=Review.objects.all(),
        label='reviewUser',
        empty_label='Select a author',
    )

    # class Meta:
    #     model = Review
    #     fields = {
    #         'text': ['icontains'],
    #     }
