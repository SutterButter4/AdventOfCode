#!/bin/bash

pip freeze | xargs pip uninstall -y
pip install -r requirements.txt
echo "#GENERATED, DO NOT EDIT" > requirements.lock
pip freeze > requirements.lock