# **University requirements finder**



This is a python app that will find the University entry requirements for any course.



You simply input a course and the app will output the requirements for all universities included in the unis list within the code.

The output will include a course (type e.g Bsc 3 years full-time), a uni name (e.g University of Birmingham), the UCAS points required for acceptance (e.g 120) and the A-levels required for exceptance.

The A-levels are calculated in the module named **'uni_class.py'** so make sure you keep that and app.py in the same folder.



Within the archive directory there is two files: **'code_auto3.py'** and **'code_auto1.py'**. These are previous versions of the app.




### code_auto1.py

Limited course options.
No A-level grades.
Less features

### code_auto3.py

This is a differtent version of the app.py that will, instead of printing results, export them to a csv file that will be opened in excel by your pc and allow for manipulation of data.




To be able to run this app you must install the requests module for python and the bs4 module, as well as ***Python 3.8***.

Install modles like so:

$ pip3 install requests

$ pip3 install bs4




## **Tkinter version**

You may see a tkinter_app directory. You will have to have Python 3.8 installed with the standard library for this to work. The tkinter GUI was only designed for my learning purposes, therefore, it is not efficient and runs slowly.

In this version, however, there is an option to export the findings to excel, just like the code_auto3.py. This may beuseful for some.

I do not advise using this version as it was not developed for public use.

