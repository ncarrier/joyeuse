version := $(shell python3 -c "import joyeuse.__version__ as v; print(v.__version__)")
# strip any suffix, such as -alphaX, as deb file names don't have it
version_stripped := $(shell echo $(version) | sed 's/[abr].*//g')
SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -ec

.PHONY: all
all: pip debian

.PHONY: pip
pip:
	python3 setup.py sdist

.PHONY: debian
debian:
	debuild -uc -us

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
