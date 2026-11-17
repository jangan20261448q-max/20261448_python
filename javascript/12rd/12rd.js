

const btn = document.getElementById("btn");

// Let btn listen for click
btn.addEventListener("click", myfunction);
btn.addEventListener("dblclick", myfunctionB);
btn.addEventListener("mouseover", myfunctionC);

function myfunction() {
    document.getElementById("demo").innerHTML = "클릭";
}

function myfunctionB() {
    document.getElementById("demo").innerHTML = "더블 클릭";
}

function myfunctionC() {
    document.getElementById("demo").innerHTML = "마우스 오버";
}
