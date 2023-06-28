#!/bin/bash
# shamelessly stolen and adapted from:
#  https://github.com/Mord3rca/gamma-launcher/blob/master/.github/scripts/release.sh

SCRIPT_NAME="${PWD}/joyeuse.py"
cat >"${SCRIPT_NAME}" <<EOF
import re
import sys
from joyeuse.__main__ import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
EOF

pyinstaller --noconsole \
	--paths . --onefile --name joyeuse \
	--exclude-module _bootlocale \
	--hidden-import=tkinter \
	"${SCRIPT_NAME}"

# quick check that the executable can at least show the help
./dist/joyeuse.exe --help

