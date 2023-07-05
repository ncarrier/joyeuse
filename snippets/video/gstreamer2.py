import sys
import os

import tkinter

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject  # noqa E402

# Needed for set_window_handle():
gi.require_version('GstVideo', '1.0')
from gi.repository import GstVideo  # noqa E402,F401


def set_frame_handle(bus, message, frame_id):
    if not message.get_structure() is None:
        if message.get_structure().get_name() == 'prepare-window-handle':
            display_frame = message.src
            display_frame.set_property('force-aspect-ratio', True)
            display_frame.set_window_handle(frame_id)


window = tkinter.Tk()
window.title("Multiple videos in a column using Tk and GST 1.0")
window.geometry('480x960')

Gst.init(None)
GObject.threads_init()

display_frame = tkinter.Frame(window, bg='')
display_frame.place(relx=0, rely=0, anchor=tkinter.NW, relwidth=1, relheight=1)
frame_id = display_frame.winfo_id()

player = Gst.ElementFactory.make('playbin', None)
fullname = os.path.abspath(sys.argv[1])
player.set_property('uri', 'file://%s' % fullname)
player.set_state(Gst.State.PLAYING)

bus = player.get_bus()
bus.enable_sync_message_emission()
bus.connect('sync-message::element', set_frame_handle, frame_id)

window.mainloop()
