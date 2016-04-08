---
layout: post
title: Comment votre ordinateur n'enregistre pas les mots de passe
ref: how-computers-dont-store-passwords
lang: fr
---

Un pirate est incapable de voler un mot de passe, car un mot de passe n'est stocké nul part... du moins en théorie.

Cela signifie que même si un pirate accède à l'intégralité de votre ordinateur, ou votre compte en ligne, il ne sera toujours pas en mesure de connaître votre mot de passe. De fait, **votre ordinateur n'a pas besoin de connaître votre mot de passe, il a seulement besoin de certifier que vous avez entré le bon.** Et aussi contre-intuitif que cela puisse paraître, un ordinateur peut s'en assurer sans connaître votre mot de passe. Il n'a besoin que de son `code de hachage`.

---

## Le principe du hachage

---

Un code de hachage est comme une empreinte, c'est un identifiant unique associé à votre mot de passe, calculé à partir de ce dernier. **Deux mots de passe différents donnent deux code de hachage complètement différents**, même si ces mots de passe ne diffèrent que d'un seul caractère. Le processus de hachage repose sur une `fonction à sens unique`.

> "En informatique, une fonction à sens unique est une fonction facile à calculer sur chaque entrée, mais pour laquelle il est difficile de retrouver l'antécédent d'une image."
– [wikipedia.org](https://fr.wikipedia.org/wiki/Fonction_%C3%A0_sens_unique)

Énoncé plus simplement, une fonction à sens unique est une transformation qui ne peut pas être inversée facilement. Par exemple, un puzzle est une fonction à sens unique, car il est très facile de prendre le puzzle complet et le casser en petites pièces, par contre il est très difficile de reconstruire le puzzle une fois désassemblé. Les grilles de Sudoku sont un autre exemple de fonction à sens unique, elles sont [faciles à créer](http://www.wikihow.com/Create-a-Sudoku), mais difficiles à résoudre.

Il convient de préciser que *"difficile"* est un terme relatif, ça dépend de qui ou quoi effectue l'exercice. Traiter une image est très facile pour un humain mais très difficile pour un ordinateur, tandis qu'effectuer des multiplications et des divisions est très difficile pour un humain, et pourtant trivial pour un ordinateur. Les puzzles et les Sudokus sont des fonctions à sens unique pour un humain, mais pas pour un ordinateur qui les résout assez facilement.

*Cette difficulté est liée au concept de [complexité de calcul](https://fr.wikipedia.org/wiki/Th%C3%A9orie_de_la_complexit%C3%A9_(informatique_th%C3%A9orique)), qui est un domaine à part entière, donc nous n'en parlerons pas plus.*

Les algorithmes de hachage sont un sous-ensemble des fonctions à sens unique. Ils sont difficiles à résoudre tant pour les humains que pour les ordinateurs, et obéissent à une `propriété de non-collision`, ce qui signifie que chaque entrée donne un résultat différent. Dans notre cas, cette propriété assure que deux mots de passe différents auront deux codes de hachage différents.

Les ordinateurs utilisent différents algorithmes de hachage, les plus connus étant le `Message Digest 5 (MD5)` et le `Secure Hash Algorithm (SHA)`. Les deux consistent à prendre une entrée, comme un mot de passe, et leur appliquer une série d'opérations mathématiques pour les transformer en chaîne hexadécimale, une chaîne constituée de chiffres et de caractères entre *A* et *F*. Ci-dessous figurent quelques exemples de mots de passe et leur code de hachage respectif en *MD5* et *SHA*:

| Mot de passe         | Hash avec MD5        | Hash avec SHA-512  |
| -------------------- | -------------------- | ------------------ |
| 123                  | 202cb962ac59075...   | 3c9909afec25354... |
| 124                  | c8ffe9a587b126f...   | 813d00895b26351... |
| Ghostbuster          | 202cb962ac59075...   | 5ce72e772ca8135... |
| Superman123          | b40b8f862d816d6...   | 9b1c3c6c94a42f4... |

*Si vous voulez essayer par vous-même, je vous recommande [onlinemd5.com](http://onlinemd5.com/), un générateur de code de hachage facile d'utilisation.*

Calculer le code de hachage d'un mot de passe est très facile, mais deviner le mot de passe correspondant à son code de hachage est quasiment impossible, sous réserve que le mot de passe soit assez robuste.

![hash transformation]({{ site.baseurl }}/images/password-certification-hashing.png)

**Cette propriété est la pierre angulaire de la certification de mot de passe.**

---

## La certification de mot de passe

---

La certification de mot de passe est le processus que votre ordinateur effectue afin de vérifier que le mot de passe que vous avez entré et bien celui qui correspond à votre compte.

Afin de fixer les idées, partons du scénario dans lequel vous créez un compte sur votre système d'exploitation favori, comme lors de son premier démarrage, puis sur lequel vous vous connectez. Le schéma serait le même pour certifier un mot de passe sur un service en ligne.

Tout d'abord, votre système d'exploitation vous propose de choisir un mot de passe. Après réflexion, vous choississez `Ghostbuster`, qui est un très mauvais mot de passe, mais gardons les choses simples. Toujours est-il que vous entrez votre mot de passe, et voici ce qu'il se passe dans les coulisses :

![password-certification-creation]({{ site.baseurl }}/images/password-certification-creation.png)

Votre mot de passe est manipulé par une fonction de hachage, comme celle dont nous parlions plus tôt. Le code de hachage généré est alors enregistré en mémoire, tandis que votre mot de passe est... **entièrement détruit et oublié !** Votre système d'exploitation n'en a plus une trace, et ne pourrait donc plus le récupérer même s'il le voulait.

Vous décidez maintenant de vous connecter. Supposons que vous fassiez une faute de frappe en entrant votre mot de passe la première fois, avant de finalement le taper correctement au second essai. Voici de nouveau ce qu'il se passe dans les coulisses :

![password-certification-login]({{ site.baseurl }}/images/password-certification-login.png)

Chaque fois que vous entrez un mot de passe, le système calcule son code de hachage, puis le compare à celui qu'il a en mémoire :

* si les deux codes de hachage ne sont pas égaux, cela signifie que le mot de passe que vous avez entré n'est pas le même que celui entré lors de la création du mot de passe, auquel cas le système vous refuse l'accès.
* si les deux codes de hachage sont égaux, cela signifie que vous avez entré le bon, et donc le système vous laisse accéder à votre compte.

J'insiste, **le système n'a eu besoin à aucun moment de connaître votre mot de passe pour certifier celui que vous avez entré**, puisqu'il a seulement utilisé les codes de hachage. Par ailleurs, un système ne peut pas confondre deux mots de passe, puisque deux mots de passe ont forcément deux codes de hachage différents.

---

## Les imperfections de la vraie vie

---

Vous avez peut-être remarqué sur certains services en ligne que la taille de mot de passe est limitée. Pourtant nous venons de démontrer qu'ils n'ont pas besoin d'enregistrer votre mot de passe, puisqu'ils peuvent utiliser son code de hachage, qui est une chaîne de caractères de taille fixe.

Par conséquent, **il n'y a aucune raison de limiter la taille de mot de passe,** puisqu'il ne sera enregistré nul part... *à moins que si*.

Dans la vraie vie, certains services enregistrent les mots de passe, ce qui est une très très mauvaise idée, parce que si un pirate pénètre leur système, ils chercheront très probablement ces mots de passe. La facilité de les obtenir dépendra si oui ou non un chiffrement a été mis en place pour protéger les mots de passe:

* **dans le meilleur cas,** le chiffrement est utilisé, si bien qu'un pirate ne pourra pas récupérer votre mot de passe, à moins que celui-ci soit faible ou que la méthode de chiffrement ait une faille.
* **dans le pire cas,** qui est d'ailleurs celui que vous devriez toujours considérer quand il s'agit de sécurité, aucun chiffrement n'est utilisé, donc votre mot de passe est enregistré en clair, et le pirate n'a qu'à le lire et l'utiliser.

Cette contrainte de taille sur les mots de passe n'est pas limitée à de petits services en ligne peu connus. Elle est présente chez des entreprises très connues, comme *Paypal* ou *Ebay*.

En restant optimiste, on pourrait supposer une raison technique. Ils pourraient ne pas avoir mis à jour l'application gérant le formulaire d'inscription, ou simplement utiliser une chaîne de caractère de taille fixe pour enregistrer temporairement le mot de passe, qui sera haché ensuite. *Ebay* limite actuellement la taille à 64 caractères, ce qui pourrait être un compromis entre un mot de passe assez long pour satisfaire la plupart des utilisateurs et éviter de gérer des chaînes de caractères de taille dynamique dans leur moteur interne, ce qui pourrait nécessiter une configuration supplémentaire, mais j'en doute. Dans ce cas, le mot de passe pourrait effectivement ne pas être enregistré, mais on ne peut pas en être sûr sans recherche plus approfondie.

Enregistrer votre mot de passe pourrait aussi servir à vous le renvoyer dans le cas où vous l'auriez oublié, ce qui évidemment est une idée stupide. À moins que vous n'ayez mis en place un chiffrement, avec [GnuPG](https://www.gnupg.org/) par exemple, **les communications par email ne sont absolument pas sécurisées,** ce qui signifie que tous les emails que vous envoyez et recevez circulent en clair sur le réseau, si bien que quiconque écoute votre traffic est en mesure de lire ces emails sans plus d'effort. Cette personne pourrait alors récupérer votre mot de passe et s'en servir. La récupération d'un mot de passe oublié devrait toujours être géré en utilisant un [lien temporaire de réinitialisation](https://www.owasp.org/index.php/Forgot_Password_Cheat_Sheet#Step_3.29_Send_a_Token_Over_a_Side-Channel).

Donc la prochaine fois que vous voyez de tels formulaires, envoyez un email à l'entreprise et demandez leur pour quel raison ils ont besoin de votre mot de passe...

---

## Anecdote de vie

---

Je me suis récemment inscrit à un service de vente en ligne. Juste après la finalisation de l'inscription, j'ai reçu un email. Imaginez vous combien j'étais content en me rendant compte que cet email contenait le mot de passe que je venais juste de choisir !

![screenshot-password-send-after-subscription.png]({{ site.baseurl }}/images/screenshot-password-send-after-subscription.png)

Le courrier se payait même le luxe de prodiguer des conseils sur comment protéger mes informations confidentielles... c'est l'hôpital qui se fout de la charité.

Je ne suis pas parvenu à imaginer de raison d'être pour cet email. J'ai envoyé un message à l'équipe du site, mais n'ai pas obtenu de réponse. Après une recherche rapide, j'ai découvert que cette habitude était répandue. Le site internet [plaintextoffenders.com](http://plaintextoffenders.com/) référence tout un tas de ce genre d'emails, dans lesquels le mot de passe était juste ... écrit.

*Ces failles de sécurité sont comme les comportements anti-sociaux: présents parce que personne ne s'en soucis activement. La prochaine fois que vous en voyez une, ne partez pas avant d'avoir envoyé un email au service concerné. Il en ignorera certainement quelques-uns, mais certainement pas des centaines.*

***prochaine étape: de la génération de mots de passe robustes au néant (prochainement)***

