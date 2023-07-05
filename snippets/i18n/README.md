https://lokalise.com/blog/beginners-guide-to-python-i18n/

xgettext -d base -o joyeuse/i18n/locales/joyeuse.pot $(find joyeuse -name '*.py')

find joyeuse/i18n/ -name '*.po' | while read p; do  msgfmt -o ${p//po/mo} ${p}; done

