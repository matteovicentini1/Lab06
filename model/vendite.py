class Vendite:

    def __init__(self,retailcod,prodnumber,ordermethod,data,qty,unitprice,unitsaleprice,anno):
        self.retailcod = retailcod
        self.prodnumber =prodnumber
        self.ordermethod =ordermethod
        self.data=data
        self.qty=qty
        self.unitprice=unitprice
        self.unitsaleprice=unitsaleprice
        self.anno=anno

    def __str__(self):
        return f'Data: {self.data}, Ricavo: {int(self.qty)*int(self.unitsaleprice)}, Retailer: {self.retailcod}, Product: {self.prodnumber}'

