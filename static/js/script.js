$(document).ready(function() {
    function updateClock() {
        $.ajax({
            url: '/get_time',
            type: 'GET',
            success: function(data) {
                $('#current-time').text(data);
            }
        });
    }

    updateClock();
    setInterval(updateClock, 1000);
});
