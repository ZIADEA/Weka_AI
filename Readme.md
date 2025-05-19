# COMPOSITION DU LIVRABLE

## Dossier codesource :
Contient le code source du projet Maven.

### Dans Eclipse :
1. Ouvrir Eclipse et sélectionner un espace de travail (workspace).
2. Importer le projet :
   - Cliquez sur File > Import
   - Sélectionnez General > Existing Projects into Workspace
   - Cliquez sur Next, puis choisissez Select archive file et naviguez jusqu'au fichier Annomalie_detection_weka.zip
   - Cliquez sur Finish pour importer le projet
3. Vérifier les dépendances :
   - Si le projet utilise des bibliothèques externes (comme Weka), assurez-vous qu'elles sont configurées dans le Build Path :
     - Cliquez-droit sur le projet > Build Path > Configure Build Path
     - Ajoutez les fichiers JAR nécessaires sous l'onglet Libraries
4. Exécuter le projet :
   - Trouvez la classe principale (généralement avec une méthode main)
   - Cliquez-droit sur la classe > Run As > Java Application

### Dans IntelliJ IDEA :
1. Ouvrir IntelliJ et choisir Open (ou File > Open)
2. Sélectionner le fichier ZIP :
   - Naviguez jusqu'à Annomalie_detection_weka.zip et sélectionnez-le
   - IntelliJ détectera automatiquement le projet et l'extraira
3. Configurer les dépendances :
   - Si des bibliothèques manquent (comme Weka), ajoutez-les :
     - File > Project Structure > Libraries
     - Cliquez sur + pour ajouter les fichiers JAR nécessaires
4. Exécuter le projet :
   - Localisez la classe principale (avec public static void main)
   - Cliquez sur l'icône ▶ à côté de la méthode main ou faites un clic-droit > Run

### Remarques :
- Structure du ZIP : Assurez-vous que le ZIP contient un projet Java valide (dossiers src, lib, etc.). Si c'est juste un fichier source, créez un nouveau projet et copiez le contenu du ZIP dedans.
- Weka : Si le projet utilise Weka, téléchargez le fichier JAR depuis le site officiel et ajoutez-le aux dépendances.
- Erreurs : En cas d'erreurs de compilation, vérifiez la configuration du JDK (File > Project Structure > Project SDK dans IntelliJ, ou Build Path dans Eclipse).

## Dossier data traitement :
Contient des fichiers python nécessaires pour :
- convertir un dataset .csv en .arff avec le fichier csv_to_arrf.py
- convertir un dataset issue de mesure de capteur en csv avec le fichier preaitement.py

## Dossier Datas :
Contient quelques fichiers test du modèle

## Dossier demo :
qui contient une video montrant comment utiliser notre application

## Dossier executable jar du GUI :
contient l'exicutable de notre application

NB : pour que le GUI soit fonctionnel le dossier resourrce contenant notre model initial obtenu avec r15.arff est imperatif.

## Dossier target :
contient les fichiers prêts à l'emploi, mais seul le .jar/.war est essentiel pour l'utilisateur. Le reste est soit technique, soit recréable avec Maven.

## Dossier rapport :
contient :
- projet_weka_java_IA_docu.pptx contient une explication detaillée de la bibliotheque weka meilleur qu'une documentation web !
- le rapport weka.pdf contenant tout le processus du projet.
- Projet_presentation_summary.pptx la presentation pour la classe.

## NB :
Pour de nouveau data different du data r15.arff il est recommander de :
1. Lancer le clustering sans utiliser le model preentrainer pour avoir des resultats qui correspondent aux données
2. Pour le choix du meilleur nombre de cluster k, se baser sur :
   - Analyse combinée de Silhouette Score
   - Méthode du coude (Elbow Method)
   - Compacité intra-cluster

Le système sélectionne le meilleur k selon un équilibre entre :
- silhouette élevée
- compacité faible
- inertie stabilisée

## Perspective d'amélioration :
Une amélioration future importante consistera à finaliser l'intégration de l'algorithme DBSCAN (Density-Based Spatial Clustering of Applications with Noise). Contrairement à KMeans, DBSCAN :
- Ne nécessite pas de fixer à l'avance le nombre de clusters
- Est particulièrement adapté à la détection d'anomalies
- Permet la découverte de clusters de formes irrégulières

Une fois les contraintes techniques résolues (notamment la compatibilité du plugin DBSCAN dans Weka avec l'environnement Maven), l'algorithme DBSCAN pourra progressivement remplacer KMeans dans l'application, pour offrir :
- Une détection plus robuste
- Une détection plus flexible