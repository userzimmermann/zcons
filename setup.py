# This file was auto-generated by zetup
#
# https://bitbucket.org/userzimmermann/zetup.py



from __future__ import print_function

import sys
import os
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


SETUP_REQUIRES = [
  'zetup >= 0.2.31',
  
  ] + (os.path.exists('requirements.setup.txt')
       and [line for line in map(str.strip, open('requirements.setup.txt'))
            if line and not line.startswith('#')]
       or []) + [
  ]


try:
    from setuptools.dist import Distribution
    from pkg_resources import get_distribution, working_set, \
      DistributionNotFound, VersionConflict
except ImportError: # no setuptools
    pass
else:
    # make sure that setup requirements
    # are always correctly resolved and accessible by:
    # - pre-processing them one after another
    # - recursively resolving their runtime requirements
    # - moving any installed eggs to the front of sys.path
    # - updating pkg_resources.working_set accordingly

    installer = Distribution().fetch_build_egg

    # don't pollute stdout
    stdout = sys.__stdout__
    sys.stdout = sys.__stdout__ = sys.__stderr__

    def resolve(requirements, parent=None):
        for req in requirements:
            qualreq = parent and '%s->%s' % (req, parent) or req
            print("Resolving setup requirement %s:" % qualreq)
            try:
                dist = get_distribution(req)
                print(repr(dist))
            except (DistributionNotFound, VersionConflict):
                dist = installer(req)
                sys.path.insert(0, dist.location)
                working_set.entries.insert(0, dist.location)
                working_set.by_key[dist.key] = dist
            extras = re.match(r'[^#\[]*\[([^#\]]*)\]', req)
            if extras:
                extras = list(map(str.strip, extras.group(1).split(',')))
            resolve(map(str, dist.requires(extras=extras or ())), qualreq)

    resolve(SETUP_REQUIRES)
    sys.stdout = sys.__stdout__ = stdout


dist = setup(
  
  setup_requires=SETUP_REQUIRES,

  use_zetup=True,
  
  )