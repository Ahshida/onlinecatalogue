$(function() {
  var availableTags = [
    "Cold Work Tool Steel",
    "Hot Work Tool Steel",
    "Plastic Moulds"
  ];
  $( "#searchbar" ).autocomplete({
    source: availableTags
  });
});
