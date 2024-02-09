$(function() {
    $('#button').click(function(event) {
	event.preventDefault();
        let title = $('#title').val();
        let content = $('#content').val();

        $.ajax({
            url: '/add-notes',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                alert(response);
            },
            error: function(error) {
                alert(error);
            }
        });
    });
});

