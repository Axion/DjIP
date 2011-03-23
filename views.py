# -*- coding: utf-8 -*-
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.cache import never_cache
from django.utils import simplejson
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

@staff_member_required
@never_cache
def browse(request):
    import pkg_resources
    from pip.commands.search import highest_version, transform_hits
    from pip.util import get_installed_distributions

    import xmlrpclib

    pypi = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')
    installed_packages = [p.project_name for p in pkg_resources.working_set]

    results = []
    for p in get_installed_distributions():
        result = {}
        hits = pypi.search({'name': p.project_name, 'summary': p.project_name}, 'or')
        hits = transform_hits(hits)
        for hit in hits:
            try:
                if hit['name'] in installed_packages:
                    dist = pkg_resources.get_distribution(hit['name'])
                    result['name'] = hit['name']
                    result['version'] = dist.version
                    result['summary'] = hit['summary'] or ''
                    try:
                        result['latest'] = highest_version(hit['versions'])
                    finally:
                        results.append(result)
            except UnicodeEncodeError:
                pass


    query = request.GET.copy()

    return render_to_response('djip/index.html', {
        'results': results,
        #'dir': path,
        #'p': p,
        #'q': q,
        #'page': page,
        #'results_var': results_var,
        #'counter': counter,
        'query': query,
        'title': _(u'PIP browser'),
        #'settings_var': get_settings_var(),
        #'breadcrumbs': get_breadcrumbs(query, path),
        'breadcrumbs_title': ""
    }, context_instance=RequestContext(request))

@staff_member_required
@never_cache
def update_all(request):
    return render_to_response('djip/update_all.html', {

    }, context_instance=RequestContext(request))