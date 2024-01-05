from flask import (
    Flask,
    request,
    jsonify,
    make_response,
    current_app,
    redirect,
    url_for,
    session,
    send_from_directory,
)
from flask.templating import render_template
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from sqlalchemy import and_
from sqlalchemy import desc
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import datetime
from sqlalchemy.exc import SQLAlchemyError

SERVER = '45.125.131.126'
DATABASE = '13TWP2023'
USERNAME = 'sa'
PASSWORD = 'Foreversystem2159'
DRIVER = 'ODBC Driver 17 for SQL Server'
SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}"

app = Flask(__name__)
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

# db = SQLAlchemy(app)
ma = Marshmallow(app)
from models import login_model,api_result,todolist_model
from services import login_service,todolist_service

todolist_service.get_customer('42914')

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/todolist')
def todo_list():
    Emp_Id = request.args.get("Emp_Id")
    Emp_Position = request.args.get("Emp_Position")
    Emp_Code = request.args.get("Emp_Code")
    data = todolist_service.get_request_list(Emp_Id)
    sum_res =  todolist_service.get_sum_sale(Emp_Code)
    return render_template("todolist.html",Emp_Position=Emp_Position,Emp_Code=Emp_Code,request_list = data,sum_res=sum_res)

@app.route('/request')
def request_page():
    Emp_Code = request.args.get("Emp_Code")
    data = todolist_service.get_customer(Emp_Code)
    return render_template("request.html",customer_list=data)


@app.route('/api/check_userlogin',methods=['POST'])
def check_login():
    try:
        result=api_result.api_result()
        username = request.json.get('username')
        password = request.json.get('password')
        res , data = login_service.check_login(username,password)
        result.data = data
        result.success = res
        if res :
            result.message = "complete"
        else:
            result.message = "failed"
    except Exception as e:
        result.success = False
        result.message = "failed"
        result.error = e
    return jsonify(result.__dict__)

@app.route('/api/get_customer')
def get_customer():
    try:
        result=api_result.api_result()
        sale_code = request.args.get("Emp_Code")
        data = todolist_service.get_customer(sale_code)
        result.data = data
        result.success = True
        result.message = "complete"
        
    except Exception as e:
        result.success = False
        result.message = "failed"
        result.error = e
    return jsonify(result.__dict__)
    
@app.route('/api/get_customer_id')
def get_customer_id():
    try:
        result=api_result.api_result()
        customer_id = request.args.get("customer_id")
        data = todolist_service.get_customer_id(customer_id)
        result.data = data
        result.success = True
        result.message = "complete"
        
    except Exception as e:
        result.success = False
        result.message = "failed"
        result.error = e
    return jsonify(result.__dict__)
    
@app.route('/api/get_sum_customer')
def get_sum_customer():
    try:
        result=api_result.api_result()
        cust_code = request.args.get("cust_code")
        sale_code = request.args.get("sale_code")
        data = todolist_service.get_sum_customer(cust_code,sale_code)
        result.data = data
        result.success = True
        result.message = "complete"
        
    except Exception as e:
        result.success = False
        result.message = "failed"
        result.error = e
    return jsonify(result.__dict__)   
    
@app.route('/api/get_sum_customer2')
def get_sum_customer2():
    try:
        result=api_result.api_result()
        cust_id = request.args.get("cust_id")
        sale_id = request.args.get("sale_id")
        data = todolist_service.get_sum_customer2(cust_id,sale_id)
        result.data = data
        result.success = True
        result.message = "complete"
        
    except Exception as e:
        result.success = False
        result.message = "failed"
        result.error = e
    return jsonify(result.__dict__)   
    
@app.route('/api/create_request' , methods=['POST'])
def create_request():
    try:
        result=api_result.api_result()
        request_no = request.json.get("request_no")
        cust_id = request.json.get("cust_id")
        sale_id = request.json.get("sale_id")
        sum_a = request.json.get("sum_a")
        sum_b = request.json.get("sum_b")
        rate_b_percent = request.json.get("rate_b_percent")
        sum_c = request.json.get("sum_c")
        bank_acc_sale = request.json.get("bank_acc_sale")
        sale_comment = request.json.get("sale_comment")
        login_name = request.json.get("login_name")
        
        data = todolist_service.create_request(request_no, cust_id, sale_id, sum_a, sum_b, rate_b_percent, sum_c, bank_acc_sale, sale_comment, login_name)
        result.data = data
        result.success = True
        result.message = "complete"
        
    except Exception as e:
        result.success = False
        result.message = "failed"
        result.error = e
    return jsonify(result.__dict__)   