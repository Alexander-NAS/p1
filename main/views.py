from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Bike Store' 
        return context
    


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'О нас' 
        return context
