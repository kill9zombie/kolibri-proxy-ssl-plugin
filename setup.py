#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import logging
from setuptools import setup
import kolibri_proxy_ssl_plugin


dist_name = 'kolibri_proxy_ssl_plugin'


# Default description of the distributed package
description = (
    """Kolibri plugin to set the SECURE_PROXY_SSL_HEADER django setting"""
)


def enable_log_to_stdout(logname):
    """Given a log name, outputs > INFO to stdout."""
    log = logging.getLogger(logname)
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    log.addHandler(ch)


long_description = """
`Kolibri <https://learningequality.org/kolibri/>`_ is the offline learning platform
from `Learning Equality <https://learningequality.org/>`_.

The `X-Forwarded-Proto` HTTP header can be set by upstream proxies that are doing SSL/TLS encryption and decryption.  By setting this header the proxy can signal to the Django app that links should be built with the https protocol.

This plugin will tell Kolibri to trust the upstream proxy to set the `X-Forwarded-Proto` header.  Please, do not use this module if you do not trust the upstream proxy to set this header for you.
"""

setup(
    name=dist_name,
    version=kolibri_proxy_ssl_plugin.__version__,
    description=description,
    long_description=long_description,
    author='Phil Helliwell',
    author_email='phil.helliwell@neon.me.uk',
    url='https://github.com/kill9zombie/kolibri-proxy-ssl-plugin',
    packages=[
        str('kolibri_proxy_ssl_plugin'),  # https://github.com/pypa/setuptools/pull/597
    ],
    entry_points={
        "kolibri.plugins": "kolibri_proxy_ssl_plugin = kolibri_proxy_ssl_plugin",
    },
    package_dir={'kolibri_proxy_ssl_plugin': 'kolibri_proxy_ssl_plugin'},
    include_package_data=True,
    license='MIT',
    install_requires=[],
    extras_require={
        'dev': [
            'setuptools',
            'wheel',
            'twine',
        ]
    },
    zip_safe=False,
    keywords='kolibri',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Education :: Computer Aided Instruction (CAI)',
        'Topic :: System :: Systems Administration :: Authentication/Directory'
    ],
)
