# This file is part of Joyeuse.

# Joyeuse is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Joyeuse is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Joyeuse. If not, see <https://www.gnu.org/licenses/>.
import os
from tkinter import Frame, Button, EW, NSEW

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject  # noqa E402

gi.require_version('GstVideo', '1.0')
from gi.repository import GstVideo  # noqa E402,F401


class TutorialsTab(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.grid_rowconfigure(0, weight=1)
        Gst.init(None)
        self.__player = None
        self.__gst = Gst.ElementFactory.make("playbin", "player")

        self.__player = Frame(self, bg='black')
        self.__wid = self.__player.winfo_id()

        bus = self.__gst.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect("message", self.__on_eos)
        bus.connect("sync-message::element", self.__set_frame_handle)

    def __on_eos(self, bus, message):
        if message.type == Gst.MessageType.EOS:
            self.stop_video()

    def __set_frame_handle(self, bus, message):
        structure = message.get_structure()
        if structure is not None:
            if structure.get_name() == 'prepare-window-handle':
                message.src.set_window_handle(self.__wid)

    def __get_video_handler(self, name):
        def video_handler():
            self.stop_video()
            self.__gst.set_property("uri", f"file:///{name}")
            self.__gst.set_state(Gst.State.PLAYING)
            self.__player.grid(
                column=0,
                row=0,
                sticky=NSEW,
                padx=(3, 3),
                pady=(3, 3)
            )

        return video_handler

    def stop_video(self):
        self.__gst.set_state(Gst.State.NULL)
        self.__gst.set_state(Gst.State.READY)
        self.__player.grid_forget()

    def load_cube_tutorials(self, tutorials):
        idx = 1
        for t in tutorials:
            name = os.path.basename(t)
            b = Button(self, text=name, command=self.__get_video_handler(t))
            b.grid(
                column=0,
                row=idx,
                sticky=EW,
                padx=(3, 3),
                pady=(3, 3)
            )
            idx += 1
        b = Button(self, text=f"▣ {_('Stop')}", command=self.stop_video)
        b.grid(
            column=0,
            row=idx,
            sticky=EW,
            padx=(3, 3),
            pady=(3, 3)
        )
