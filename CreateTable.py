from connection.connection import Con
c=Con()
con=c.getCon()
print(con)
ram=con.cursor()
ram.execute("Create table swiggy.khaana (sn int primary key auto_increment,name varchar(30), taste varchar(30),quality varchar(30), rating int)")