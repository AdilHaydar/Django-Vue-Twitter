from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def upload_to(instance, filename):
    username = instance.user.username
    return '%s/%s/%s' %('TweetFiles', username, filename)

class CommonField(models.Model):
    content = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        abstract = True
        ordering = ['-created_date']

class Like(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'likes')
	post = models.ForeignKey("Tweet",on_delete=models.CASCADE)
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username +" Liked "+ str(self.post.id)

class Tweet(CommonField):
    user = models.ForeignKey(User, related_name='tweets', on_delete=models.CASCADE, null=False, blank=False)
    likes = models.ManyToManyField(User,related_name='tweet_user', blank=True, through=Like)
    file = models.FileField(upload_to=upload_to, null=True, blank=True)

    def __str__(self):
        return self.content

class Comment(CommonField):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=False, blank=False)

# class File(models.Model):
# 	post = models.ForeignKey(to=Tweet, on_delete=models.CASCADE,related_name='files')
# 	file = models.FileField(upload_to=upload_to, null=True, blank=True)

