from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model 
from django.contrib.auth.models import User
# Create your models here.





class detail_matches(models.Model):
    team1= models.CharField(max_length=100)
    team2= models.CharField(max_length=100)
    date=models.DateField()


    def __str__(self):
        return str(self.id,self.team1,self.team2)


class update_matches(models.Model):
    team1= models.CharField(max_length=100)
    team2= models.CharField(max_length=100)
    option1= models.CharField(max_length=100)
    option2= models.CharField(max_length=100)
    option3= models.CharField(max_length=100)
    
    date=models.DateField()


    def __str__(self):
        return str(self.id)

class submitted_detail(models.Model):
    user_id =  models.ForeignKey(User,  on_delete=models.CASCADE)
    match_id = models.ForeignKey(update_matches,  on_delete=models.CASCADE)
    # match_key_id = models.IntegerField(default=0, auto)
    submitted_ans= models.CharField(max_length=100)
    date = models.DateField()
   
    def __str__(self):
        return str(self.id)
    

class submitted_ans(models.Model):
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    answer = models.IntegerField()
   
    def __str__(self):
        return str(self.answer)

class results_update_final(models.Model):
    team1= models.CharField(max_length=100)
    team2= models.CharField(max_length=100)
    flag1= models.CharField(max_length=100)
    flag2= models.CharField(max_length=100)
    result= models.CharField(max_length=100)
    group= models.CharField(max_length=100)
    date= models.DateField()

    

   
    def __str__(self):
        return str(self.id)



