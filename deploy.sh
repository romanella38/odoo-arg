#!/bin/sh
cd ~/odoo-dev/11/proyecto1/src/addons-ar

git merge -s recursive -X theirs master
git pull origin master


echo "done"
