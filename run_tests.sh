# was: python quicktest.py modeldiff
export DJANGO_SETTINGS_MODULE=settings
PYTHONPATH=".:tests:$PYTHONPATH" python -Wd `which django-admin.py` test tests
