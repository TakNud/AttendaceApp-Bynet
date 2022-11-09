###############
##Almog Sofer##
###############

import pandas as pd
import os
import shutil
import glob
import re
import pysftp
from datetime import date
import mysql.connector as msql
from mysql.connector import Error


def download_csvs():
    Hostname = "185.164.16.144"
    Username = "almogs"
    Password = "123456"
    localFilePath = "/uploads"
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host=Hostname, username=Username, password=Password, cnopts=cnopts) as sftp:
        print("Connection successfully established ... ")
        # Switch to a remote directory
        sftp.get_r("/var/tmp/csv_files/", localFilePath)
        print("done")


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
    csvNew = df_new.to_csv("output.csv")
    importIntoDb(csvNew)
    return csvNew
    #print("Merge All File in Directory Succeed! !")


def removeFiles():
    folder = '/path/to/folder'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def importIntoDb(csvFlie):
    try:
        conn = msql.connect(host='localhost', database='test_db', user='root')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            print('Creating table....')
            cursor.execute(
                "CREATE TABLE `{text}` (name varchar(40) ,sum varchar(10) ".format(text=date.today()))
            print("table is created....")
            for i, row in csvFlie.iterrows():
                sql = "INSERT INTO test_db.`{text}` VALUES (%s,%s,%s,%s,%s)".format(
                    text=date.today())
                cursor.execute(sql, tuple(row))
                print("Record inserted")
                conn.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)
