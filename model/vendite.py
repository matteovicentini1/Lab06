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
        self.soldi=float(self.qty)*float(self.unitsaleprice)

    def __str__(self):
        return f'Data: {self.data}, Ricavo: {float(self.qty)*float(self.unitsaleprice)}, Retailer: {self.retailcod}, Product: {self.prodnumber}'

