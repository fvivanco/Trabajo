from flask import Flask, jsonify, request

#!/usr/bin/env python
# -*- coding: utf-8 -*-

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
	if(request.method=='POST'):
		some_json= request.get_json()
		return jsonify({'You have sent': some_json}), 201
	else:
		return jsonify({"Hi":"Hello underworld"})	
@app.route('/validacion/<int:num>/<string:var>', methods=['GET'])
def get_exponencial2(num,var):
	if(num==10 or num == 14):
		return jsonify({"Su número de cuenta es": f"Nro: {num**2} {num*6} {num+5} {num*7}" ,
						"Su codigo secreto es " : var.upper()+"g$#1123" })
	else:
		 return jsonify({"ERROR": "Ingreso no permitido"})	
	
if __name__ == '__main__':
	
	app.run(debug = True, port=8000)