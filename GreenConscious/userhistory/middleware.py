# userhistory/middleware.py
from django.utils.deprecation import MiddlewareMixin
from datetime import date
from django.urls import resolve
from .models import UserHistory
from django.conf import settings


class UserVisitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            # Exclude media and static paths
            if request.path.startswith(settings.MEDIA_URL) or request.path.startswith(settings.STATIC_URL):
                return

            # Get the current path
            path = resolve(request.path_info).url_name
            if path is None:
                path = request.path_info

            user = request.user
            today = date.today()

            # Check if there is already an entry for today and this path
            history, created = UserHistory.objects.get_or_create(
                user=user,
                path=path,
                date=today,
                defaults={'visit_count': 1}  # Start with 1 for the first visit
            )
            if not created:
                history.visit_count += 1
                history.save()
