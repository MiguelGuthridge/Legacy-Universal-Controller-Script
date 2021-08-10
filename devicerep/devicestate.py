"""devicestate.py

Contains class representing the state of a device. Contains the list of
control sets, which themselves contain controls.

WARNING: DO NOT INHERIT FROM THIS CLASS. Instead create a wrapper class derived
from CLASSNAME that adds properties to an instance of this class. That way,
the management of device controls can be abstracted away, and can be
improved upon without breaking derived device implementations
"""

from .controlsurface import ControlSurface
from .controlmapping import ControlMapping

class DeviceState:
    """Represents the current state of a controller
    """
    
    def __init__(self) -> None:
        self._control_sets = []
    
    def addControlSet(self, name: str) -> int:
        """Add a control set to the device. This is used to group controls into
        logical sets (eg faders, drum pads etc)

        Args:
            name (str): name of the new control set

        Returns:
            int: control set index
        """
        self._control_sets.append(ControlSet(name))
        return len(self._control_sets) - 1
    
    def addControl(self, set: int, control: ControlSurface) -> ControlMapping:
        """Adds a control to a control set

        Args:
            set (int): set ID
            control (ControlSurface): control to add

        Returns:
            ControlMapping: mapping where the control was inserted
        """
        return self._control_sets[set].addControl(control)
