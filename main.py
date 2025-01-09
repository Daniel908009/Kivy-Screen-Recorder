from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup



# this is a test script to record the screen, it still has some problems so I am looking into it
import subprocess
import time
test_command = [
    "ffmpeg",
    "-f", "x11grab",
    "-video_size", "1920x1080",
    "-framerate", "25",
    "-i", ":0.0+0.0",
    "output.mp4"
]
proces = subprocess.Popen(test_command)
time.sleep(10)
proces.terminate()
print("recording stopped")



class MainGrid(GridLayout):
    def startRecording(self):
        pass


class RecorderApp(App):
    def build(self):
        return MainGrid()

#if __name__ == "__main__":
#    RecorderApp().run()