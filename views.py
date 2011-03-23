# -*- coding: utf-8 -*-
from django.utils import simplejson
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from catalog.api import CatalogJson
