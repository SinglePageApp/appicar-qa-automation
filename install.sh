#!/bin/bash

sudo echo "deb http://ppa.launchpad.net/qameta/allure/ubuntu xenial main" > /etc/apt/sources.list
sudo apt-get update
sudo apt-get install allure