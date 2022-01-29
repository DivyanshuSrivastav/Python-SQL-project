from connection.connection import Con
c=Con()
con=c.getCon()
print(con)
ram=con.cursor()
ram.execute("insert into swiggy.khaana (name,taste,quality,rating) "
            "values('kauwa biryani','mumber1','good',5),('paneer pyaza','number3','poor',2)")
con.commit()