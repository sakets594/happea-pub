from django import forms
# from betterforms.multiform import MultiModelForm
from .models import Question,Plot,Choice,Category


class PlotForm(forms.ModelForm):
    category    =   forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            queryset=Category.objects.all())
    class Meta:
        model = Plot
        fields = ('plot','category')


class ChoiceForm(forms.ModelForm):
    
    class Meta:
        model = Choice
        fields = ('question','choice','assessment')


QuizChoiceFormset=forms.inlineformset_factory(Plot,Choice,form=ChoiceForm,extra=4)



# class QuestionForm(forms.ModelForm):
    
#     class Meta:
#         model = Question
#         fields=('question',)


# class PlotForm(forms.ModelForm):
        
#     class Meta:
#         model = Plot
#         fields=('plot',)



# class ChoiceForm(forms.ModelForm):
    
#     class Meta:
#         model = Choice
#         fields=('choice','position')

# class QuizForm(MultiModelForm):
#     form_classes = {
#         'question': QuestionForm,
#         'plot': PlotForm,
#         'choice1':ChoiceForm,
#         'choice2':ChoiceForm,
        
#     }

