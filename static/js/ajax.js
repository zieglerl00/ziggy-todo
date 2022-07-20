function editTodo(todo) {

    let url = '{% url todo:edit_todo %}'

    $.ajax({

        url : url,
        type : 'GET',
        success : function(data) {
            console.log('Data: '+data);
        },
        error : function(request,error)
        {
            alert("Request: "+JSON.stringify(request));
        }
    });
}
