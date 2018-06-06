class Effect(object):

    """An effect can be an action, a passive status modifier or any active or
    passive trait of an item."""

    def __init__(self, scope, mindmg, maxdmg, duration, element, 
            eff_range, status):
        """Define function of an Effect object.

        :scope: onemob, onegroup, onerow, allmobs
        :strength: base effect strength
        :duration: base effect duration in turns
        :element: physical, fire, water, earth, air, poison, life
        :eff_range: 0 - player selects row. 1 - first row. 2 - second row.
        :status: what status effect gained?

        """
        self.scope = scope
        self.mindmg = mindmg
        self.maxdmg = maxdmg
        self.duration = duration
        self.element = element
        self.eff_range = eff_range
        self.status = status
        self.enabled = True
