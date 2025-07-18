

#qs - query set,
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from tweets.models import Tweet

#basically list of posts ng mga input ng users para lumitaw sa admin site naten ung linalagay nila





def list_view(request):
    qs = Tweet.objects.all()
    for foo in qs:
        print(foo)      #prints every object undery query set
    print(qs)           #prints query set
    context ={
        'tae':qs,
        'message':'Tweet successfully created',
    }
    return render(request, 'tweets/list.hmtl',context)


#kumbaga detailed view, sa shopee, pag pinindot mo ung isang product, lahat ng related details sakanya
def detailview(request, pk=1):
    obj = Tweet.objects.get(pk=pk)
    return render, 'tweets/detail.html',({'pk' : pk})

# class TweetListView(ListView):
#     queryset = Tweet.objects.all()
#     template_name = 'tweets/application.html'
#
# class TweetDetailView(DetailView):
#     queryset = Tweet.objects.all()
#     template_name = 'tweets/detail.html'
#
#     def get_object(self, *args, **kwargs):
#         pk = self,kwargs.get('pk')
#         #keyword argument, basta kukunin ung id ng pk
#         return Tweet.objects.get(pk=pk)
