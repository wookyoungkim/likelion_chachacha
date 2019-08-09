from django.conf import settings
from django.contrib import auth
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Bar
from users.models import User
# from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random

# Create your views here.
def home(request):
    bars = Bar.objects.all()
    current_user = request.user
    tmp_bar = []
    if current_user.first:
            tmp_bar.append(current_user.first)
    else:
            pass
    if current_user.second:
            tmp_bar.append(current_user.second)
    else:
            pass
    if current_user.third:
            tmp_bar.append(current_user.third)
    else:
            pass
    if current_user.fourth:
            tmp_bar.append(current_user.fourth)
    else:
            pass
    if current_user.fifth:
            tmp_bar.append(current_user.fifth)
    else:
            pass

    

    return render(request, 'bars_home.html', {'bar':bars, 'current_user':current_user, 'tmp_bar':tmp_bar})

def bar_detail(request, bar_id):
    bar_detail=get_object_or_404(Bar, pk=bar_id)
    return render(request, 'bar_detail.html',{'bar':bar_detail})

#### 정혁
def bar_detail_detail(request, bar_id):
        bar_detail_detail=get_object_or_404(Bar, pk=bar_id)
        return render(request, 'bars_detail_detail.html',{'bar':bar_detail_detail})


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
    
# def bar_review(request, bar_id):
#         bar=get_object_or_404(Bar, id=bar_id)
#         reviews=Review.object.filter(review.reivew_bar=bar)
#         return render(request, 'bars_detail_review.html', {'bar':bar, 'reviews':reviews})  우경이 진행중
    
