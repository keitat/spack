# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RRunit(RPackage):
    """R Unit Test Framework.

    R functions implementing a standard Unit Testing framework, with additional
    code inspection and report generation tools. """

    cran = "RUnit"

    version('0.4.32', sha256='23a393059989000734898685d0d5509ece219879713eb09083f7707f167f81f1')

    depends_on('r@2.5.0:', type=('build', 'run'))
