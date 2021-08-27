"""transport_buttons.py

Control definitions for transport buttons

Author: Miguel Guthridge
"""

from . import Button

class TransportButton(Button):
    """Generic transport button
    """

class MenuButton(TransportButton):
    """Button used to active the script's menu
    """

class PlayPauseButton(TransportButton):
    """Play/Pause control button
    """

class StopButton(TransportButton):
    """Stop control button
    """

class JogButton(TransportButton):
    """Fast-forward and rewind buttons
    """

class FastForwardButton(JogButton):
    """Fast forward control button
    """

class RewindButton(JogButton):
    """Rewind control button
    """

class LoopButton(TransportButton):
    """Loop control button
    """

class RecordButton(TransportButton):
    """Record button
    """

class TrackButton(TransportButton):
    """Generic track navigation button
    """

class NextTrackButton(TrackButton):
    """Next track
    """

class PrevTrackButton(TrackButton):
    """Previous track
    """
