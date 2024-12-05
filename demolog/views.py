from django.shortcuts import render
import logging
from django.contrib.auth.models import User
# Create your views here.


logger = logging.getLogger(__name__) # demolog.views

def index(request):
    context = {}
    # pass some message in logger
    logger.info("Testing my logger")
    try:
        User.objects.get(pk=1)
    except User.DoesNotExist:
        logger.error("User with ID %s does not exist",1)
    return render(request, "index.html", context)