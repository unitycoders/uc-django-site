/**
 * Blocks of javascript code for the website
 */

/**
 * getCookie required for django CSRF tokens
 */
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

/**
 * Generate markdown preview based on our markdown engine
 */
 function doPreview(e){
 	var previewUrl = "/api/articles/preview/";
 	var retVal = "";
 	var csrftoken = getCookie('csrftoken');
 	var params = {'body': e.getContent(), 'csrfmiddlewaretoken':csrftoken}

 	jQuery.ajax({
 		url: previewUrl,
 		data: params,
 		success: function(html) {
 			retVal = html;
 		},
 		method: 'POST',
     		async:false
   	});

 	return retVal.markdown;
 }
