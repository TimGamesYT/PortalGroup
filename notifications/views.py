from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def notification_list(request):
    notifications = request.user.notifications.all()

    return render(request, 'notifications/notification-list-template.html', {'notifications': notifications})

def mark_as_read(request, notification_id):
    notification = request.user.notifications.get(id=notification_id)
    
    notification.is_read = True
    notification.save()

    return redirect('notification-list')

def mark_all_as_read(request):
    notifications = request.user.notifications.all().filter(is_read=False)

    for notification in notifications:
        notification.is_read = True
        notification.save()

    return redirect('notification-list')