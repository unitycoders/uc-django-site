from django import template
import hashlib

register = template.Library()

def gravatar_hash(value):
    """Returns the gravatar url for a given email address"""
    return hashlib.md5(value.lower()).hexdigest()
register.filter('gravatar_hash', gravatar_hash)

def gravatar(value):
	"""Returns the gravatar url for a given email"""
	hashval = gravatar_hash(value)
	return "https://www.gravatar.com/avatar/%s" % (hashval,)
register.filter('gravatar', gravatar)
