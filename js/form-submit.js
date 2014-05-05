// Attach a submit handler to the form
$( "#login-form" ).submit(function( event ) {
 
  // Stop form from submitting normally
  event.preventDefault();
 
  // Get some values from elements on the page:
  var $form = $( this ),
    username = $form.find( "input[name='inputUsername']" ).val(),
    password = $form.find( "input[name='inputPassword']" ).val(),
    url = $form.attr( "action" );
 
  // Send the data using post
    var posting = $.post( url, { inputUsername: username } );
  
  $( "#result" ).empty().append( "We've sent the data" );
 
  // Put the results in a div
  /*posting.done(function( data ) {
    var content = $( data ).find( "#content" );
    $( "#result" ).empty().append( content );
  });
  */
});