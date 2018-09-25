"""jenkinsServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from questions.views import get_questions, send_question
from answers.views import get_answer
from users.views import send_username
from jenkinsServer.views import index
from jenkinsServer import views

# from questions.views import get_questions

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('home/',index),
    url('get_questions/', get_questions),
    url('send_question/', send_question),
    url('get_answer/', get_answer),
    url('send_username/', send_username)
]
