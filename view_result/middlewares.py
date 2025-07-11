from django.shortcuts import redirect

def auth(view_function):
    def wrapped(request, *args, **kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        return view_function(request, *args, **kwargs)
    return wrapped

def guest(view_function):
    def wrapped(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('result')
        return view_function(request, *args, **kwargs)
    return wrapped
