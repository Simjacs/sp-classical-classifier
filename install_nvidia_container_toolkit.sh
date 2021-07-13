#!/bin/bash

# import variables with information about os from os-release file
. /etc/os-release 
# check if distribution is elementary os
if [[ $ID == 'elementary' ]]
then 
    echo 'it is elementary my dear watson'
    use_distro=ubuntu18.04
    echo 'using the version for the following distro instead:'
    echo "$use_distro"
else 
    echo 
    use_distro=$ID$VERSION_ID
    echo "$use_distro"
fi

# install nvidia container toolkit
# installs ubuntu version for elementary os
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
&& curl -s -L https://nvidia.github.io/nvidia-docker/"$use_distro"/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list


sudo apt-get update
sudo apt-get install -y nvidia-docker2
sudo systemctl daemon-reload
sudo systemctl restart docker

# test the installation
sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
