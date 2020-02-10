import os
import vlc
import time


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
    def __init__(self, fullscreen=True, wait=True):
        self._wait = wait
        self._instance = vlc.Instance()
        self._player = self._instance.media_player_new()
        self._player.set_fullscreen(fullscreen)
        # print(dir(self._player))

    def play(self, file_path):
        if os.path.exists(file_path):
            media = self._instance.media_new_path(file_path)
            media.get_mrl()
            self._player.set_media(media)
            self._player.play()
            if self._wait:
                time.sleep(1.5)
                duration = self._player.get_length() / 1000
                time.sleep(duration)
        else:
            raise Exception("File doesn't exist: '{}'".format(file_path))


if __name__ == "__main__":
    video = '/home/alex/Downloads/video.mov'
    VideoPlayer().play(video)
