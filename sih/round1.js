let currentQuestion = 0;
const questions = document.querySelectorAll('.question');
const totalQuestions = questions.length;
const statuses = document.querySelectorAll('.status-icon i');

// Show the first question
questions[currentQuestion].classList.add('active');

function navigate(direction) {
    // Hide current question
    questions[currentQuestion].classList.remove('active');

    // Update current question index
    currentQuestion += direction;

    // Ensure the index is within bounds
    if (currentQuestion < 0) currentQuestion = 0;
    if (currentQuestion >= totalQuestions) currentQuestion = totalQuestions - 1;

    // Show new current question
    questions[currentQuestion].classList.add('active');
}

// Submit the answer for the current question
function submitAnswer(questionNumber) {
    // Get the selected answer
    const selectedOption = document.querySelector(`input[name="q${questionNumber}"]:checked`);
    
    // Only update if an answer is selected
    if (selectedOption) {
        // Mark the question as attempted
        const statusIcon = statuses[questionNumber - 1];
        statusIcon.className = 'fas fa-check'; // Update to checkmark
    } else {
        // Optionally, add feedback for no selection
        alert('Please select an answer before proceeding.');
        return; // Stop execution if no answer is selected
    }

    // Navigate to the next question
    navigate(1);
}

// Optional: Add click event listeners to navigation links
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default anchor behavior
        const target = this.getAttribute('href').substring(1);
        const index = Array.from(questions).findIndex(q => q.id === target);

        // Navigate to the clicked question
        if (index !== -1) {
            questions[currentQuestion].classList.remove('active');
            currentQuestion = index;
            questions[currentQuestion].classList.add('active');
        }
    });
});
