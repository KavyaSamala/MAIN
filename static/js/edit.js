$(document).ready(function () {
    $(document).on("dblclick",".editable",function(){
        var value=$(this).text();
        var input="<input type='text' value='"+value+"' class='form-control'>";
        $(this).html(input);

    });

    $(document).on("keyup",".editable",function(e){
        var key=e.which;
        if (key == 13){
            current_value = $(this).find('input').val()
            update_value = `<td ><a href='www.google.com'>${current_value}</a></td>`
            $(this).html(update_value);

        }
    });
})
