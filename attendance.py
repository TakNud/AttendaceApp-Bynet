###############
##Almog Sofer##
###############

import pandas as pd
import os
import glob
import re
#import pysftp

import mysql.connector

mydb = mysql.connector.connect(
    host="184.72.127.1",
    user="root",
    password="root",
    database="test_db"
)


# def download_csvs():
#   Hostname = "185.164.16.144"
#   Username = "almogs"
#   Password = "123456"
#   localFilePath = "/app"
#   cnopts = pysftp.CnOpts()
#   cnopts.hostkeys = None
#   with pysftp.Connection(host=Hostname, username=Username, password=Password, cnopts=cnopts) as sftp:
#     print("Connection successfully established ... ")
#     # Switch to a remote directory
#     sftp.get_r("/var/tmp/csv_files/", localFilePath)
#     print("done")

def att():
    # get the current path
    path = os.getcwd()+'/uploads'
    # load all the files on directory
    csv_files = glob.glob(os.path.join(path, "par*.csv"))
    # Create new empty dic
    data = {'Name': {}}

    print("Start to Merge all files . . ")
    # loop over the list of csv files
    for f in csv_files:
        # read the csv file
        df = pd.read_csv(f, sep="\t", encoding="UTF-16LE")
        # change the names to lowercase and Convert time from string to integer
        for i in range(len(df)):
            cur_name = df.at[i, 'Name'].lower()
            cur_duration = re.findall(r'\d+', df.at[i, 'Attendance Duration'])
            cur_duration = int(''.join(cur_duration))
            # Add all to dictionary
            if cur_name not in data['Name']:  # if name not exist
                data['Name'].update({cur_name: cur_duration})
            else:  # if name exist
                data['Name'][cur_name] += cur_duration

    df_new = pd.DataFrame.from_dict(data)

    return df_new.to_csv("output.csv")
    #print("Merge All File in Directory Succeed! !")
