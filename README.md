# CryptoFinance

## Minage 1+2
`one+two.py`

![Figure_1](https://user-images.githubusercontent.com/41857236/209958962-9127be22-69b2-4aff-be4e-9834b8b554ce.png)
![Figure_2](https://user-images.githubusercontent.com/41857236/209958955-e8abea31-69dc-4fdc-98f7-c15b87748d3e.png)

## Jeu du minage

`mining_game.py`

L'idée est de calculer l'espérance de gain maximale en fonction de la puissance de hashage du mineur afin de détermier à partir de quel seuil il est plus rentable d'abandonner la stratégie de minage classique.
On trouve qu'il est plus rentable de l'abandonner quand `q = 0.3293929`, soit à partir d'une puissance de hashage de `32.93929%`

## Selfish mining
`selfish_mining.py`

Simulation du rendement en fonction du hasrate avec une attaque de minage égoïste 

![Figure_1](https://user-images.githubusercontent.com/41857236/209969530-0ed55347-b600-40a6-ba65-e1e9c627cb57.png)

```Algo
1. S mines on top of the last block of the official blockchain
2. If H is firrst to validate a block, then Sgoes back to 1 (end of a cycle). 
3. If S is first to validate a block, then S keeps on mining secretly on top of her secret block
4. If S is first to validate a block but then H mines one block before S validates a secondone,S broadcasts immediately her secret block. A competition follows. After resolution of thiscompetition, S goes back to 1 (end of a cycle). 
5. If S mines two blocks in a row then, S keeps on mining secretly on top of her secret fork6. When the advance of S reduces to 1, S broadcasts her entire fork (end of a cycle).
```
