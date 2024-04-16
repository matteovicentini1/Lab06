from database import DAO

class Model:
    def __init__(self):
        self.retailer = DAO.DAO().retails()
        self.venditedecr = DAO.DAO().venditedecr()
        self.join= DAO.DAO().product()

    def take(self,y,b,re):
        r=[]
        if y==None and b==None and re!=None:
            for i in self.venditedecr:
                if int(i.retailcod)== int(re):
                    r.append(i)
            return r
        elif re ==None and b==None and y!=None:
            for i in self.venditedecr:
                if int(i.anno)==int(y):
                    r.append(i)
            return r
        elif re==None and y==None and b!=None:
            for i in self.join:
                for k in self.venditedecr:
                    if i.pbrand==b and int(k.prodnumber)==i.number:
                        r.append(k)
            return r
        elif re==None and y!=None and b!=None:
            for i in self.join:
                for k in self.venditedecr:
                    if i.pbrand==b and int(k.prodnumber)==i.number and int(k.anno)==int(y):
                        r.append(k)
            return r
        elif re != None and y != None and b == None:
            for i in self.venditedecr:
                if int(i.retailcod)== int(re) and int(i.anno)==int(y):
                    r.append(i)
            return r
        elif re!=None and y==None and b!=None:
            for i in self.join:
                for k in self.venditedecr:
                    if i.pbrand==b and int(k.prodnumber)==i.number and int(k.retailcod)== int(re):
                        r.append(k)
            return r
        elif re!=None and y!=None and b!=None:
            t=[]
            for i in self.join:
                for k in self.venditedecr:
                    if i.pbrand==b and int(k.prodnumber)==i.number :
                        t.append(k)
            for i in t:
                if int(i.retailcod) == int(re) and int(i.anno) == int(y):
                    r.append(i)
            return r
    def solditot(self,list):
        som=0
        for i in list:
            som +=i.soldi
        return som

    def contaretails(self,lista):
        s=0
        st = set()
        for i in lista:
            st.add(i.retailcod)
        return len(st)

    def contaprodotti(self,lista):
        s=0
        st = set()
        for i in lista:
            st.add(i.prodnumber)
        return len(st)

