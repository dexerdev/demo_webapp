var Emp_Code = getcookies("Emp_Code");
var Emp_Id = getcookies("Emp_Id");
var username = getcookies("username");
var Emp_Position = getcookies("Emp_Position");
function selectCustomer(customer_id) {

    fetch('/api/get_customer_id?customer_id=' + customer_id).then(response => response.json()).then((data) => {
        var customer_data = data.data;
        document.getElementById('Cust_Code').value = customer_data.Cust_Code;
        document.getElementById('Cust_Name').value = customer_data.Cust_Name;
        document.getElementById('Cust_Type').value = customer_data.Cust_Type;
        document.getElementById('Cust_Province').value = customer_data.Cust_Province;
        document.getElementById('Cust_Add1').value = customer_data.Cust_Add1;
        document.getElementById('Cust_Add2').value = customer_data.Cust_Add2;
        document.getElementById('Cust_ZipCode').value = customer_data.Cust_ZipCode;
        document.getElementById('Cust_Contact1').value = customer_data.Cust_Contact1;
        document.getElementById('Cust_Tel1').value = customer_data.Cust_Tel1;
        document.getElementById('Cust_Tel2').value = customer_data.Cust_Tel2;
        var sum_Item_Total = 0;
        var percentage = parseInt(document.getElementById("percentage").value) / 100;

        fetch('/api/get_sum_customer?sale_code=' + Emp_Code + "&cust_code=" + customer_data.Cust_Code).then(res => res.json()).then((data_2) => {
            var sum1 = data_2.data;
            if (isEmptyObject(sum1)) {
                document.getElementById('total_1').value = 0;
                document.getElementById('disc_1').value = 0;
                document.getElementById('nettotal_1').value = 0;
            }
            else {
                sum_Item_Total = sum1.Item_Total;
                document.getElementById('net_a').value = sum_Item_Total;
                document.getElementById('net_b').value = ((sum_Item_Total - (sum_Item_Total * 0.25)) * percentage)
                document.getElementById('total_1').value = sum1.Item_Total;
                document.getElementById('disc_1').value = sum1.Discount;
                document.getElementById('nettotal_1').value = sum1.NetTotal;
            }
        });
        fetch('/api/get_sum_customer2?sale_id=' + Emp_Id + "&cust_id=" + customer_id).then(res => res.json()).then((data_3) => {
            var sum3 = data_3.data;
            if (isEmptyObject(sum3)) {
                document.getElementById('sum_c').value = 0;
                document.getElementById('sum_d').value = 0;
                document.getElementById('sum_e').value = 0;
            }
            else {
                document.getElementById('sum_c').value = sum3.Sum_C;
                document.getElementById('sum_d').value = sum3.Sum_D;
                document.getElementById('sum_e').value = sum3.Sum_E;
            }
        });
        //     id="hidden_cust_id">
        // <input type="hidden" id="hidden_sale_id">
        // <input type="hidden" id="hidden_login_name"></input>
        document.getElementById('hidden_cust_id').value = customer_id;
        document.getElementById('hidden_sale_id').value = Emp_Id;
        document.getElementById('hidden_login_name').value = username;
        $("#modalCustomer").modal("hide");
    })

}
function recal_net_b() {
    var percentage = parseInt(document.getElementById("percentage").value) / 100;
    var sum_Item_Total = parseFloat(document.getElementById('net_a').value);
    document.getElementById('net_b').value = ((sum_Item_Total - (sum_Item_Total * 0.25)) * percentage);
}

function clear_request() {
    Swal.fire({
        title: "ยืนยัน ปิดการสร้างใบขออนุเคราะห์ ใช่หรือไม่?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Yes"
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/todolist?Emp_Id=" + Emp_Id + "&Emp_Position=" + Emp_Position + "&Emp_Code=" + Emp_Code;
        }
    })
}

function create_request() {
    var Request_No = "REQ";
    var today = new Date();
    var year = today.getFullYear().toString();
    year = year.slice(-2);
    var month = String(today.getMonth() + 1).padStart(2, "0");
    const randomNumber = Math.floor(Math.random() * 1000);
    var number = String(randomNumber).padStart(3, '0');
    Request_No += year + month + number
    var customer_id = document.getElementById('hidden_cust_id').value;
    var Emp_Id = document.getElementById('hidden_sale_id').value;
    var username = document.getElementById('hidden_login_name').value;
    var sum_a = document.getElementById('net_a').value;
    var sum_b = document.getElementById('net_b').value;
    var sum_c = document.getElementById('net_c').value;
    var sale_comment = document.getElementById('sale_comment').value;
    var bank_acc_sale = document.getElementById('bankaccount').value;
    var rate_b_percent = document.getElementById('percentage').value;
    var json_data = JSON.stringify({
        "request_no": Request_No,
        "cust_id": customer_id,
        "sale_id": Emp_Id,
        "sum_a": sum_a,
        "sum_b": sum_b,
        "rate_b_percent": rate_b_percent,
        "sum_c": sum_c,
        "bank_acc_sale": bank_acc_sale,
        "sale_comment": sale_comment,
        "login_name": username
    });
    console.log(json_data);
    Swal.fire({
        title: "ยืนยัน บันทึกสร้างใบขออนุเคราะห์ ใช่หรือไม่?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Yes"
    }).then((result) => {

        if (result.isConfirmed) {
            fetch("/api/create_request", {
                method: "POST",
                body: json_data,
                headers: {
                    "Content-type": "application/json; charset=utf-8"
                }
            }).then(response => response.json()).then((data) => {
                if (data.success) {
                    Swal.fire({
                        title: "บันทึกสำเร็จ",
                        icon: "success",
                        showconfirmbutton: true

                    }).then(function () {
                        window.location.href = "/todolist?Emp_Id=" + Emp_Id + "&Emp_Position=" + Emp_Position + "&Emp_Code=" + Emp_Code;
                    })
                }
                else {
                    Swal.fire(
                        "บันทึกไม่สำเร็จ",
                        "",
                        "error"
                    );
                }
            })
        }
    })
}

function isEmptyObject(obj) {
    return Object.keys(obj).length === 0 && obj.constructor === Object;
}