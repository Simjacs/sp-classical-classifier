classical music era classifier
==============================

classifies classical pieces by era (baroque, classical, romantic)

see branch feat/convolutional-network for current work

To build the image, run the following from within the project directory: 
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
python3.8 /usr/src/app/src/[script_name]
```

To exit the image's shell, run `exit`
