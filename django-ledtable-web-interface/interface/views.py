from django.shortcuts import render, redirect
from interface.models import Animation, Option
from django.views import generic
import sys
import os

# Create your views here.

class IndexView(generic.ListView):
    model = Animation
    template_name='interface/index.html'

class AnimationBuilderView(generic.DetailView):
    model = Animation
    template_name = 'interface/animation_builder.html'

def format_color_list(color_list):
    joined_list = ','.join(color_list)
    return "\"["+joined_list+"]\""

def build(request):
    exec_args = []
    for key, value in request.POST.iteritems():
        if "csrf" in key:
            continue
        elif "colors" in key:
            exec_args.append("--colors="+format_color_list(request.POST.getlist('colors[]'))+" ")
        elif "color" in key:
	    exec_args.append("--color=\""+value+"\" ")
	else:
            exec_args.append("--"+key+"="+value+" ")
    os.system("python /home/pi/lights/LEDTable/animate_strip/animate_strip.py "+" ".join(exec_args))
    return redirect('/interface')
