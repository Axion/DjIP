# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.forms.models import ModelMultipleChoiceField
from django.forms.util import ValidationError
from django.forms.widgets import TextInput
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils.encoding import force_unicode
