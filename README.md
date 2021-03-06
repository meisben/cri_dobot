# Common Robot Interface (Wrapper for dobot magician)

***Important Note***: This is a dobot magician wrapper for the cri library from John Lloyd. It enables use of the cri library for the dobot magician robot arm. The wrapper is compatible with:
- dobot magician firmware version 3.7.0
- the latest [as of Feb 2020 v0.0.1] version of the cri library.


## Prerequisites
The cri library must be installed to use this wrapper: https://github.com/jlloyd237/cri

I recommend installing this libary by navigating to the directory of 'setup.py' in a terminal window, then running the command:

```sh
pip install -e .
```

This will create an editable install of the cri library

## Installation (part 1)

To install the package on Windows, OS X or Linux, clone the repository and use the 'pip install' command inside the repository root directory.

It is suggested to do this in a virtual environment by:

(1) create a virtual environment (e.g. using venv or conda). 
(2) open a terminal window with the virtual environment activated
(3) navigate the the local directory of dobot_tactile_toolbox setup.py using the 'cd' command
(2) Then run the following command

```sh
pip install -e .
```

## Installation (part 2) of .dll for use with dobot magician arm: 

For both windows and mac you should *not* need to do anything with the dll. The 64 bit dlls are packaged with cri_dobot. If you get an error message relating to the dll library try the steps below. Please reach out for help if this isn't working! Please also note that currently dobot have yet to supply the .so files for this verision of firmware, so this is untested on a linux system.

To use the dobot dll (which is a prerequisite) follow these instructions 
- [A] use the correct DLL from dobot (64 bit or 32 bit), and
- [B] put the dll in either 
  - \cri_dobot\dobotMagician\dll_files
  - or the system root directory, for example on windows this is (%SystemRoot%\system32)

You can find the dll at (https://www.dobot.cc/downloadcenter/dobot-magician.html) - Look for Development Protocol -> 'DobotDemovX.X.zip' - Ensure you extract the correct DLL for your system (windows/linux/mac) (x64/x32)

## Usage

- For examples of basic usage with cri library see script in tests folder

### Tool center point

With a Tactip attachment the corresponding Tool Center Point using cri_dobot is = (59.7, 0, 0, 0, 0, 0). The origin is not well described in the dobot magician user documentation, but is instead shown in the image below. The working which shows how this is infered is defined by the the point described in the excel sheet in the \images directory

![tcp_origin.jpg](images/tcp_origin.jpg)

## Bug list

(1) Tool Center Point [Now squished]

For info only: TCP bug has been rectified by dobot in the new firmware version. TCP is now working correctly!

