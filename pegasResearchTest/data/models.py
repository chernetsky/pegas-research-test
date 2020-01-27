from django.db import models

#
# Client data model
#
class ClientData(models.Model):
    timestamp = models.DateTimeField()
    value = models.IntegerField()
