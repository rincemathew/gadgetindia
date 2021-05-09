const searchField = document.querySelector("#searchField");

searchField.addEventListener('keyup',(e)=>{
const searchValue = e.target.value;
if(searchValue.trim().length>0){
console.log("searchValue",searchValue)
console.log("fieldsdfsfdd")
document.getElementById("searchField").name.value = "real";

fetch("search_query",{
body: JSON.stringify({searchText: searchValue}),
method: "POST"
})
.then((res) => res.json())
.then((data) => {
console.log("comeon")
console.log("data", data)
});
}
});
/* index.html */
/* $('#left-button').click(function() {
    event.preventDefault();
    $('#content-inside').animate({
      scrollLeft: "-=100px"
    }, "slow");
  });

   $('#right-button').click(function() {
    event.preventDefault();
    $('#content-inside').animate({
     scrollLeft: "+=100px"
    }, "slow");
  }); */
