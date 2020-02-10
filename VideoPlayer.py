import cv2
import numpy as np
from playsound import playsound
import os
import vlc


video_mapping = {
    '11': 'data/it/video1.mov',
    '12': 'data/it/video2.mov',
    '13': 'data/it/video3.mov',

    '21': 'data/de/video1.mov',
    '22': 'data/de/video2.mov',
    '23': 'data/de/video3.mov',

    '31': 'data/en/video1.mov',
    '32': 'data/en/video2.mov',
    '33': 'data/en/video3.mov',

    'idle': ''
}


class VideoPlayer:
    def __init__(self, fullscreen=True):
        self._instance = vlc.Instance()
        self._player = self._instance.media_player_new()
        self._player.set_fullscreen(fullscreen)

    def play(self, file_path):
        if os.path.exists(file_path):
            media = self._instance.media_new_path(file_path)
            media.get_mrl()
            self._player.set_media(media)
            self._player.play()
        else:
            raise Exception("File doesn't exist: '{}'".format(file_path))


"""
Media = Instance.media_new_path('/home/alex/Downloads/video.mov')
Media.get_mrl()
player.set_media(Media)
player.play()

Media = Instance.media_new_path('/home/alex/Downloads/video2.mp4')
Media.get_mrl()
player.set_media(Media)
player.play()
"""
