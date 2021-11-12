# Cloud-Computing---lab-2

Bienvenue sur le lab 2

Voici l'ensemble de notre travail pour ce TD
### Installation :
```pip install flask```

### Commande pour lancer l'application :
```python -m flask run```

### Projet :
On a une page sur laquelle 4 photos sont affichées aléatoirement parmi tout le contenu du bucket s3.
Sous chaque photo, l'utilisateur peut choisir s'il s'agit d'un hot-dog ou non puis envoyer son résultat.
Tous les résultats s'additionnent aux précendents qui sont upload sous forme de json dans le bucket s3.
A chaque lancement du programme, le json contenant les anciens résulats est téléchargé puis complété au fur et à mesure.

Il y a également une section où l'utilisateur peut upload ses propres images vers le bucket s3 (Le nom du fichier ne doit pas contenir d'espaces).
Ses images pourront ensuite apparaître dans la séléction du dessus.

### Contenu du .json :
```{"download (3).jpg": [1, 0], "download (12).jpg": [1, 1], "download (19).jpg": [1, 1], "download (5).jpg": [1, 0], "download (15).jpg": [1, 0], "download (9).jpg": [1, 0]}```

On associe au nom de chaque photo le nombre de votes "Oui" ou "Non". Le premier indice correspondant au nombre de "Oui" et le second au nombre de "Non".

### Vidéo :

https://user-images.githubusercontent.com/72745033/141534941-a0b52228-8330-4de5-9a9e-0afd6caf7199.mp4

