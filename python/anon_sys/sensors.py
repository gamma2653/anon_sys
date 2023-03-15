import numpy as np
import cv2

import speech_recognition as sr

from anon_sys.system import Sensor

class CV2Camera(Sensor):
    device: cv2.VideoCapture

    def __init__(self, name, idx: int = 0, *args, **kwargs):
        self._name = name
        self.device = cv2.VideoCapture(idx)
        self._config = {}
    def read(self) -> np.ndarray:
        pass

    def config(self, kv_map={}, **kwargs):
        self._config.update(kv_map, **kwargs)

    def is_rgb(self, n_samples = 3):
        frame = self.device.read()
        
        if len(frame.shape)==3 and frame.shape[2]==3:
            return True

        height, width, _ = frame.shape
        step_x, step_y = int(width/n_samples), int(height/n_samples)
        x, y = int(width/(n_samples*2)), int(height/(n_samples*2))
        xrange, yrange = np.arange(x, width, step_x), np.arange(y, height, step_y)
        if any(frame[xrange,yrange]!=0):
            return True
        try:
            return len(frame.shape)==3 and frame.shape[2]==3
        except IndexError:
            return False
        start_x = x
        for _ in range(n_samples):
            for _ in range(n_samples):
                pixel = frame[x,y]
                if len(pixel) != 3 or pixel[:]:
                    return False
                x+=step_x
            x = start_x
            y+=step_y
        
        


        print(frame)
        # self.device.read()

class SRMicrophone(Sensor):
    device: sr.Microphone()
