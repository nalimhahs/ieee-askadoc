from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings


def is_doctor(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=settings.LOGIN_REDIRECT_URL):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_doc,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
