from django import forms
from bulletin.models import Comment, Feedback, Event



class CommentForm(forms.ModelForm):
	"""Form Comentario"""
	class Meta:
		model = Comment
		fields = ['comment']
		widgets = {
            'comment': forms.TextInput(attrs={
                'id': 'post-text', 
                'required': True, 
                'placeholder': 'Escribe un Comentario...'
            }),
        }

class FeedbackForm(forms.ModelForm):
	"""Form para Feedsback"""
	class Meta:
		model = Feedback
		fields = ['title', 'text']

class EventForm(forms.ModelForm):
	"""Form para Admin de eventos para poder ver el input de colores"""

	class Meta:
		model = Event
		fields = '__all__'
		widgets = {
			'backgroundColor' : forms.TextInput(attrs={
				'type' : 'color'
				}),
			'start_date' : forms.TextInput(attrs={
				'class' : 'datepicker'
				}),
			'start_time' : forms.TextInput(attrs={
				'class' : 'timepicker'
				}),
			'end_date' : forms.TextInput(attrs={
				'class' : 'datepicker'
				}),
			'end_time' : forms.TextInput(attrs={
				'class' : 'timepicker'
				})
		}

			
