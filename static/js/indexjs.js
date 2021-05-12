/* brand list in horizontal list */
$('#left-button').click(function() {
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
  });

/* new phone list in horizontal list */
$('#left-button-new').click(function() {
    event.preventDefault();
    $('#content-inside-new').animate({
      scrollLeft: "-=100px"
    }, "slow");
  });

   $('#right-button-new').click(function() {
    event.preventDefault();
    $('#content-inside-new').animate({
     scrollLeft: "+=100px"
    }, "slow");
  });
/* make the first option of <select> selected with jQuery */
  $("#target").val($("#target option:first").val());

/* budget phone list in horizontal list */
$('#left-button-budget').click(function() {
  event.preventDefault();
  $('#content-inside-budget').animate({
    scrollLeft: "-=100px"
  }, "slow");
});

 $('#right-button-budget').click(function() {
  event.preventDefault();
  $('#content-inside-budget').animate({
   scrollLeft: "+=100px"
  }, "slow");
});

/* articles list in horizontal list */
$('#left-button-review').click(function() {
  event.preventDefault();
  $('#content-inside-review').animate({
    scrollLeft: "-=100px"
  }, "slow");
});

 $('#right-button-review').click(function() {
  event.preventDefault();
  $('#content-inside-review').animate({
   scrollLeft: "+=100px"
  }, "slow");
});