from app.app import *

def get_request_list(sale_id):
    session = Session()
    try:
        # Execute the query
        query = text("""
            SELECT *
            FROM View_Request_List
            WHERE Sale_Id = :sale_id
            ORDER BY Created_Date DESC, RStatus_Approve;
        """)
        result = session.execute(query, {"sale_id": sale_id}).fetchall()
        columns = ["Request_Id","Request_No","Cust_Id","Sale_Id","RStatus_Approve","RStatus_Pay","Sum_A","Sum_B","RateB_Percen","Sum_C","Sale_BankAcc","Sale_Comment","Sum_D_Type","Sum_D_Percen","Sum_D","D_Approve","D_Approve_Date","D_Comment","Sum_E_Type","Sum_E_Percen","Sum_E","E_Approve","E_Approve_Date","E_Comment","Created_Date","Created_By","Updated_Date","Updated_By","Cust_Code","Cust_Name","Cust_Add1","Cust_Add2","Cust_Add3","Cust_Province","Cust_Zipcode","Cust_Contact1","Cust_Contact2","Cust_Tel1","Cust_Tel2","Cust_RefSaleCode","Emp_Code","Emp_Name","Gold_SO"]
        data = [dict(zip(columns, row)) for row in result]
        return data
    except Exception as e:
        # Handle exceptions
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()
        
def get_customer(sale_code):
    session = Session()
    try:
        # Execute the query
        query = text("""
            select * 
            from View_Set_Customer
            where Cust_RefSaleCode = :sale_code
            order by Cust_Name;
        """)
        result = session.execute(query, {"sale_code": sale_code}).fetchall()
        columns = ["Cust_Id","Cust_Code","Cust_Name","Cust_Type","Cust_ShortName","Cust_TaxNo","Cust_Add1","Cust_Add2","Cust_Add3","Cust_Province","Cust_Zipcode","Cust_Contact1","Cust_Contact2","Cust_Tel1","Cust_Tel2","Cust_Group","Cust_RefSaleCode","Cust_Area","Cust_Status","Comp_Id","CSize","CSizeName","CUnder","CLevel","CSaleType","CDisBeforePT","CDisBeforePTABC","CDisBeforePTAll","CDisHighENG","CDisHighTH","CDisLibrary","CDisEdu","CDisDict","CDisImpProd","Emp_Id","Emp_Code","Emp_Name"]
        data = [dict(zip(columns, row)) for row in result]
        return data
    except Exception as e:
        # Handle exceptions
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

def get_customer_id(get_customer_id):
    session = Session()
    try:
        # Execute the query
        query = text("""
            select * 
            from View_Set_Customer
            where Cust_Id = :get_customer_id
            order by Cust_Name;
        """)
        result = session.execute(query, {"get_customer_id": get_customer_id}).fetchone()
        columns = ["Cust_Id","Cust_Code","Cust_Name","Cust_Type","Cust_ShortName","Cust_TaxNo","Cust_Add1","Cust_Add2","Cust_Add3","Cust_Province","Cust_Zipcode","Cust_Contact1","Cust_Contact2","Cust_Tel1","Cust_Tel2","Cust_Group","Cust_RefSaleCode","Cust_Area","Cust_Status","Comp_Id","CSize","CSizeName","CUnder","CLevel","CSaleType","CDisBeforePT","CDisBeforePTABC","CDisBeforePTAll","CDisHighENG","CDisHighTH","CDisLibrary","CDisEdu","CDisDict","CDisImpProd","Emp_Id","Emp_Code","Emp_Name"]
        data = dict(zip(columns, result))
        return data
    except Exception as e:
        # Handle exceptions
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()
        
