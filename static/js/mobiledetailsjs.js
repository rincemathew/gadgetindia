/* color select */ 
$('#dropDownColor').change(function () {
  var indexNumber = $("#dropDownColor").prop('selectedIndex');
  indexNumber++;
  for (var i = 1; i <= arrlength; i++) {
    if (i == indexNumber) {
      $('#' + i).show('slow');
    } else {
      $('#' + i).hide();
    }
  }
});

$(document).ready(function(){
for (var i = 1; i <= arrlength; i++) {
  if (i == 1) {
    $('#' + i).show();
  } else {
    $('#' + i).hide();
  }
}
});

// $('#carouselExampleControls').carousel({interavel:500});
// window.initializeCarousel=()=>{
//   console.log('comein')
//   $('#carouselExampleControls').carousel({interavel:500});
// }


/* picture scroll */ 
$('#left-button-scroll').click(function() {
  event.preventDefault();
  $('#content-inside-scroll').animate({
    scrollLeft: "-=100px"
  }, "slow");
});

 $('#right-button-scroll').click(function() {
  event.preventDefault();
  $('#content-inside-scroll').animate({
   scrollLeft: "+=100px"
  }, "slow");
});

/* popover */
$('.popover-dismiss').popover({
  trigger: 'focus'
})