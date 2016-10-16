---
layout: post
title: Passwords just suck the big one
ref: Passwords_just_suck_the_big_one
lang: en
---

Through 20 years of effort, we've trained people to have their passwords cracked.

Don't get me wrong, usual password recommandations, like those from [Microsoft](http://windows.microsoft.com/en-gb/windows-vista/tips-for-creating-a-strong-password) or the french [security agency](http://www.ssi.gouv.fr/guide/mot-de-passe/), are actually relevant, in the sense they build passwords very hard to crack.

However, **these methods are barely usable**, because they forget to mention human bottlenecks, like his ability to remember complicated passwords - and *a forfiori* a lot of them - and the burden to type complicated passwords on the login screen.

---

## Password strengh

---

Password strengh relies on three key-components which are `size`, `alphabet` and `randomness`. In this context, *alphabet* means the set of keys used on the keyboard, lower and upper case characters, digits and symbols. The rule of thumb here is trivial: **the more the better.** Evalute the strengh of a password with these components is difficult though, because they are intertwined. You can't tell if a short password with wider alphabet is stronger than a long password with strunken alphabet, for example *`g&34$`* versus *`abbaabaaabaaababaa`*.

That's where `entropy` comes in.

Entropy depends only on size and alphabet, and provides a numerical value of how strong your password is, or said otherwise how difficult it is to crack. The more entropy you get, the stronger your password is. Here is a map between alphabet and entropy per symbol found on [Wikipedia](https://en.wikipedia.org/wiki/Password_strength):

| Alphabet             | Symbol set                | Entropy per symbol |
| -------------------- | ------------------------- | -------------------|
| Arabic numerals      | [0-9]                     | 3.322              |
| Latin alphabet       | [a-zA-Z]                  | 5.700              |
| Alphanumeric         | [a-zA-Z0-9]               | 5.964              |
| All ascii characters | [a-zA-Z0-9 !"#$%...]      | 6.570              |

To calculate the entropy of a password, you just multiply its length with the entropy per symbol corresponding to the alphabet you used. Here's some examples to make things clear:

| Password     | Length | Entropy per symbol | Entropy |
| ------------ | ------ | ------------------ | ------- |
| 1234         | 4      | 3.322              | 13.288  |
| 123456       | 6      | 3.322              | 19.932  |
| abC          | 3      | 5.700              | 17.1    |
| Superman     | 8      | 5.700              | 45.600  |
| YgzlgdnT     | 8      | 5.700              | 45.600  |
| Jekyll12     | 8      | 5.964              | 47.712  |
| C0mbu$t1on!  | 11     | 6.570              | 72.270  |

But we've said password strengh depends on randomness too, while entropy doesn't.

That's because the values we used to calculate entropy suppose a random password. For instance, both *`Superman`* and *`YgzlgdnT`* have an entropy of *45.6*, but *Superman* is easier to guess because it's not random, it is based on something known, so it's easier to crack. The more known or patterned a password is, the lesser its real entropy is.

If you read my [previous post]({% post_url 2016-09-18-Password_cracker_dont_guess_just_try %}), you'll understand very well why patterned passwords are easier to crack: they're very vulnerable to dictionary attacks.

*Out of curiosity, you can visit [howsecureismypassword.net](https://howsecureismypassword.net/), type passwords and see an estimation of the time required to crack them. You'll see that "Superman" and "YgzlgdnT" are totally different, because the algorithm underneath takes into account known words and patterns. It's worth mentionning that even if you type-in your actual passwords, you'll be safe, as data are not sent on the internet, the estimation is processed locally on your computer.*


---

## Strong password manual generation

---

The recommandation are usually as follow:

* **at least** 8 characters long
* use **all** alphabet sets, namely letters, digits and symbols
* **does not contain anything known,** like a famous place or person, your name, username, society, address, pet name, etc…
* **your password is unique for every single account you have!**

> The most common mistake about choosing a password is thinking that it is safe enough.

Password crackers have become incredibly clever. Using dictionary and rainbow table attacks instead of brute-force attacks, they do not just guess most used password, such as `123456, password, football, superman`… They are now able to guess complicated passwords like `k1araj0hns0n, Sh1a-labe0uf, Apr!l221973, Qbesancon321`, ... ([source](http://arstechnica.com/security/2013/05/how-crackers-make-minced-meat-out-of-your-passwords/3/)).

They easily handle common substitutions - ‘o’ to ‘0’ or ‘a’ to ’@’ - as well as concatenation, like appending numbers. It also means that anything that is either common knownledge (famous characters, date, location, quotation, ...) or easily retrievable personal intelligence (your name, username, address, favorite book, pet name, …) are absolutely not suitable as password material.

In 2008, *Bruce Schneier* published a [method](https://www.schneier.com/blog/archives/2014/03/choosing_secure_1.html) that still makes sense today: take a sentence and turn it into a password. Pick a sentence you totally made-up - can be nonsense - and just get letters from it, preferably encoding them a little, using [Leet speak](https://fr.wikipedia.org/wiki/Leet_speak) for example.

Using this method, the sentence `“I endorse the whimsical code of bunny trumpeters!”` could turn into `1eTheWc0deO|3Ts!`. You can try that one on any decent password checker, I guarantee it will be labelized as a pretty strong one.

> A strong password is untypable and unmemorable. If it is, it’s likely not a strong password.

So yeah, you’ve manage – supposedly – to build a strong password, but look at it! It’s damn hard to remember, and even more painfull to type each time you log in. You’ll end up asking your browser to remember it, which is a very bad decision.

Hum… and did I mentionned that your passwords should be unique for every single account you have? Yep. That means you have two choices:

* **ninja-style:** building *N* sentences, converting them to passwords, and remember all of them… you may need an eidetic memory for that *(if you cry because others are stupid and it makes you sad, you're good to go though)*
* **normal-person-style:** keeping the same password, just changing it a little for each account, based for instance on the name of the service hosting your account. The password `1eTheWc0deO|3Ts!` we built previously could become for Facebook: `Face1eTheWc0deO|3Ts!Book`, and for Twitter: `Twit1eTheWc0deO|3Ts!ter`.

At this point, we have actually an almost good password policy, with unique passwords meeting strengh requirements. However, it’s very tedious to use on a daily basis.

Moreover, if a hacker get one of your passwords, he may figure out how it’s built and gain access to all your other accounts. Tremendous!

*If you read my posts so far, congratulation! It might have been such a pain, for so little practical advices. I should have started with a 'Bear with me', it seems to work during conferences to keep an audience focused through a whole half-hour digression on a side-topic... Anyway, we're half the journey, and from the next post we'll introduce concepts I actually use in my security policy. See you soon!*

**next milestone: create passwords with dices (released soon)**