def get_sum_customer(cust_code,sale_code):
    session = Session()
    try:
        # Execute the query
        query = text("""
            select WSale_Name , Sum(Item_Total) as Item_Total , 
            Sum(Discount) as Discount , Sum(NetTotal) as NetTotal 
            from View_SO_NetTotal
            where so_status <> 13 and 
            Year = year(getdate())-1 and
            Cust_Code=  :cust_code and
            WSale_Code = :sale_code
            group by WSale_Name	;
        """)
        result = session.execute(query, {"sale_code": sale_code,"cust_code":cust_code}).fetchone()
        if result != None :
            columns = ["WSale_Name","Item_Total","Discount","NetTotal"]
            data = dict(zip(columns, result))
        else:
            data = {}
        return data
    except Exception as e:
        # Handle exceptions
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()
    
    

def get_sum_customer2(cust_id,sale_id):
    session = Session()
    try:
        # Execute the query
        query = text("""
            select Cust_Code , Cust_Name , Emp_Code , Emp_Name , Gold_So , 
            Sum(Sum_C) as Sum_C , Sum(Sum_D) as Sum_D , Sum(Sum_E) as Sum_E
            from View_Request_List
            where RStatus_Approve = 5 and Cust_id = :cust_id and Sale_id = :sale_id
            group by Cust_Code , Cust_Name , Emp_Code , Emp_Name , Gold_So
        """)
        result = session.execute(query, {"sale_id": sale_id,"cust_id":cust_id}).fetchone()
        if result != None :
            columns = ["Cust_Code","Cust_Name","Emp_Code","Emp_Name","Gold_So","Sum_C","Sum_D","Sum_E"]
            data = dict(zip(columns, result))
        else:
            data = {}
        return data
    except Exception as e:
        # Handle exceptions
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()
    

def create_request(request_no, cust_id, sale_id, sum_a, sum_b, rate_b_percent, sum_c, bank_acc_sale, sale_comment, login_name):
    try:
        session = Session()
        current_time = datetime.datetime.now()
        query = """
            INSERT INTO Request_List (
                Request_No, Cust_Id, Sale_Id, RStatus_Approve, RStatus_Pay,
                Sum_A, Sum_B, RateB_Percen, Sum_C, Sale_BankAcc, Sale_Comment,
                Created_Date, Created_By, Updated_Date, Updated_By
            ) VALUES (
                :request_no, :cust_id, :sale_id, 1, 1, :sum_a, :sum_b, :rate_b_percent,
                :sum_c, :bank_acc_sale, :sale_comment, :current_time, :login_name,
                :current_time, :login_name
            )
        """
        session.execute(text(query), {
            'request_no': request_no,
            'cust_id': cust_id,
            'sale_id': sale_id,
            'sum_a': sum_a,
            'sum_b': sum_b,
            'rate_b_percent': rate_b_percent,
            'sum_c': sum_c,
            'bank_acc_sale': bank_acc_sale,
            'sale_comment': sale_comment,
            'current_time': current_time,
            'login_name': login_name
        })
        session.commit()
        return True  # or return some meaningful response
    except SQLAlchemyError as e:
        session.rollback()
        print(e)
        return False  # or return an error response
    
    
# def get_requestno(request_no):
#     session = Session()
#     try:
#         # Execute the query
#         query = text("""
#             select Cust_Code , Cust_Name , Emp_Code , Emp_Name , Gold_So , 
#             Sum(Sum_C) as Sum_C , Sum(Sum_D) as Sum_D , Sum(Sum_E) as Sum_E
#             from View_Request_List
#             where RStatus_Approve = 5 and Cust_id = :cust_id and Sale_id = :sale_id
#             group by Cust_Code , Cust_Name , Emp_Code , Emp_Name , Gold_So
#         """)
#         result = session.execute(query, {"request_no"}).fetchone()
#         if result != None :
#             columns = ["Cust_Code","Cust_Name","Emp_Code","Emp_Name","Gold_So","Sum_C","Sum_D","Sum_E"]
#             data = dict(zip(columns, result))
#         else:
#             data = {}
#         return data
#     except Exception as e:
#         # Handle exceptions
#         return jsonify({"error": str(e)}), 500
#     finally:
#         session.close()