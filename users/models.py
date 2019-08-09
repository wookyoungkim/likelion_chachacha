from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from bars.models import Bar

# AbstractUser은 장고에 기본적으로 있는 유저 모델입니다.
# 이 모델은 유용한 필드들을 미리 지정해놓았기 때문에 이 모델을 상속받고, 필요한 필드들을 추가했습니다.
class User(AbstractUser):
    """ User Model """
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
   
    name = models.CharField(max_length=140, blank=False,null=True) # 유저 실명
    phone = models.CharField(max_length=225, blank=False,null=True) # 핸드폰 번호->논의 필요
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    age = models.IntegerField(null=True)
    owner = models.BooleanField(default=False)
    owner_bar_phone = models.IntegerField(blank=True, null=True)
    owner_bar_name = models.CharField(max_length=100, blank=True, null=True)


    first = models.ForeignKey(Bar,on_delete=models.CASCADE, null=True,related_name='+', blank=True)
    second = models.ForeignKey(Bar,on_delete=models.CASCADE, null=True,related_name='+', blank=True)
    third = models.ForeignKey(Bar,on_delete=models.CASCADE, null=True,related_name='+', blank=True)
    fourth = models.ForeignKey(Bar,on_delete=models.CASCADE, null=True,related_name='+', blank=True)
    fifth = models.ForeignKey(Bar,on_delete=models.CASCADE, null=True,related_name='+', blank=True)
    
    first_date = models.DateField(null=True, blank=True)

class TimeStampedModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class Message(TimeStampedModel):
    NUMBER_CHOICES=(
        ('1', '1명'),
        ('2', '2명'),
        ('3', '3명'),
        ('4', '4명'),
        ('5', '5명'),
        ('6', '6명'),
        ('7', '7명'),
        ('8', '8명'),
        ('9', '9명'),
        ('10', '10명'),
        
    )
    message_to= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,       #메세지 보낸 상대가 삭제됐을때의 대응
        default='알수없음',
        related_name='message_to',
        null=True
    )
    message_from=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,       #메세지 보낸 상대가 삭제됐을때의 대응-> 알수없음으로 뜨도록
        default='알수없음',
        related_name='message_from',
        null=True

    )
    text=models.TextField(null=True)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return f'{self.id}:{self.message_to}-{self.message_from}:{self.text}'

    def summary(self):
        return self.text[:40]



class Route(models.Model):
    route_author = models.ForeignKey(User, on_delete=models.CASCADE)


    name_route = models.CharField(max_length=55, blank=False)
    pub_date = models.DateField(null=True, blank=True)

    first_bar = models.ForeignKey(Bar,on_delete=models.CASCADE, null=True,related_name='+', blank=True)
    second_bar = models.ForeignKey(Bar,on_delete=models.CASCADE, null=True,related_name='+', blank=True)
    third_bar = models.ForeignKey(Bar,on_delete=models.CASCADE, null=True,related_name='+', blank=True)
    fourth_bar = models.ForeignKey(Bar,on_delete=models.CASCADE, null=True,related_name='+', blank=True)
    fifth_bar = models.ForeignKey(Bar,on_delete=models.CASCADE, null=True,related_name='+', blank=True)

    def __str__(self):
        pd = str(self.pub_date)
        return pd


class Review(models.Model):
    review_author = models.ForeignKey(User, on_delete=models.PROTECT)
    review_bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return (str(self.review_bar)+"에 대한 "+ str(self.review_author)+"의 댓글")

class Heart(TimeStampedModel):
    user_heart = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True, 
        related_name='user_heart'
        ) #좋아요 한 유저
    bar_heart = models.ForeignKey(
        Bar,
        on_delete=models.SET_DEFAULT, 
        default='알수없음',
        null=True,
        related_name='bar_heart'
        ) #좋아요 받은 바

    def __str__(self):
        return (str(self.user_heart)+"가 "+ str(self.bar_heart)+"를 좋아합니다")