# release mechanism controller

A simple python script to control the release mechanism for the physics experiments setup.

## Install

Create a venv:

```sh
python -m venv .venv
source .venv/bin/activate
```

Install required dependencies:

```sh
pip install -r requirements.txt
```

### macOs

On macOs make sure you've installed `libusb`:

```sh
brew install libusb
```

## Usage

The release mechanism is controlled over serial usb, so make sure to bring a usb-c to usb adapter
if your laptop doesn't have a usb port!

Once the release mechanism is powered using the plug that's connected to it,
plug it into your laptop using the usb cable.

You're now ready to control the release mechanism using the script provided in this repository,
the script is quite simple:

```sh
# to open the release mechanism:
python main.py open

# to close it:
python main.py close
```
