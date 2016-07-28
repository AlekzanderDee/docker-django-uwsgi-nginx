from django.views.generic import TemplateView

import sys

class HelloView(TemplateView):
    template_name = 'website/hello.html'

    def get(self, request):
        return self.render_to_response({"python_version": sys.version_info[0]})
