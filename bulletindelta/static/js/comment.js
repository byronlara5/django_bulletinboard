
$(function() {

    // Submit post on submit
$('#post-form1').on('submit', function(event){
    event.preventDefault();
    var memo_num1 = $('#memo_num1').val()
    console.log("form submitted!")  // sanity check
    console.log(memo_num1)
    create_post(memo_num1);
});

$('#post-form2').on('submit', function(event){
    event.preventDefault();
    var memo_num2 = $('#memo_num2').val()
    console.log("form submitted!")  // sanity check
    console.log(memo_num2)
    create_post(memo_num2);
});

$('#post-form3').on('submit', function(event){
    event.preventDefault();
    var memo_num3 = $('#memo_num3').val()
    console.log("form submitted!")  // sanity check
    console.log(memo_num3)
    create_post(memo_num3);
});

$('#post-form4').on('submit', function(event){
    event.preventDefault();
    var memo_num4 = $('#memo_num4').val()
    console.log("form submitted!")  // sanity check
    console.log(memo_num4)
    create_post(memo_num4);
});

$('#post-form5').on('submit', function(event){
    event.preventDefault();
    var memo_num5 = $('#memo_num5').val()
    console.log("form submitted!")  // sanity check
    console.log(memo_num5)
    create_post(memo_num5);
});

$('#post-form6').on('submit', function(event){
    event.preventDefault();
    var memo_num6 = $('#memo_num6').val()
    console.log("form submitted!")  // sanity check
    console.log(memo_num6)
    create_post(memo_num6);
});

$('#post-form7').on('submit', function(event){
    event.preventDefault();
    var memo_num7 = $('#memo_num7').val()
    console.log("form submitted!")  // sanity check
    console.log(memo_num7)
    create_post(memo_num7);
});

$('#post-form8').on('submit', function(event){
    event.preventDefault();
    var memo_num8 = $('#memo_num8').val()
    console.log("form submitted!")  // sanity check
    console.log(memo_num8)
    create_post(memo_num8);
});

// AJAX for posting
function create_post(post_num) {
    console.log("create post is working!") // sanity check

    $.ajax({
        url : "create_post/", // the endpoint
        type : "POST", // http method
        data : { 
            the_post : $('#post-text'+post_num).val(), memo : $('#memo'+post_num).val(),
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#post-text'+post_num).val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            window.location.reload();
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};




    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});