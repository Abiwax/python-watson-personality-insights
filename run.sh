#!/bin/bash
if [ -z "$VCAP_APP_PORT" ];
then SERVER_PORT=80;
else SERVER_PORT="$VCAP_APP_PORT";
fi
echo port is $SERVER_PORT

echo "make migrations"
python manage.py makemigrations

echo "migrate"
python manage.py migrate

python manage.py runserver 0.0.0.0:$SERVER_PORT --noreload
