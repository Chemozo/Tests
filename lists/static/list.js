var initialize = function() {
  $('input[name="text"]').on('keypress', function() {
    $('.has-error').hide();
  });
};
console.log('list.js loaded');

$('input[name="text"]').on('keypress', function() {
  $('.has-error').hide();
});

$('input[name="text"]').on('keypress', function() {
  console.log('in keypress handler');
  $('.has-error').hide();
});
console.log('list.js loaded');
