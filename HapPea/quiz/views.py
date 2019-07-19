from django.shortcuts import render
from django.utils import timezone
from .models import Plot
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import path,include,reverse_lazy
# from .forms import QuizForm
# Create your views here.

from users.models import Profile,CustomUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from social.apps.django_app.default.models import UserSocialAuth
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse
from .models import *
from .forms import *
from datetime import datetime, date, time, timedelta
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
# from django.utils import simplejson
import json
import random
# from django.contrib.auth.forms import AuthenticationForm

#gobal variable for number of questions per questionaire
N=10

def redirecttologin(request):
    return redirect(reverse_lazy('account_login'))


class PlotListView(ListView):
    model = Plot
    template_name = "list.html"


# @login_required
def home(request):
    
    # if request.user.is_authenticated:
    #     print(request.user.profile.contactnu)
    news=News.objects.all().order_by('-id')
    news=news[:min(len(news),3)]
    newsflag=False
    if len(news)>=1:
        newsflag=True
        if len(news)<3:
            news=news*3
            news=news[:min(len(news),3)]
    
    return render(request, 'html/main.html',{'newsflag':newsflag,'news':news})




def checkprofile(request):
    if not request.user.is_authenticated:
        print('user is not authenticacted')
        return redirect(reverse_lazy('account_login'))
    # if request.user.profile.contactnu

def loginpage(request):
    if request.user.profile.agegroup:
        print(request.user.profile.agegroup)
    else:
        print("age is not present")
        
    return render(request,"core/login.html")

def quizintro(request):
    print("quiz intro")    

    
    request.session['introdone']=True
    return render(request,'html/quiz_intro.html')


def oldresult(request):
    print("old result intro")    

    try:
        how_many_days=60
        print("questionare command ran ")
        questionaires=UserQuestionnaire.objects.all().filter(user=request.user,completed=True,starttime__gte=datetime.now()-timedelta(days=how_many_days))
        print("questionare command ran ")
        print("index might run  ")
        q=questionaires.reverse()[0]
        #showOldResult(request,q)
        print("index not out  run  ")
        
        print("started ats")
        print(q.starttime)
        result=q.score
        if result<50:
                remark="Not satisfied with life"
                colour="r"
        elif result<75:
            remark="Satsified with life"
            colour="o"    
        else:
            remark="On top of the world"
            colour="p" 

        return render(request,'html/result.html',{'result':q.score,'colour':colour,"remark":remark})
    except:
        print("old result exceptions")
        request.session["quizavail"]=True
    return -1
    
    # return redirect(reverse_lazy('quizes'))



def profileinfocheck(request,home=True):
    profile=Profile.objects.get(pk=request.user.profile.pk)
    if request.method=='POST':
        try:
            profile=Profile.objects.get(pk=request.user.profile.pk)
            g=request.POST.get('gender')
            profile.gender=g
            profile.save()
            print("post gender"+str(g))
        except :
            pass
        try:
            profile=Profile.objects.get(pk=request.user.profile.pk)
            a=request.POST.get('agegroup')
            profile.agegroup=a
            profile.save()
            
            print("post agegroup"+str(a)+str())
        except :
            pass
        try:
            profile=Profile.objects.get(pk=request.user.profile.pk)
            print("enterd post phonenumber")
            p=request.POST.get('phonenumber')
            #profile.update(contactnu=p)

            if len(p)==10:
                profile.contactnu=p
            profile.save()
            if profile.contactnu=="":
                return profileinfocheck(request)
            print("post phonenumber"+str(p))
        except Exception as e:
            print(e)
            pass
        
    profile=Profile.objects.get(pk=request.user.profile.pk)
    if profile.gender != 0:
        print(request.user.profile.agegroup)
    else:
        print("gender is not preset")
        return render(request,'html/gender.html')
    
    if profile.agegroup!=0:
        print("agegroup is present"+str(request.user.profile.agegroup))
    else:
        print("agefroup is not preset")
        print("gender"+str(profile.gender))
        if profile.gender==1:
            return render(request,'html/male.html')
        else:
            return render(request,'html/female.html')

    if profile.contactnu is not None and len(profile.contactnu.strip())==10 :
        print(request.user.profile.contactnu)
    else:
        return render(request,'html/phone.html')   
    if home:
        return redirect(reverse_lazy("home"))
    else:
        return -1

    




