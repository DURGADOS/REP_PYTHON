#########################################################################################
# PROGRAM_NAME:dmz_get_all_series_name.py                                               #
# This is a converted python program from dmz_get_all_series_name PERL program.         #
# Assumption: The original perl program calls the shell run_in_sdw.ksh which connects   #
#            to oracle for executing oracle query. Couldn't reproduce the run_in_sdw    #
#            script due to unavailability of Oracle and Linux environment               #
#########################################################################################

from subprocess import check_output,CalledProcessError,PIPE
from subprocess import check_output,CalledProcessError,PIPE
import sys
import os

#############Function that generates the file for invalid arguments #####################
def file_creation():
    mypath ="C:/py/"
    if not os.path.exists(mypath):
        print("path is created")
    fname = mypath + "/" + "test.txt"
    with open(fname,"w") as x:
        x.write("Multiple arguments given in the command line")
#########################################################################################

#############Check for arguments passed & error out for invalid args#####################
program_name = sys.argv[0]
total_arg=len(sys.argv)
#print(program_name)
#print(total_arg)
if(total_arg>1):
    #print("one")
    #print("error argument")
    file_creation()
    exit()
#########################################################################################

#############Execute sql query get table names using run_in_sdw.ksh ######################    
SQLCmd = "SELECT DISTINCT TABLE_NAME FROM ALL_TAB_COLUMNS WHERE OWNER = \'SDW_WEB\'  AND TABLE_NAME LIKE \'V_%_FAME_SERIES\' \
ORDER BY TABLE_NAME "
command= "/bin/run_in_sdw.ksh -f SDW "
execute_stat=0
uri_1=command + SQLCmd
#print(uri_1)
# Assume the above query returns table1, table2, table3
uri="""table1
table2 """
try:
    #uri= check_output([command + SQLCmd],stderr=PIPE)
    print (uri)
except:
        #print("Exception occurred")
        exit()
#print(uri)
contents=uri
#print (contents)
data_ref=contents.split('\n')
#############################################################################################


total = 0
dataset_counter = 0
all_dataset_counter = 0
#print(total)
#print(dataset_counter)
#print(all_dataset_counter)

#############Get the series key from each table ##############################################
for i in data_ref:
    #print(i)
    secondsqlcmd = "SELECT DISTINCT SERIES_KEY FROM SDW_WEB.V_" +i+ "_FAME_SERIES ORDER BY SERIES_KEY";
    #print(secondsqlcmd)
    #uri_2=command + secondsqlcmd
    uri_2="""keyvalue1
    keyvalue2"""
    content=uri_2
    series=contents.split('\n')
    count_series_key=len(series)
    #print(i)
    #print(count_series_key)
    all_dataset_counter +=1 
    #print(all_dataset_counter)
    if(count_series_key > 0):
        #print ("series key greater than 0")
        dataset_counter +=1
        total+=count_series_key
        print(i,"has", count_series_key,"series key(s)")
#############Print the final results #########################################################
if(total>0):      
    print(total, " Series Key(s) in ",dataset_counter, "/", all_dataset_counter, "datasets" )
print("End of program")
##############################################################################################    











    


