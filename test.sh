#!/bin/bash
declare -a directories=("sweet-factory" "cake-api" "milkshake-api" "toothache-api")
for dir in "${directories[@]}"
do
  cd ${dir}
  sudo apt update
  sudo apt upgrade
  sudo apt install python3 python3-pip python3.8-venv
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  python3 -m pytest --cov --cov-report xml -v
  deactivate
  cd ..
done