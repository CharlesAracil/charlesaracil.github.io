---
layout: post
title: An iterative journey to security
ref: an-iterative-journey-to-security
lang: en
---

Let’s get things straight: perfect security does not exist, there'll always be a weakest link.

Whatever you do to enhance your security policy, you’ll merely translate this weakest link to another place in the chain. The weakness can be a security bug, a virus, a [zero-day exploit](https://en.wikipedia.org/wiki/Zero-day_(computing)), or just you, because you may have chosen an easy-to-guess password, left an unsecure port open on your firewall, or opened a malicious email attachment. As it turns out, hazardous user actions are responsible for the vast majority of hacking records, resulting in almost [half the population](http://money.cnn.com/2014/05/28/technology/security/hack-data-breach/) having their personnal information stolen, and [millions of computers](http://www.cnet.com/news/finjan-finds-botnet-of-1-9-million-infected-computers/) turned into [zombies](https://en.wikipedia.org/wiki/Zombie_(computer_science)).

However, with just a few things, you can build a security policy that will make it really difficult to hack you, and dramatically mitigate damage in the worst case.

>To know your Enemy, you must become your Enemy.
– Sun Tzu, The Art of War

In my opinion, it’s not enough to just pick up techniques around the Web, you must understand the basis of what you’re doing. If you don’t, the weakest link will still be you, and surely you don’t want that.

I’m not saying you have to become highly skilled hackers - I’m not one myself - but you might want to get enough knowledge not to blindly rely on tools. That way, you’ll know what the tools do, how to use them properly, and above all how to protect them. Because if a hacker fails to penetrate your system with regular techniques, he’ll try to penetrate the tools you’re using to protect it first.

*Everyone has different standards regarding how secure they want their system. Security policy is a matter of balance between security and user-friendliness. To accommodate that, I pursue an incremental setup toward security. You could stop reading when you find your security policy is good enough for your needs and expectations. However, the more the better.*

Here’s an overview of what we’ll see in next posts:

* strong passwords manual generation
* password managers and automatic strong password generation
* double-authentification for bullet-proof security

But first things first, it might be appropriate - mandatory - to remind what hacking is.

---

## Refocus on hacking definition

---

Over the past years, the media have shamelessly misguided us on what hacking is. We could forgive the film industry to do so, because its common purpose is not to inform, but to entertain. I think that’s just laziness.

The Wachowkis honourably used the actual port scanner security tool `Nmap` in their Matrix sequel movie. The serie “Mr Robot” from Sam Esmail based its universe on a really accurate knowledge of computer hacking techniques, introducing *RUDY attacks*, *rootkits* or use of a *Raspberry Pi*. Both of them managed to keep their creation breathtaking anyway.

News broadcasters and governments seem not to understand digital technologies at all. They keep refering to servers as “those big computers in highly secret facilities” in the news, while the french government plans to solve security issues with its delirious [souvereign os](http://lexpansion.lexpress.fr/high-tech/delphine-batho-defend-la-creation-d-un-os-souverain-et-desespere-internet_1756517.html), a government-made operating system. The pressure of the US government to make [Apple develop a software](http://www.nytimes.com/2016/03/18/technology/apple-encryption-engineers-if-ordered-to-unlock-iphone-might-resist.html?&_r=0) - an operating system actually but they didn’t know that at the time - to break into everyone’s phone is quite revealing of their misunderstanding of the privacy and security stakes which come along with our technologies.

In real life, hackers do not type like crazy on their computer, they do not wear masks and absolutely don’t make pop-ups with skulls appear furiously on your screen.

>“Hacking is the practice of modifying the features of a system, in order to accomplish a goal outside of the creator’s original purpose. The person who is consistently engaging in hacking activities, and has accepted hacking as a lifestyle and philosophy of their choice, is called a hacker.”
– [whatishacking.org](http://whatishacking.org/)

The definition implies that “hacker” is not specifically related to computer science. Artists using toothpicks to create beautiful sculptures are actually hackers, since they take toothpicks out of their expected use. But for the sake of clarity, we’ll focus on computer hackers.

The purpose of a hacker is not to get on your nerves - even if he manages that quite well - but to obtain something from you. Its means that **the best interest for a hacker is that you’re not aware you’ve been hacked.** That way he can:

* spy on you to gather more useful information than he was able to steal with his current access to your system. Personal intelligence, credit card numbers or account passwords are valuable pieces of information that a hacker might like to get
* use your computer to hack someone else’s system, your computer is then called a [zombie](https://en.wikipedia.org/wiki/Zombie_(computer_science)). Zombies are very useful because hacking often requires a lot of computational power, either to crack passwords, or to perform attacks like *Denial of Service (DoS)*, which basically consists in sending a huge amount of requests to a server, more than it can handle, to shut it down or make it unable to treat genuine requests.

But to do so, they can't just make your computer do whatever they want, like magic. They have to find a way in, an open door, a flaw in your system to exploit. Sometimes, the flaw is something you can't control, like a bug in your operating system - or a backdoor... - but they become very sparse. Often, you create the flaw, which means you can prevent it from happening by knowing a little about computers, and fixing it.

For the sake of fairness, I’d like to point out that **hackers are not all evil malicious criminals.** Actually, there are three types of hackers:

* **black hats:** that’s the type of hackers you know, who “use their superpowers for evil”.
* **white hats:** ethical hackers, hacking systems in order to find security flaws, and warn their developers so that they can fix them. They want to make the world a better place.
* **grey hats:** they’re kind of between black and white hats. They hack systems for an ideology they fight for. They don’t want to hurt people specifically, but may be fighting against the system in place because they find it unfair. Guy Fawkes, from “V for Vendetta”, is an iconic grey hat.

As computer scientists and white hats work to make our computers more secure, black hats have fewer and fewer leeway to penetrate systems. However, due to the lack of education in computer science, people still aren’t aware of good security policies, meaning black hats favour human flaws as a way in. If absolute security is purely utopian, the least you can do is to be sure that you didn’t leave a door wide open.

*Hackers, in their largest definition, are clever people, and I actually like and embrace their state of mind. They’re curious, passionate, they have a critical mind and see the world not as they’re told to, but how they want it to be. White hats may be more efficient at making our technological world more secure than companies and surely governments, who keep telling you without distinction that all hackers are bad people. Curiosity didn't kill the cat, manichaeism surely did.*

[**next milestone: how computers don't store passwords**]({% post_url 2016-04-09-How-computers-dont-store-passwords%})

