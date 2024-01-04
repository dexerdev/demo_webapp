function getcookies(cname){
    var name=cname+"=";
    var decodecookies=decodeURIComponent(document.cookie);
    var cookiesarray=decodecookies.split(";");
    for (var i=0;i<cookiesarray.length;i++){
        var c=cookiesarray[i];
        while (c.charAt(0)==" "){
            c=c.substring(1);
        }
        if (c.indexOf(name)==0){
            return c.substring(name.length,c.length);
        }
    }
    return "";
}
var username = getcookies("username");
document.getElementById("navUsername").innerHTML = username;