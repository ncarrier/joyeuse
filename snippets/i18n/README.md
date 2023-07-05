https://lokalise.com/blog/beginners-guide-to-python-i18n/

xgettext -d base -o locales/joyeuse.pot i18n.py

msgfmt -o locales/fr/LC_MESSAGES/joyeuse.{m,p}o

