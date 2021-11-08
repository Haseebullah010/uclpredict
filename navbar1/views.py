from django.contrib.auth.models import User
from django.http import response
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
import requests
from django.http import HttpResponse , HttpResponseRedirect
from django.db.models import F
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.models import update_last_login
from datetime import date
import random
import pandas as pd
from random import randrange


import requests
from bs4 import BeautifulSoup

from django.contrib.auth.decorators import login_required

from datetime import datetime, timezone
from navbar1.models import detail_matches , update_matches , submitted_detail , submitted_ans ,results_update_final

# from .forms import   UserCreation

# Create your views here.
import json

def one(request):

    return render(request,"1.html")
def two(request):

    return render(request,"2.html")
def three(request):

    return render(request,"3.html")
def four(request):

    return render(request,"4.html")
def five(request):

    return render(request,"5.html")
def six(request):

    return render(request,"6.html")
def seven(request):

    return render(request,"7.html")
def eight(request):

    return render(request,"8.html")
def nine(request):

    return render(request,"9.html")
def ten(request):

    return render(request,"10.html")
def eleven(request):

    return render(request,"11.html")

def twelve(request):

    return render(request,"12.html")
def getmethod(request):
    i =0
    if request.user.is_authenticated:
        user = request.user
    

        if request.method == "POST":
            print ("method POST")
           

            value3 = request.POST.get("Option3")
            matchid = request.POST.get("custId")
            print ("match id ",matchid)

            match_object = update_matches.objects.filter(id=matchid)[0]
            print ("match object:",match_object)

            context = {

                'value':value3,

            }
            a=submitted_detail.objects.create(user_id=user,match_id=match_object,match_key_id=matchid,date=date.today(),submitted_ans=value3)
            
            print(a.match_id.team1)
            
            a.save()

            ans =  "user enter ans is " + value3

            print (ans)
            i = i + 1
            return redirect('take_quiz',i = i )

            # return render(request,"Nomatch.html",{'context': ans})

def results(request):

    overallresults_flag = results_update_final.objects.all().order_by("date")
    
    return render(request,"result.html",{'context': overallresults_flag})

def fixture(request):

    return render(request,"fixtureS.html")
def home1(request):
    if request.user.is_authenticated:
        return render(request,"home2.html")
    else:


        return render(request,"home.html")

def ucltop(request):
    
    return render(request,"ucltopscorer.html")

def greatestall(request):


    return render(request,"greatestalltime.html")

def transfer(request):


    return render(request,"transferrumor.html")

def uclwinner(request):
    url = 'https://www.topendsports.com/sport/soccer/list-league-uefa.htm'
    r = requests.get(url)
    soup = BeautifulSoup (r.text, 'html.parser')
    rows_ = []

    for table in soup.find_all('table',class_='list'):
        for row in table.find_all('tr'):
            rows_.append(row.text)
        
    mod_row = []
    for row in rows_:
        mod_row.append(list(filter(bool,row.splitlines())))
    
    df  = pd.DataFrame(data=mod_row)

    df = df.iloc[2: , :]
    df.columns= ['Season','Winner','RunnerUp','Score']
    print (df)
    
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    print (data)
    context = {'d': data}

    return render(request,"uclwinner.html" ,{'context':data} )


def toppred(request):

    allpredictora=submitted_ans.objects.all().order_by("-answer")
    print ("allpredictora:",allpredictora)



    return render(request,"toppredictor.html",{'content': allpredictora})

def top8(request):


    return render(request,"top8teams.html")


def check_user(request):
    if request.method =="GET":
        un = request.GET["user_n"]
        check = User.objects.filter(username=un)

        if len(check)==1:
            return HttpResponse("Exists")
        else :
            return HttpResponse ("Not Exists")
        print (check,len(check))
        print (un)
    return HttpResponse("Hello")

