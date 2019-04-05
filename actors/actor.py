#!/usr/bin/env python3

""" New version started April 1st 2019. This version will make several
important changes, including the removal of all print() calls and a focus on
more "pure" functions.

If determined not to be overly difficult, removal of numpy will be attempted.
All YAML functions will be pulled into a separate module.

"Actor" objects will now encompass all player characters and monsters/NPCs.
"""

from numpy import random, linspace


class Actor(object):

    """Define an acting character. Includes player characters, mobs, NPCs.


    """

    def __init__(self):
        """Initialize all base characteristics. """
        pass
