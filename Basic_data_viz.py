# Load Indicators and the pounds millions OTS data
Indicators = pd.read_excel("Data.xlsx", sheet_name= "Standardised", engine='openpyxl')
OTSData = pd.read_excel("Data.xlsx", sheet_name = "Data" , engine='openpyxl')   

#dataframe visual inspection
Indicators.style.background_gradient(cmap='coolwarm').highlight_null('black')

Data.plot(figsize=(8, 8)) 
plt.show()

#scatter matrix plot
axes = scatter_matrix(Indicators, figsize=(50,50))

for ax in axes.flatten():
    ax.xaxis.label.set_rotation(90)
    ax.yaxis.label.set_rotation(0)
    ax.yaxis.label.set_ha('right')

plt.tight_layout()
plt.gcf().subplots_adjust(wspace=0, hspace=0)
plt.show()

#subplot

data.plot(subplots=True, figsize=(50, 50))
plt.show()


def insert_space(string, integer):
    return string[:integer] + '-' + string[integer:]

Data['Month'] = Data['Month'].apply(lambda x: insert_space(x, 4))

Data1['Month'] = Data1['Month'].apply(lambda x: insert_space(x, 4))

#Formatting the Datetime 
Data["Month"] = [datetime.datetime.strptime(str(i).replace(" ","").upper()[0:8], "%Y-%b") for i in Data["Month"]]
Data1["Month"] = [datetime.datetime.strptime(str(i).replace(" ","").upper()[0:10], "%Y-%b",) for i in Data1["Month"]]


