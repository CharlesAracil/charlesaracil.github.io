---
layout: post
title: Les mots de passe sont dépassés
ref: Passwords_just_suck_the_big_one
lang: fr
---

En 20 ans d'effort, nous avons éduqué les gens à avoir leurs mots de passe craqués.

Comprenez-moi bien, les recommandations habituelles sur les mots de passe, comme ceux de [Microsoft](http://windows.microsoft.com/en-gb/windows-vista/tips-for-creating-a-strong-password) ou encore l'agence de [sécurité française](http://www.ssi.gouv.fr/guide/mot-de-passe/), sont bien pertinentes, au sens où elles construisent effectivement des mots de passe difficiles à craquer.

Néanmoins, **ces méthodes sont presque inutilisables**, car elles omettent les limitations de l'humain, comme sa capacité à se rappeler de mots de passe compliqués, et à fortiori un grand nombre d'entre eux, et la corvée d'avoir à les taper sur la fenêtre de connexion à chaque fois.

---

## Robustesse d'un mot de passe

---

La robustesse d'un mot de passe dépend de trois composantes: sa `taille`, son `alphabet` et son caractère `aléatoire`. Dans ce contexte, *l'alphabet* signifie l'ensemble des touches de clavier utilisé, les lettres majuscules ou minuscules, les chiffres et les symboles. La règle est simple: **au plus, au mieux.** Evaluer la force d'un mot de passe sur la seule base de ses composantes est cependant difficile, car elles sont liées les unes aux autres. Vous ne pouvez pas dire si un mot de passe court avec un alphabet étendu est plus efficace qu'un mot de passe long avec un alphabet restreint. Il est par exemple difficile de comparer *`g&34$`* et *`abbaabaaabaaababaa`*.

C'est là que `l'entropie` entre en jeu.

L'entropie ne dépend que de la taille et de l'alphabet, et fournit une quantification numérique de la force d'un mot de passe, autrement dit d'à quel point il sera difficile de la craquer. Plus l'entropie est grande, plus le mot de passe est robuste. Voici une table de correspondance entre l'alphabet et l'entropie par symbole trouvée sur [Wikipedia](https://en.wikipedia.org/wiki/Password_strength):

| Alphabet             | Symboles utilisés         | Entropie par symbole |
| -------------------- | ------------------------- | -------------------- |
| Arabic numerals      | [0-9]                     | 3.322                |
| Latin alphabet       | [a-zA-Z]                  | 5.700                |
| Alphanumeric         | [a-zA-Z0-9]               | 5.964                |
| All ascii characters | [a-zA-Z0-9 !"#$%...]      | 6.570                |

Pour calculer l'entropie d'un mot de passe, il suffira donc de multiplier sa longueur avec l'entropie par symbole correspondant à l'alphabet utilisé. Voici quelques exemples pour clarifier les choses:

| Mot de passe | Longueur | Entropie par symbole | Entropie |
| ------------ | -------- | -------------------- | -------- |
| 1234         | 4        | 3.322                | 13.288   |
| 123456       | 6        | 3.322                | 19.932   |
| abC          | 3        | 5.700                | 17.1     |
| Superman     | 8        | 5.700                | 45.600   |
| YgzlgdnT     | 8        | 5.700                | 45.600   |
| Jekyll12     | 8        | 5.964                | 47.712   |
| C0mbu$t1on!  | 11       | 6.570                | 72.270   |

Cependant, nous indiquions que la force d'un mot de passe dépend de son caractère aléatoire. En revanche, l'entropie n'en dépend pas.

C'est parce les valeurs indiquées par *l'entropie par symbole* supposent un mot de passe complètement aléatoire. Par exemple, *`Superman`* et *`YgzlgdnT`* ont tous deux une entropie de *45.6*, mais *Superman* est plus facile à deviner parce que ce n'est pas une suite de caractères aléatoire, c'est quelque chose de connu, et donc c'est plus facile à craquer. Plus un mot de passe repose sur du connu, ou un motif répété, moins son entropie réelle est grande.

D'ailleurs, si vous avez lu mon [billet précédent]({% post_url 2016-09-18-Les craqueurs de mots de passe ne devinent pas ils essaient %}), vous comprendrez très bien pourquoi un mot de passe reposant sur quelque chose de connu ou un motif est plus facile à craquer: il est plus vulnérable aux attaques par dictionnaire.

*Si la cusiosité vous prend, vous pouvez visiter [howsecureismypassword.net](https://howsecureismypassword.net/), y entrer des mots de passe et voir l'estimation de leur robustesse et du temps nécessaire pour les craquer. Vous verrez que "Superman" and "YgzlgdnT" sont totalement différents, car l'algorithme utilisé sur le site prend un compte les mots connus et les motifs. Le site n'enregistre pas les mots de passe que vous tapez, le calcul étant entièrement fait sur votre ordinateur, vous pouvez donc vous amuser sans crainte. Bon, ne tapez pas votre vrai mot de passe pour autant, ça ne sert à rien de chercher les ennuis hein.*

---

## Génération manuelle de mots de passe robustes

---

Les recommandations usuelles proposent:

* **au moins** 8 caractères
* utiliser **tous** les alphabets du clavier: lettres, chiffres et symboles
* **ne contient absolument rien de connu,** comme des choses célèbres, votre nom, pseudo, addresse, entreprise, animal de compagnie, etc...
* **votre mot de passe doit être absolument unique entre tous vos comptes!**

> L'erreur la plus courante dans le choix d'un mot de passe et de penser qu'il est assez sûr.

Les craqueurs de mots de passe sont devenus extrêmement malins. En utilisant des attaques par dictionnaire et des tables arc-en-ciel au lieu d'attaques par force brute, ils ne devinent plus que des mots de passe simples et très utilisés, comme `123456, password, football, superman`… Ils sont maintenant capables de trouver des mots de passe compliqués, comme `k1araj0hns0n, Sh1a-labe0uf, Apr!l221973, Qbesancon321`, ... ([source](http://arstechnica.com/security/2013/05/how-crackers-make-minced-meat-out-of-your-passwords/3/)).

Ils gèrent très facilement les substitutions les plus courantes, comme changer ‘o’ en ‘0’ ou ‘a’ en ’@’, de même que les concaténation, par exemple ajouter des chiffres. Cela signifie aussi que tous ce qui est du domaine publique (personnage célèbre, date, endroit, citation, ...) ou qui peut être facilement obtenu (votre nom, pseudo, adresse, livre favori, animal de compagnie, ...) ne sont en aucun cas pertinent dans le choix d'un mot de passe.

En 2008, *Bruce Schneier* a proposé une [méthode](https://www.schneier.com/blog/archives/2014/03/choosing_secure_1.html) toujours pertinente aujourd'hui: prendre une phrase et la transformer en mot de passe. Choississez donc une phrase entièrement inventée, elle peut même ne rien vouloir dire, et extrayez-en des lettres, en les encodant au passage si vous le souhaitez, par exemple en utilisant du [Leet speak](https://fr.wikipedia.org/wiki/Leet_speak), ou encore mieux un encodage maison.

Avec cette méthode, la phrase `“I endorse the whimsical code of bunny trumpeters!”` peut devenir `1eTheWc0deO|3Ts!`. N'importe quel vérificateur de mot de passe le classifiera en tant que mot de passe fort.

> Un mot de passe robuste est difficile à taper et se rappeler. Dans le cas contraire, cela n'en est sûrement pas un.

Donc cool, vous avez peut-être réussi à créer un mot de passe fort, mais regardez un peu le truc! C'est une tannée à s'en rappeler, et encore plus à le taper sur l'écran de connexion à chaque fois. Vous finiriez sûrement pas demander au navigateur de le mémoriser, ce qui est une mauvaise décision.

Par ailleurs, aurais-je déjà mentionné que votre mot de passe doit être unique pour chacun de vos comptes ? Yep. Cela vous laisse deux possibilités:

* **ninja-style:** créer *N* phrases, convertir chacune d'elles en mot de passe, et se les rappeler toutes… vous aurez sûrement besoin d'une mémoire eidétique pour cela.
* **normal-person-style:** garder le même mot de passe, et le changer juste un tout petit peu pour chaque compte, et se basant par exemple sur le nom du service. Le mot de passe `1eTheWc0deO|3Ts!` que nous avons créé préalablement pourrait ainsi donner `Face1eTheWc0deO|3Ts!Book` pour Facebook, et `Twit1eTheWc0deO|3Ts!ter` pour Twitter.

Dès lors, vous avez enfin une politique de sécurité plutôt correcte, avec un mot de passe unique remplissant les recommandations. C'est cependant très chiant à utiliser chaque jour.

De plus, si un pirate récupère un de vos mots de passe, ils pourrait assez facilement comprendre sa construction et ainsi obtenir l'accès à tous vos comptes. Chuper!

*Si vous avez lu tous mes billets jusqu'ici, félicitations ! Cela n'a pas dû être facile, surtout pour si peu de conseils pratiques. Dès le prochain article, nous commencerons à rentrer dans du concret, et des outils que j'utilise au quotidien. A plus!*

**next milestone: create passwords with dices (released soon)**
