# coding=utf-8
from django.views.generic.base import ContextMixin
# from catalog.models import Gensetengine
# from services.models import Service

# class GensetengineListMixin(ContextMixin):
# 	def get_context_data(self, **kwargs):
# 		context = super(GensetengineListMixin, self).get_context_data(**kwargs)
# 		context["gensetengines"] = Gensetengine.objects.all()
# 		context["services"] = Service.objects.all()

		# return context

class PageNumberMixin():
  def get_context_data(self, **kwargs):
    context = super(PageNumberMixin, self).get_context_data(**kwargs)
    try:
      context["pn"] = self.request.GET["page"]
    except KeyError:
      context["pn"] = "1"
    return context