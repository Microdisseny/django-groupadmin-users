from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User, Group
from django.test import TestCase

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
        # GET the import form
        response = self.client.get('/admin/auth/group/1/change/')
        self.assertEqual(response.status_code, 200)

        data = {
            'name': 'admins',
            'permissions': ('1', '2'),
            'users': ('1',),
        }
        response = self.client.post('/admin/auth/group/1/change/', data,
                                    follow=True)
        self.assertEqual(response.status_code, 200)

        group = Group.objects.all().last()
        self.assertTrue(group.name == 'admins')
        self.assertTrue(group.permissions.all().count() == 2)
        self.assertTrue(group.user_set.first() == self.admin)
