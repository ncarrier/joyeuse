import tkinter as tk
from tkVideoPlayer import TkinterVideo

root = tk.Tk()

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load("/home/nicolas/workspace/joyeuse/examples/copie/Secrets/Tutos vidéo/1-Allumer la Conteuse.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play() # play the video

root.mainloop()
