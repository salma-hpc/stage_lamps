# Implémentation du format CSR pour Matrices de Connectivité

**Stage de Master 1 - Calcul Haute Performance et Simulation**
*Laboratoire LAMPS, Université de Perpignan Via Domitia (UPVD)*

## 📌 Description
Ce projet implémente le format de stockage **CSR (Compressed Sparse Row)** pour optimiser la manipulation de matrices de connectivité creuses, couramment utilisées dans la modélisation de systèmes granulaires et d'interactions particulaires.

L'objectif principal est de réduire l'empreinte mémoire et d'accélérer les opérations algébriques par rapport aux matrices denses classiques, grâce notamment à une parallélisation des calculs.

## 🚀 Fonctionnalités
- **Conversion Optimisée** : Algorithme de transformation Matrice Dense $\rightarrow$ Format CSR.
- **Stockage Compact** : Utilisation de trois tableaux unidimensionnels (`values`, `col_indices`, `row_ptr`).
- **Parallélisation** : Implémentation avec le module `multiprocessing` pour accélérer la construction sur de grands jeux de données.
- **Analyse de Performance** : Scripts de benchmark pour comparer les approches séquentielles et parallèles.

## 📊 Résultats Expérimentaux (Extraits du Rapport)

### 1. Gain Mémoire (Dense vs CSR)
Le format CSR offre une réduction spectaculaire de l'espace mémoire nécessaire, idéale pour les matrices très creuses (densité < 1%).

| Taille Matrice | Mémoire Dense (éléments) | Mémoire CSR (éléments) | Réduction Mémoire |
| :--- | :--- | :--- | :--- |
| **1000 x 1000** | 1 000 000 | 10 007 | **~99.0%** |
| **2000 x 2000** | 4 000 000 | 20 010 | **~99.5%** |
| **5000 x 5000** | 25 000 000 | 50 013 | **~99.8%** |

### 2. Performance Temporelle (Séquentiel vs Parallèle)
L'implémentation parallèle permet de diviser par deux le temps de traitement sur les grandes instances.

| Taille Matrice | Temps Séquentiel (s) | Temps Parallèle (s) | Speedup (Gain) |
| :--- | :--- | :--- | :--- |
| **1000 x 1000** | 2.34 s | 1.17 s | **x 2.0** |
| **2000 x 2000** | 9.78 s | 4.89 s | **x 2.0** |
| **5000 x 5000** | 42.56 s | 21.78 s | **x 1.95** |

> **⚠️ Note technique** : Les résultats d'exécution peuvent varier selon la machine utilisée.
> Le fichier [`results/log_execution.txt`](./results/log_execution.txt) contient un exemple d'exécution récent sur une machine personnelle moderne (où les temps sont plus courts, rendant le gain de parallélisation moins visible sur de petites matrices).

## 📁 Structure du Projet
stage_lamps/
├── src/ # Code source Python (CSR, Parallèle, Benchmark)
├── docs/ # Rapport de stage complet (PDF)
├── results/ # Logs d'exécution et graphiques de performance
└── README.md # Documentation du projet


## 🛠️ Technologies
- **Langage** : Python 3.x
- **Bibliothèques** : `NumPy`, `SciPy`, `Multiprocessing`


## 👥 Auteur
**Salma Bensmail** (Étudiante M1 CHPS)
*Encadré par M. Serge Dumont*
