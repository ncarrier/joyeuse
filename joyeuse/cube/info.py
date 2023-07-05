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
import json
import sys
import re


class Info(object):
    @staticmethod
    def __js_to_json(js_text):
        json_text = js_text.replace("var info = ", "")
        json_text = json_text.replace(";", "")
        json_text = json_text.replace("'", '"')

        json_text = re.sub(r"([^ ]*):", r'"\1":', json_text)

        return json_text

    def __init__(self, path):
        with open(path, "r") as f:
            js_text = f.read()
            json_text = Info.__js_to_json(js_text)
            self.__json = json.loads(json_text)

    @property
    def version(self):
        return self.__json['VERSION']

    @property
    def serial_number(self):
        return self.__json['SERIAL_NUMBER']

    @property
    def baby_mode(self):
        return self.__json['BABY_MODE'] == "Y"

    @property
    def legacy_hw(self):
        return self.__json['LEGACY_HW'] == "Y"

    @property
    def bilingual_mode(self):
        return self.__json['BILINGUAL_MODE'] == "Y"

    @property
    def locales(self):
        return [k.lower()
                for k in self.__json.keys()
                if len(k) == 2]

    @property
    def locale(self):
        for l in self.locales:
            if self.__json[l.upper()] == "Y":
                return l
        return "en"

    @property
    def international_mode(self):
        return self.__json['INTERNATIONAL_MODE'] == "Y"


if __name__ == '__main__':
    info = Info(sys.argv[1])

    print(
        f"version = {info.version}\n"
        f"serial_number = {info.serial_number}\n"
        f"baby_mode = {info.baby_mode}\n"
        f"legacy_hw = {info.legacy_hw}\n"
        f"bilingual_mode = {info.bilingual_mode}\n"
        f"locales = {info.locales}\n"
        f"locale = {info.locale}\n"
        f"international_mode = {info.international_mode}"
    )
