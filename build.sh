#!/usr/bin/env bash
# exit on error

set -o errexit

pip install --upgrade pip;
pip install asgiref==3.8.1 beautifulsoup4==4.12.3 bs4==0.0.2 certifi==2024.7.4 charset-normalizer==3.3.2 Django django-pandas==0.6.7 docutils==0.21.2 idna==3.7 lxml==5.3.0 numpy==2.1.0 pandas==2.2.2 python-dateutil==2.9.0.post0 pytz==2024.1 requests==2.32.3 six==1.16.0 soupsieve==2.6 sqlparse==0.5.1 statistics==1.0.3.5 tzdata==2024.1 urllib3==2.2.2


# python manage.py collectstatic --no-input
python manage.py migrate