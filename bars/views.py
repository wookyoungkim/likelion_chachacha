from django.conf import settings
from django.contrib import auth
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Bar
from users.models import User
# from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    bars = Bar.objects.all()
    return render(request, 'bars_home.html', {'bar':bars})

def bar_detail(request, bar_id):
    bar_detail=get_object_or_404(Bar, pk=bar_id)
    return render(request, 'bar_detail.html',{'bar':bar_detail})

# def create_review(request, bar_id):
#     bar=get_object_or_404(Bar, pk=bar_id)
#     if request.method == 'POST':
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             review=form.save(commit=False)
#             review.bar=bar
#             review.save()
#             return redirect('/bars/detail/'+ str(bar.id), {'bar':bar})
#     elif request.method == 'GET':
#         return render(request, 'bar_review.html', {'bar':bar})
    

    
