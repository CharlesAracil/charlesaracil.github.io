---
layout: post
title: Diceware, mots de passe et dés
ref: Diceware_passwords_dices
lang: fr
---

Les meilleurs mots de passe sont créés en lançant des dés.

Nous introduisons ici une méthode garantissant à 100% l'obtention d'un mot de passe fort, ou plutôt une **phrase de passe**, l'alternative moderne des mots de passe. Cette méthode vous évitera la corvée d'avoir à créer un mot de passe fort par vous même. Cool!

# Aléatoire vs homogénéité

Dans les billets précédents, nous avons mis en évidence que les meilleurs mots de passe sont aléatoires. Malheureusement, les humains sont trop nuls à l'aléatoire, car **le cerveau humain confond l'aléatoire avec l'homogène.**

Pour le démontrer, je vous propose une expérience.

Demandez à quelqu'un de lancer une pièce de monnaie plusieurs fois (un grand nombre de fois), et notez la suite de piles et faces obtenue. Dans une autre pièce, faites pareil, mais au lieu de lancer une vraie pièce, imaginez le lancer, autrement dit essayez de reproduire mentalement le résultat aléatoire d'un lancer de pièce de monnaie. Pour faciliter la notation, on notera `face=0`, and `pile=1`.

Une fois l'expérience terminée, comparez vos résultats. Vous aurez tous les deux, en moyenne, un nombre égal de *0* et de *1*. Et effectivement, en faisant l'effort d'imaginer un lancer aléatoire, vous avez fait gaffe d'avoir une quantité à peu près égale des deux résultats. Le cerveau comprend intuitivement cette contrainte de l'aléatoire: vu que pile et face ont tous deux 50% de chance d'apparaître, ils devraient le faire un même nombre de fois, en moyenne.

![diceware homogeneity]({{ site.baseurl }}/assets/figures/diceware_g1.png)

Cependant, ce que le bon sens entend par *aléatoire* correspond en réalité à de *l'homogénéité*. Pour le vérifier, **regroupons les lancers par groupe de trois.** Par exemple, si vous obtenez un *face, face, pile*, cela correspondra à un *001*. Dès lors, les résultats possibles ne sont plus simplement *0* ou *1*, mais *000*, *001*, *010*, *011*, *100*, *101*, *110*, *111*.

Maintenant, si vous comptez la fréquence d'apparition de ces différents résultats, vous remarquerez qu'effectivement, avec la vraie pièce de monnaie, ils apparaissent en moyenne autant les uns que les autres. En revanche, avec votre pièce imaginaire, ce n'est pas le cas! **Certains résultats apparaissent plus souvent que d'autres.**

![diceware frequency stability property]({{ site.baseurl }}/assets/figures/diceware_g3.png)

C'est **la proriété de stabilité fréquentielle.** Une pièce de monnaie possède cette propriété, **le cerveau humain ne la possède pas**, car il utilise sa mémoire pour tenir compte des résultats précédents, et essaye de compenser ces résultats dans les tirages précédents, en vue d'obtenir ce qui lui semble être un résultat aléatoire.

Et c'est pour cette même raison que vous ne devriez pas essayer de générer des mots de passe aléatoires vous-même.

