function getCustomer() {
    var Emp_Code = getcookies("Emp_Code");
    var tbody = document.getElementById('tbCustomerList');
    fetch('/api/get_customer?Emp_Code=' + Emp_Code).then(respoinse => respoinse.json()).then((data) => {
        for (var i = 0; i < data.data.length; i++) {
            debugger;
            var customer = data.data[i];
            var row = tbody.insertRow();
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            var cell3 = row.insertCell(2);
            var cell4 = row.insertCell(3);
            var cell5 = row.insertCell(4);
            var cell6 = row.insertCell(5);
            var cell7 = row.insertCell(6);
            var cell8 = row.insertCell(7);
            var cell9 = row.insertCell(8);
            var cell10 = row.insertCell(9);
            var cell11 = row.insertCell(10);
            var cell12 = row.insertCell(11);
            var cell13 = row.insertCell(12);
            cell1.innerHTML = "<td class='text-center'>" + '<button class="btn btn-primary" onclick="selectCustomer(' + customer.Cust_Code + ')">เลือก</button>' + "</td>"
            cell2.innerText = customer.Cust_Code;
            cell3.innerText = customer.Cust_Name;
            var type = "";
            if (customer.Cust_Type == 1) {
                type = "ลูกค้าหลัก";
            } else {
                type = "ลูกค้าของลูกค้า";
            }
            cell4.innerText = type;
            cell5.innerText = customer.Cust_Province;
            cell6.innerText = customer.Cust_Add1;
            cell7.innerText = customer.Cust_Add2;
            cell8.innerText = customer.Cust_Add3;
            cell9.innerText = customer.Cust_ZipCode;
            cell10.innerText = customer.Cust_Contact1;
            cell11.innerText = customer.Cust_Contact2;
            cell12.innerText = customer.Cust_Tel1;
            cell13.innerText = customer.Cust_Tel2;
        }
        $("#tbCustomer").DataTable({
            "paging": true,
            "searching": true,
            "ordering": true,
            "responsive": true,
        });
        $("#modalCustomer").modal("show");
    });
}

function selectCustomer(Cust_Code){
    
}