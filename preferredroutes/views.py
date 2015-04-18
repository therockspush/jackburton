from __future__ import absolute_import
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import *
import datetime
from django.views.generic import View, ListView
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import mechanize, urllib, re
from Link.models import Link
from django.template import Context, RequestContext
from .forms import RouteWXForm
from Link.models import Link

class HomePageView(ListView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        linklist = Link.objects.all()
        
        if linklist.count() > 3:
            firstlink = linklist[0]
            secondlink = linklist[1]
            thirdlink = linklist[2]
        else:
            firstlink = ''
            secondlink = ''
            thirdlink = ''
        
        
        template_name = 'home.html'
        context = {'firstlink':firstlink,'secondlink':secondlink,'thirdlink':thirdlink,}
        return render_to_response('home.html', context, context_instance=RequestContext(request))

class StoriesView(ListView):
    template_name = 'stories.html'

    def get(self, request, *args, **kwargs):
        a = Link.objects.all()
        if a.count > 3:
            therest = a[3:30]
        else:
            therest = ''
        template_name = 'stories.html'
        context = {'therest':therest,}
        return render_to_response('stories.html', context, context_instance=RequestContext(request))


class TracksView(ListView):
    template_name = 'tracks.html'
    
    

    def get(self, request, *args, **kwargs):
        url = 'https://www.notams.faa.gov/common/nat.html?'
        a = urllib.urlopen(url).read(200000)
        b = re.findall(r'<font\scolor="#\w+">\s\w+\s+\w+\s+.*?\)', str(a), re.DOTALL)
        track_list = []
        for c in b:
            track_list.append(c[22:])
        context = {'tracks':track_list,}
        return render_to_response('tracks.html', context, context_instance=RequestContext(request))


class StuffView(ListView):
    template_name = 'stuff.html'
    model = Link
    
    #def post(self, request, *args, **kwargs):
    #return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        response = HttpResponse()
        dep = request.GET['dep']
        arr = request.GET['arr']
        alt = request.GET['alt']
        
        taf_list = get_wx(dep, arr, alt)
        
        route = get_route(dep, arr)
        
        
        context = {'tafs':taf_list, 'routes':route, 'dep':dep.upper(), 'arr':arr.upper(),}
        return render_to_response('stuff.html', context, context_instance=RequestContext(request))


class RouteWXView(generic.TemplateView):
    form_class = RouteWXForm
    
    template_name = 'routewx.html'
'''
def routewx(request):
    template_name = 'home.html'
    
    def printwx(dep='', arr='', alt=''):
        urlprefix = 'http://www.aviationweather.gov/taf/data?ids='
        urlsuffix = '&format=raw'
        if alt == '':
            aptcodes = dep + '+' + arr
            taf_url = urlprefix + aptcodes + urlsuffix
        else:
            aptcodes = dep + '+' + arr + '+' + alt
            taf_url = urlprefix + aptcodes + urlsuffix

        c = urllib.urlopen(taf_url).read(200000)
        
        tafs = re.findall(r'<code>.*?</(?m)', str(c))
        return tafs

def routewx1(self, request, *args, **kwargs):
    self.object_list = self.get_queryset()
    response = HttpResponse()
    dep = request.GET['dep']
    arr = request.GET['arr']
    alt = request.GET['alt']
    
    context = {'dep': dep, 'arr': arr, 'alt': alt,}
    return render_to_response('stuff.html', context, context_instance=RequestContext(request))
'''

def get_wx(dep='', arr='', alt=''):
    urlprefix = 'http://www.aviationweather.gov/taf/data?ids='
    urlsuffix = '&format=raw'

    aptcodes = dep + '+' + arr + '+'
    taf_url = urlprefix + aptcodes + urlsuffix
    if alt:
        aptcodes_alt = aptcodes + '+' + alt
        taf_url = urlprefix + aptcodes_alt + urlsuffix

    c = urllib.urlopen(taf_url).read(200000)
    tafs = re.findall(r'<code>.*?</(?m)', str(c))
    taf_list = []
    for t in tafs:
        taf = re.sub('<br/>&nbsp;&nbsp;', ' ', t[6:-2])
        taf_list.append(taf)
    return taf_list

def get_route(dep='', arr=''):
    
    if dep.startswith('u') and arr.startswith('u'):
        route = ru_route(dep, arr)
    elif dep.startswith('k') or dep.startswith('c') or dep.startswith('m') or dep.startswith('t'):
        route = fa_route(dep, arr)
    elif dep.startswith('e') or dep.startswith('l'):
        route = eu_route(dep, arr)

    else:
        route = 'No Dice buddy'
    return route
    




        




def fa_route(dep, arr):
    fa_urlprefix = 'http://flightaware.com/analysis/route.rvt?origin='
    fa_urlsuffix = '&destination='
    routeurl = fa_urlprefix + dep + fa_urlsuffix + arr
    d = urllib.urlopen(routeurl).read(200000)
    route1 = re.search(r'FL\d\d\d.*?row2">.*?<', str(d), re.DOTALL)

    if route1 == None:
        route = 'Sorry Buddy'
    else:
        route2 = route1.group(0)
        route3 = re.search(r'">.*?<', str(route2))
        route = route3.group(0)[2:-1]



    return route

def ru_route(dep, arr):
    ru_urlprefix = 'https://infogate.matfmc.ru/ehtme/routes.htme?form-submit=FIRSForm.FIRSHtmlForm&fPntIn='
    ru_urlsuffix = '&fPntOut='
    ru_urlfinale = '&SearchBtn=+Search+'
    finalurl = ru_urlprefix + dep + ru_urlsuffix + arr + ru_urlfinale
    br = mechanize.Browser()
    a = br.open(finalurl)
    b = a.read()
    c = re.search(r'font></td><td\salign=center>.*?<', str(b), re.DOTALL)
    
    if c.group(0) == 'font></td><td align=center>&nbsp&nbsp<':
        route = 'Sorry Comrade'
    else:
        route = c.group(0)[27:-1]

    return route

def eu_route(dep, arr):
    one_day = datetime.timedelta(days=1)
    now = datetime.datetime.utcnow() + one_day
    date = now.strftime('%y%m%d')
    eu_part1 = 'https://www.eurofpl.eu/originalfpl/scripts/find_plist.php?o=289&d='


    eu_part2 = '&r=&rte=DCT&f='
    
    eu_part3 = '&t=1200&a='
    eu_part4 = '&u=F&l=300&vpts=&apts=&vspc=&aspc=&ffrz=&tfrz&tim=1427'
    

    finalurl = eu_part1 + date + eu_part2 + dep.upper() + eu_part3 + arr.upper() + eu_part4

    
    b = urllib.urlopen(finalurl)
    c = b.read()
    d = re.search(r'value=.*?"/>', str(c), re.DOTALL)

    if d == None:
        route = 'Scheize'
    else:
        route = d.group(0)[7:-3]

    return route







