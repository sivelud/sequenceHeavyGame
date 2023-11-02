document.addEventListener("DOMContentLoaded", function() {
    const gameBoardElement = document.querySelector('.game-board pre');
    const playerCardList = document.getElementById('card-list');
    const resetButton = document.getElementById('reset-btn');

    // Function to update the game board
    function updateGameBoard(board_str) {
        gameBoardElement.textContent = board_str;
    }

    // Function to update the player's cards list
    function updatePlayerCards(cards) {
        playerCardList.innerHTML = ''; // Clear current cards

        cards.forEach(card => {
            const li = document.createElement('li');
            li.textContent = card;

            const button = document.createElement('button');
            button.textContent = 'Play';
            button.className = 'play-card-btn';
            button.dataset.card = card;
            button.onclick = function() {
                playCard(card);
            };

            li.appendChild(button);
            playerCardList.appendChild(li);
        });
    }

    // Function to play a card
    function playCard(card) {
        fetch('/play_card', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ card: card })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                updateGameBoard(data.board_str);
                updatePlayerCards(data.player_cards);
            } else {
                console.error(data.message);
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }

    // Function to reset the game
    function resetGame() {
        fetch('/reset_game', {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();
            } else {
                console.error(data.message);
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }

    // Attach event listener for the reset button
    resetButton.addEventListener('click', resetGame);

    // Event listeners for card images
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('click', function() {
            console.log(this.alt); // log the alt text of the card when clicked
        });
    });

    // Event listeners for 'play card' buttons (initial buttons)
    const cardButtons = document.querySelectorAll('.play-card-btn');
    cardButtons.forEach(button => {
        button.addEventListener('click', function() {
            const card = button.getAttribute('data-card');
            playCard(card);
        });
    });
});
