from django.shortcuts import render, redirect
from interface.models import Animation, Option
from django.views import generic
import sys

# Create your views here.

class IndexView(generic.ListView):
    model = Animation
    template_name='interface/index.html'

class AnimationBuilderView(generic.DetailView):
    model = Animation
    template_name = 'interface/animation_builder.html'

def format_color_list(color_list):
    joined_list = ','.join(color_list)
    return "("+joined_list+")"
def build(request):
    exec_args = []
    for key, value in request.POST.iteritems():
        if "csrf" in key:
            continue
        elif "colors" in key:
            exec_args.append("--colors="+format_color_list(request.POST.getlist('colors[]'))+" ")
        else:
            exec_args.append("--"+key+"="+value+" ")
    print " ".join(exec_args)
    return redirect('/interface')