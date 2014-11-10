# encoding: utf-8
"""
Python module for reading/writing 9ML user layer files in XML format.

Functions
---------

    parse - read a 9ML file in XML format and parse it into a Model instance.

Classes
-------
    Model
    Definition
    BaseComponent
        SpikingNodeType
        SynapseType
        CurrentSourceType
        Structure
        ConnectionRule
        ConnectionType
        RandomDistribution
    Parameter
    PropertySet
    Value
    Network
    Population
    PositionList
    Projection
    Selection
    Operator
        Any
        All
        Not
        Comparison
        Eq
        In


:copyright: Copyright 2010-2013 by the Python lib9ML team, see AUTHORS.
:license: BSD-3, see LICENSE for details.
"""

import urllib
from lxml import etree
from .base import NINEML


from .dynamics import SpikingNodeType, SynapseType, CurrentSourceType
from .population import (Population, PositionList, Structure,
                         Operator, Any, All, Not, Comparison, Eq, In)
from .containers import Network, Selection, Concatenate
from .projection import Projection
from .random import RandomDistribution
from .components import (PropertySet, BaseComponent as Component, Reference,
                         Definition, Prototype, Quantity)