def signup(request):
    if request.method == 'POST':
        fname=request.POST["firstname"]
        lname=request.POST["lastname"]
        fulname=request.POST["username"]
        e_mail=request.POST["email"]
        pas_word=request.POST["password1"]
        # pas_word2=request.POST["password2"]
        
        print (request.POST)
        usr = User.objects.create_user(fulname,e_mail,pas_word)
        usr.first_name = fname
        usr.last_name = lname
        usr.is_staff=False
        usr.save()
        # return HttpResponse("")
        return render(request,"signup2.html",{'status': "{} account has been created successfully".format(fname)})

    print ("in signup ")

    

    return render(request,"signinup.html")


def take_quiz(request):

    if request.user.is_authenticated:
        user = request.user
        

        if request.method == 'GET':
            
            user = request.user
            today = date.today()
            todays_matches = update_matches.objects.filter(date=today)
            
            if todays_matches.count() == 0 :    
                print ("herer")      

                return render (request,"Nomatch.html",{'contexxt':"NO Match Today"})
            
            else:
                todays_match = todays_matches[0]
                id = todays_match.id

                
                user_submitted_todays_matches = submitted_detail.objects.filter(date=today,user_id=user)
                if user_submitted_todays_matches.count() >= (todays_matches.count()):
                    return render(request,"nomatch.html",{'contexxt':"All Today Matches done "})

                for match in user_submitted_todays_matches:
                    todays_matches = todays_matches.exclude(id=match.match_id.id)
                
                
                context = {
                    'firstname': user.first_name,
                    'lastname': user.last_name , 
                    'name': user.username,
                    'email' : user.email,
                    'datejoined': user.date_joined,
                    'lastlogin': user.last_login,
                    'data2': todays_matches[0],
                    'total_matches': todays_matches.count(),
                }
                return render(request,"makeprediction.html",context)

        if request.method == 'POST':
            print ("method POST")
            value3 = request.POST.get("Option3")
            matchid = request.POST.get("custId")
            toatalmatches = request.POST.get("custId2")
            print ("match id ",matchid)

            match_object = update_matches.objects.filter(id=matchid)[0]
            print ("match object:",match_object)

            context = {

                'value':value3,

            }
            a=submitted_detail.objects.create(user_id=request.user,match_id=match_object,date=date.today(),submitted_ans=value3)
            
            print(a.match_id.team1)
            
            a.save()
            
            option1, option2, option3 = random.sample(range(1, 4), 3)

            ans =  "user enter ans is " + value3 + " and our predict " + str(option1)
            
            if value3==str(option1):
                userdatadetail= submitted_ans.objects.filter(user_id=user).count()
                if userdatadetail > 0 :

                    userdata= submitted_ans.objects.filter(user_id=user).update(answer=F('answer')+1)

                    print ("userdata",userdata)


                    
                    print ("correct")
                else:
                    a =submitted_ans.objects.create(user_id=user,answer=1)
                    a.save()

            print ("total matches",toatalmatches)
            print (ans)

            if toatalmatches > str(1):
            
                return redirect('take_quiz' )
            
            else:
                return render(request,"nomatch.html",{'context': "All done"})

            pass
    else:
        return redirect("HOME")

def singin(request):
    

    if request.user.is_authenticated:
        return redirect("take_quiz")
    else:
        if request.method =="POST":
            un= request.POST["username"]
            pas= request.POST["password"]
            print(un)
            
            user= authenticate(username=un,password=pas)

            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect('/admin')
                if user.is_active:
                    return redirect("take_quiz")
            else:
                return render(request,"signin.html",{'context':"Error in username or password"})

        elif request.method =="GET":
            return render(request,"signin.html",{'context':""})

    return render(request,"signin.html")


def user_logout(request):
    logout(request)
    
    return HttpResponseRedirect("/")

@login_required
def make_pred(request):

    return render(request,"makeprediction.html")

def fifapro(request):


    return render(request,"fifapro11.html")