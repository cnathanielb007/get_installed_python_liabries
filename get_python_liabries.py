__author__ = "nathaniel"
#as of now it is made for windows
#this program finds out all the packages you have installed on python 
#and if ever you loose your data all you hvae to do is go and download this requirements.txt and install it

#please make sure this scripts updates everyday

import smtplib
from time import gmtime, strftime
import os





file_dir = input("what is your python file directory")
windows = "cd "
windows = windows + file_dir
temp = "/Lib/site-packages"
windows = windows + temp
os.system(windows)
#gone to python directory which has all modules


a=os.listdir()# got the list of directories into a list


f= open("list_of_python_liab.txt","r+")
for x in a:
    if x[-4:]=="info":
        a.remove(x)
    if x[-3:]==".py":
        a.remove(x)
    else:
        f.write(x)#writes all the data in the requirements.txt

f.close()


change_loc = input("what is your python file directory")

# this could be made static incase you don't want to keep putting the input
#for doing that just remove "input("what is your python file directory")"
#and replace it with the folder location in ""



change = "move [/Y | /-Y] " + windows + "list_of_python_liab.txt" + change_loc
os.system(change)






def email_info(final):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("your email", "your password")
    s.sendmail("your email", "send email to", final)
    s.quit()