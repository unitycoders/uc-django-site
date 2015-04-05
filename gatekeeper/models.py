from django.db import models

from django.contrib.auth.models import User

import string
import random
import hashlib

class Member(User):
    class Meta:
        proxy = True

    @models.permalink
    def get_absolute_url(self):
        return ('profile-detail', (), {
            'slug': self.username,
        })

    def _get_gravatar(self):
        return hashlib.md5(self.email.lower()).hexdigest()
    gravatar = property(_get_gravatar)

# Create your models here.
class Invite(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	request_date = models.DateField(auto_now_add=True)
	requester = models.ForeignKey('auth.user')
	key = models.CharField(max_length=25, blank=True)

	def generate_key(self):
		random_key = "-".join([self.__random() for _ in range(3)])
		return "%s"%(random_key,)

	def __random(self, size=5):
		return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))

	def save(self, force_insert=False, force_update=False):
		if not self.key:
    			self.key = self.generate_key()
    		super(Invite, self).save(force_insert, force_update)

	def __unicode__(self):
		return "%s" % (self.name,)
