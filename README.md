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
