---
layout: post
title: Un cheminement itératif en sécurité
ref: an-iterative-journey-to-security
lang: fr
---

Soyons clair : la sécurité parfaite n'existe pas, il y aura toujours un maillon faible.

Quoi que vous fassiez pour améliorer votre politique de sécurité, vous ne ferez que déplacer ce maillon faible vers un autre dans la chaîne. Le point faible peut être un bogue de sécurité, un virus, une vulnérabilité "[Zéro-Day](https://fr.wikipedia.org/wiki/Vuln%C3%A9rabilit%C3%A9_Zero_day)", ou simplement vous, car vous auriez choisi un mot de passe facile à deviner, laissé un port incertain ouvert sur votre pare-feu, ou ouvert la pièce-jointe malveillante d'un mail. Il s'avère que les comportements dangereux des utilisateurs sont responsables de la plupart des actes de piratage enregistrés. Conséquence: plus de [la moitié de la population déjà piratée]((http://money.cnn.com/2014/05/28/technology/security/hack-data-breach/)), et des [millions d'ordinateurs]((http://www.cnet.com/news/finjan-finds-botnet-of-1-9-million-infected-computers/)) transformés en [zombies](https://fr.wikipedia.org/wiki/Machine_zombie).

Il vous faut pourtant peu pour vous construire une politique de sécurité vous rendant difficile à pirater, et réduire grandement les dégâts dans le pire cas.

>Pour connaître ton Ennemi, tu dois devenir ton Ennemi.
– Sun Tzu, L'Art de la Guerre

Selon moi, glanner des techniques de protection sur le net n'est pas suffisant, il faut comprendre un minimum ce que vous faites. Dans le cas contraire, le maillon faible sera toujours vous, ce que vous ne voulez certainement pas.

Il ne s'agit pas de devenir un pirate de haute voltige, j'en suis moi-même très loin, mais assimiler assez de connaissances de base pour ne pas dépendre aveuglement des outils et techniques de protection. Ainsi, vous saurez ce que font les outils, comment les utiliser correctement, et surtout comment les protéger. Car si un pirate ne parvient pas à pénétrer votre système par les moyens conventionnels, il essaiera de pénétrer les outils que vous utilisez pour le protéger.

*À quel point un système doit être sécurisé dépend des attentes de chacun. Une politique de sécurité est une affaire d'équilibre entre sécurité et facilité d'utilisation. Pour en tenir compte, j'adopterai une installation incrémentale (brique par brique). Je vous laisse juge pour savoir quand vous arrêter. Évidemment, plus c'est sécurisé, mieux c'est.*

Voici ce que l'on va voir : 

* génération manuelle de mots de passe robustes
* gestionnaire de mots de passe et génération automatique de mots de passe robustes
* double-authentification pour une sécurité à toute épreuve.

Mais avant toute chose, il serait approprié, voire nécessaire, de rappeler ce qu'est le piratage.

---

## Recadrage sur la définition de piratage

---

Ces dernières années, les médias ont éhontément déformé la notion de piratage. L'industrie du cinéma est également responsable, bien qu'on pourrait la pardonner plus facilement, son but premier n'étant pas de nous informer mais de nous distraire. Je pense que c'est de la paresse.

Les Wachowkis ont fait l'effort de faire apparaître l'outil de balayage de port `Nmap` dans le second opus de la trilogie Matrix. La série "Mr Robot" de Sam Esmail a basé son univers sur des connaissances extrêmement pointues du monde informatique et des techniques de piratage, introduisant *attaques RUDY*, *rootkits* et *Rasberry Pi*. Ces deux oeuvres n'en restent pas moins des plus palpitantes.

Diffuseurs d'information et gouvernements ne semblent pas comprendre les technologies numériques. Pour parler de serveurs, ils continuent de faire référence à "ces sortes de gros ordinateurs dans des batiments top-secret", pendant que le gouvernement français songe à résoudre les problèmes de sécurité informatique avec son projet délirant d'[os souverain](http://lexpansion.lexpress.fr/high-tech/delphine-batho-defend-la-creation-d-un-os-souverain-et-desespere-internet_1756517.html), un système d'exploitation qui serait développé par les entités gouvernementales. Le litige entre le gouvernement américain et Apple pour qu'[Apple développe un logiciel](http://www.nytimes.com/2016/03/18/technology/apple-encryption-engineers-if-ordered-to-unlock-iphone-might-resist.html?&_r=0) (un système d'exploitation en fait, mais ils semblent ne pas l'avoir su sur le coup) permettant de forcer l'accès du téléphone de n'importe quel utilisateurs est très révélateur de l'incompréhension régnant au sein de nos sphères dirigeantes sur les enjeux de sécurité et de respect de la vie privée engendrés par nos technologies.

Dans le vrai monde de la vérité véritable, les pirates ne tapent pas comme des dingues sur leur clavier, ils ne portent pas de masques (merci les campagnes anti-piratage encombrant nos DVD...) et surtout ne provoque pas l'apparition frénétique de têtes de mort sur nos écrans.

>“Le piratage est la discipline consistant à modifier les propriétés d'un système, dans le but d'accomplir un objectif différent de celui prévu initialement. La personne engagée de façon continue dans des activités de piratage, et ayant accepté le piratage en tant que mode de vie et philosophie, est appelée un pirate."
– [whatishacking.org](http://whatishacking.org/)

Cette définition implique que le terme "pirate" n'est pas spécifiquement lié à l'informatique. Un artiste qui utilise des cure-dents pour créer de superbes scultures sont de ce point de vue des pirates, puisqu'ils utilisent les cure-dents en dehors de leur contexte d'utilisation initial. Cependant à des fins de clarté, nous réduirons la définition aux pirates informatiques.

Le but d'un pirate n'est pas de vous taper sur le système (même s'ils y arrivent plutôt bien) mais de vous soutirer quelque chose. En conséquence, **il est de son intérêt que vous ne sachiez pas que vous avez été piraté.** Il pourra alors:

* vous espionner pour collecter plus d'information utiles que ce qu'il été capable de voler lors de son accès à votre système. Des données personnelles, des numéros de cartes banquaires ou les mots de passe de vos comptes sont des informations valables qu'un pirate pourrait vouloir vous prendre.
* utiliser votre ordinateur pour pirater le système d'un autre, votre ordinateur est alors appelé un [zombie](https://en.wikipedia.org/wiki/Zombie_(computer_science)). Les zombies sont très utiles car le piratage requiert souvent beaucoup de puissance de calcul, soit pour casser des mots de passe, soit pour des attaques comme du "Déni de service (DoS)", qui grossièrement consiste à envoyer une quantité massive de requêtes à un serveur, plus qu'il ne peut en supporter, pour le forcer à s'arrêter ou ne plus pouvoir traiter les requêtes légitimes d'autres utilisateurs.

Mais pour ce faire, ils ne peuvent pas juste prendre le contrôle de votre ordinateur, comme par magie. Ils doivent trouver un chemin, une porte d'entrée, une faille à exploiter dans votre système. Parfois, la faille est quelque chose que vous ne pouvez pas contrôler, comme un bug dans votre système d'exploitation (ou une porte dérobée...), mais ils deviennent très rares. Souvent, vous créez la faille vous même, ce qui signifie que vous pouvez l'éviter en en sachant un peu plus sur les ordinateurs, et en la corrigeant.

Par soucis de justice, j'aimerais noter que tous les pirates ne sont pas de malveillants criminels. En réalité, il y a trois types de pirates, désignés par des couleurs de chapeaux (*hats* en anglais) :

* **black hats** : ce sont les pirates que vous connaissez, qui "utilisent leurs super-pouvoirs pour faire le mal".
* **white hats** : les pirates éthiques, s'introduisant dans les systèmes dans le but de trouver leurs failles de sécurité, et prévenir les développeurs pour qu'ils puissent les corriger. Ils souhaitent faire du monde un meilleur endroit.
* **grey hats** : ils sont en quelque sorte un mélange de "white hats" et "black hats". Leurs activités de pirate servent une idéologie pour laquelle ils se battent. Ils ne veulent pas spécialement blesser quiconque, mais peuvent se battre contre le système en place, qu'ils trouvent injuste. Guy Fawkes, du film "V for Vendetta", est un célèbre "grey hat".

Les ingénieurs en informatique et les "white hats" travaillent à rendre nos ordinateurs de plus en plus sûrs, si bien que les "black hats" ont une marge de manoeuvre de plus en plus restreinte. Cependant, à cause d'un manque d'éducation, les gens n'ont toujours pas connaissances de bonnes politiques de sécurité, ce qui implique que les pirates privilégieront souvent la faille humaine lors de leurs attaques. Si l'existence d'une politique de sécurité absolue n'est que pure utopie, le moins que vous puissiez faire est d'être sûr de ne avoir laissé de porte grande ouverte.

*Les pirates, au sens large, sont des personnes intelligentes, j'apprécie et adopte leur état d'esprit. Ils sont curieux, passionnés, ont un esprit critique et voient le monde non-pas comme on leur dit de le voir, mais comme ils veulent qu'il soit. Les "white hats" sont probablement plus efficace à rendre nos technologies plus sécurisés que les entreprises ou les gouvernements, qui continuent à vous dire sans distinctions que les pirates sont des méchants. La curiosité n'est pas un vilain défaut, le manichéisme en revanche...*

***prochaine étape: mots de passe (prochainement)***

