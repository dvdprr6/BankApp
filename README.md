


##Python Requirements
1. Python version 3.0 or higher
2. Setuptools 7.0

##Python Installation and Environment setup

1. First download the latest python distribution here: https://www.python.org/downloads/
2. untar the .xz package `tar -xJf Python.3.x.x.tar.xz`
3. Enter the Python.3.x.x directory and run `./configure --prefix=/opt/python3.x`
4. To install the binaries run the makefile `make && sudo make install`Now setup up the python environment, so the dependencies can be properly managed
5. Create the python virtualenv `/opt/python3.x/bin/python3.x -m venv /home/david/projects/BankApp/BankAppEnv`
6. Now install the setuptools. Download here: https://pypi.python.org/pypi/setuptools. To install the tools run `/home/david/projects/BankApp/BankAppEnv/bin/python setup.py install`
7. To install the requirements, first pip needs to be installed `/home/david/projects/BankApp/BankAppEnv/bin/easy_install pip` Now install the requirements `/home/david/projects/BankApp/BankAppEnv/bin/pip install -r requirements.txt`


