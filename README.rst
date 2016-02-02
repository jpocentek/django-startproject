Start Project
=============

Django starting package, ready to go and with custom account apps onboard. It
is highly personalized. It's running well on Debian (Jessie and Stretch tested) and Python 2 (Python 3 should also work).

Installation
============

Create virtualenv::

    mkvirtualenv <project_name>

Create directory::

    mkdir <project_name>

Change directory::

    cd <project_name>

Clone repository::

    git clone https://jpocentek@bitbucket.org/jpocentek/startproject.git .

For the first time you have to provide project name as argument for installation
script. This name will be used everywhere in project configuration files.
Remember that there is no error reporting so far, so you have to provide clean
Python package name (e.g. myproj or my_proj) by yourself. To include all
dependencies at once, run this command::

    ./install -df <project_name>

Now you have to add projects applications into Python path::

    add2virtualenv ./<project_name>/apps

And you are ready to go with standard Django installation process (creating
database and superuser etc.)

Repository
==========

During installation, this project will be DETATCHED from main repository. It is
intentional. If you want to develop remotely, you have to provide new upstream
by yourself (see ``man git remote`` if you don't know what I'm talking about).
