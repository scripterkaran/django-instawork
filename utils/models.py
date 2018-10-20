import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel


class BaseModelClass(models.Model):
    class Meta:
        abstract = True


class UUIDModel(BaseModelClass,TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

