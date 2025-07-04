from django.shortcuts import redirect
from functools import wraps



def if_is_main(view_func):
    @wraps(view_func)
    def wrapper(request):
        user = request.user
        if not user.is_main:
            return redirect('/')
        return view_func(request)
    
    return wrapper
