#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the python-chess library.
# Copyright (C) 2012-2017 Niklas Fiekas <niklas.fiekas@backscattering.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import chess
import os
import setuptools
import sys
import platform


def read_description():
    """
    Reads the description from README.rst and substitutes mentions of the
    latest version with a concrete version number.
    """
    description = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

    # Link to the documentation of the specific version.
    description = description.replace(
        "//python-chess.readthedocs.io/en/latest/",
        "//python-chess.readthedocs.io/en/v{0}/".format(chess.__version__))

    # Use documentation badge for the specific version.
    description = description.replace(
        "//readthedocs.org/projects/python-chess/badge/?version=latest",
        "//readthedocs.org/projects/python-chess/badge/?version=v{0}".format(chess.__version__))

    # Show Travis CI build status of the concrete version.
    description = description.replace(
        "//travis-ci.org/niklasf/python-chess.svg?branch=master",
        "//travis-ci.org/niklasf/python-chess.svg?branch=v{0}".format(chess.__version__))

    return description


def dependencies():
    deps = []

    if sys.version_info < (2, 7):
        deps.append("backport_collections")

    return deps


def extra_dependencies():
    extras = {}

    if sys.version_info < (3, 2):
        extras["uci"] = ["futures"]
    else:
        extras["uci"] = []

    if platform.python_implementation() == "CPython":
        if sys.version_info < (3, 3):
            extras["gaviota"] = ["backports.lzma"]
        else:
            extras["gaviota"] = []

    extras["test"] = extras["uci"] + extras.get("gaviota", [])

    if sys.version_info < (2, 7):
        extras["test"].append("unittest2")

    if platform.python_implementation() == "CPython":
        extras["test"].append("spur")

    return extras


setuptools.setup(
    name="python-chess",
    version=chess.__version__,
    author=chess.__author__,
    author_email=chess.__email__,
    description=chess.__doc__.replace("\n", " ").strip(),
    long_description=read_description(),
    license="GPL3",
    keywords="chess fen pgn polyglot syzygy gaviota uci",
    url="https://github.com/niklasf/python-chess",
    packages=["chess"],
    test_suite="test",
    install_requires=dependencies(),
    extras_require=extra_dependencies(),
    tests_require=extra_dependencies().get("test"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Games/Entertainment :: Board Games",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