def bar_select(request):
        if request.method == 'POST':
                q1 = Q()
                q2 = Q()
                q3 = Q()
                q4 = Q()
                
                if 'mood1' in request.POST:
                        # mood1 = request.POST['mood1']
                        q1.add(Q(mood1=True), q1.OR)
                        # pass
                else:
                        pass
                        # q.add(Q(mood1=True), q.OR)
                if 'mood2' in request.POST:
                        # mood2 = request.POST['mood2']
                        q1.add(Q(mood2=True), q1.OR)
                        # pass
                else:
                        # mood2 = False
                        # q.add(Q(mood2=True), q.OR)
                        pass
                if 'mood3' in request.POST:
                        # mood3 = request.POST['mood3']
                        q1.add(Q(mood3=True), q1.OR)
                        # pass
                else:
                        # mood3 = False
                        # q.add(Q(mood3=True), q.OR)
                        pass
                if 'mood4' in request.POST:
                        # mood4 = request.POST['mood4']
                        q1.add(Q(mood4=True), q1.OR)
                        # pass
                else:
                        # mood4 = False
                        # q.add(Q(mood4=True), q.OR)
                        pass
                if 'mood5' in request.POST:
                        # mood5 = request.POST['mood5']
                        q1.add(Q(mood5=True), q1.OR)
                        # pass
                else:
                        # mood5 = False
                        # q.add(Q(mood5=True), q.OR)
                        pass
                if 'mood6' in request.POST:
                        # mood6 = request.POST['mood6']
                        q1.add(Q(mood6=True), q1.OR)
                        # pass
                else:
                        # mood6 = False
                        # q.add(Q(mood6=True), q.OR)
                        pass
                if 'mood7' in request.POST:
                        # mood7 = request.POST['mood7']
                        q1.add(Q(mood7=True), q1.OR)
                        # pass
                else:
                        # mood7 = False
                        # q.add(Q(mood7=True), q.OR)
                        pass
                if 'mood8' in request.POST:
                        # mood8 = request.POST['mood8']
                        q1.add(Q(mood8=True), q1.OR)
                        # pass
                else:
                        # mood8 = False
                        # q.add(Q(mood8=True), q.OR)
                        pass
                
                # mood1 = request.POST['mood1']
                # mood2 = request.POST['mood2']
                # mood3 = request.POST['mood3']
                # mood4 = request.POST['mood4']
                # mood5 = request.POST['mood5']
                # mood6 = request.POST['mood6']
                # mood7 = request.POST['mood7']
                # mood8 = request.POST['mood8']


                if 'chicken' in request.POST:
                        # chicken = False
                        q2.add(Q(chicken=True), q2.OR)
                        # pass
                else:
                        # chicken = True
                        # q2.add(Q(chicken=True), q.OR)
                        pass

                if 'jokbal' in request.POST:
                        # jokbal = False
                        q2.add(Q(chicken=True), q2.OR)
                        # pass
                else:
                        # jokbal = True
                        pass
                if 'jokbal' in request.POST:
                        # ijakaya = request.POST['ijakaya']
                        q2.add(Q(chicken=True), q2.OR)
                else:
                        # ijakaya = False
                        pass
                if 'gogi' in request.POST:
                        q2.add(Q(gogi=True), q2.OR)
                else:
                        pass
                if 'joongkuk' in request.POST:
                        q2.add(Q(joongkuk=True), q2.OR)
                else:
                        # joongkuk = False
                        pass
                if 'whui' in request.POST:
                        q2.add(Q(whui=True), q2.OR)
                else:
                        # whui = False
                        pass
                if 'pojang' in request.POST:
                        q2.add(Q(pojang=True), q2.OR)
                else:
                        # pojang = False
                        pass
                if 'junjip' in request.POST:
                        q2.add(Q(junjip=True), q2.OR)
                else:
                        # junjip = False
                        pass
                if 'pizza' in request.POST:
                        q2.add(Q(pizza=True), q2.OR)
                else:
                        # pizza = False
                        pass
                if 'hopjip' in request.POST:
                        q2.add(Q(hopjip=True), q2.OR)
                else:
                        # hopjip = False
                        pass
                if 'gookbab' in request.POST:
                        q2.add(Q(gookbab=True), q2.OR)
                else:
                        # gookbab = False
                        pass
                if 'yang' in request.POST:
                        q2.add(Q(yang=True), q2.OR)
                else:
                        # yang = False
                        pass
                if 'hansik' in request.POST:
                        q2.add(Q(hansik=True), q2.OR)
                else:
                        # hansik = False
                        pass

                # chicken = request.POST['chicken']
                # jokbal = request.POST['jokbal']
                # ijakaya = request.POST['ijakaya']
                # gogi = request.POST['gogi']
                # joongkuk = request.POST['joongkuk']
                # whui = request.POST['whui']
                # pojang = request.POST['pojang']
                # junjip = request.POST['junjip']
                # pizza = request.POST['pizza']
                # hopjip = request.POST['hopjip']
                # gookbab = request.POST['gookbab']
                # yang = request.POST['yang']
                # hansik = request.POST['hansik']

                if 'inwon_xsmall' in request.POST:
                        q3.add(Q(inwon_xsmall=True), q3.OR)
                        # inwon_xsmall = request.POST['inwon_xsmall']
                else:
                        # inwon_xsmall = False
                        pass
                if 'inwon_small' in request.POST:
                        # inwon_small = request.POST['inwon_small']
                        q3.add(Q(inwon_small=True), q3.OR)
                else:
                        # inwon_small = False
                        pass
                if 'inwon_medium' in request.POST:
                        # inwon_medium = request.POST['inwon_medium']
                        q3.add(Q(inwon_medium=True), q3.OR)
                else:
                        # inwon_medium = False
                        pass
                if 'inwon_large' in request.POST:
                        # inwon_large = request.POST['inwon_large']
                        q3.add(Q(inwon_large=True), q3.OR)
                else:
                        # inwon_large = False
                        pass
                if 'inwon_xlarge' in request.POST:
                        # inwon_xlarge = request.POST['inwon_xlarge']
                        q3.add(Q(inwon_xlarge=True), q3.OR)
                else:
                        # inwon_xlarge = False
                        pass
                        
                # # inwon_xsmall = request.POST['inwon_xsmall']
                # # inwon_small = request.POST['inwon_small']
                # # inwon_medium = request.POST['inwon_medium']
                # # inwon_large = request.POST['inwon_large']
                # # inwon_xlarge = request.POST['inwon_xlarge']

                if 'silwoi' in request.POST:
                        # silwoi = request.POST['silwoi']
                        q4.add(Q(silwoi=True), q4.OR)
                else:
                        # silwoi = False
                        pass
                if 'silne' in request.POST:
                        # silne = request.POST['silne']
                        q4.add(Q(silne=True), q4.OR)
                else:
                        # silne = False
                        pass
                if 'gongyong' in request.POST:
                        # gongyong = request.POST['gongyong']
                        q4.add(Q(gongyong=True), q4.OR)
                else:
                        # gongyong = False
                        pass
                if 'bulli' in request.POST:
                        # bulli = request.POST['bulli']
                        q4.add(Q(bulli=True), q4.OR)
                else:
                        # bulli = False
                        pass

                # silwoi = request.POST['silwoi']
                # silne = request.POST['silne']
                # gongyong = request.POST['gongyong']
                # bulli = request.POST['bulli']
                # # nomatter = request.POST['nomatter']

                # q = Q()
                # q = Q(chicken=chicken)|Q(jokbal=jokbal)|Q(ijakaya=ijakaya)|Q(gogi=gogi)|Q(joongkuk=joongkuk)|Q(whui=whui)|Q(pojang=pojang)|Q(junjip=junjip)|Q(pizza=pizza)|Q(hopjip=hopjip)|Q(gookbab=gookbab)|Q(yang=yang)|Q(hansik=hansik)
                # q.add(Q(chicken=chicken)|Q(jokbal=jokbal)|Q(ijakaya=ijakaya)|Q(gogi=gogi)|Q(joongkuk=joongkuk)|Q(whui=whui)|Q(pojang=pojang)|Q(junjip=junjip)|Q(pizza=pizza)|Q(hopjip=hopjip)|Q(gookbab=gookbab)|Q(yang=yang)|Q(hansik=hansik),q.AND)
                # q.add(Q(inwon_xsmall=inwon_xsmall)|Q(inwon_small=inwon_small)|Q(inwon_medium=inwon_medium)|Q(inwon_large=inwon_large)|Q(inwon_xlarge=inwon_xlarge),q.AND)
                # q.add(Q(silwoi=silwoi)|Q(silne=silne)|Q(bulli=bulli),q.AND)
                # q.add(Q(mood1=mood1)|Q(mood2=mood2)|Q(mood3=mood3)|Q(mood4=mood4)|Q(mood5=mood5)|Q(mood6=mood6)|Q(mood7=mood7)|Q(mood8=mood8),q.AND)
                # q.add(Q(chicken=chicken) & Q(jokbal=jokbal), q.AND)
                # selected_bar = Bar.objects.filter(Q(chicken=chicken) | Q(jokbal=jokbal))
                # q = Q()
                # q.add(q1 & q1, q.AND)
                selected_bar = Bar.objects.filter(q1)
                selected_bar = selected_bar.filter(q2)
                selected_bar = selected_bar.filter(q3)
                selected_bar = selected_bar.filter(q4)


                return render(request, 'bars_select.html', {'selected_bar':selected_bar})

        
        return render(request, 'bars_select.html')

def bar_review(request, bar_id):
        user=request.user
        bar=get_object_or_404(Bar, id=bar_id)
        reviews=Review.objects.filter(review_bar=bar)
        count=reviews.count()
        heart = Heart.objects.filter(user_heart=user,bar_heart=bar)
        return render(request, 'bars_detail_review.html', {'bar':bar, 'reviews':reviews, 'heart':heart, 'count':count, 'user':user})
    
def bar_menu(request, bar_id):
        user=request.user
        bar=get_object_or_404(Bar, id=bar_id)
        menu=bar.menu
        heart = Heart.objects.filter(user_heart=user,bar_heart=bar)
        return render(request,'bar_detail_menu.html', {'bar':bar, 'menu':menu,'heart':heart,'user':user})