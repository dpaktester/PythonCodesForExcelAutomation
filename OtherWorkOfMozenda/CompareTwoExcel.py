import pandas as pd
import os
import openpyxl
df1=pd.read_excel(r"C:\Users\dmahapatra\Downloads\Download_Error_Page_List.xlsx",sheet_name="Invalid URL")

InvalidListOfURL=df1['URL'].values.tolist()
df2=pd.read_excel(r"C:\Users\dmahapatra\Downloads\Errorred URL.xlsx",sheet_name="URLs")
NotCapturedListOFURL=df2['URL'].values.tolist()
CommonData=set(NotCapturedListOFURL).intersection(set(InvalidListOfURL))
print("length of Common data Betwen both the sheets is :",CommonData.__len__())
print('Common Data between both the shets are ',CommonData)
CommonDataList=pd.DataFrame()
CommonDataList['URLs']=pd.Series(list(CommonData))
CommonDataList.to_excel("URL_Which_Are_Common.xlsx",index=False,sheet_name='Invalid URL')
differentData=set(NotCapturedListOFURL).difference(set(InvalidListOfURL))
print("Length of Differernt Data Between both the sheets is : ",differentData.__len__())
print('Different data between both the sheets are ',differentData)
MissingListofURL = pd.DataFrame()
print(MissingListofURL)
MissingListofURL['MissingURL']=pd.Series(list(differentData))
print(MissingListofURL)
MissingListofURL.to_excel("URL_Which_is_Not_Scraped10.xlsx",index=False,sheet_name='Not Captured URL')
print("Copied to the location ",os.getcwd())



#MissingListofURL['Missing URL ']=list(differentData)
#MissingListofURL.to_excel("URL_Which_is_Not_Scraped")
