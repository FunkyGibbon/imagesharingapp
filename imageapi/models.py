from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Media(models.Model):
    caption = models.CharField(max_length=100)
    liked = models.ManyToManyField(User,default=None, blank=True)
    image = models.ImageField(upload_to='static/images', default='https://www.fillmurray.com/640/360')
    dateuploaded= models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return str(self.caption)
    
    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES=(
    ('like','like'),
    ('unlike','unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Media, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followedby = models.ManyToManyField(User,default=None, blank=True, related_name='followedby')
    description = models.CharField(max_length=100)

    @property
    def num_followers(self):
        return self.followedby.all().count()

FOLLOW_CHOICES=(
    ('follow','follow'),
    ('unfollow','unfollow'),
)

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followee')
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


