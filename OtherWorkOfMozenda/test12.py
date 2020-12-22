import pandas as pd
df1=pd.read_excel(r"C:\Users\dmahapatra\OneDrive - BusinessOne Technologies, Inc\Agent_Info_For_Automation\Find_Missing_Agents.xlsx",sheet_name="InValidURL")

ourlist=df1['InValid URL'].values.tolist()
list1 = df1['Not Scraped URL'].values.tolist()
elenor_data=[i for i in list1 if (str(i) != 'nan')]
#print(elenor_data)
df2=pd.read_excel(r"C:\Users\dmahapatra\OneDrive - BusinessOne Technologies, Inc\Agent_Info_For_Automation\Find_Missing_Agents.xlsx",sheet_name="ELEANOR DATA")
downloadxl_list=df2['Download'].values.tolist()
diff1=set(ourlist).intersection(set(elenor_data))
print("length=",diff1.__len__())
print(diff1)
print(set(elenor_data).__len__())
actual_diff=set(elenor_data).difference(set(diff1))
#print("actual_diff",actual_diff.__len__())
#print(actual_diff)
final_missing=set(downloadxl_list).difference(elenor_data)
#print("Final missing count= ",final_missing.__len__())
#print(final_missing)
missing_data_list=actual_diff.difference(set(downloadxl_list).intersection(elenor_data))
#print("count missing_data_list =",missing_data_list.__len__())
#print("missed data list=",missing_data_list)

#print(actual_diff)

##(set(ourlist).difference(set(elenor_data)))


