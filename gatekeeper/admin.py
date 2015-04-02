from django.contrib import admin

from models import Invite

# Register your models here.
class InviteManager(admin.ModelAdmin):
	search_fields = ['name', 'email']
	list_display = ['name', 'email', 'request_date']
	list_filter = ['requester', 'request_date']
admin.site.register(Invite, InviteManager)
