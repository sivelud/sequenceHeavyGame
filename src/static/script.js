document.addEventListener("DOMContentLoaded", function() {
    const playerCardList = document.getElementById('card-list');
    const cardGridElement = document.querySelector('.card-grid');

    function updateGameBoard(boardDots) {
        const cardImages = cardGridElement.querySelectorAll('img');
        const dotDivs = cardGridElement.querySelectorAll('.yellow-dot, .red-dot');
        
        // Clear any existing dots
        dotDivs.forEach(dot => dot.remove());

        cardImages.forEach((img, index) => {
            const dotValue = boardDots[index];
            if(dotValue == "1" || dotValue == "2") {
                const dotDiv = document.createElement('div');
                dotDiv.classList.add(dotValue == "1" ? "yellow-dot" : "red-dot");
                img.parentElement.appendChild(dotDiv);
            }
        });
    }

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
                // Fetch the updated board state after successfully playing a card
                fetch('/get_current_board')
                .then(resp => resp.json())
                .then(boardDots => {
                    updateGameBoard(boardDots);
                    updatePlayerCards(data.player_cards);
                });
            } else {
                console.error(data.message);
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }

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
    document.getElementById('reset-btn').addEventListener('click', resetGame);

    // Attach event listeners to play card buttons
    const cardButtons = document.querySelectorAll('.play-card-btn');
    cardButtons.forEach(button => {
        button.addEventListener('click', function() {
            const card = button.getAttribute('data-card');
            playCard(card);
        });
    });
});
