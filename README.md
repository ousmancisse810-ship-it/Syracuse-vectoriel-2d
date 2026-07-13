# 2D Disjunctive Vector Extension of the Collatz Conjecture
> *Extension vectorielle disjonctive 2D de la conjecture de Syracuse*

Ce dépôt présente une variante vectorielle originale en dimension 2 de la conjecture de Syracuse (problème $3n+1$). En introduisant un opérateur logique disjonctif OU (OR) pour découpler le traitement de la parité des composantes, le système semble neutraliser le chaos dynamique classique et forcer une convergence systématique vers la diagonale identitaire, puis vers un attracteur cyclique stationnaire de période 3.

---

## 🔬 Énoncé Mathématique

### Définition de l'application
Soit l'espace vectoriel discret $\mathbb{Z}^2$ où chaque point est défini par un vecteur $\vec{v} = (x, y)$. On définit l'application $f: \mathbb{Z}^2 \to \mathbb{Z}^2$ par :

$$
f(x, y) = 
\begin{cases} 
\left(\frac{x}{2}, y\right) & \text{si } x \equiv 0 \pmod 2 \text{ et } y \equiv 1 \pmod 2 \\
\left(x, \frac{y}{2}\right) & \text{si } x \equiv 1 \pmod 2 \text{ et } y \equiv 0 \pmod 2 \\
\left(\frac{x}{2}, \frac{y}{2}\right) & \text{si } x \equiv 0 \pmod 2 \text{ et } y \equiv 0 \pmod 2 \\
(3x + 1, 3y + 1) & \text{si } x \equiv 1 \pmod 2 \text{ et } y \equiv 1 \pmod 2 
\end{cases}
$$

### Conjecture empirique (La diagonale fermée)
Pour tout vecteur initial $\vec{v}0 \in (\mathbb{Z}^*+)^2$, la suite définie par $\vec{v}_{t+1} = f(\vec{v}_t)$ intercepte la diagonale identitaire $\Delta = \{(n, n) \mid n \in \mathbb{Z}\}$ en un nombre fini d'étapes. Une fois sur la diagonale, les deux composantes se synchronisent. Le système se réduit alors à la conjecture de Syracuse classique 1D et converge vers l'unique cycle trivial :

$$C = \{ (1, 1) \to (4, 4) \to (2, 2) \to (1, 1) \}$$

---

## 📊 Résultats des Simulations Numériques

Une vérification exhaustive par force informatique a été menée pour tester la robustesse de cette conjecture en utilisant un algorithme optimisé de mémoïsation (mise en cache des trajectoires validées).

| Plage de recherche ($x$ et $y$) | Nombre de couples testés | Contre-exemples trouvés | Statut empirique |
| :--- | :--- | :--- | :--- |
| $[1, 1000] \times [1, 1000]$ | *1 000 000* | *0* | *Validée* |

### Exemple de trajectoire : $\vec{v}_0 = (3, 5)$
Le système converge de façon strictement bornée (borne supérieure $y_{max} = 16$) en exactement 10 étapes de transition avant d'entrer dans l'attracteur :
$$\begin{aligned}
(3,5) \to (10,16) \to (5,8) \to (16,4) \to (8,2) \to (4,1) \to (2,1) \to (1,1) \dots
\end{aligned}$$

---

## 💻 Structure du Projet

Le dépôt contient les scripts Python suivants :
*   verification_massive.py : Script à haute performance (mémoïsation) utilisé pour valider le premier million de couples en quelques secondes.
*   generer_graphe.py : Script permettant de tracer et de visualiser l'orbite d'un vecteur donné dans l'espace 2D.

---

## 📬 Contact et Discussion
Ce projet est partagé publiquement pour stimuler la recherche de pistes ou d'outils d'analyse dynamique globale permettant de prouver analytiquement cette convergence. 
Les discussions mathématiques avancées ont lieu sur le forum [les-mathematiques.net](https://les-mathematiques.net).
