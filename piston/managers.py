from django.db import models
from django.contrib.auth import get_user_model

KEY_SIZE = 18
SECRET_SIZE = 32


def generate_random(length):
    return get_user_model().objects.make_random_password(length=length)


class ConsumerManager(models.Manager):
    def create_consumer(self, name, description=None, user=None):
        """
        Shortcut to create a consumer with random key/secret.
        """
        return self.create(
            name=name,
            description=description,
            user=user,
            key=generate_random(KEY_SIZE),
            secret=generate_random(SECRET_SIZE))

    _default_consumer = None

class ResourceManager(models.Manager):
    _default_resource = None

    def get_default_resource(self, name):
        """
        Add cache if you use a default resource.
        """
        if not self._default_resource:
            self._default_resource = self.get(name=name)

        return self._default_resource        

class TokenManager(models.Manager):
    def create_token(self, consumer, token_type, timestamp, user=None):
        """
        Shortcut to create a token with random key/secret.
        """
        return self.create(
            consumer=consumer,
            token_type=token_type,
            timestamp=timestamp,
            user=user,
            key=generate_random(KEY_SIZE),
            secret=generate_random(SECRET_SIZE))
