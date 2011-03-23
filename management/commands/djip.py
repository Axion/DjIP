# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
import pkg_resources

from optparse import make_option
from django.core.management.base import BaseCommand, LabelCommand, CommandError
from django.conf import settings
from django.db import connection as conn


class Command(LabelCommand):
    args = ""
    label = " sdvsd "
    help = ""
    can_import_settings = True
    """
    option_list = BaseCommand.option_list + (
        make_option('--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete poll instead of closing it'),
        )
    """

    def info(self, **options):
        from djip import get_version
        from pip.commands.search import transform_hits, print_results
        from pip.util import get_installed_distributions

        import xmlrpclib

        pypi = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')

        print "DjIP version %s\n" % get_version()

        for p in get_installed_distributions():
            hits = pypi.search({'name': p.project_name, 'summary': p.project_name}, 'or')
            hits = transform_hits(hits)
            self.print_results(hits)

    def not_implemented(self, **options):
        raise CommandError('Enter at least one %s.' % self.label)

    def print_results(self, hits):
        from pip.commands.search import highest_version
        installed_packages = [p.project_name for p in pkg_resources.working_set]
        for hit in hits:
            name = hit['name']
            summary = hit['summary'] or ''
            try:
                if name in installed_packages:
                    print name,
                    dist = pkg_resources.get_distribution(name)
                    try:
                        latest = highest_version(hit['versions'])
                        if dist.version == latest:
                            print 'version: %s (latest)' % dist.version
                        else:
                            print 'version: %s, LATEST %s' % (dist.version, latest)
                    finally:
                        pass
            except UnicodeEncodeError:
                pass

    def handle_label(self, label, **options):
        os.system(['clear','cls'][os.name == 'nt'])

        try:
            import pip
        except ImportError:
            raise CommandError("Can't import PIP")

        from pip.util import in_venv
        if not in_venv():
            raise CommandError("Can be run only in virtualenv")
        
        getattr(self, label, self.not_implemented)(**options)