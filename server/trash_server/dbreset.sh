#!/bin/sh

cd /mnt/c/Users/seals/Documents/garbage/garbage_test/server/trash_server/snippets/
rm -d -r migrations/
cd ..
rm -d -r db.sqlite3
python3 manage.py makemigrations 
python3 manage.py migrate

