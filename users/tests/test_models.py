import pytest

from ..models import User

pytestmark = pytest.mark.django_db


def test_create_user():
    user = User.objects.create_user(
        username='usuario_test', email='email_test@test.com', password='passw0rd'
    )
    assert user.username == 'usuario_test'
    assert user.email == 'email_test@test.com'
    assert user.is_active
    assert not user.is_staff
    assert not user.is_staff


def test_create_superuser():
    user = User.objects.create_superuser(
        username='superuser_test', email='superuser@super.com', password='superpassw0rd'
    )
    assert user.username == 'superuser_test'
    assert user.email == 'superuser@super.com'
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser
