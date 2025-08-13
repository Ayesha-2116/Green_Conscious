# userhistory/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserHistory
from datetime import date


@login_required
def user_history(request):
    visit_history = UserHistory.objects.filter(user=request.user, date=date.today()).order_by('-visit_count')
    context = {
        'visit_history': visit_history,
    }
    return render(request, 'history.html', context)
