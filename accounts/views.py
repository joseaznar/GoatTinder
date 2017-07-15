# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
# here comes all de logic 
def home (request):
	#querys
	numbers =[1,2,3,4,5]
	name='Carlos Bárcena'

	args={'myName':name, 'numbers':numbers} # dictionary object
	return render (request,'accounts/home.html', args)
