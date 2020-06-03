from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from imageapi.models import Media, Like, UserProfile, Follow
from imageapi.serializers import MediaSerializer
from django.db.models import Count
from django.contrib.auth.models import User

# Create your views here.

def MediaViewSet(request):
    queryset = Media.objects.all().annotate(num_like=Count('liked')).order_by('-num_like')
    user = request.user
    context= {
    'queryset': queryset,
    'user': user,
    }
    return render(request, 'posts/main.html', context)

def GalleryViewSet(request):
    user = request.user
    queryset = Media.objects.filter(author = user).annotate(num_like=Count('liked')).order_by('-num_like')
    context= {
    'queryset': queryset,
    'user': user,
    }
    return render(request, 'posts/gallery.html', context)


def UserViewSet(request):
    user = request.user
    userqueryset =User.objects.all()

    context= {
    'userqueryset': userqueryset,
    'user': user,
    }
    return render(request, 'posts/searchResults.html', context)

def like_post(request):
    user=request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Media.objects.get(id=post_id)

        if user in post_obj.liked.all():
           post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like,created = Like.objects.get_or_create(user=user, post_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value='Like'
            like.save()
    return redirect('posts:post-list')



def follow_user(request):
    user=request.user
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_obj = UserProfile.objects.get(user_id=user_id)

        if user in user_obj.followedby.all():
            user_obj.followedby.remove(user)
        else:
            user_obj.followedby.add(user)
        follow,created = Follow.objects.get_or_create(user=user, user_id=user_id)
        if not created:
            if follow.value == 'follow':
                follow.value = 'unfollow'
            else:
                follow.value='follow'
            follow.save()
    return redirect('posts:follow-user')

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_name = self.request.GET.get('search', '')
    context['all_search_results'] = User.objects.filter(username__icontains=user_name )
    return context

