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
    

    
def bar_select(request):
        if request.method == 'POST':
                mood2 = reqeust.POST['mood2']
                mood1 = reqeust.POST['mood1']
                mood3 = reqeust.POST['mood3']
                mood4 = reqeust.POST['mood4']
                mood5 = reqeust.POST['mood5']
                mood6 = reqeust.POST['mood6']
                mood7 = reqeust.POST['mood7']
                mood8 = reqeust.POST['mood8']

                chicken = request.POST['chicken']
                jokbal = request.POST['jokbal']
                ijakaya = request.POST['ijakaya']
                gogi = request.POST['gogi']
                joongkuk = request.POST['joongkuk']
                whui = request.POST['whui']
                pojang = request.POST['pojang']
                junjip = request.POST['junjip']
                pizza = request.POST['pizza']
                hopjip = request.POST['hopjip']
                gookbab = request.POST['gookbab']
                yang = request.POST['yang']
                hansik = request.POST['hansik']

                inwon_xsmall = request.POST['inwon_xsmall']
                inwon_small = request.POST['inwon_small']
                inwon_medium = request.POST['inwon_medium']
                inwon_large = request.POST['inwon_large']
                inwon_xlarge = request.POST['inwon_xlarge']

                silwoi = request.POST['silwoi']
                silne = request.POST['silne']
                gongyong = request.POST['gongyong']
                bulli = request.POST['bulli']
                # nomatter = request.POST['nomatter']

                q = Q()

                q.add(Q(chicken=chicken)|Q(jokbal=jokbal)|Q(ijakaya=ijakaya)|Q(gogi=gogi)|Q(joongkuk=joongkuk)|Q(whui=whui)|Q(pojang=pojang)|Q(junjip=junjip)|Q(pizza=pizza)|Q(hopjip=hopjip)|Q(gookbab=gookbab)|Q(yang=yang)|Q(hansik=hansik),q.AND)
                q.add(Q(inwon_xsmall=inwon_xsmall)|Q(inwon_small=inwon_small)|Q(inwon_medium=inwon_medium)|Q(inwon_large=inwon_large)|Q(inwon_xlarge=inwon_xlarge),q.AND)
                q.add(Q(silwoi=silwoi)|Q(silne=silne)|Q(bulli=bulli),a.AND)
                q.add(Q(mood1=mood1)|Q(mood2=mood2)|Q(mood3=mood3)|Q(mood4=mood4)|Q(mood5=mood5)|Q(mood6=mood6)|Q(mood7=mood7)|Q(mood8=mood8),q.AND)
                selected_bar = Bar.objects.filter(q)

                return render(request, 'bar_selected.html', {'selected_bar':selected_bar})

        
        return render(request, 'bars_select.html')
