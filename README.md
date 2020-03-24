# Common Robot Interface (Wrapper for dobot magician)

***Important Note***: This is a dobot magician wrapper for the cri library from John Lloyd. It enables use of the cri library for the dobot magician robot arm. The wrapper is compatible with the latest [as of Feb 2020 v0.0.1] version of the cri library.


## Prerequisites
The cri library must be installed to use this wrapper: https://github.com/jloyd237/cri

## Installation (part 1)

To install the package on Windows, OS X or Linux, clone the repository and run the setup script from the repository root directory:

```sh
python setup.py install
```

To use with a virtual environment

(1) create a virtual environment (e.g. using conda). 
(2) Then run the following command in the local directory of cri_dobot setup.py: 

```sh
pip install -e . 
```

## Installation (part 2) of .dll for use with dobot magician arm: 

To use the dobot dll (which is a prerequisite) follow these instructions 
- [A] use the correct DLL from dobot (64 bit or 32 bit), and
- [B] put the dll in either the Anaconda root directory or the system root directory (%SystemRoot%\system32) whichever one works :)

You can find the dll at (https://www.dobot.cc/downloadcenter/dobot-magician.html) - Look for Development Protocol -> 'DobotDemovX.X.zip' - Ensure you extract the correct DLL for your system (windows/linux/mac) (x64/x32)

## Usage

- For examples of basic usage with cri library see script in tests folder
- For usage with vsp library and TacTip sensor see script inside tests\vsp\ folder
  - This requires that the vsp library is also installed (https://github.com/jloyd237/vsp)

## Bug list

(1) TCP

Dobot magician has a Tool Center Point (TCP) bug which means that it always assumed it's tool center point values (x,y,z) are 0,0,0. For this reason the tool center point is not currently used with the dobot magician in production code. It is yet to be determined whether this functionality will be replicated in future versions of the cri_dobot wrapper. An question has been opened on this topic in the dobot magician forums.
