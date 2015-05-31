$(function() {
		$(".gd").click(function() {
			 var id = parseInt($(this).attr("id"));
			 $.ajax({
			        type: 'POST',
			        url: '/k_means/page',
			        data:{
			        	'page':id,
			        },
//			        dataType: 'json',
			        success: function(a) {
			        	alert(a);
			        },
			        error: function(XMLHttpRequest, textStatus, errorThrown) {
			        	alert(XMLHttpRequest.status);
//			        	alert(XMLHttpRequest.readyState);
//			        	alert(textStatus);
			        	alert(errorThroen);
			        	},
			      });
	});
});