def quizes(request):#count should be increased on valid post request   
    
    if not request.user.is_authenticated:
        print("inside not")
        return redirect(reverse_lazy("account_login"))   
    
    r=profileinfocheck(request,home=False) 
    if r !=-1:
        print("profiel not present")
        return redirect(reverse_lazy('profileinfocheck'))
    cnt=-1
    last=timezone.now()
    
    # return render(request,'html/quiz_intro.html')
    if "introdone" not in request.session:
        return quizintro(request)
    
    if "quizavail" not in request.session:
        r=oldresult(request)
        if r!=-1:
            return r
        

    if "questionaire" not in request.session:
        print("quastionaire added") 
        request=newUserQuestionnaire(request)
        request.session["answers"]=[]
        request.session["time"]=[]
        request.session['count']=0
        last=timezone.now()

    if request.method == "POST":
        print('choosen value is')
        try:
            v=request.POST.get('choice')
            print("=="+str(v))

            cnt=int(request.session['count'])
            request.session['count']=cnt+1
            request.session["answers"].append(v)
            request.session["time"].append((timezone.now()-last).total_seconds()*1000)
            print("time"+str((last-timezone.now()).total_seconds()*100000))
            last=timezone.now()
        except:
            pass


       
    try:
        cnt=int(request.session['count'])
        print(request.session['plots'])
        try:
            if len(request.session['plots'])==0:
                return render(request,"html/noquiz.html")
        except:
            pass
        if(cnt>=len(request.session['plots'])):
            return showresult(request)
        plot=Plot.objects.get(pk=request.session['plots'][cnt])
        choices=Choice.objects.filter(question=plot)
        print(cnt)
    except:
        showresult(request)
    
    quiz_imgs=None
    ri=0
    try:
        quiz_imgs=QuizImage.objects.random()
        # ri=random.randint(1,count(quiz_imgs))
        # quiz_imgs=quiz_imgs[ri]
        print("ramdominteger "+str(ri))
        
    except:
        print("ramdominteger "+str(ri))
        print("image not fund")
        pass

    
    # count++
    return render(request,'html/quiz.html',{"count":cnt+1,"plot":plot.plot,"question":plot.plot,"choices":choices,"quiz_img":quiz_imgs})


def showresult(request):
    print(request.session["plots"])
    print(request.session["answers"])
    result=0
    remark=""
    colour="o"
    
    if len(request.session['plots'])==len(request.session['answers']):

        questionaire=UserQuestionnaire.objects.get(id=request.session["questionaire"])

        for i in range(len(request.session['plots'])):
            plot=Plot.objects.get(pk=int(request.session['plots'][i]))
            choice=Choice.objects.get(pk=int(request.session['answers'][i]))
            result = result + choice.assessment
            responseOption=ResponseOption.objects.create(choice=choice,time=request.session['time'][i])
            responseOption.save()

            userresponse=UserResponse.objects.create(user_questionnaire=questionaire,plot=plot,response_option=responseOption)
            userresponse.save()
        questionaire.completed=True
        questionaire.score=result
        if result<50:
            remark="Not satisfied with life"
            colour="r"
        elif result<75:
            remark="Satsified with life"
            colour="o"    
        else:
            remark="On top of the world"
            colour="p" 
        questionaire.save()
    else :
        print("error un equal nuber of response and answers")

    return render(request,'html/result.html',{'result':result,'colour':colour,"remark":remark})



    
    




