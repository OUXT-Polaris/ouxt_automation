#!/bin/bash

usermod -u $USER_ID -g $GROUP_ID -G sudo ros
chown ros:ros -R /home/ros

/bin/bash
