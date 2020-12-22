import pyodbc
import os
import openpyxl
import pandas as pd
import configparser as cp
import datetime

cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=botsqlprod01.database.windows.net;PORT=1433;DATABASE=Phoenix;UID=PhoenixReadOnly;PWD=K5Lrtp68cvfu8A9n0dmjSsqNIMRP2o7YzyQiWYBEgkTawhVD')
cursor = cnxn.cursor()
NameofFile="NewLinks"
NameOfSheet="NewlyAddedLinks"
def getNewlyAddedLinks():
 NewlyAddedData="SELECT * FROM LINK WHERE recordStatusID=1 AND UpdateTime >getdate()-3 ORDER BY URL ASC"
 Newlinksdf=pd.read_sql(NewlyAddedData,cnxn)
 ##print(Newlinksdf)
 Newlinksdf.to_excel(NameofFile+"_"+str(datetime.date.today())+".xlsx",index=False,sheet_name=NameOfSheet)

 print("Copied to the location ",os.getcwd())


getNewlyAddedLinks()
