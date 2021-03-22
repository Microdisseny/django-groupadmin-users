from contextlib import contextmanager

from django import VERSION
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import Group, User
from django.db import DEFAULT_DB_ALIAS, connections
from django.test import TestCase
from django.test.utils import CaptureQueriesContext

from groupadmin_users.admin import GroupAdmin


class MockRequest:
    pass


request = MockRequest()


class ModelAdminTests(TestCase):

    def setUp(self):
        self.group = Group.objects.create(
            name='admins',
        )

        self.site = AdminSite()

        user = User.objects.create_user('admin', 'admin@example.com',
                                        'password')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.admin = user

        self.client.login(username='admin', password='password')

    @contextmanager
    def withAssertNumQueriesLessThan(self, value, using=DEFAULT_DB_ALIAS):
        with CaptureQueriesContext(connections[using]) as context:
            yield  # your test will be run here
        executed = len(context.captured_queries)
        msg = "%d queries executed, %d expected\nCaptured queries were:\n%s" % (
            executed, value,
            '\n'.join(
                '%d. %s' % (i, query['sql']) for i, query in enumerate(context.captured_queries, start=1)
            )
        )
        self.assertLess(len(context.captured_queries), value, msg=msg)

    def test_default_fields(self):
        ga = GroupAdmin(Group, self.site)

        self.assertEqual(list(ga.get_form(request).base_fields),
                         ['name', 'permissions', 'users'])
        self.assertEqual(list(ga.get_fields(request)),
                         ['name', 'permissions', 'users'])
        self.assertEqual(list(ga.get_fields(request, self.group)),
                         ['name', 'permissions', 'users'])
        # self.assertIsNone(ga.get_exclude(request, self.band))

    def test_form_add(self):
        # GET the import form
        response = self.client.get('/admin/auth/group/add/')
        self.assertEqual(response.status_code, 200)

        data = {
            'name': 'editors',
            'permissions': ('1', '2', '3'),
            'users': ('1',),
        }
        response = self.client.post('/admin/auth/group/add/', data,
                                    follow=True)
        self.assertEqual(response.status_code, 200)

        group = Group.objects.all().last()
        self.assertTrue(group.name == 'editors')
        self.assertTrue(group.permissions.all().count() == 3)
        self.assertTrue(group.user_set.first() == self.admin)

    def test_form_edit(self):
        if VERSION <= (1, 9):
            url = '/admin/auth/group/1/'
        else:
            url = '/admin/auth/group/1/change/'

        # GET the import form
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        data = {
            'name': 'admins',
            'permissions': ('1', '2'),
            'users': ('1',),
        }
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)

        group = Group.objects.all().last()
        self.assertTrue(group.name == 'admins')
        self.assertTrue(group.permissions.all().count() == 2)
        self.assertTrue(group.user_set.first() == self.admin)

    def test_group_permission_performance(self):
        with self.withAssertNumQueriesLessThan(12):  # instead of 259!
            response = self.client.get('/admin/auth/group/%s/' % self.group.pk, follow=True)
            self.assertEqual(response.status_code, 200)
