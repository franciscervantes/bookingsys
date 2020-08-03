

function init(){
	room = document.getElementById("id_room_id").value
	document.getElementById(room).style.display = "block";

}

 window.onload = function() {
  init();
};	
  function showRoom(value){
  	hideDivs = document.getElementsByClassName("room_details");
  	for(var i = 0; i < hideDivs.length; i++){
        	hideDivs[i].style.display = "none"; 
    }

    document.getElementById(value).style.display = "block";



}

  // $(function() {
  //   $( ".datepicker" ).datepicker({
  //      dateFormat: "yy-mm-dd",
  //     changeMonth: true,
  //     changeYear: true,
  //     minDate: 0,
  //   });
  // });

$(function () {
     $("#datein").datepicker({
         minDate: 0,
         dateFormat: "yy-mm-dd",
         changeMonth: true,
         numberOfMonths: 1,
         changeYear: true,
         onClose: function (selectedDate, inst) {
             var minDate = new Date(Date.parse(selectedDate));
             minDate.setDate(minDate.getDate() + 1);
             $("#dateout").datepicker("option", "minDate", minDate);
         }
     });

     $("#dateout").datepicker({
         minDate: "+1D",
         dateFormat: "yy-mm-dd",
         changeMonth: true,
         numberOfMonths: 1,
         changeYear: true,
         onClose: function (selectedDate, inst) {
             var maxDate = new Date(Date.parse(selectedDate));
             maxDate.setDate(maxDate.getDate() - 1);
             $("#datein").datepicker("option", "maxDate", maxDate);
         }
     });
     // $("#id_room_id").value()
 });


$('#reservation-form').on('submit', function(e){

e.preventDefault();
token = $("#reservation-form").find('input[name=csrfmiddlewaretoken]').val();

  $.ajax({
       type : "POST", 
       url: $("#reservation-form").attr("data-ajax-target"), /* django ajax posting url  */
       data: {
        first_name : $('#id_first_name').val(),
        last_name : $('#id_last_name').val(),
        client_email: $('#id_client_email').val(),
        date_in: $('#datein').val(),
        date_out: $('#dateout').val(),
        client_phone: $('#id_client_phone').val(),
        room_id: $('#id_room_id').val(),
        csrfmiddlewaretoken: token,
        dataType: "json",

       },
       
       success: function(data){
          // $('#output').html(data.msg) /* response message */
          console.log(data);
          if(data.status == 'created')
            toastr.success('Successfully created');
          else{

            toastr.error('Invalid Dates')
          }
       },

       failure: function() {
           console.log("error");
       }


   });

        });  