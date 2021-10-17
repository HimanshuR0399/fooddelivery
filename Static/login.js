function come_in() {
    var div1 = document.getElementById('target');
    div1.innerHTML = "<img src='static/donut1.gif' alt='scooter.png' height='200px'>"
    div1.classList = 'come'
    // document.body.appendChild(div1);
}
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
} async function login() {
    var div1 = document.getElementById('target');
    div1.className = "popup1"
    await sleep(550)
    div1.innerHTML = "<h1>Log In</h1><label>Username</label><input type='text' size='17'><br><label>Password</label><input type='password' size='17'> <br><br><button onclick = 'click_signup()'>Sign Up</button><button>Log in</button>"
}
async function signup() {
    var div1 = document.getElementById('target');
    div1.className = "popup2"
    await sleep(550)
    div1.innerHTML = `<h1>Sign Up</h1>
    <label style = 'margin-top = 1px;'>Full Name</label>
    <input type='text' id = "name" size='17' style = 'margin-top = 1px;'>
    <br>
    <label style = 'margin-top = 1px;'>Gender</label>
    <br><input type='radio' name='gender' style = 'margin-top = 1px;'><label style = 'margin-top = 1px;' value "M">Male</label>
    <input type='radio' name='gender' style = 'margin-top = 1px;'><label style = 'margin-top = 1px;' value = "F">Female</label>
    <input type='radio' name='gender' style = 'margin-top = 1px;'><label style = 'margin-top = 1px;' value = "O">Other</label>
    <br><label style = 'margin-top = 1px;'>Contact number</label><input type='text' size='10' style = 'margin-top = 1px;' id = "contact">
    <br><label style = 'margin-top = 1px;'>Username</label><input type='text' size='17' id = "username" style = 'margin-top = 1px;'>
    <label style = 'margin-top = 1px;' >Password</label><input type='password' size='17' style = 'margin-top = 1px;' id = "password">
    <br><label style = 'margin-top = 1px;' >Confirm Password</label><input type='password'id = "cpassword" size='17' style = 'margin-left: 10px'> 
    <br><br><button onclick = 'click_login()' style = 'margin-top:10px;'>Log in</button>
    <button style = 'margin-top:10px;' onclick = 'site_signup()'>Sign up</button>`
}
async function popup(action) {
    var div1 = document.getElementById('target');
    await sleep(550);
    while (div1.firstChild) {
        div1.removeChild(div1.lastChild);
    }

    action()
}
async function godown() {
    var div1 = document.getElementById('target');
    while (div1.firstChild) {
        div1.removeChild(div1.lastChild);

    }
    div1.className = "popdown"
    await sleep(550)
    div1.innerHTML = "<img src='static/donut1.gif' alt='scooter.png' height='200px'>"
    div1.className = "go"
    await sleep(550)
    while (div1.firstChild) {
        div1.removeChild(div1.lastChild);

    }

}
async function click_login() {
    godown()
    await sleep(1200)
    come_in()
    popup(login)
}
async function click_signup() {
    godown()
    await sleep(1200)
    come_in()
    popup(signup)
}
function site_signup(){
    var data = {}
    data['name'] = document.getElementById('name').value;
    data['gender'] = $("input[type='radio'][name='gender']:checked").val();
    data['contact'] = document.getElementById('contact').value;
    data['username'] = document.getElementById('username').value;
    data['password'] = document.getElementById('password').value;
    data['cpassword'] = document.getElementById('cpassword').value;
    const encodeQueryData = (datas) =>{
        const ret = [];
        for (let d in datas)
          ret.push(encodeURIComponent(d) + '=' + encodeURIComponent(datas[d]));
        return ret.join('&');
     }
    url = '/login/signup'
    var http = new XMLHttpRequest();
    http.open('POST', url, true);

//Send the proper header information along with the request
http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

http.onreadystatechange = function() {//Call a function when the state changes.
    if(http.readyState == 4 && http.status == 200) {
        message = document.createElement('div');
        message.innerHTML = `'<div class="alert alert-' + type + ' alert-dismissible" role="alert">` + http.responseText + `<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>`;
        document.body.appendChild(message)
    }
}
http.send(encodeQueryData(data));

// start from herer


}
come_in();
popup(login)
