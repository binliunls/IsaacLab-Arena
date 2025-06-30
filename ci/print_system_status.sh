#!/bin/bash

echo ""
echo "GPU"
echo "--------------------------------------------------"
nvidia-smi

echo ""
echo "NVIDIA_DRIVER_CAPABILITIES"
echo "--------------------------------------------------"
echo ${NVIDIA_DRIVER_CAPABILITIES}

echo ""
echo "RAM"
echo "--------------------------------------------------"
free -h

echo ""
echo "SHARED MEM"
echo "--------------------------------------------------"
df -h | grep "/dev/shm"

echo ""
echo "DISK USAGE"
echo "--------------------------------------------------"
df -h

echo ""
echo "INSIDE DOCKER?"
echo "--------------------------------------------------"
inside="NO"
[[ -f /.dockerenv ]] && inside="YES"
echo $inside
