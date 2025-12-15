# Code from https://stackoverflow.com/a/39648244/593907
# modified according to https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#the-save-method  # noqa
from django import VERSION, forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class AdminFilteredSelectMultiple(FilteredSelectMultiple):
    """
    FilteredSelectMultiple that renders with proper wrapper for admin layout.
    This ensures the label positioning is correct across Django 1.8 through 5.x.
    """

    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget with proper wrapper for consistent layout across Django versions."""
        # Django 1.11+ added the renderer parameter
        if VERSION >= (1, 11):
            output = super().render(name, value, attrs, renderer)
        else:
            output = super().render(name, value, attrs)

        return format_html(
            '<div class="related-widget-wrapper" data-model-ref="user">\n{}\n</div>',
            output,
        )


# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field.
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        # Use the pretty 'filter_horizontal widget'.
        widget=AdminFilteredSelectMultiple(_('users'), False),
        label=_('Users'),
        help_text=_('Hold down "Control", or "Command" on a Mac, to select more than one.'),
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        # Deprecated in Django 1.10: Direct assignment to a reverse foreign key
        #                            or many-to-many relation
        if VERSION < (1, 9):
            self.instance.user_set = self.cleaned_data['users']
        else:
            self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance
