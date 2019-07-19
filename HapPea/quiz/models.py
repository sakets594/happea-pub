from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
# Create your models here.
from users.choices import AGEGROUP_CHOICES

class Plot(models.Model):
    plot=models.CharField(max_length=1000)
    category =   models.ManyToManyField("quiz.Category", verbose_name="category")

    def __str__(self):
        return self.plot
    
    

class Question(models.Model):
    question = models.CharField(max_length=500)
    plot=models.OneToOneField("quiz.Plot", verbose_name="plot", on_delete=models.CASCADE)



class Category(models.Model):

    name    =   models.CharField( max_length=50)
    age     =   models.IntegerField(choices=AGEGROUP_CHOICES,default=0)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")





class Choice(models.Model):
    question = models.ForeignKey("Plot", related_name="choices",on_delete=models.CASCADE)
    choice = models.CharField("Choice", max_length=200)
    # position = models.IntegerField("position",blank=True)
    assessment=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])


    # class Meta:
    #     # unique_together = [
    #     #     # no duplicated choice per question
    #     #     ("question", "choice"), 
    #     #     # no duplicated position per question 
    #     #     ("question", "position") 
    #     # ]
    #     ordering = ("position",)

# class Questionaire(models.Mmodel):
#     starttime=models.TimeField(_("start"), auto_now=False, auto_now_add=True)
#     user=models.ForeignKey("users.CustomUser", verbose_name=_("user"), on_delete=models.CASCADE)
#     questions=models.ManyToManyField("quiz.Plot", verbose_name=_("stories"))


 
# class Questionnaire(models.Model):
#     # name = models.CharField(max_length=255)
# 	# A questionnaire can have many questions. 
# 	# A question can be part of many questionnaires.
#     plots = models.ManyToManyField(Plot)
 
 
# class Question(models.Model):
#     prompt = models.CharField(max_length=255)
# 	# A question can have many response options.
# 	# A response option can be part of many questions.
#     response_options = models.ManyToManyField(ResponseOption)
 
 
class ResponseOption(models.Model):
    choice=models.ForeignKey(Choice, on_delete=models.CASCADE,null=True,blank=True)
    time=models.FloatField()


class UserQuestionnaire(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)
    score=models.IntegerField(null=True,blank=True)
    starttime=models.DateTimeField( auto_now=False, auto_now_add=True)
    class Meta:
        ordering = ['id',]
 
 
class UserResponse(models.Model):
    user_questionnaire = models.ForeignKey(UserQuestionnaire,on_delete=models.CASCADE)
    plot = models.ForeignKey(Plot,on_delete=models.CASCADE)
    response_option = models.ForeignKey(ResponseOption,on_delete=models.CASCADE) 




class News(models.Model):
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to = 'news/')
    description=models.CharField(max_length=500)
    url=models.URLField( max_length=200)
    class Meta:
            ordering = ['id',]
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('newslist')


from django.db.models.aggregates import Count
from random import randint

class QuizImageRandomManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

class QuizImage(models.Model):
    img=models.ImageField(upload_to = 'quizimages/')
    objects=QuizImageRandomManager()


    


    

    