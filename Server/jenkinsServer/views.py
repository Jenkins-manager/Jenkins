"""
    Jenkins server controller
"""

from django.shortcuts import render_to_response

def index(_):
    return render_to_response('index.html')
