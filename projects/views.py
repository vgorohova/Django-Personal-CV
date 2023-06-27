from django.shortcuts import render
from django.http import Http404
# from django.template import loader
# from django.http import HttpResponse
from django.views import generic

from .models import Project

# Create your views here.
# def index(request):
    # return HttpResponse("Hello from the <b>projects</b> view!")
    
def index(request):
    projects_list = Project.objects.order_by("date_end")[:5]
    # template = loader.get_template("index.html")
    context = {
        "projects_list": projects_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "index.html", context)


# class DetailView(generic.DetailView):
#     model = Project
#     template_name = "detail.html"

def detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist!")
    
    context = {
        "project": project,
    }
    return render(request, "detail.html", context)