let menu = document.querySelector(".burger_menu_button")
menu.onclick = function() { ChangeActive() }

function ChangeActive(){
    let menuList = document.querySelector(".menu_list")
    if(menuList.classList.contains("active")){
        menuList.classList.remove("active")
        menu.classList.remove("burger_active")
    }
    else{
        menuList.classList.add("active")
        menu.classList.add("burger_active")
    }
}