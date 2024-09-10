import pandas as pd
import numpy as np
class Univariate:
    
    def quanQual(self,dataset) :
        quan=[]
        qual=[]
        for columnName in dataset.columns :
            if dataset[columnName].dtype == 'O':
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual



    def univariateTable (self,dataset,quan):
        descriptive= pd.DataFrame(index=['Mean','Median','Mode','Q1:25%','Q2:50%','Q3:75%','99%','Q4:100%','IQR','1.5Rule','Lesser','Greater','Min','Max','Kurtosis','Skew'],columns=quan)
        
    
        for columnName in quan :
            descriptive[columnName]["Mean"]= dataset[columnName].mean()
            descriptive[columnName]["Median"]= dataset[columnName].median()
            descriptive[columnName]["Mode"]= dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]= dataset.describe()[columnName]['25%']
            descriptive[columnName]["Q2:50%"]= dataset.describe()[columnName]['50%']
            descriptive[columnName]["Q3:75%"]= dataset.describe()[columnName]['75%']
            descriptive[columnName]["99%"]= np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100%"]= dataset.describe()[columnName]['max']
            # IQR = Q3 - Q1
            descriptive[columnName]['IQR']= descriptive[columnName]["Q3:75%"] - descriptive[columnName]["Q1:25%"]
            descriptive[columnName]['1.5Rule']= 1.5*descriptive[columnName]['IQR']
            # Lesser Outlier = Q1- 1.5*IQR
            descriptive[columnName]['Lesser']= descriptive[columnName]["Q1:25%"] - descriptive[columnName]['1.5Rule']
            # Greater Outlier = Q3 + 1.5*IQR
            descriptive[columnName]['Greater']= descriptive[columnName]["Q3:75%"] + descriptive[columnName]['1.5Rule']
            descriptive[columnName]['Min']= dataset[columnName].min()
            descriptive[columnName]['Max']= dataset[columnName].max() 
            descriptive[columnName]['Kurtosis']= dataset[columnName].kurtosis()
            descriptive[columnName]['Skew']= dataset[columnName].skew()
        return descriptive



    def OutliersColumns(self, quan, descriptive) :
        lesser = []
        greater= []
        for columnName in quan:
            if descriptive[columnName]['Min'] < descriptive[columnName]['Lesser'] :
                lesser.append(columnName)
            if descriptive[columnName]['Max'] > descriptive[columnName]['Greater'] :
                greater.append(columnName)
        return lesser, greater



    def ReplacingOutliers(self,dataset, descriptive, lesser, greater) :
        for columnName in lesser :
            dataset[columnName][dataset[columnName] < descriptive[columnName]['Lesser']] = descriptive[columnName]['Lesser']
        for columnName in greater :
            dataset[columnName][dataset[columnName] > descriptive[columnName]['Greater']] = descriptive[columnName]['Greater']
        print("Outliers Replaced Successfully")


    def freqTable(self,columnName, dataset) :
        freqTable = pd.DataFrame(columns=['Unique_Values','Frequency','Relative_Frequency','Cumsum'])
    
        freqTable['Unique_Values'] = dataset[columnName].value_counts().index
        freqTable['Frequency'] = dataset[columnName].value_counts().values
        freqTable['Relative_Frequency']= (freqTable['Frequency'] / 103)
        freqTable['Cumsum'] = freqTable['Relative_Frequency'].cumsum()
    
        return freqTable
    














