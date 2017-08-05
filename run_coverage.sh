# was: coverage run --source='.' quicktest.py modeldiff
#      coverage report -m
export DJANGO_SETTINGS_MODULE=settings
PYTHONPATH=".:tests:$PYTHONPATH"
coverage run \
    --omit='quicktest.py,setup.py' \
    --source=. tests/manage.py test tests
coverage report -m
