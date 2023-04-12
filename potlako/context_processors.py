from django.conf import settings


def offline(context):
    return {'OFFLINE': settings.OFFLINE}
