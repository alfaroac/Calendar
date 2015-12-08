from django import forms
from .models import CalendarEvent, Evidences
from django.utils.translation import ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets  
CSS_CLASS_CHOICES = (
        ('', _('Seleccione prioridad')),
        ('event-warning', _('Advertencia')),
        ('event-info', _('Informativo')),
        ('event-success', _('Satisfactorio')),
        ('event-inverse', _('Inverso')),
        ('event-special', _('Especial')),
        ('event-important', _('Importante')),
    )
    
class EventForm(forms.ModelForm):
	css_class = forms.ChoiceField(CSS_CLASS_CHOICES)
	class Meta:
		model=CalendarEvent
		fields = ['title', 'url', 'css_class','start','end','place','description','users']
		exclude=()
		widgets={
		'title':forms.TextInput(attrs={'class':'form-control col-md-6','placeholder':'Ingrese titulo del evento'}),
		'url':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese (#), o url de pagina web'}),
		'place':forms.TextInput(attrs={'class':'form-control','placeholder':'Lugar del evento'}),
		'description':forms.Textarea(attrs={'class':'form-control'}),
		'users':forms.CheckboxSelectMultiple(),
		}

	def __init__(self, *args, **kwargs):
		super(EventForm, self).__init__(*args, **kwargs)
		self.fields['start'].widget = widgets.AdminSplitDateTime()
		self.fields['end'].widget = widgets.AdminSplitDateTime()

class EvidenceForm(forms.ModelForm):
	class Meta:
		model=Evidences
		exclude=()
		widgets={
		'title':forms.TextInput(attrs={'class':'form-control'}),
		'description':forms.TextInput(attrs={'class':'form-control'}),
		'fileEvidence':forms.FileInput(attrs={'class':'btn btn-warning'}), 
		}