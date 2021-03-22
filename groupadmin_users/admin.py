from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin as GroupAdminDefault

from groupadmin_users.forms import GroupAdminForm

# Unregister the original Group admin.
admin.site.unregister(Group)


# Create a new Group admin.
class GroupAdmin(GroupAdminDefault):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']


# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)
