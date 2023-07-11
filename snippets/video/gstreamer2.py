#!/usr/bin/env python3
import sys
import os

import tkinter

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject, GLib  # noqa E402

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


def quit_window(loop, player, window):
    stop_video(player)
    loop.quit()
    window.destroy()


def get_on_message(loop, player, window):
    def on_message(bus, message):
        if message.type == Gst.MessageType.EOS:
            print("eos")
            quit_window(loop, player, window)

    return on_message


def refresh(root):
    root.update()
    return True


Gst.init(None)
loop = GLib.MainLoop()

window = tkinter.Tk()
GLib.idle_add(lambda: refresh(window))
player = Gst.ElementFactory.make('playbin', None)
fullname = os.path.abspath(sys.argv[1])
window.protocol('WM_DELETE_WINDOW', lambda: quit_window(loop, player, window))

window.title("Example tk-gstreamer video player")
window.geometry('640x360')

display_frame = tkinter.Frame(window, bg='')
display_frame.place(relx=0, rely=0, anchor=tkinter.NW, relwidth=1, relheight=1)
frame_id = display_frame.winfo_id()

player.set_property('uri', 'file://%s' % fullname)
player.set_state(Gst.State.PLAYING)

bus = player.get_bus()
bus.add_signal_watch()
bus.enable_sync_message_emission()
bus.connect('sync-message::element', set_frame_handle, frame_id)
bus.connect('message', get_on_message(loop, player, window))

loop.run()
