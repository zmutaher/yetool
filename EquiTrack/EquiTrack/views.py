__author__ = 'jcranwellward'

from django.views.generic import TemplateView

from registration.backends.default.views import RegistrationView

from partners.models import PCA
from reports.models import Sector, ResultStructure

from .forms import UnicefEmailRegistrationForm


class DashboardView(TemplateView):

    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):

        sectors = {}
        sructure = self.request.GET.get('structure', 1)
        current_structure = ResultStructure.objects.get(id=sructure)
        for sector in Sector.objects.all():
            indicators = sector.indicator_set.filter(
                view_on_dashboard=True,
                result_structure=current_structure
            )
            if not indicators:
                continue
            sectors[sector.name] = [
                indicator for indicator in indicators
            ]

        return {
            'sectors': sectors,
            'current_structure': current_structure,
            'structures': ResultStructure.objects.all(),
            'pcas': {
                'active': PCA.objects.filter(
                    status=PCA.ACTIVE,
                    amendment_number=0,
                ).count(),
                'implemented': PCA.objects.filter(
                    status=PCA.IMPLEMENTED,
                    amendment_number=0,
                ).count(),
                'in_process': PCA.objects.filter(
                    status=PCA.IN_PROCESS,
                    amendment_number=0,
                ).count(),
                'cancelled': PCA.objects.filter(
                    status=PCA.CANCELLED,
                    amendment_number=0,
                ).count(),
            }
        }


class MapView(TemplateView):

    template_name = 'map.html'


class EquiTrackRegistrationView(RegistrationView):

    form_class = UnicefEmailRegistrationForm

    def register(self, request, send_email=True, **cleaned_data):
        """
        We override the register method to disable email sending
        """
        send_email = False

        return super(EquiTrackRegistrationView, self).register(
            request, send_email, **cleaned_data
        )