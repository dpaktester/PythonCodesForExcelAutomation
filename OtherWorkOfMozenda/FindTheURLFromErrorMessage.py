import pandas as pd
import os
import openpyxl
df1=pd.read_excel(r"C:\Users\dmahapatra\Downloads\Errorred URL.xlsx",sheet_name="Errored URLs")

URLListFromMessage=df1['URL'].values.tolist()
##print(URLListFromMessage)

URLNameList= [str(str(i).split('LinkUrl:')[1]).split('--')[0].strip() for i in URLListFromMessage]

MozendaAgentIDList= [str(str(i).split('mozendaAgentId:')[1]).split(' ')[1].strip() for i in URLListFromMessage]
LinkCodeList= [str(str(i).split('LinkCode:')[1]).split(' ')[1].strip() for i in URLListFromMessage]
print("URLNameList: ",URLNameList)
print("MozendaAgentIDList: ",MozendaAgentIDList)
print(("LinkCodeList: ",LinkCodeList))
##setOfURLs=set(URLNameList)
df2=pd.DataFrame()
df2['Agent Id']=pd.Series(MozendaAgentIDList)
df2['Link Code']=pd.Series(LinkCodeList)
df2['Captured URL']=pd.Series(URLNameList)
##df2['URLs which are not scraped']=pd.Series(list(setOfURLs))
print(df2)
##df2.to_excel('URLs need to see',index=False,sheet_name='NeedRemovalData')
df2.to_excel('Urls_To_be_Removed.xlsx',sheet_name='ToBeRemoved',index=False)
print("Copied to the location ",os.getcwd())

