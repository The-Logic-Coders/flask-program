window.onload = function() {
    
    var score = parseInt(document.getElementById('finalScore').textContent);
    var total = parseInt(document.getElementById('quizLength').textContent);
    updateCircleProgress(score, total);
};


function updateCircleProgress(score, total) {
    const radius = 50;
    const circumference = 2 * Math.PI * radius;
    const offset = circumference - (score / total) * circumference;
  
    const svgCircle = `<svg width="120" height="120" viewBox="0 0 120 120">
      <circle cx="60" cy="60" r="${radius}" stroke="#ccc" stroke-width="10" fill="transparent"/>
      <circle cx="60" cy="60" r="${radius}" stroke="#a67b5b" stroke-width="10" fill="transparent" stroke-dasharray="${circumference}" stroke-dashoffset="${offset}" transform="rotate(-90 60 60)"/>
      <text x="60" y="65" text-anchor="middle" font-size="24" fill="#333">${score}/${total}</text>
    </svg>`;
  
    document.querySelector('.circle-progress-container').innerHTML = svgCircle;
  }