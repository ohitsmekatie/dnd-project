document.addEventListener('DOMContentLoaded', () => {
    const itemButton = document.getElementById("item-button");
    const monsterButton = document.getElementById("monster-button");
    const itemOutput = document.getElementById("item-output");

    itemButton.addEventListener("click", async () => {
        try {
            const response = await fetch("/random-item");
            if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
            const data = await response.json();

            itemOutput.innerHTML = `
                <div class="item-card">
                    <h2 class="item-name">${data.name || 'Unknown Item'}</h2>
                    <p class="item-rarity">${data.rarity?.name || 'Unknown Rarity'}</p>
                    ${data.desc?.map(d => `<p class="item-desc">${d}</p>`).join('') || ''}
                </div>
            `;
        } catch (error) {
            console.error('Error fetching item:', error);
            itemOutput.innerHTML = `<p class="error">Failed to load item: ${error.message}</p>`;
        }
    });

    monsterButton.addEventListener("click", async () => {
        try {
            const response = await fetch("/random-monster");
            if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
            const monster = await response.json();

            itemOutput.innerHTML = `
                <div class="item-card">
                    <h2 class="item-name">${monster.name}</h2>
                    <p class="item-rarity">Type: ${monster.type}</p>
                    <p class="item-desc">Challenge Rating: ${monster.challenge_rating}</p>
                    <p class="item-desc">Size: ${monster.size}</p>
                    <p class="item-desc">Alignment: ${monster.alignment}</p>
                </div>
            `;
        } catch (error) {
            console.error('Error fetching monster:', error);
            itemOutput.innerHTML = `<p class="error">Failed to load monster: ${error.message}</p>`;
        }
    });

});