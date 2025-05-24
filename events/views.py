from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from datetime import date
from .forms import EventForm



def calendar_view(request):
    events = Event.objects.all()
    return render(request, 'events/calendar.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('events:calendar')
    return redirect('events:calendar')
