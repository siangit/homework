//  먼저 form 제출시 새로고침 방지
const form = document.getElementById("form")

form.addEventListener("submit",
function(e){e.preventDefault();
    // 입력값 받기
    let nick = document.getElementById("nick");
    console.log(nick.value);

    let pw1 = document.getElementById("pw1");
    console.log(pw1.value);

    let pw2 = document.getElementById("pw2");
    console.log(pw2.value);

    let name = document.getElementById("name");
    console.log(name.value);

    let num = document.getElementById("num");
    console.log(num.value);

    let job = document.getElementById("job");
    console.log(job.value);

    let gender = document.querySelector('input[name="gender"]:checked');
    console.log(gender.value)

    let email = document.getElementById("email").value;
    let address = document.getElementById("address").value;
    let fullemail =`${email}@${address}`
    console.log(fullemail)
    let info = document.getElementById("info");
    console.log(info.value); 


    // 입력값 문제 인식
    //return을 사용하면 조건이 만족하지 않으면 코드실행을 immediately 멈추고 더 이상 진행 안함
    if(nick.value.length <5){alert("아이디가 너무 짧습니다.")
return};
    if(pw1.value!=pw2.value){alert("입력하신 비밀번호가 일치하지 않습니다")
return}

    //환영인사
    document.body.innerHTML =""
    const done = document.createElement("h1")
    done.textContent = "가입을 환영합니다!"
    document.body.appendChild(done)



})