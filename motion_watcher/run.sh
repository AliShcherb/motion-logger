#!/bin/bash
mkdir -p motion_watcher/logs
nohup python3 motion_watcher/motion_watcher.py > motion_watcher/logs/motion_watcher.log 2>&1 &
echo "🚀 Motion Watcher is running in background."
