import datetime
import locale

from CONFIG import LANGUAGE


def time_in_locale():
    if LANGUAGE == 'fr':
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')  # Set the locale to French
        formatted_time = datetime.datetime.now().strftime('%Hh %M')
        return f"Il est {formatted_time} Monsieur"
    else:
        locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')  # Set the locale to English
        formatted_time = datetime.datetime.now().strftime('%Ih %M %p')
        return f"It's {formatted_time} Sir"

def date_in_locale():
    if LANGUAGE == 'fr':
        locale.setlocale(locale.LC_TIME, 'fr_FR')  # Set the locale to French
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime('%A %d %B %Y')
        return f"Nous sommes le {formatted_datetime} Monsieur"
    else:
        locale.setlocale(locale.LC_TIME, 'en_US')  # Set the locale to English
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime('%A %d %B %Y')
        return f"It's {formatted_datetime} Sir"