// L'URL du fichier JSON (à remplacer par votre URL réelle)
const url = './listsession';

// Fonction pour obtenir les données JSON
async function fetchData() {
    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error('Erreur réseau');
        }

        const data = await response.json();
        console.log(data);

        // Appeler la fonction pour créer le tableau HTML
        createTable(data);

    } catch (error) {
        console.error('Il y a eu un problème avec la requête fetch :', error);
    }
}

async function delAbs(id) {
    const url = '/profil/' + id;

    try {
        const response = await fetch(url, {
            method: 'DELETE'
        });

        if (response.ok) {
            // Gérer la réponse réussie
            console.log('Suppression réussie');
            // Par exemple, recharger la page ou mettre à jour l'interface utilisateur
            window.location.href = "./profil";
        } else {
            // Gérer les erreurs
            console.error('Erreur lors de la suppression');
        }
    } catch (error) {
        // Gérer les erreurs de réseau
        console.error('Erreur réseau', error);
    }
}


// Fonction pour créer le tableau HTML
function createTable(data) {
    // Créer un élément table
    const table = document.createElement('table');
    table.border = "1";

    // Créer l'en-tête du tableau
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    const headers = ['Date', 'ID Joueur', 'ID Session', 'ID Sudoku', 'Nombre d\'erreurs', 'Actions'];

    headers.forEach(headerText => {
        const th = document.createElement('th');
        th.appendChild(document.createTextNode(headerText));
        headerRow.appendChild(th);
    });

    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Créer le corps du tableau
    const tbody = document.createElement('tbody');

    data.forEach(item => {
        const row = document.createElement('tr');

        // Créer les cellules pour chaque colonne
        Object.keys(item).forEach(key => {
            const cell = document.createElement('td');
            cell.appendChild(document.createTextNode(item[key]));
            row.appendChild(cell);
        });

        // Créer la cellule pour le bouton
        const actionCell = document.createElement('td');
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Supprimer';
        deleteButton.className = 'delete-button';

        // Ajouter l'événement de clic pour rediriger vers l'URL de suppression
        deleteButton.onclick = function() {
            delAbs(item['id_session']);
        };

        actionCell.appendChild(deleteButton);
        row.appendChild(actionCell);

        tbody.appendChild(row);
    });

    table.appendChild(tbody);

    // Remplacer le contenu de la div avec l'id "tableau" par le tableau créé
    const tableauDiv = document.getElementById('tableau');
    tableauDiv.innerHTML = ''; // Vider le contenu existant
    tableauDiv.appendChild(table); // Ajouter le nouveau tableau
}

// Appeler la fonction fetchData pour obtenir et afficher les données
fetchData().then(data => {
  createTable(data);
});
