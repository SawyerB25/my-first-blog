from django import forms

from .models import Post

"""
#from django.db.models import Q
#from simple_search import BaseSearchForm
#from blog.models import MyModel, MyCategory
"""


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


"""class MyModelSearchForm(BaseSearchForm):
    class Meta:
        base_qs = MyModel.objects

        search_fields = ('^author', 'title', ' @text')

        # assumes a fulltext index has been defined on the fields
        # 'name,description,specifications,id'
        fulltext_indexes = (
            ('name', 2),  # name matches are weighted higher
            ('name,description,specifications,id', 1),
        )


    category = forms.ModelChoiceField(
        queryset=MyCategory.objects.all(),
        required=False
    )


    start_date = forms.DateField(
        required=False,
        input_formats=('%Y-%m-%d',),
    )

    def prepare_start_date(self):
        if self.cleaned_data['start_date']:
            return Q(creation_date__gte=self.cleaned_data['start_date'])
        else:
            return ""
"""
