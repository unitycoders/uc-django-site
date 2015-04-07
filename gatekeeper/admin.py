from django.contrib import admin

from models import Member,Invite

class MemberManager(admin.ModelAdmin):
	search_fields = ['username', 'first_name', 'last_name']
	list_display = ['username', 'email'] 
	pass
admin.site.register(Member, MemberManager)

class InviteManager(admin.ModelAdmin):
	search_fields = ['name', 'email']
	list_display = ['name', 'email', 'request_date']
	list_filter = ['requester', 'request_date']
admin.site.register(Invite, InviteManager)
