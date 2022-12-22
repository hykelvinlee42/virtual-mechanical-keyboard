import os
import sys
from enum import Enum

from pydub import AudioSegment


class Switch_Type(Enum):
    GX_BLUE = 1
    GX_BROWN = 2
    GX_RED = 3
    GL_CLICKY = 4
    GL_TACTILE = 5
    GL_LINEAR = 6
    RG_TACTILE = 7
    RG_LINEAR = 8
    

SWITCH_SOUND = {
    "GX_BLUE": "sound/gx-blue.mp3",
    "GX_BROWN": "sound/gx-brown.mp3",
    "GX_RED": "sound/gx-red.mp3",
    "GL_CLICKY": "sound/gl-clicky.mp3",
    "GL_TACTILE": "sound/gl-linear.mp3",
    "GL_LINEAR": "sound/gl-tactile.mp3",
    "RG_TACTILE": "sound/romer-g-linear.mp3",
    "RG_LINEAR": "sound/romer-g-tactile.mp3",
}

class Switch(object):
    def __init__(self, switch_type=Switch_Type.GX_BLUE):
        self.type = switch_type
        self.name = self.type.name

    def getsound(self):
        try:
            audio_segment = AudioSegment.from_mp3(SWITCH_SOUND[self.name])
        except FileNotFoundError:
            os.chdir(sys._MEIPASS)
            audio_segment = AudioSegment.from_mp3(SWITCH_SOUND[self.name])

        return audio_segment
