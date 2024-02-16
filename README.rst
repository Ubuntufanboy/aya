Aya - Lightweight Logging Framework
=======

.. image:: https://github.com/Ubuntufanboy/aya/blob/master/aya2.png
    :height: 100px
    :alt: Aya logo
    :align: center

.. image:: badge.svg

About
=====

Aya is a very lightweight logging suite with heavily customizable options like plugins and templates.
Aya is still in a very early stage of development so please report all bugs to me to fix or open a pull request

Features
========

- Custom logging templates
- Verbose line-tracking logs
- Logging to file
- Colorful logging messages

Getting Started
===============


.. code-block:: python
    import aya # make sure to import the whole module

    mylog = Logger(template="{DATE} {TIME} {FILE}:{LINE} - {TYPE}: {MSG}", logfile="test.txt")
    mylog.debug("This is a debug message")
    mylog.info("This is a info message")
    mylog.warn("This is a warning message")
    mylog.error("This is an error message")
    mylog.critical("This is a critical message")

    # Default template and no logging to file
    boring_log = Logger()
    boring_log.debug("This is a boring debug message...")

See the docs folder for some more examples

Install
=======

Sadly this project is not on pypi yet so you must manualy import it for now. Don't worry it's easy
::
    git clone https://www.github.com/Ubuntufanboy/aya
    cp aya/aya.py your/project/directory

Template Keywords
=================

Input Keywords
::
    {TIME} A timestamp of the time the log was called
    {DATE} The day the log was called
    {TYPE} The type of log that was called
    {LINE} The line number that the log was called 
    {LOGFILE} The file the logger logs to
    {FILE} The file that the logger is running on

Output Keywords
::
    {msg} the message the logger will display

Contributing
============

Please feel free to contribute since the more hands the better!
There are no set guidelines to contribute except verify your code works before making a project
