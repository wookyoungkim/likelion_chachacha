
# Create your models here.
from django.db import models
# from users.models import User
import datetime


# Create your models here.
# class Liquor(models.Model):
#     soju = models.BooleanField(default=False)
#     wine = models.BooleanField(default=False)
#     makgurli = models.BooleanField(default=False)
#     wisky = models.BooleanField(default=False)
#     beer = models.BooleanField(default=False)
#     cocktail = models.BooleanField(default=False)



class Bar(models.Model):
    """ Bar Model """
    name = models.CharField(max_length=80)
    represent_image = models.ImageField(upload_to='bars',null=True,blank=True)
    first_image = models.ImageField(upload_to='bars',null=True,blank=True)
    second_image = models.ImageField(upload_to='bars',null=True,blank=True)
    summary = models.CharField(max_length=300, null=True)
    text = models.TextField(max_length=200) 
    location_url = models.TextField(max_length=200,null=True,blank=True) 
    keyword = models.CharField(max_length=80, null=True) 
    # address = models.CharField(max_length=300, null=True) 
    hours=models.CharField(max_length=80,null=True)
    menu = models.CharField(max_length=150, null=True, blank=True)
    bar_phone = models.IntegerField(null=True)

    lat = models.FloatField(max_length=40)
    lng = models.FloatField(max_length=40)

    # 무드
    mood1 = models.BooleanField(default=False)
    mood2 = models.BooleanField(default=False)
    mood3 = models.BooleanField(default=False)
    mood4 = models.BooleanField(default=False)
    mood5 = models.BooleanField(default=False)
    mood6 = models.BooleanField(default=False)
    mood7 = models.BooleanField(default=False)
    mood8 = models.BooleanField(default=False)

    # 14 bar_sort
    chicken = models.BooleanField(default=False)
    jokbal = models.BooleanField(default=False)
    ijakaya = models.BooleanField(default=False)
    gogi = models.BooleanField(default=False)
    joongkuk = models.BooleanField(default=False)
    whui = models.BooleanField(default=False)
    pojang = models.BooleanField(default=False)
    junjip = models.BooleanField(default=False)
    pizza = models.BooleanField(default=False)
    hopjip = models.BooleanField(default=False)
    gookbab = models.BooleanField(default=False)
    yang = models.BooleanField(default=False)
    hansik  =models.BooleanField(default=False)

    # 인원수 1~2/3~5/6~10/11~20/21~30
    inwon_xsmall = models.BooleanField(default=False)
    inwon_small = models.BooleanField(default=False)
    inwon_medium = models.BooleanField(default=False)
    inwon_large = models.BooleanField(default=False)
    inwon_xlarge = models.BooleanField(default=False)

    #화장실

    silwoi = models.BooleanField(default=False)
    silne = models.BooleanField(default=False)
    gongyong = models.BooleanField(default=False)
    bulli = models.BooleanField(default=False)
    nomatter = models.BooleanField(default=False)

    

 

    def __str__(self):
        return self.name





# class Review(models.Model):
#     bar=models.ForeignKey(
#         Bar,
#         on_delete=models.CASCADE,
#         related_name='reviews',
#         null=True
#     )
#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     content = models.TextField()
#     rating = models.IntegerField()

#     def __str__(self):
#         return (str(self.bar)+"에 대한 "+ str(self.author)+"의 댓글")
    



# class Product(models.Model):
#     name = models.CharField(max_length=256, verbose_name='상품명')
#     price = models.IntegerField(verbose_name='상품가격')
#     description = models.TextField(verbose_name='상품설명')
#     stock = models.IntegerField(verbose_name='재고', null=True, blank=True)
#     register_date = models.DateField(default=datetime.date.today, name='등록날짜')

    
    
#     def __str__(self):
#         return self.name

    