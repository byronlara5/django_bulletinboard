(function($){
  $(function(){

    $('.sidenav').sidenav();

    $('.datepicker').datepicker({
    	format: 'yyyy-mm-dd',
    });

    $('.timepicker').timepicker({
    	twelveHour : false,
    	format: 'HH:ii:SS',
    });

    // For adding seconds (00)
    $('.timepicker').on('change', function() {
        let receivedVal = $(this).val();
        $(this).val(receivedVal + ":00");
    });

  }); // end of document ready
})(jQuery); // end of jQuery name space
