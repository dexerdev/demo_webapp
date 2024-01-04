from app.app import ma

class EmployeeSchema(ma.Schema):
    class Meta:
        fields = (
            "Emp_Id", "Emp_Code", "Emp_Prefix", "Emp_Name", "Emp_Nickname",
            "Emp_Position", "Emp_Dept", "Emp_StartDate", "Emp_Tel", "Emp_Status",
            "Emp_UUser", "Emp_PPass", "Gold_SO", "Dept_Name", "PST_Name"
        )
        
