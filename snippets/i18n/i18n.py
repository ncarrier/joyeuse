# Import gettext module
import gettext
# Set the local directory
appname = 'joyeuse'
localedir = './locales'
# Set up Gettext
en_i18n = gettext.translation(appname, localedir, fallback=True)
# Create the "magic" function
en_i18n.install()
# Translate message
print(_("Hello World"))
print(_("How are you"))
