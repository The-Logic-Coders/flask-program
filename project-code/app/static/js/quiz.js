$(document).ready(function() {
    $('.quiz label').click(function() {
        $('.quiz label').removeClass('selected-option');
        $(this).addClass('selected-option');
    });
    if (window.quizCompleted) {
        $("#quizScore").text('Your score is: ' + window.finalScore); // Update the modal with the final score
        $("#score_modal").modal('show'); // Show the modal
    }
});

