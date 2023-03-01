import numpy as np
import cv2

import speech_recognition as sr

class Camera:
    device: cv2.VideoCapture

    def __init__(self, name, idx: int = 0, *args, **kwargs):
        self._name = name
        self.device = cv2.VideoCapture(idx)
    
    def read():
        pass

    def config():
        pass

    def is_rgb(self, n_samples = 3):
        frame = self.device.read()
        
        if len(frame.shape)==3 and frame.shape[2]==3:
            return True

        height, width, _ = frame.shape
        step_x, step_y = width//n_samples, height//n_samples
        x, y = width//(n_samples*2), height//(n_samples*2)
        xrange, yrange = np.arange(x, width, step_x), np.arange(y, height, step_y)
        if any(frame[xrange,yrange]!=0):
            return True
        try:
            return len(frame.shape)==3 and frame.shape[2]==3
        except IndexError:
            return False

        # self.device.read()

class Microphone:
    device: sr.Microphone()

cam = Camera()