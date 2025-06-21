from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import logging

# Configure logger
logger = logging.getLogger(__name__)

def index(request):
    try:
        logger.info("Rendering index page")
        return render(request, 'index.html')
    except Exception as e:
        logger.error(f"Error rendering index page: {str(e)}")
        return HttpResponse("Error loading the page", status=500)

def about(request):
    try:
        logger.info("Rendering about page")
        return render(request, 'about.html')
    except Exception as e:
        logger.error(f"Error rendering about page: {str(e)}")
        return HttpResponse("Error loading the page", status=500)

def services(request):
    try:
        logger.info("Rendering services page")
        return render(request, 'services.html')
    except Exception as e:
        logger.error(f"Error rendering services page: {str(e)}")
        return HttpResponse("Error loading the page", status=500)

def gallery(request):
    try:
        logger.info("Rendering gallery page")
        return render(request, 'gallery.html')
    except Exception as e:
        logger.error(f"Error rendering gallery page: {str(e)}")
        return HttpResponse("Error loading the page", status=500)

def packages(request):
    try:
        logger.info("Rendering packages page")
        return render(request, 'packages.html')
    except Exception as e:
        logger.error(f"Error rendering packages page: {str(e)}")
        return HttpResponse("Error loading the page", status=500)

def venues(request):
    try:
        logger.info("Rendering venues page")
        return render(request, 'venues.html')
    except Exception as e:
        logger.error(f"Error rendering venues page: {str(e)}")
        return HttpResponse("Error loading the page", status=500)

def testimonials(request):
    try:
        logger.info("Rendering testimonials page")
        return render(request, 'testimonials.html')
    except Exception as e:
        logger.error(f"Error rendering testimonials page: {str(e)}")
        return HttpResponse("Error loading the page", status=500)

def contact(request):
    try:
        logger.info("Rendering contact page")
        context = {
            'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
        }
        return render(request, 'contact.html', context)
    except Exception as e:
        logger.error(f"Error rendering contact page: {str(e)}")
        return HttpResponse("Error loading the page", status=500)

def page_not_found(request, exception):
    logger.warning(f"404 error occurred: {request.path}")
    return render(request, '404.html', status=404)

def server_error(request):
    logger.error("500 error occurred")
    return render(request, '500.html', status=500)
