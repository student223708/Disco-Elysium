let x = true;
let side = document.getElementsByClassName("sidebar_zone");
let main = document.getElementsByTagName("main");
let filler = document.getElementsByClassName("sidebar_filler");
let button = document.getElementsByClassName("sidebar_button");


function hideNav() {
  if (x==true)
  {
  //document.getElementsByClassName("sidebar_zone").style.width = "280px";
  //document.getElementsByTagName("main").style.marginLeft = "280px";

  side[0].style.width="0px";
  filler[0].style.visibility="visible";

  setTimeout(() => {
  side[0].style.visibility="hidden";
}, 1);

  main[0].style.marginLeft="280px";
  filler[0].style.width="80px";
  
  button[0].style.marginLeft="-200px";


  x=false;
  }
  else{
  //document.getElementsByClassName("sidebar_zone").style.width = "0";
  //document.getElementsByTagName("main").style.marginLeft = "0";

  side[0].style.width="280px";
  main[0].style.marginLeft="0px";
  filler[0].style.width="280px";
  filler[0].style.visibility="hidden";

setTimeout(() => {
  side[0].style.visibility="visible";
}, 499);
  
  button[0].style.marginLeft="-0px";

  x=true;
  }
}

//TO DO: click spam bug