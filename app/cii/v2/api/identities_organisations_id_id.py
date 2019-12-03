# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from flask import jsonify, make_response

from flask import request, g

from . import Resource
from .. import schemas

import mysql.connector
import json


class IdentitiesOrganisationsIdId(Resource):

    def get(self, id):
        scheme = request.args.get('scheme')
        if scheme == None:
            return make_response("Scheme missing",400)
        
    	mydb = mysql.connector.connect(
			host="127.0.0.1",
			user="root",
			passwd="ciipasswd",
			database="cii"
		)
		
	mycursor = mydb.cursor()

        sql = "select int_id from identities where id=" + id + " and scheme='" + scheme + "'"
        mycursor.execute (sql)
        row = mycursor.fetchone()
        if row is not None:

            sql = "select scheme, id, legalName from identities where int_id=%s or int_id in (select id2 from id_matches where id1=%s)"
	    mycursor.execute (sql, (row[0],row[0]))
	
	    regarr = []
	    regdict = {}
	    for (scheme, orgid, legalName) in mycursor:
                regdict=dict (zip(["scheme","id","legalName"],[scheme,orgid,legalName]))
    	        regarr.append (regdict)
	
                outdata = '{"identifiers":' + json.dumps(regarr) + '}'

#        try:
#          with open ("cii/identities/" + id + ".txt","r") as orgfile:
#            orgdata = orgfile.read()
                return make_response(outdata, 200)
#        except:
#          return make_response("", 404)
        return make_response("Organisation Not Found", 404)
