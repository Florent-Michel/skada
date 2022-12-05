# -*- coding: utf-8 -*-
"""
Domain Adaptation estimators

"""
# Author: Remi Flamary <remi.flamary@polytechnique.edu>
#         Alexandre Gramfort <firstname.lastname@inria.fr>
#
# License: BSD 3-Clause
try:
    from . import feature
except ImportError:
    print("Torch and skorch are required to use feature's based methods.")

from ._reweight import (
    ReweightDensity, GaussianReweightDensity, DiscriminatorReweightDensity
)
from ._subspace import SubspaceAlignment, TransferComponentAnalysis

from ._mapping import (
    OTmapping, EntropicOTmapping, ClassRegularizerOTmapping, LinearOTmapping
)

from ._mapping import CORAL

__all__ = [
    "feature",
    "ReweightDensity",
    "GaussianReweightDensity",
    "DiscriminatorReweightDensity",
    "SubspaceAlignment",
    "TransferComponentAnalysis",
    "OTmapping",
    "EntropicOTmapping",
    "ClassRegularizerOTmapping",
    "LinearOTmapping",
    "CORAL"
]
