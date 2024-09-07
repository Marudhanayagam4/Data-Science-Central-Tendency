class Univariate :
    def quanQual(self,dataset) :
        quan=[]
        qual=[]
        for columnName in dataset.columns :
            # print('ColumnName:',columnName, ', Data type:', end=" ")
            if (dataset[columnName].dtype == 'O') :
                # print('Qual') 
                qual.append(columnName)
            else :
                # print('Quan')
                quan.append(columnName)
        return quan, qual
