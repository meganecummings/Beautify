# payments/views.py
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.pk_test_ZNASggyuMPivZNtUeAVSRigy00Ksb2rkKa
        return context