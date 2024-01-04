from marshmallow import Schema, fields

class RequestListSchema(Schema):
    Request_Id = fields.Integer()
    Request_No = fields.String()
    Cust_Id = fields.Integer()
    Sale_Id = fields.Integer()
    RStatus_Approve = fields.String()
    RStatus_Pay = fields.String()
    Sum_A = fields.Decimal()
    Sum_B = fields.Decimal()
    RateB_Percen = fields.Decimal()
    Sum_C = fields.Decimal()
    Sale_BankAcc = fields.String()
    Sale_Comment = fields.String()
    Sum_D_Type = fields.String()
    Sum_D_Percen = fields.Decimal()
    Sum_D = fields.Decimal()
    D_Approve = fields.String()
    D_Approve_Date = fields.DateTime()
    D_Comment = fields.String()
    Sum_E_Type = fields.String()
    Sum_E_Percen = fields.Decimal()
    Sum_E = fields.Decimal()
    E_Approve = fields.String()
    E_Approve_Date = fields.DateTime()
    E_Comment = fields.String()
    Created_Date = fields.DateTime()
    Created_By = fields.String()
    Updated_Date = fields.DateTime()
    Updated_By = fields.String()
    Cust_Code = fields.String()
    Cust_Name = fields.String()
    Cust_Add1 = fields.String()
    Cust_Add2 = fields.String()
    Cust_Add3 = fields.String()
    Cust_Province = fields.String()
    Cust_Zipcode = fields.String()
    Cust_Contact1 = fields.String()
    Cust_Contact2 = fields.String()
    Cust_Tel1 = fields.String()
    Cust_Tel2 = fields.String()
    Cust_RefSaleCode = fields.String()
    Emp_Code = fields.String()
    Emp_Name = fields.String()
    Gold_SO = fields.Decimal()
    # Add any other fields as needed



    