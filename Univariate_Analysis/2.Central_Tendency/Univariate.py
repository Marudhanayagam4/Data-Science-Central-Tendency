class Univariate:
    def quanQual(self,dataset) :
        quan=[]
        qual=[]
        
        for columnName in dataset.columns :
            # print(columnName, end=": ")
            if dataset[columnName].dtype == 'O' :
                # print("qual")
                qual.append(columnName)
            else :
                # print("quan")
                quan.append(columnName)
        return quan,qual

    