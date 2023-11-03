document.addEventListener("DOMContentLoaded", function() {
    console.log("Script loaded!");
    
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

    function playCard(card) {
        console.log("playCard function called with:", card);
        
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
                    console.log("updating player cards", data.player_cards)
                    location.reload()

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

    // Initially set up the click listeners on the cards
    const cardImages = document.querySelectorAll('.clickImage');
    cardImages.forEach(img => {
        const card = img.alt;
        img.addEventListener('click', function() {
            console.log("Card clicked:", card);
            playCard(card);
        });
    });
});
