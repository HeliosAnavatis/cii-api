import mysql.connector
import json

mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="ciipasswd",
        database="cii"
#        auth_plugin='mysql_native_passwd'
)

print (mydb)

mycursor = mydb.cursor()

sql = "select scheme, id, legalName from identities where int_id=1 or int_id in (select id2 from id_matches where id1=1)";

mycursor.execute(sql)
regarr = []
regdict = {}
for (scheme, orgid, legalName) in mycursor:
    regdict=dict (zip(["scheme","id","legalName"],[scheme,orgid,legalName]))
#    print json.dumps(regdict)
    regarr.append (regdict) 

print '{"identifiers":'
print json.dumps(regarr)
print '}'

#     print (x)
#print ("{")
#for x in myresult:
#    print(json.dumps(x, separators=(", ")) )
#print ("}")