*Pour une présentation plus visuelle de ce phénomène, allez voir [cette vidéo](https://www.youtube.com/watch?v=H2lJLXS3AYM), qui l'illustre très bien. Vous trouverez le code source des graphiques de ce billet [ici](https://raw.githubusercontent.com/CharlesAracil/charlesaracil.github.io/master/assets/python/diceware.py).*
# Créer des mots de passe robustes réellement aléatoires: utilisez des dés!

Le **Diceware** est une méthode pour générer des mots de passe aléatoires par agrégation de mots communs du dictionnaire. Donc, en lieu et place de mots de passe comme `Face1eTheWc0deO|3Ts!Book`, vous vous retrouvez maintenant avec une suite de mots aléatoires, comme `correct horse battery staple`. C'est une **phrase de passe, ou passphrase.**

Les passphrases sont plus robustes que des mots de passe si elles sont bien construites, et beaucoup plus facile à mémoriser. En essence, c'est la même chose, les deux notions ne différant qu'en construction, mais elles sont toutes deux des suites de caractères à taper au clavier. Par conséquent, elles peuvent systématiquement substituer les mots de passe traditionnels pour la connexion à vos comptes. **Oubliez les mots de passe, utilisez les passphrases.**

*Il y a cependant une exception. Si le site internet vous empêche d'utiliser de longues séquences de caractères, vous ne pourrez pas utiliser les passphrases. Ce type de contraintes est chiant et inutile, très peu de sites les appliquent encore. Dans tous les cas ne vous en faites pas, on introduira une solution à ce problème dans le prochain billet.*

![xkcd diceware](http://imgs.xkcd.com/comics/password_strength.png)

*Ouais, je sais, beaucoup d'entres vous on déjà vu ce [xkcd](https://xkcd.com/936/) des dizaines de fois, mais bon c'est tellement bien résumé que je ne pouvais pas faire autrement...*

Donc, voici comment ça fonctionne. La méthode *Diceware* est accompagnée d'une [longue liste de mots](http://world.std.com/~reinhold/diceware.wordlist.asc). Chacun de ces mots est couplé avec un nombre. En voici un petit bout:

| Code           | Mot            |
| :------------- | :------------- |
| 21552          | crave          |
| 21553          | craw           |
| 21554          | crawl          |
| 21555          | craze          |
| 21556          | crazy          |
| 21561          | creak          |
| 21562          | cream          |

Chaque chiffre dans le code correspond au résultat d'un lancer de dé. Comme un code à 5 chiffres, vous devrez lancer 5 dés pour obtenir un mot. Par exemple, si mes dés me donnent `2, 1, 5, 5 and 6`, j'obtiendrai le mot `crazy`.

Faites la même chose au moins 6 fois (vous pourriez faire moins, mais 6 est le minimum recommandé) pour obtenir votre passphrase finale. J'ai par exemple obtenu lors de la préparation de ce billet: `verify lagoon province gala anyplace unworn`.

En supposant vos dés parfaitement équilibrés, les résultats sont équiprobables. Il n'y a aucune corrélation algorithmique entre un code, ou ses chiffres, et le mot correspondant. C'est une simple table de correspondance. En conséquence, tous les mots sont également équiprobables. Du point de vue du pirate, cela signifie qu'aucun mot n'a plus de chance d'apparaître qu'un autre, donc la méthode ne donne aucun indice à exploiter pour une éventuelle attaque par dictionnaire. Et puisque une passphrase fait au moins 6 mots, les attaques par force brute sont aussi inutilisables.

*Vous trouverez [ici](https://www.rempe.us/diceware/#eff) un générateur de diceware, juste pour essayer. Bien qu'il utilise le protocole https et des générateurs de nombres aléatoires robustes, il recommande l'utilisation de vrais dés pour générer votre passphrase.*

Si vous vous rappelez mes billets précédents, vous pourriez defendre que des mots communs du dictionnaire ne sont pas adaptés pour construire un mot de passe, puisqu'ils sont connus et composés seulement de lettres en minuscule. Et cela paraîtrait effectivement logique. Pourtant, il s'avère que la taille de la passphrase générée, et le caractère aléatoire des mots qui le composent, compensent largement ces considérations. Par conséquent, les passphrases *diceware* sont parfaitement adaptées pour une passphrase.

Vous vous retrouvez ainsi avec **un mot de passe, ou en l'occurrence une passphrase, plus facile à mémoriser et à taper**, car il est constitué de mots que vous connaissez et utilisez peut-être au quotidien. **Et son caractère aléatoire le rend extrêmement robuste.**

*Il reste un problème non-résolu: votre passphrase doit toujours être unique pour tous vos comptes. Or retenir un grand nombre de passphrases est de toute évidence impossible. Mais il y a une solution pour cela: les gestionnaires de mots de passe ! Combinés avec une seule passphrase diceware, vous obtenez une politique de sécurité presque impénétrable. C'est parti !*

[**prochaine étape: gestionnaires de mots de passe**](released soon)
