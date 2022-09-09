#!/bin/bash

cd /home/ubuntu

sudo npm install -g pm2@3.2.2
pm2 start server.js