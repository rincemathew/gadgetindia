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