import os
import sys
from enum import Enum

from pydub import AudioSegment


class Switch_Type(Enum):
    LOGITECHG_GX_BLUE = 1
    LOGITECHG_GX_BROWN = 2
    LOGITECHG_GX_RED = 3
    LOGITECHG_GL_CLICKY = 4
    LOGITECHG_GL_TACTILE = 5
    LOGITECHG_GL_LINEAR = 6
    LOGITECHG_RG_TACTILE = 7
    LOGITECHG_RG_LINEAR = 8
    CHERRY_MX_BLUE = 9
    CHERRY_MX_BROWN = 10
    CHERRY_MX_RED = 11
    CHERRY_MX_BLACK = 12
    CHERRY_MX_SLIENT_RED = 13
    CHERRY_MX_SLIENT_BLACK = 14
    CHERRY_MX_SPEED_SILVER = 15
    

SWITCH_SOUND = {
    "LOGITECHG_GX_BLUE": "sound/gx-blue.mp3",
    "LOGITECHG_GX_BROWN": "sound/gx-brown.mp3",
    "LOGITECHG_GX_RED": "sound/gx-red.mp3",
    "LOGITECHG_GL_CLICKY": "sound/gl-clicky.mp3",
    "LOGITECHG_GL_TACTILE": "sound/gl-linear.mp3",
    "LOGITECHG_GL_LINEAR": "sound/gl-tactile.mp3",
    "LOGITECHG_RG_TACTILE": "sound/romer-g-linear.mp3",
    "LOGITECHG_RG_LINEAR": "sound/romer-g-tactile.mp3",
    "CHERRY_MX_BLUE": "sound/mx-blue.mp3",
    "CHERRY_MX_BROWN": "sound/mx-brown.mp3",
    "CHERRY_MX_RED": "sound/mx-red.mp3",
    "CHERRY_MX_BLACK": "sound/mx-black.mp3",
    "CHERRY_MX_SLIENT_RED": "sound/mx-slient-red.mp3",
    "CHERRY_MX_SLIENT_BLACK": "sound/mx-slient-black.mp3",
    "CHERRY_MX_SPEED_SILVER": "sound/mx-speed-silver.mp3",
}

class Switch(object):
    def __init__(self, switch_type=Switch_Type.LOGITECHG_GX_BLUE):
        self.type = switch_type
        self.name = self.type.name

    def getsound(self):
        try:
            audio_segment = AudioSegment.from_file(SWITCH_SOUND[self.name], duration=0.5)
        except FileNotFoundError:
            os.chdir(sys._MEIPASS)
            audio_segment = AudioSegment.from_file(SWITCH_SOUND[self.name], duration=0.5)

        return audio_segment
