from .celery import app as celery_app

__all__ = ("celery_app",)

from gevent import monkey
monkey.patch_all()