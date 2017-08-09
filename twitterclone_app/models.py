from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import hashlib

# Create your models here.

class Tweet(models.Model):
    content = models.CharField(max_length=160)
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def gravatar_url(self):
        # return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()
        return "http://db3.memegenerator.net/cache/images/folder282/60x60/1986282.jpg"
 
 
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])