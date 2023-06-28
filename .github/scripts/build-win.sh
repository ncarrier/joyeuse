#!/bin/bash
# shamelessly stolen and adapted from:
#  https://github.com/Mord3rca/gamma-launcher/blob/master/.github/scripts/release.sh

pyinstaller --noconsole \
	--paths . --onefile --name joyeuse \
	--exclude-module _bootlocale \
	--hidden-import=tkinter \
	--collect-submodules=pillow \
	"${PWD}/script/joyeuse.py"
