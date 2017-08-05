# was: python quicktest.py modeldiff
export DJANGO_SETTINGS_MODULE=settings
PYTHONPATH=".:tests:$PYTHONPATH" django-admin.py test tests
