from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)
html = """lorem"""


def index(request):
    logger.info('Index page accessed')
    return HttpResponse(html)


def about(request):
    logger.info('About page accessed')
    return HttpResponse(html)
