from django import forms

from .widgets import ListTextWidget

GOAL_CHOICES = [
    ('1', 'Think Positive'),
    ('2', 'Build Confidence'),
    ('3', 'Live Healthier'),
    ('4', 'Practise Meditation'),
    ('5', 'Decrease Anxiety'),
    ('6', 'Reduce Stress'),
    ('7', 'Improve Social Skills'),
]

MOOD_CHOICES = [
    ('great', 'Great!'),
    ('fine', 'Fine.'),
    ('okay', 'Okayish...'),
    ('sad', 'Sad :/'),
    ('awful', 'Awful ;_;'), 
]

ACTIVITY_CHOICES = [
    ('1', 'work'),
    ('2', 'relax'),
    ('3', 'friends'),
    ('4', 'sports'),
    ('5', 'party'),
    ('6', 'movies'),
    ('7', 'reading'),
    ('8', 'gaming'),
    ('9', 'shopping'),
    ('10', 'travel'),
    ('11', 'good meal'),
    ('12', 'sleeping'),
    ('13', 'social media'),
]

def validate_goal_count(value):
      count = len(value)
      if count > 3:
            raise forms.ValidationError(('Please select up to 3 goals'), params={'count': count},)

class GoalForm(forms.Form):
    goals = forms.MultipleChoiceField(required = True, choices = GOAL_CHOICES, 
            widget = forms.CheckboxSelectMultiple, validators = [validate_goal_count]) 

class MoodForm(forms.Form):
    mood = forms.CharField(widget = forms.RadioSelect(choices = MOOD_CHOICES), required = True)

class ActivityForm(forms.Form):
    activity = forms.MultipleChoiceField(required = True, choices = ACTIVITY_CHOICES, 
            widget = forms.CheckboxSelectMultiple) 


'''
   char_field_with_list = forms.CharField(required = True)

   def __init__(self, *args, **kwargs):
      _activity_list = kwargs.pop('ACTIVITY_LIST', None)
      super(ActivityForm, self).__init__(*args, **kwargs)

      self.fields['char_field_with_list'].widget = ListTextWidget(data_list=_activity_list, name='ACTIVITY_LIST')
'''
