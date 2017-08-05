Django GroupAdmin Users
=======================

|Build Status| |Coverage Status|

Edit users in group from the Group add and edit pages.

Credit goes to this `Stack Overflow
answer <https://stackoverflow.com/a/39648244/593907>`__

Usage
-----

Add ''groupadmin\_users'' to INSTALLED\_APPS after
''django.contrib.auth''. That's it.

Alternatively, don't add ''groupadmin\_users'' to INSTALLED\_APPS, but
use and further customize this code:

::

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

Demo
----

Example image from Stack Overflow answer:

.. figure:: example.png?raw=true
   :alt: Example image

.. |Build Status| image:: https://travis-ci.org/Microdisseny/django-groupadmin-users.svg?branch=master
   :target: https://travis-ci.org/Microdisseny/django-groupadmin-users
.. |Coverage Status| image:: https://coveralls.io/repos/github/Microdisseny/django-groupadmin-users/badge.svg?branch=master
   :target: https://coveralls.io/github/Microdisseny/django-groupadmin-users?branch=master
