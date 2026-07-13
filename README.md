# Extension vectorielle disjonctive 2D de la conjecture de Syracuse / 2D Disjunctive Vectorial Syracuse Conjecture

---

## 🇫🇷 Version Française

Ce dépôt explore une extension vectorielle en dimension 2 de la célèbre *Conjecture de Syracuse (Collatz)*. En utilisant une condition logique OU (disjonctive) sur la parité des coordonnées, cette variante neutralise les divergences chaotiques classiques et force une convergence systématique vers un attracteur cyclique diagonal.

### Théorème de la diagonale fermée de Syracuse vectorielle 2D

Soit l'espace vectoriel discret $\mathbb{Z}^2$ où chaque état est défini par un vecteur $\vec{v}t = (x_t, y_t)$. On définit l'application de Syracuse vectorielle disjonctive $S: \mathbb{Z}^2 \rightarrow \mathbb{Z}^2$ par la relation de récurrence $\vec{v}{t+1} = S(\vec{v}_t)$ suivante :

- Si $x$ est pair et $y$ est impair : $\vec{v}_{t+1} = (x // 2, y)$
- Si $x$ est impair et $y$ est pair : $\vec{v}_{t+1} = (x, y // 2)$
- Si $x$ et $y$ sont pairs : $\vec{v}_{t+1} = (x // 2, y // 2)$
- Si $x$ et $y$ sont impairs : $\vec{v}_{t+1} = (3x + 1, 3y + 1)$

### Validation numérique intensive

Pour tester la robustesse de cette règle, un algorithme de vérification massive a été exécuté sur une grille de *1 000 000 de couples de vecteurs uniques* :

$$\forall (x, y) \in \llbracket 1, 1000 \rrbracket^2$$

* *Total de couples testés* : 1 000 000
* *Taux de succès* : 100%
* *Contre-exemples trouvés* : 0
* *Attracteur cible* : Tous les vecteurs convergent strictement vers l'attracteur cyclique de période 3 : 
  $$C = \{ (1, 1) \rightarrow (4, 4) \rightarrow (2, 2) \rightarrow (1, 1) \}$$

### Comment exécuter les scripts
1. *Vérification massive* : Lancez Verification_massive.py pour tester le million de couples.
2. *Génération de graphiques* : Lancez generer_graphe.py pour afficher le visuel de la trajectoire.

---

## 🇬🇧 English Version

This repository explores a novel 2D vectorial extension of the famous *Collatz (Syracuse) Conjecture. By utilizing a **logical OR (disjunctive) condition* on coordinate parities, this variant successfully neutralizes standard chaotic complex/vectorial divergences, forcing a systematic convergence toward a strict diagonal attractor loop.

### The Theorem of the Closed Identity Diagonal

Let $\mathbb{Z}^2$ be a discrete vector space where each state is defined by a vector $\vec{v}t = (x_t, y_t)$. The disjunctive Syracuse map $S: \mathbb{Z}^2 \rightarrow \mathbb{Z}^2$ is defined by the following recurrence relation $\vec{v}{t+1} = S(\vec{v}_t)$:

- If $x$ is even and $y$ is odd: $\vec{v}_{t+1} = (x // 2, y)$
- If $x$ is odd and $y$ is even: $\vec{v}_{t+1} = (x, y // 2)$
- If $x$ and $y$ are even: $\vec{v}_{t+1} = (x // 2, y // 2)$
- If $x$ and $y$ are odd: $\vec{v}_{t+1} = (3x + 1, 3y + 1)$

### Extensive Numerical Validation

To challenge the robustness of this disjunctive rule, a brute-force verification script was executed over a grid of *1,000,000 unique vector pairs*:

$$\forall (x, y) \in \llbracket 1, 1000 \rrbracket^2$$

* *Total couples tested*: 1,000,000
* *Success rate*: 100%
* *Counter-examples found*: 0
* *Target Attractor*: All tested vectors strictly converge into the period-3 cyclic identity attractor: 
  $$C = \{ (1, 1) \rightarrow (4, 4) \rightarrow (2, 2) \rightarrow (1, 1) \}$$

### How to Run
1. *Massive Verification*: Run Verification_massive.py to check the 1,000,000 couples.
2. *Graph Generation*: Run generer_graphe.py to plot the trajectory vectors.
