/* news list in horizontal list */
$('#left-button-news').click(function() {
    event.preventDefault();
    $('#content-inside-news').animate({
      scrollLeft: "-=100px"
    }, "slow");
  });
  
   $('#right-button-news').click(function() {
    event.preventDefault();
    $('#content-inside-news').animate({
     scrollLeft: "+=100px"
    }, "slow");
  });

  /* howto list in horizontal list */
$('#left-button-howto').click(function() {
    event.preventDefault();
    $('#content-inside-howto').animate({
      scrollLeft: "-=100px"
    }, "slow");
  });
  
   $('#right-button-howto').click(function() {
    event.preventDefault();
    $('#content-inside-howto').animate({
     scrollLeft: "+=100px"
    }, "slow");
  });

  /* reviews list in horizontal list */
$('#left-button-reviews').click(function() {
    event.preventDefault();
    $('#content-inside-reviews').animate({
      scrollLeft: "-=100px"
    }, "slow");
  });
  
   $('#right-button-reviews').click(function() {
    event.preventDefault();
    $('#content-inside-reviews').animate({
     scrollLeft: "+=100px"
    }, "slow");
  });