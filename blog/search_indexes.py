import datetime
from haystack import indexes
from blog.models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    published_date = indexes.DateTimeField(model_attr='published_date')
    created_date = indexes.DateTimeField(model_attr='created_date')
    title = indexes.CharField(model_attr='title')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(published_date__lte=datetime.datetime.now())
