from app.app import *


def check_login(username, password):
    session = Session()
    try:
        query = text("SELECT * FROM view_set_employee WHERE Emp_UUser = :username AND Emp_PPass = :password AND Emp_Position <> 5")

        result = session.execute(query, {"username": username, "password": password}).fetchone()
        columns = ["Emp_Id", "Emp_Code", "Emp_Prefix", "Emp_Name", "Emp_Nickname",
            "Emp_Position", "Emp_Dept", "Emp_StartDate", "Emp_Tel", "Emp_Status",
            "Emp_UUser", "Emp_PPass", "Gold_SO", "Dept_Name", "PST_Name"]
        if result != None:
            employee_dict = dict(zip(columns, result))
            print("Login successful")
            return True,employee_dict 
        else:
            print("Login failed")
            return False,{}
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        session.close()