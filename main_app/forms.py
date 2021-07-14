from django.forms import ModelForm
from .models import Proposal, Activity

class ProposalForm(ModelForm):
  class Meta:
    model = Proposal
    fields = ['suggestion', 'location']