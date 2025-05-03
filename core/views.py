from django.shortcuts import redirect

def set_theme(request):
    if request.method == 'POST':
        theme = request.POST.get('theme')
        if theme in ['light', 'dark']:
            request.session['theme'] = theme
    return redirect(request.META.get('HTTP_REFERER', '/'))