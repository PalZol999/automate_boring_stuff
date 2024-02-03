* Create your script in python

For adding your project to the Run terminal:
* On search: 
  Advanced system settings> Environement variables > Path > Edit.. > C:\Users\zoltan\ (the name of the VScode folder)

For runing the script:
 Add .bat file with the following script
     echo off
    cd /d C:\Users\zoltan\Desktop\Letoltes\WebDev\GUI_auto
    python name_of_the _file.py %*
    @pause

* Windows + R = open the Run

* write the name of the file you want to run: "name_of_the _file (param if necessary) " > ok
