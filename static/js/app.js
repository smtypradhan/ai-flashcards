let currentCard = 0;
let score = 0;
let sessionStarted = false;
let cards = document.querySelectorAll('.card');
const welcome = document.getElementById('welcome');
const result = document.getElementById('result');
const actions = document.querySelector('.actions');
const controls = document.querySelector('.controls');
const keyboardHint = document.querySelector('.keyboard-hint');

let flipAudio;

function initAudio() {
  if (!flipAudio) {
    const flipUrl = document.body.dataset.flipSound || 'static/sounds/card-flip.wav';
    flipAudio = new Audio(flipUrl);
    flipAudio.volume = 0.5;
  }
}

function playFlipSound() {
  if (flipAudio) {
    flipAudio.currentTime = 0;
    flipAudio.play();
  }
}

// Start session
document.getElementById('start-btn').onclick = () => {
  initAudio();
  welcome.style.display = 'none';
  controls.style.display = 'flex';
  keyboardHint.classList.add('show');
  sessionStarted = true;
  showCard(currentCard);
  setTimeout(() => keyboardHint.classList.remove('show'), 3000);
};

// Show specific card
function showCard(index) {
  if (!sessionStarted) return;
  cards.forEach((card) => {
    card.classList.remove('active');
    card.classList.remove('flipped');
  });
  if (index >= 0 && index < cards.length) {
    const card = cards[index];
    card.classList.add('active');
    card.querySelector('.progress').innerText = `${index + 1} / ${cards.length}`;
    actions.classList.remove('show');
    card.classList.remove('flipped');
  }
}

// Flip current card
function flipCard() {
  if (!sessionStarted || currentCard >= cards.length) return;
  const card = cards[currentCard];
  card.classList.toggle('flipped');
  if (card.classList.contains('flipped')) {
    actions.classList.add('show');
  } else {
    actions.classList.remove('show');
  }
  playFlipSound();
}

// Navigation
function prevCard() {
  if (currentCard > 0) {
    currentCard--;
    showCard(currentCard);
  }
}
function nextCard() {
  if (currentCard < cards.length - 1) {
    currentCard++;
    showCard(currentCard);
  } else {
    showResult();
  }
}

// Scoring
function markAnswer(correct) {
  if (correct) score++;
  const button = event.target;
  const originalText = button.innerHTML;
  button.innerHTML = correct ? '✓ Correct!' : '✗ Try again!';
  button.style.transform = 'scale(0.95)';
  setTimeout(() => {
    button.innerHTML = originalText;
    button.style.transform = 'scale(1)';
    nextCard();
  }, 500);
}

// Keyboard controls
document.addEventListener('keydown', (e) => {
  // Allow Enter to start when welcome is visible
  if (!sessionStarted) {
    if (e.key === 'Enter') {
      const welcomeEl = document.getElementById('welcome');
      if (welcomeEl && welcomeEl.style.display !== 'none') {
        const startBtn = document.getElementById('start-btn');
        if (startBtn) startBtn.click();
      }
    }
    return;
  }
  // In-session controls
  switch (e.key) {
    case 'ArrowLeft': e.preventDefault(); prevCard(); break;
    case 'ArrowRight': e.preventDefault(); nextCard(); break;
    case ' ': case 'Enter': e.preventDefault(); flipCard(); break;
    case 'g': case 'G': e.preventDefault(); if (actions.classList.contains('show')) markAnswer(true); break;
    case 'm': case 'M': e.preventDefault(); if (actions.classList.contains('show')) markAnswer(false); break;
  }
});

// Click to flip
cards.forEach(card => {
  card.addEventListener('click', (e) => {
    if (e.target.closest('.actions')) return;
    flipCard();
  });
});

// Result
function showResult() {
  sessionStarted = false;
  document.getElementById('card-container').style.display = 'none';
  controls.style.display = 'none';
  actions.style.display = 'none';
  const percentage = Math.round((score / cards.length) * 100);
  let message = '';
  if (percentage >= 90) message = "🌟 Excellent! You're mastering this material!";
  else if (percentage >= 70) message = '👍 Good job! Keep up the great work!';
  else if (percentage >= 50) message = '📚 Not bad! Review the missed cards and try again.';
  else message = '💪 Keep studying! Practice makes perfect.';
  document.getElementById('score').innerHTML = `
    <div style="font-size: 2rem; margin: 20px 0;">${score} / ${cards.length}</div>
    <div style="font-size: 1.5rem; margin: 10px 0; color: #007bff;">${percentage}%</div>
    <div style="margin-top: 20px;">${message}</div>
  `;
  result.style.display = 'block';
}

function restart() {
  currentCard = 0;
  score = 0;
  sessionStarted = false;
  result.style.display = 'none';
  document.getElementById('card-container').style.display = 'block';
  welcome.style.display = 'block';
  controls.style.display = 'none';
  actions.classList.remove('show');
  cards.forEach(c => c.classList.remove('active', 'flipped'));
}

// Initialize
showCard(0);

// Add arrows next to the card container
const cardContainer = document.getElementById('card-container');
const leftArrow = document.createElement('button');
leftArrow.className = 'nav-arrow left';
leftArrow.setAttribute('aria-label', 'Previous card');
leftArrow.innerHTML = '&lt;';
leftArrow.onclick = () => prevCard();
const rightArrow = document.createElement('button');
rightArrow.className = 'nav-arrow right';
rightArrow.setAttribute('aria-label', 'Next card');
rightArrow.innerHTML = '&gt;';
rightArrow.onclick = () => nextCard();
cardContainer.appendChild(leftArrow);
cardContainer.appendChild(rightArrow);

function shuffleDeck() {
  const container = document.getElementById('card-container');
  const cardNodes = Array.from(container.querySelectorAll('.card'));
  for (let i = cardNodes.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [cardNodes[i], cardNodes[j]] = [cardNodes[j], cardNodes[i]];
  }
  const beforeNode = leftArrow;
  cardNodes.forEach(node => container.insertBefore(node, beforeNode));
  cards = document.querySelectorAll('.card');
  currentCard = 0;
  score = 0;
  actions.classList.remove('show');
  cards.forEach(c => c.classList.remove('active', 'flipped'));
  if (sessionStarted) showCard(0);
}

// Expose functions for inline handlers
window.flipCard = flipCard;
window.shuffleDeck = shuffleDeck;
window.markAnswer = markAnswer;
window.prevCard = prevCard;
window.nextCard = nextCard;
window.restart = restart;
