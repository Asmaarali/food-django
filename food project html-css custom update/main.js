// ---------------------custom nav with scroll--------------


const sections = document.querySelectorAll("section");
const navLi = document.querySelectorAll(".menu a");
window.addEventListener("scroll", () => {
  let current = "";
  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;
    if (pageYOffset >= sectionTop - 70) {
      current = section.getAttribute("id");
    }
  });

  navLi.forEach((a) => {
    a.classList.remove("active");
    if (a.classList.contains(current)) {
      a.classList.add("active");
    }
  });
});






//back to top


let backtobtn=document.querySelector('.back-to-top')
window.onscroll = () => {
    if(document.documentElement.scrollTop > 200){
        backtobtn.style.display='flex';
    } 
    else{
        backtobtn.style.display='none';

    }
}


                //top nav menu

// let menuitems=document.getElementsByClassName('menu-item')
// Array.from(menuitems).forEach((item,index)=>{
//     item.onclick=(e)=>{
//             let currmenu=document.querySelector('.menu-item.active')
//             currmenu.classList.remove('active')
//             item.classList.add('active')
//     }
// })

                 // food category

let foodMenuList = document.querySelector('.food-item-wrap')

let foodCategory = document.querySelector('.food-category')

let categories = foodCategory.querySelectorAll('button')

Array.from(categories).forEach((item, index) => {
    item.onclick = (e) => {
        let currCat = foodCategory.querySelector('button.active')
        currCat.classList.remove('active')
        e.target.classList.add('active')
        foodMenuList.classList ='food-item-wrap '+ e.target.getAttribute('data-food-type')
    }
})


                // on scroll animation

let scroll = window.requestAnimationFrame || function(callback) {window.setTimeout(callback, 1000/60)}

let elToShow = document.querySelectorAll('.play-on-scroll')

isElInViewPort = (el) => {
    let rect = el.getBoundingClientRect()

    return (
        (rect.top <= 0 && rect.bottom >= 0)
        ||
        (rect.bottom >= (window.innerHeight || document.documentElement.clientHeight) && rect.top <= (window.innerHeight || document.documentElement.clientHeight))
        ||
        (rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight))
    )
}

loop = () => {
    elToShow.forEach((item, index) => {
        if (isElInViewPort(item)) {
            item.classList.add('start')
        } else {
            item.classList.remove('start')
        }
    })

    scroll(loop)
}

loop()



             // mobile nav

// let bottomNavItems = document.querySelectorAll('.mb-nav-item')

// let bottomMove = document.querySelector('.mb-move-item')

// bottomNavItems.forEach((item, index) => {
//     item.onclick = (e) => {
//         console.log('object')
//         let crrItem = document.querySelector('.mb-nav-item.active')
//         crrItem.classList.remove('active')
//         item.classList.add('active')

//         bottomMove.style.left = index * 25 + '%'
//     }
// })

// -----------------------------------custom nav scroll for mobile-------------------
const section = document.querySelectorAll("section");
const navL = document.querySelectorAll(".mb-nav div");
const bottomMove = document.querySelector('.mb-move-item')
const bottomNavItems = document.querySelectorAll('.mb-nav-item')


window.addEventListener("scroll", () => {
  let current = "";
  section.forEach((section) => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;
    if (pageYOffset >= sectionTop-70) {
      current = section.getAttribute("id");
    }
  });



  navL.forEach((div) => {
    div.classList.remove("active");
    if (div.classList.contains(current)) {
      div.classList.add("active");
    }
  });


            //for moving div nav

  bottomNavItems.forEach((item, index) => {
    if(item.classList.contains(current)){

      bottomMove.style.left = index * 25 + '%'
  }
})



});



