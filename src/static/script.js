document.addEventListener("DOMContentLoaded", function() {
    // Add event listeners to all play card buttons.
    const playCardButtons = document.querySelectorAll('.play-card-btn');

    playCardButtons.forEach(button => {
        button.addEventListener('click', function() {
            const card = this.dataset.card;
            playCard(card);
        });
    });
});

function playCard(card) {
    console.log("Playing card:", card);  // Debug statement

    fetch('/play_card', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ card })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updateGameBoard(data.board);
            updatePlayerCards(data.player_cards);
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function updateGameBoard(board) {
    // Assuming you have an element to show the game board state
    // This is a basic example, you'd probably want a more visual representation.
    const boardElement = document.querySelector('.game-board');
    boardElement.innerHTML = '<h2>Game Board</h2>';  // Clear previous state and add title

    for (let card in board) {
        if (board[card] !== null) {
            // If a card has been played on the board, visualize it.
            boardElement.innerHTML += `<p>${card}: ${board[card]}</p>`;
        }
    }
}

function updatePlayerCards(cards) {
    const cardList = document.getElementById('card-list');
    cardList.innerHTML = ''; // Clear current cards
    
    cards.forEach(card => {
        const li = document.createElement('li');
        li.textContent = card;
        
        const button = document.createElement('button');
        button.textContent = 'Play';
        button.className = 'play-card-btn';
        button.dataset.card = card;
        button.onclick = () => playCard(card);
        
        li.appendChild(button);
        cardList.appendChild(li);
    });
}
