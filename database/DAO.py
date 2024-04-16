from database.DB_connect import DBConnect
import model.retailer as m
import model.vendite as v
import model.prodotti as p

class DAO():
    def __init__(self):
        pass

    def anni(self):
        cnx=DBConnect.get_connection()
        cursore = cnx.cursor()
        result=[]
        query='''SELECT distinct year(Date)
                FROM go_daily_sales gds '''
        cursore.execute(query)
        for i in cursore:
            result.append(i[0])
        cnx.close()
        cursore.close()
        return result

    def prodotti(self):
        cnx = DBConnect.get_connection()
        cursore = cnx.cursor()
        result = []
        query = '''SELECT distinct Product_brand 
                    FROM go_products '''
        cursore.execute(query)
        for i in cursore:
            result.append(i[0])
        cnx.close()
        cursore.close()
        return result

    def retails(self):
        cnx = DBConnect.get_connection()
        cursore = cnx.cursor(dictionary=True)
        result = []
        query = '''SELECT * 
                            FROM go_retailers '''
        cursore.execute(query)
        for i in cursore:
            result.append(m.Retailer(i['Retailer_code'],i['Retailer_name'],i['Type'],i['Country']))
        cnx.close()
        cursore.close()
        return result

    def venditedecr(self):
        cnx = DBConnect.get_connection()
        cursore = cnx.cursor()
        result = []
        query = '''SELECT *,year(Date)
                    FROM go_daily_sales
                     ORDER BY Unit_sale_price * Quantity DESC'''
        cursore.execute(query)
        for i in cursore:
            result.append(v.Vendite(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
        cnx.close()
        cursore.close()
        return result

    def product(self):
        cnx = DBConnect.get_connection()
        cursore = cnx.cursor()
        result = []
        query = '''SELECT *
                            FROM go_products'''
        cursore.execute(query)
        for i in cursore:
            result.append(p.Prodotti(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
        cnx.close()
        cursore.close()
        return result

