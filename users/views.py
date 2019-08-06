from django.conf import settings
from django.contrib import auth
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import User, Message
from django.db.models import Q
from .forms import MessagePost
from django.contrib.auth.decorators import login_required
from bars.models import Bar


# Create your views here.
def home(request):
    return render(request, 'users_home.html')
    

# 로그인
def login(request):
    if request.method == 'GET':
        error_message = '로그인페이지입니다.'
        return render(request, 'login.html', {'error_message':error_message})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)        
        if user is not None:
            auth.login(request, user)
            return render(request, 'users_home.html', {'user':user})
    error_message = '잘못된 요청입니다. 다시 로그인해주세요.'  
    return render(request, 'login.html', {'error_message':error_message})
        
@login_required
def logout(request):
    auth.logout(request)
    return redirect('users/')



# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                name=request.POST.get('name'), 
                password=request.POST['password1'], 
                age=request.POST['age'],
                gender=request.POST['gender'], 
                
                # bar_name=request.POST['bar_name'],
                # phone=request.POST['phone'],
                )
            if user is not None:
                auth.login(request, user)
                return redirect('/users')
    print("회원가입 안됨")
    return render(request, 'signup.html') 

def signup_owner(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                name=request.POST.get('name'), 
                password=request.POST['password1'], 
                # age=request.POST['age'],
                gender=request.POST['gender'], 

                owner = True,                
                owner_bar_name=request.POST['owner_bar_name'],
                owner_bar_phone=request.POST['owner_bar_phone'],
                )
            if user is not None:
                auth.login(request, user)
                return redirect('/users')
    print("회원가입 안됨")
    return render(request, 'signup_owner.html') 

#쪽지 보내기
@login_required
def message_post(request, user_id):
    if request.user.is_authenticated and request.method == 'POST':
        form = MessagePost(request.POST)
        if form.is_valid():
            message = form.save(commit=False)        #db에 데이터를 저장하기 전에 특정 행동을 하고싶을땨
            message.message_to = get_object_or_404(User, id=user_id)
            message.message_from = request.user      #로그인 한 유저
            message.pub_date=timezone.datetime.now()
            # message.number=request.POST['number']
            message.save()       #db에 저장
            # return redirect('/users/messages/from', {'message':message })    #보낸 쪽지리스트보여주는 페이지로
            return redirect('/users/messages/box/'+str(user_id))
    elif request.method == 'GET':
        message_to = get_object_or_404(User, id=user_id)
        message_from=request.user
        form = MessagePost()
        return render(request, 'post.html',{'form':form, 'message_to':message_to, 'message_from':message_from })

#디테일 
@login_required
def message_detail(request, message_id):
    user=request.user
    detail_message=get_object_or_404(Message, pk=message_id)
    return render(request, 'detail.html', {'message':detail_message, 'user':user})

#보관함
@login_required
def message_box(request):
    # if type=='to': #받은쪽지보기
    #     message_to_list = Message.objects.filter(message_to=request.user)
    #     #특정 조건(message_to가 나인)에 해당하는 row 가져오기
    #     return render(request, 'message_box.html', {'message':message_to_list})
    # elif type=='from':  #보낸쪽지보기
    #     message_from_list=Message.objects.filter(message_from=request.user)
    #     return render(request, 'message_box.html', {'message':message_from_list})
    user=request.user
    messages=Message.objects.filter(Q(message_to=user) | Q(message_from=user))
    user_list=[]
    
    for i in messages:
        check=1
        if user == i.message_from: #발신자가 나인 메세지
            for j in range(0,len(user_list)):
                if user_list[j]==i.message_to:
                    check=0
            if check==1:
                user_list.append(i.message_to)
                
        else:
            for j in range(0, len(user_list) ): #수신자가 나인 메세지
                if user_list[j]==i.message_from:
                    check=0
            if check==1:
                user_list.append(i.message_from)  
    return render(request, 'message_box.html', {'user':user,'messages':messages, 'user_list':user_list})


def message_room(request, user_id):
    user=request.user
    owner=get_object_or_404(User, id=user_id)
    # message=Message.objects.all()
    message_list=Message.objects.filter(Q(message_to=user) | Q(message_from=user))   #내가 보내거나 받은 메세지
    message_list=message_list.filter(Q(message_to=owner) | Q(message_from=owner)) #그중에 수신자나 발신자 owner인거
    message_list=message_list.order_by('pub_date')
    return render(request, 'message_room.html', {'messages':message_list,'owner':owner})

#쪽지 삭제
@login_required
def message_delete(request, message_id):
    user=request.user
    message=get_object_or_404(Message, id=message_id)
    message.delete()
    if message.message_to==user:
        return redirect('/users/messages/to')   #내가 받은 ㅁ세지 삭제
    elif message.message_from==user:
        return redirect('/users/messages/from')     #내가 보낸 메세지 삭제

@login_required
def create_review(request, bar_id):
    bar=get_object_or_404(Bar, pk=bar_id)
    if request.method == 'POST':
        review_author = request.user
        review_bar = request.bar
        content = request.POST['content']
        rating = request.POST['rating']
        # review=form.save(commit=False)
        # review.bar=bar
        # review.save()
        return redirect('/bars/detail/'+ str(bar.id), {'bar':bar})
    elif request.method == 'GET':
        return render(request, 'bar_review.html', {'bar':bar})
    

    