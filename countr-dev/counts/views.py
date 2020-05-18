from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Counter

def index(req):
    latest = Counter.objects.order_by('-created_date')[:5]
    ctx = {'latest': latest}
    
    return render(req, 'counts/index.html', ctx)

def detail(req, counter_id):
    try:
        counter = get_object_or_404(Counter, id=counter_id)
        ctx = {
            'id'    : counter_id,
            'label' : counter.label,
            'value' : counter.value
        }
        return render(req, 'counts/detail.html', ctx)
    except Counter.DoesNotExist:
        raise Http404("Counter not found")