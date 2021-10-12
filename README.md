classical music era classifier
==============================

classifies classical pieces by era (baroque, classical, romantic)

see branch feat/convolutional-network for current work

Because this project uses GPU acceleration to train the model, the NVIDIA container toolkit has to be installed before the image can be used correctly.
To install it, run the following command 
```bash
sudo make install-nvidia-toolkit
```
You should get an output like:
```bash
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 450.119.04   Driver Version: 450.119.04   CUDA Version: 11.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce RTX 2070    Off  | 00000000:09:00.0  On |                  N/A |
| 16%   31C    P8    28W / 175W |    343MiB /  7981MiB |      5%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+
```
Which demonstrates that my containers now have access to my GPU, which is an RTX 2070. 
If the GPU you're hoping to use doesn't appear in the output, you will have to google it because I haven't finished this README yet. 

To build the image, run the following from within the project environment: 
```bash
make build-image
```

If it raises `PermissionError: [Errno 13] Permission denied`, the permissions on docker are such that the current user doesn't have access. Run with sudo instead:

```bash
sudo make build-image
```

To open a bash shell within the image, after the image has built run:
```bash
sudo make shell
```

Then from the image's bash shell, to run the scripts:
```bash 
python3.8 /usr/src/app/src/[script_name].py
```

To exit the image's shell, run `exit`
