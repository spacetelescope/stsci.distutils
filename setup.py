#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

from pkg_resources import working_set


# This is a workaround for http://bugs.python.org/setuptools/issue20; most
# packages that have this package as a setup-requirement also have d2to1 as
# a setup-requirement, which can lead to bugginess.
# See also http://mail.python.org/pipermail/distutils-sig/2011-May/017812.html
# for a description of the problem (in my example, package_A is d2to1 and
# package_B is stsci.distutils).

save_entries = working_set.entries[:]
save_entry_keys = working_set.entry_keys.copy()
save_by_key = working_set.by_key.copy()

try:
    setup(
        setup_requires=['d2to1'],
        d2to1=True,
        use_2to3=True
    )
finally:
    working_set.entries = save_entries
    working_set.entry_keys = save_entry_keys
    working_set.by_key = save_by_key
