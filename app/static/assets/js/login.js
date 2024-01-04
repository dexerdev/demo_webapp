function checklogin(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var jsondata = JSON.stringify({
        "username": username,
        "password": password,

    });
    fetch("/api/check_userlogin", {
        method: "POST",
        body: jsondata,
        headers: {
            "Content-type": "application/json"
        }
    }).then(response => response.json()).then((data) => {
        console.log(data.data);
        if (data.success) {
            Swal.fire({
                title: 'ยินดีต้อนรับเข้าสู่ระบบ',
                icon: 'success',
                showconfirmbutton: true,
                allowoutsideclick: false,
                allowescapekey: false
            }).then(function () {
                document.cookie = "Emp_Code=" + data.data.Emp_Code;
                document.cookie = "Emp_Id=" + data.data.Emp_Id;
                document.cookie = "Emp_Position=" + data.data.Emp_Position;
                document.cookie = "username=" + username;
                window.location.href = "/todolist?Emp_Id="+ data.data.Emp_Id + "&Emp_Position="+data.data.Emp_Position + "&Emp_Code="+data.data.Emp_Code;
            });
        } else {
            Swal.fire(
                'เข้าสู่ระบบผิดพลาด',
                data.message,
                'error'
            );
        }
    });
}