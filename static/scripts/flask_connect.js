class Person{
    constructor(name,email){
        this.name=name;
        this.email=email;
    }
}

function submitFormData(){

    let name=document.getElementById("username").value;
    let email=document.getElementById("email").value;
    let p1 = new Person(name,email);
    let form_JSON=JSON.stringify(p1);
    //console.log(form_JSON);
    const xhttp = new XMLHttpRequest();
    xhttp.onload=function(){
        document.getElementById("username").value="";
        document.getElementById("email").value="";
        document.getElementById("responseText").innerText = this.responseText;
    }
    xhttp.open("POST","/addUser");
    xhttp.setRequestHeader("Content-Type","application/json");
    xhttp.send(form_JSON);

}