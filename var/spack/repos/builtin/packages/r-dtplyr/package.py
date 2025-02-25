# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RDtplyr(RPackage):
    """Data Table Back-End for 'dplyr'.

    Provides a data.table backend for 'dplyr'. The goal of 'dtplyr' is to allow
    you to write 'dplyr' code that is automatically translated to the
    equivalent, but usually much faster, data.table code."""

    cran = "dtplyr"

    version('1.2.1', sha256='2640e9cde4eaa06f02cff29e3f2b99fdd08488df07ea2e6629b2ed6a8285d0f3')
    version('1.2.0', sha256='a6dedfb6dd80dfc1d29d005ab634c060b7bfda8cb49835ece84d3b7d12077414')
    version('1.1.0', sha256='99681b7285d7d5086e5595ca6bbeebf7f4e2ee358a32b694cd9d35916cdfc732')

    depends_on('r@3.3:', type=('build', 'run'))
    depends_on('r-crayon', type=('build', 'run'))
    depends_on('r-data-table@1.12.4:', type=('build', 'run'))
    depends_on('r-data-table@1.13.0:', type=('build', 'run'), when='@1.2.0:')
    depends_on('r-dplyr@1.0.3:', type=('build', 'run'))
    depends_on('r-ellipsis', type=('build', 'run'))
    depends_on('r-glue', type=('build', 'run'))
    depends_on('r-lifecycle', type=('build', 'run'))
    depends_on('r-rlang', type=('build', 'run'))
    depends_on('r-tibble', type=('build', 'run'))
    depends_on('r-tidyselect', type=('build', 'run'))
    depends_on('r-vctrs', type=('build', 'run'))
