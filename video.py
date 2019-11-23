import cv2
import time
import numpy as np
from playsound import playsound
from concurrent.futures import ProcessPoolExecutor


def play_audio():
    playsound("/home/alex/Downloads/video.wav")


def play_video():
    video_path = "/home/alex/Downloads/video.mov"
    width, height = 1920, 1080

    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        start = time.time()
        ret, frame = cap.read()
        if isinstance(frame, type(None)):
            break

        image = np.zeros((height, width, 3), dtype=np.uint8)
        fh, fw, _ = frame.shape
        ws = int(width / 2 - fw / 2)
        hs = int(height / 2 - fh / 2)
        image[hs:hs + fh, ws:ws + fw, :] = frame

        cv2.namedWindow('window', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('window', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('window', image)

        duration = 33 - (time.time() - start)
        if cv2.waitKey(int(duration)) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def play_movie():
    executor = ProcessPoolExecutor(max_workers=2)
    audio_task = executor.submit(play_audio)
    video_task = executor.submit(play_video)


def do_nothing():
    time.sleep(20)


def main():
    executor = ProcessPoolExecutor(max_workers=2)
    task1 = executor.submit(play_movie)
    task2 = executor.submit(do_nothing)


if __name__ == '__main__':
    main()
