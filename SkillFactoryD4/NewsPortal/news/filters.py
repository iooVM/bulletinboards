
from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFromToRangeFilter
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post

#        fields = ('author', 'categoryType', 'dateCreation', 'postCategory', 'title', 'content','rating' )  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
#          fields = {
# #             'dateCreation':  ['gt'],
#              'author': ['icontains'],
#              'title':  ['icontains'],
#         }
        fields = {
             'title':['icontains'],


             'author__authorUser__username': ['icontains'],
             'dateCreation': ['gt'],

        }
