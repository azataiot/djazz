"""
A ready-to-use Django project tailored for practical, real-world applications, djazz comes with pre-configured essential settings and industry best practices built-in, ensuring a streamlined development process right out of the box. Ideal for developers looking to jumpstart their projects without the hassle of initial setup.
"""
from .celery import app as celery_app # noqa

__all__ = ('celery_app',)
