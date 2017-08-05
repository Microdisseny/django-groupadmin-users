Django GroupAdmin Users
=======================

[![Build Status](https://travis-ci.org/microdisseny/django-groupadmin-users.svg?branch=master)](https://travis-ci.org/microdisseny/django-groupadmin-users)
[![Coverage Status](https://coveralls.io/repos/github/microdisseny/django-groupadmin-users/badge.svg?branch=master)](https://coveralls.io/github/microdisseny/django-groupadmin-users?branch=master)

Edit users in group from the Group add and edit pages.

Credit goes to this [Stack Overflow answer](https://stackoverflow.com/a/39648244/593907)

Usage
-----

Add ''groupadmin_users'' to INSTALLED_APPS after ''django.contrib.auth''. That's it.

Alternatively, don't add ''groupadmin_users'' to INSTALLED_APPS, but use and further customize this code:

```
from django.contrib import admin
from django.contrib.auth.models import Group

from groupadmin_users.forms import GroupAdminForm


# Unregister the original Group admin.
admin.site.unregister(Group)


# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)
````

Demo
----

Example image from Stack Overflow answer:

![Example image](example.png?raw=true)
