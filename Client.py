<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Formulaire d'envoi de données</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      background-color: #f0f0f0;
      margin: 0;
      padding: 20px;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    form {
      background: #fff;
      padding: 25px;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      width: 350px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input, textarea {
      width: 100%;
      padding: 8px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background-color: #6200ea;
      color: #fff;
      border: none;
      padding: 10px 15px;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #4500b5;
    }
    .message {
      margin-top: 15px;
    }
  </style>
</head>
<body>
  <form id="dataForm">
    <label for="nom">Nom</label>
    <input type="text" id="nom" name="nom" required>

    <label for="prenom">Prénom</label>
    <input type="text" id="prenom" name="prenom" required>

    <label for="budget">Budget</label>
    <input type="number" id="budget" name="budget" required>

    <label for="tel">Numéro de téléphone</label>
    <input type="tel" id="tel" name="tel" required>

    <label for="description">Description</label>
    <textarea id="description" name="description" rows="4" required></textarea>

    <button type="submit">Envoyer</button>
    <div class="message" id="responseMessage"></div>
  </form>

  <script>
    document.getElementById('dataForm').addEventListener('submit', async function(event) {
      event.preventDefault();  // Empêche le rechargement de la page

      // Récupère les données du formulaire
      const data = {
        nom: document.getElementById('nom').value,
        prenom: document.getElementById('prenom').value,
        budget: document.getElementById('budget').value,
        tel: document.getElementById('tel').value,
        description: document.getElementById('description').value
      };

      try {
        // Effectue la requête POST en envoyant un JSON
        const response = await fetch('http://fnode1.astrast.host:7031/receive_data', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        });

        const message = document.getElementById('responseMessage');
        if (response.ok) {
          message.style.color = "green";
          message.textContent = "Données envoyées avec succès !";
        } else {
          message.style.color = "red";
          message.textContent = "Erreur lors de l'envoi des données.";
        }
      } catch (error) {
        console.error("Erreur :", error);
        document.getElementById('responseMessage').style.color = "red";
        document.getElementById('responseMessage').textContent = "Erreur de connexion au serveur.";
      }
    });
  </script>
</body>
</html>