def newUserQuestionnaire(request):
    questionaire=UserQuestionnaire.objects.create(user=request.user,score=0)
    # questionaire.user=request.user
    request.session['questionaire']=questionaire.pk
    questionaire.save()
    # asked=UserResponse.objects.all().filter(user_questionnaire_user=request.user).values_list('plot', flat=True)
    questionaires=UserQuestionnaire.objects.all().filter(user=request.user).values_list('pk',flat=True)
    
    profile=Profile.objects.get(pk=request.user.profile.pk)
    doneresponses=UserResponse.objects.all().filter(user_questionnaire__in=questionaires).values_list('plot',flat=True)
        
    unrepeatedplots=Plot.objects.all().filter(category__age__exact=profile.agegroup).exclude(id__in=doneresponses)
    unN=len(unrepeatedplots)
    if unN>N:
        unN=N
    unrepeatedplots=unrepeatedplots[:unN]
    if unN<N:
        unrepeatedplots=list(unrepeatedplots)+list(Plot.objects.all().filter(category__age__exact=profile.agegroup).exclude(id__in=unrepeatedplots)[:min((N-unN),len(Plot.objects.all()))])

    print(unrepeatedplots)
    print("filters passed")
    # allplots=Plot.objects.all().exclude(id in asked)
    request.session['plots']=[i.pk for i in unrepeatedplots]
    # print("entered the new uestionaire")
    return request

@login_required
def settings(request):
    user = request.user

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'core/settings.html', {
        # 'github_login': github_login,
        # 'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })




@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'core/password.html', {'form': form})




@user_passes_test(lambda u:u.is_staff, login_url=reverse_lazy('login'))
def addquiz(request,*args, **kwargs):
    if request.method == 'POST':
        quiz_form = PlotForm(request.POST, request.FILES, prefix='quiz_form')
        quiz_choice_forms = QuizChoiceFormset(request.POST, request.FILES, prefix='quiz_choice_form')

        # validate the forms separately first so that we can show errors for all forms if multiple
        # forms have an error
        quiz_valid = quiz_form.is_valid()
        quiz_choice_valid = quiz_choice_forms.is_valid()
        # print(quiz_choice_forms.errors)
        

        if quiz_valid and quiz_choice_valid:
            # save the quiz then set it as the instance on the formset before
            # saving the chldren via the formset so that Django
            # can create the relationship in the db
            quiz = quiz_form.save(commit=False)
            category=quiz_form.cleaned_data['category']
            quiz.save()
            quiz.category.set(category)
            quiz.save()
            
            quiz_choice_forms.instance = quiz
            quiz_choice_forms.save()
            return redirect('addQuiz')

        else:
            return render(request, 'addd.html', {'quiz_form': quiz_form, 'quiz_choice_form': quiz_choice_form})
            # print(quiz_valid)
            # print(quiz_choice_valid)
            quiz_form = PlotForm(prefix='quiz_form')
            quiz_choice_form = QuizChoiceFormset(prefix='quiz_choice_form')
    else:
        quiz_form = PlotForm(prefix='quiz_form')
        quiz_choice_form = QuizChoiceFormset(prefix='quiz_choice_form')

    return render(request, 'addd.html', {'quiz_form': quiz_form, 'quiz_choice_form': quiz_choice_form})




@method_decorator(staff_member_required(login_url=reverse_lazy('login')), name='dispatch')
class NewsCreateView(CreateView):
    model = News
    template_name = "news/create.html"
    fields=['title','img','description','url']
    # success_url =


    

@method_decorator(staff_member_required(login_url=reverse_lazy('login')), name='dispatch')
class NewsCreateView(CreateView):
    model = News
    template_name = "news/create.html"
    fields=['title','img','description','url']
    # success_url =

@method_decorator(staff_member_required(login_url=reverse_lazy('login')), name='dispatch')
class NewsUpdateView(UpdateView):
    model = News
    template_name = "news/update.html"
    fields=['title','img','description','url']
    # success_url =

@method_decorator(staff_member_required(login_url=reverse_lazy('login')), name='dispatch')
class NewsListView(ListView):
    model = News
    paginate_by = 10
    template_name = "news/list.html"
    fields=['title','img','description','url']
    # success_url =

class NewsDeleteView(DeleteView):
    model = News
    template_name = "news/delete.html"
    success_url=reverse_lazy('newslist')

@method_decorator(staff_member_required(login_url=reverse_lazy('login')), name='dispatch')
class QuizImageCreateView(CreateView):
    model = QuizImage
    template_name = "news/create.html"
    fields=['img']
    success_url=reverse_lazy('addquizimage')
