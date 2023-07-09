#!/usr/bin/env python3
import sys
import os

import tkinter

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject  # noqa E402

gi.require_version('GstVideo', '1.0')
from gi.repository import GstVideo  # noqa E402,F401


def stop_video(gst):
    gst.set_state(Gst.State.NULL)
    gst.set_state(Gst.State.READY)


def set_frame_handle(bus, message, frame_id):
    structure = message.get_structure()
    if structure is not None:
        if structure.get_name() == 'prepare-window-handle':
            display_frame = message.src
            display_frame.set_property('force-aspect-ratio', True)
            display_frame.set_window_handle(frame_id)


def quit_window(player, window):
    stop_video(player)
    window.destroy()


def on_message(bus, message):
    # TODO doesn't work
    print("on message")
    t = message.type
    if t == Gst.MessageType.EOS:
        print("eos")


Gst.init(None)

window = tkinter.Tk()
player = Gst.ElementFactory.make('playbin', None)
fullname = os.path.abspath(sys.argv[1])
window.protocol('WM_DELETE_WINDOW', lambda: quit_window(player, window))

window.title("Example tk-gstreamer video player")
window.geometry('640x360')

display_frame = tkinter.Frame(window, bg='')
display_frame.place(relx=0, rely=0, anchor=tkinter.NW, relwidth=1, relheight=1)
frame_id = display_frame.winfo_id()

player.set_property('uri', 'file://%s' % fullname)
player.set_state(Gst.State.PLAYING)

bus = player.get_bus()
bus.enable_sync_message_emission()
bus.connect('sync-message::element', set_frame_handle, frame_id)
bus.connect('message', on_message)

window.mainloop()
