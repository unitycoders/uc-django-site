from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.utils.translation import ugettext, ugettext_lazy as _
from models import Member,Invite

# based on https://github.com/django/django/blob/master/django/contrib/auth/admin.py
class MemberManager(UserAdmin):
	 fieldsets = (
		(None, {
			'fields': ('username', 'password')
		}),
		(_('Personal info'), {
				'fields': (('first_name', 'last_name'), 'email', 'bio')
		}),
		(_('Permissions'), {
				'classes': ('collapse',),
				'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
		}),
		(_('Important dates'), {
				'classes': ('collapse',),
				'fields': ('last_login', 'date_joined')
		}),
	)

admin.site.register(Member, MemberManager)

class InviteManager(admin.ModelAdmin):
	search_fields = ['name', 'email']
	list_display = ['name', 'email', 'request_date']
	list_filter = ['requester', 'request_date']
admin.site.register(Invite, InviteManager)
