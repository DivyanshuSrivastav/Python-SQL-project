from connection.connection import Con
c=Con()
con=c.getCon()
print(con)
ram=con.cursor()
ram.execute("select * from swiggy.khaana")
res=ram.fetchall()
for i in res:
    print(i)