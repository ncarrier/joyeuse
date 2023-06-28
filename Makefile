version := $(shell python3 -c "import joyeuse.__version__ as v; print(v.__version__)")
# strip any suffix, such as -alphaX, as deb file names don't have it
version_stripped := $(shell echo $(version) | sed 's/[abr].*//g')
SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -ec
python_version := 3.9.9

.PHONY: all
all: debian pip windows

.PHONY: pip
pip:
	python3 setup.py sdist

.PHONY: debian
debian:
	debuild -uc -us

windows:
	set -x
	PREFIX=$$(mktemp -d)
	echo "building in temporary directory $${PREFIX}"
	# Here we want to create a wine prefix, but we want it to happen in
	# headless mode. For that, we execute a dummy windows command (ping)
	# but take care of unsetting the DISPLAY variable to force wine to not
	# attempt to interact with us
	export WINEPREFIX=$${PREFIX}
	unset DISPLAY
	rm -rf $${PREFIX}
	mkdir -p $${PREFIX}
	#export WINEDEBUG=err-all,warn-all,fixme-all,trace-all
	wine ping > /dev/null || true
	winetricks win10

	# now we install python, this time, having a seemingly working DISPLAY
	# is mandatory (don't ask me why) so we create a dummy one using Xvfb
	echo "install python $(python_version)"
	wget --directory-prefix=$${PREFIX} \
		https://www.python.org/ftp/python/$(python_version)/python-$(python_version).exe
	: $${BUILD_NUMBER:=99}
	export DISPLAY=:$$((BUILD_NUMBER % 10000))
	Xvfb -ac $${DISPLAY} > /dev/null 2>&1 &
	trap "set +e; wineserver --wait; kill -TERM $$!; rm -rf $${PREFIX}" EXIT
	wine $${PREFIX}/python-$(python_version).exe /quiet PrependPath=1 Include_pip=1

	echo "install the dependencies for joyeuse"
	unbuffer wine python -m pip install --upgrade pip
	unbuffer wine pip install -r requirements.txt

	echo "generate the windows executable"
	unbuffer wine pyinstaller --noconsole \
		--paths . --onefile --name joyeuse \
		--exclude-module _bootlocale \
		--hidden-import=tkinter \
		--collect-submodules=pillow \
		script/joyeuse.py
	chmod +x dist/joyeuse.exe

.PHONY: clean
clean:
	rm -rf dist \
		joyeuse.egg-info \
		`find -name __pycache__` \
		`find -name '*.pyc'` \
		.pybuild \
		debian/joyeuse \
		debian/.debhelper \
		debian/debhelper-build-stamp \
		debian/files \
		debian/joyeuse.postinst.debhelper \
		debian/joyeuse.prerm.debhelper \
		debian/joyeuse.substvars \
		../joyeuse_$(version_stripped).dsc \
		../joyeuse_$(version_stripped).tar.xz \
		../joyeuse_$(version_stripped)_all.deb \
		../joyeuse_$(version_stripped)_amd64.build \
		../joyeuse_$(version_stripped)_amd64.buildinfo \
		../joyeuse_$(version_stripped)_amd64.changes \
		build \
		joyeuse.spec \

.PHONY: stylecheck
stylecheck:
	flake8

.PHONY: check
check: all clean stylecheck