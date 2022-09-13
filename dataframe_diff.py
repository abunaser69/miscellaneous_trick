def dataframe_difference(df1, df2, which=None):
    """Find rows which are different between two DataFrames."""
    comparison_df = df1.merge(df2,
                              indicator=True,
                              how='outer')
    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    diff_df.to_csv('data/diff.csv')
    return diff_df

dfk.loc[dfk['County Name_x'] != dfk['County Name_y']]
df1['is_equal']= (df1['State']==df1['State_1'])
print(df1)

df = pd.concat([df1, df2]) # concat dataframes
df = df.reset_index(drop=True) # reset the index
df_gpby = df.groupby(list(df.columns)) #group by
idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1] #reindex

#Find Common Rows between two Dataframe Using Merge Function
df = df1.merge(df2, how = 'inner' ,indicator=False)

#Find Common Rows Between Two Dataframes Using Concat Function
df = pd.concat([df1, df2])

df = df.reset_index(drop=True)

df_gpby = df.groupby(list(df.columns))

idx = [x[0] for x in df_gpby.groups.values() if len(x) != 1]

df.reindex(idx)

#Find Rows in DF1 Which Are Not Available in DF2
df = df1.merge(df2, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only']

#Find Rows in DF2 Which Are Not Available in DF1
df = df1.merge(df2, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='right_only']

#Check If Two Dataframes Are Exactly Same
df2.equals(df1)

#Check If Columns of Two Dataframes Are Exactly Same
df2['Temp'].equals(df1['Temp'])

#Find Rows Which Are Not common Between Two dataframes
pd.concat([df1,df2]).drop_duplicates(keep=False)

#Find All Values in a Column Between Two Dataframes Which Are Not Common
set(df1.Temp).symmetric_difference(df2.Temp)

