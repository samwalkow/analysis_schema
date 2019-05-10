# -*- coding: utf-8 -*-

"""Top-level package for Analysis Schema."""

__author__ = """Matthew Turk"""
__email__ = 'matthewturk@gmail.com'
__version__ = '0.1.0'

from .data_objects import (
    Sphere,
    Region,
    AllData,
    DataSource,
)

from .operations import (
    Average,
    Sum,
    Minimum,
    Maximum,
    Integrate,
    operations,
)

from .products import (
    Projection,
)

from .quantities import (
    UnitfulValue,
    UnitfulArray,
    unyt_array_model,
    Coordinate,
    Vector,
    Path,
)
