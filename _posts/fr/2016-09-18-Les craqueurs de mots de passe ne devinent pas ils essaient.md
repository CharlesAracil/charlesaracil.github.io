---
layout: post
titre: Ceux qui craquent les mots de passe ne devinent pas, ils essaient.
ref: Password_cracker_dont_guess_just_try
lang: fr
---

Conçevoir de bons mots de passe sans savoir comment ils sont craqués est comme créer de bonnes serrures sans savoir comment elles sont crochetées.

Je vous propose donc une courte introduction sur le fonctionnement d'un craqueur de mot de passe, l'outil permettant de craquer des mots de passe. Ainsi, vous verrez un peu plus précisement ce contre quoi vous devez lutter.

---

## Fonctionnement d'un craqueur de mot de passe

---

Un craqueur de mot de passe ne peut pas deviner votre mot de passe sans coup de pouce. Il a besoin d'un indice à partir duquel travailler. Et [si vous vous souvenez]({% post_url 2016-04-09-Comment-ordinateur-enregistre-pas-mot-de-passe %}), la seule information rémanente qu'il subsiste de votre mot de passe sur l'ordinateur est... son code de hachage. **Donc pour craquer un mot de passe, on a d'abord besoin de son code de hachage, où qu'il soit stocké.**

Ce n'est pas un problème si vous avez un accès physique à l'ordinateur, mais c'est beaucoup plus complexe à réaliser depuis un accès à distance. C'est cependant tout à fait possible, et [ça arrive souvent](https://haveibeenpwned.com/PwnedWebsites), même à des groupes travaillant dans le domaine de la sécurité, par exemple le gestionnaire de mot de passe [LastPass](https://lastpass.com/fr), [piraté en 2015](http://lifehacker.com/lastpass-hacked-time-to-change-your-master-password-1711463571). Les pirates visaient très probablement les codes de hachage des utilisateurs.

Plus précisement, la location des codes de hachage des mots de passe dépend du système d'exploitation que vous utilisez:

* **Windows:** `"C:\Windows\system32\config\SAM"`
* **Linux:** `/etc/passwd` and `/etc/shadow`
* **Mac:** `/var/db/dslocal/nodes/Default/users/username.plist`

Dans tout les cas, ce ne sont que des fichiers texte: ils peuvent être lus directement, si vous en avez accès. Encore une fois, l'obtention de cet accès est complexe à distance, mais réalisable, mais toujours triviale avec un accès physique à l'ordinateur, sous réserve que le disque dur ne soit pas chiffré, ce qui n'est pas le cas la plupart du temps.

Cependant, une fois un code de hachage obtenu (volé), il reste un problème majeur: le *hachage* est une *fonction à sens unique*, ce qui signifie qu'il est impossible de calculer le mot de passe original à partir de son code de hachage.

Il est seulement possible de faire ce que fait votre ordinateur pour [certifier votre mot de passe]({% post_url 2016-04-09-Comment-ordinateur-enregistre-pas-mot-de-passe %}): choisir un mot de passe, calculer son code de hachage, et le comparer à celui volé. S'ils sont égaux, ça veut dire que le mot de passe choisi était le bon.

Et bien, c'est tout. Un craqueur de mot de passe n'est qu'un logiciel qui génère une flopée de mots de passe, calcule leur code de hachage, et les compare au code de hachage volé. Si un de ces mots de passe correspond, cela veut dire que c'est le mot de passe recherché.

![password cracking principle]({{ site.baseurl }}/assets/figures/password-cracker-principle.png)

*Un craqueur de mot de passe est à peine un outil de piratage, plus une calculette de code de hachage.*

---

## Crocheter la serrure ou trouver la clé.

---

L'idée reçue dominante est que les craqueurs de mot de passe craquent directement votre session Windows, ou votre compte sur le site visé, comme s'ils les leuraient pour leur faire avouer le mot de passe, ou comme s'ils tapaient des mots de passe jusqu'à ce que la session s'ouvre.

C'est en vérité impossible, car les systèmes possèdent des mécanismes de sécurité contre de telles techniques.

Une protection basique, appliquée par exemple sur les cartes SIM ou la version *Enterprise* de Windows, est de vérouiller le compte au bout de *N* tentatives, généralement trois. Etant donné qu'un craqueur de mot de passe doit essayer des millions de mots de passe, la session se trouverait vérouillée bien avant qu'il trouve le mot de passe.

Je ne suis pas fan de cette protection, car on finit tous par vérouiller notre propre session, en aillant pas remarqué que le vérouillage majuscule était activé...

Une meilleure solution, maintenant implémentée par n'importe quel système décent, est d'imposer une temporisation. Chaque fois qu'on entre un mauvais mot de passe dans notre système, il attendra un peu avant de nous laisser essayer à nouveau. Cela peut être une attente courte, comme une seconde, ce qui n'est pas très génant pour nous, mais terrible pour un craqueur de mot passe, car dans la période qu'il doit attendre, il aurait pu essayer un million de mots de passe. Ainsi, son déroulement est ralenti par un facteur de un million.

D'ailleurs, la temporisation est imposée *per se* pour les sites internet, à cause de la latence du réseau, qui empêche les attaques par force brute sur les serveurs. Bon... en fait ça se fait, mais ça s'appelle une *"attaque par déni de service"*, qui vise à faire crasher les serveurs plutôt qu'à obtenir leurs informations. Aucun intérêt dans notre cas.

*Les craqueurs de mot de passe ne crochètent pas la serrure, ils ne peuvent pas. Ils essaient juste de trouver la clé, et ouvrent la serrure avec.*

---

## Stratégie de hacking: choisir des mots de passes à essayer

---

Nous avons vu que les craqueurs de mot de passe essaient juste des mots de passe, et comparent leur code de hachage à celui volé.

Ce n'est cependant pas si facile, car **tester tous les mots de passe possibles est impossible.** Il y en a trop, une infinité en fait.

De ce fait, le pirate a besoin de penser en amont et de définir une stratégie, qui consiste à déterminer **quel mots de passe devrait essayer son craqueur de mot de passe.**

Voici les trois techniques les plus courantes.

### Force brute

Une attaque par force brute consiste simplement à tester toutes les combinaisons possibles, dans un intervalle défini.

Si nous craquions un cadenas à 4 chiffres, nous testerions alors les combinaisons *0000*, *0001*, *0002*... jusqu'à *9999*. On pourrait le faire manuellement avec un shuya de patience. Disons un essai par seconde, donc presque 3 heures de manipulation dans le pire cas. Un ordinateur le fait presque instantanément.

Si nous craquions un mot de passe de 8 caractères de long composé uniquement de minuscules, on essaierait *a, b... z, aa, ab, ac... zz, aaa, aab... zzz, aaa... aaaaaaa... zzzzzzz*. Evidemment, on ne pourrait plus le faire manuellement, comme il y a 208.827.064.576 combinaisons différentes. Un ordinateur moyen pourrait cependant toutes les essayer en deux jours, en estimant qu'il fasse 10,000,000 essais par seconde. Un bon ordinateur, ou un groupe d'ordinateurs travaillant ensemble, peut faire 100,000,000 par secondes, donc environ une demi-heure seulement serait nécessaire.

Mais les mots de passe ne sont pas limités en taille, et peuvent contenir des caractères minuscules et majuscules, des chiffres et des symboles, pour un total de 96 signes typographiques. Par conséquent, le nombre de combinaisons pour un mot de passe de taille `N` est `96^N`.

Un mot de passe de 8 caractères a maintenant 7.2 quadrillion de combinaisons, et toutes les essayer prendrait plus de deux siècles sur un ordinateur moyen, 23 ans sur un très bon, ce qui est... plutôt dissuasif.

Par conséquent, une attaque par force brute n'est valable que pour craquer des mots de passe très courts, à savoir inférieur à 8 caractères. Malheureusement, un grand nombre de mots de passe couramment utilisés sont inférieurs à cette taille.

Des pirates avec peu d'unités de calcul pourraient ne pas être capables de craquer un mot de passe de 8 caractères. Mais de tels mots de passe sont vulnérables face à des groupes mieux équipés en puissance de calcul. [Trois ans auparavant](http://arstechnica.com/security/2012/12/25-gpu-cluster-cracks-every-standard-windows-password-in-6-hours), un cluster SLI cluster, à savoir plusieurs cartes graphiques travaillant ensembles, s'est avéré capable de **craquer par force brute n'importe quel mot de passe de 8 caractères de long en moins de 6 heures!**

**N'utilisez pas de mots de passe plus court que 8 caractères... jamais.**

### Dictionnaire

Une attaque par dictionnaire est une approche plus maligne. Elle repose sur le simple fait que beaucoup de gens utilisent les mêmes mots de passe.

Tristement, des mots de passe tels que *123456*, *football*, *qwertyuiop* ou *starwars* sont toujours en [tête de liste](http://gizmodo.com/the-25-most-popular-passwords-of-2015-were-all-such-id-1753591514) des mots de passe les plus couramment utilisés.

De ce fait, on peut se procurer une liste de ces mots de passe, et tester spécifiquement ces derniers. De telles listes se trouvent facilement sur le net ([exemple](http://www.openwall.com/wordlists/)). La plupart sont gratuites, bien qu'elles puissent être moins complètes, et contiennent déjà des millions de mots de passe.

Cette méthode est statistiquement plus efficace qu'une attaque par force brute, car elle prend en compte les habitudes des utilisateurs, et ne se limite pas à une taille de 8 caractères.

**Soyez sûr de ne pas choisir un mot de passe qui a des chances d'avoir déjà été pensé par d'autres.**

### Rainbow table

Une attaque par table arc-en-ciel est une légère amélioration d'une attaque par dictionnaire. Quand on effectue une attaque par dictionnaire, on a toujours besoin de calculer un code de hachage pour chaque mot de passe contenu dans le dictionnaire, ce qui prend beaucoup de temps. En comparaison, comparer ces codes de hachage est une opération rapide.

Par conséquent, on préfererait avoir un code de hachage pré-calculé avec le mot de passe dans une table d'équivalence. C'est fondamentalement ce qu'offre une table arc-en-ciel: elle fournit directement le code de hachage correspondant à un mot de passe, ou plus exactement un mot de passe correspondant à un code de hachage.

De cette façon, pour un code de hachage volé, on a seulement à regarder dans notre table arc-en-ciel si ce code de hachage existe. Si c'est le cas, elle fournie immediatement le mot de passe correspondant, qui est celui que nous cherchions.

**Si votre mot de passe est un de ceux disponible dans les tables arc-en-ciel, soyez assuré qu'il ne prendra pas beaucoup de temps à craquer.**

---

## Combiner cette approche avec de l'ingénierie sociale

---

Les tactiques mentionnées précedement ne reposent sur aucune information personnelle: ils n'ont pas besoin de savoir qui vous êtes pour pour essayer de vous pirater. Paradoxalement, c'est une faiblesse, car plus vous en savez sur quelqu'un, plus vous disposez d'armes contre lui.

C'est pourquoi il est dit que l'amitié doit être octroyé avec discernement: vous donnez des armes en supposant que votre ami ne s'en servira pas contre vous. C'est aussi pourquoi l'utilisation par Facebook du mot *"ami"* est très dangereuse et enclin à des comportements imprudnets. Mais c'est sûr, dire *"j'ai 297 connaissances!"*, ça a moins de gueule.

Dans la perspective d'un pirate, les informations sur votre cible peuvent être utilisées pour craquer son mot de passe. L'hypothèse ici étant que les gens utilisent leurs informations personnelles pour créer leur mot de passe.

D'ailleurs, information personnelle ne veut pas nécessairement dire information privée, mais regroupe à la fois informations publiques et privées, tant que c'est quelque chose qui vous identifie.

De telles données peuvent être: prénom, nom de famille, pseudonyme, date de naissance, nom de jeune fille, nom de l'animal de compagnie, ville de naissance, ville actuelle, truc préféré (animal, acteur, personnage, groupe de musique, chanson, film, lieu, couleur, ...), profession, nom du frangin, ... etc.

Par exemple, si nous voulions pirater spécifiquement une personne du nom de *Sophie*, nous pourrions utiliser soit une attaque par force brute ou une attaque par dictionnaire, mais en y ajoutant les spécificités de *Sophie*. On pourrait essayer toutes sortes de combinaisons contenant *Sophie, Soph, Sof, Sophle, ...* et calculer différentes combinaisons, ajouter des lettres, chiffres ou symboles: *Sophie0145, !SofPwd7894, S0ph1E38004, ...*

Les ordinateurs sont très bons pour créer des millions de ces variations, ils pourraient bien trouver une correspondance, surtout s'ils n'utilisent pas seulement le nom mais tout ce qu'on pourrait trouver sur notre cible.

Vu la facilité avec laquelle nos informations peuvent maintenant être trouvées sur internet, il y matière...

**Prenez garde à ce que vous publiez sur internet. Considerez que chaque information que vous lachez n'est plus valable pour en faire un mot de passe.**

*Pour des raisons de clarté, je me suis permis quelques approximations. Par exemple, un même mot de passe peut avoir deux codes de hachage différents, en utilisant un processus appelé le salage. Donc pour craquer un mot de passe, il faudrait en fait récupérer son code de hachage et le sel. Read [wikipedia](https://fr.wikipedia.org/wiki/Salage_(cryptographie)) pour plus d'info.*

[**next milestone: Les mots de passe sont dépassés**]({% post_url 2016-09-25-Les-mots-passes-sont-depasses %})
