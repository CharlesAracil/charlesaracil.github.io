---
layout: post
title: Diceware, passwords and dices
ref: Diceware_passwords_dices
lang: en
---

Best passwords are created rolling dices.

We'll introduce here a method providing a 100% chances of building a strong password, or rather what's called a **passphrase.** Meanwhile, you get rid of the hassle of building a strong password yourself. Sweet!

# Randomness vs homogeneity

In previous posts, we've pointed out that best passwords are random ones. Unfortunately, humans suck at randomness. They do because **the human brain mixes up randomness with homogeneity.**

Here's an experiment to illustrate the idea.

Ask someone to flip a coin several times - a lot of times - and write down the serie of heads and tails he gets. In another room, do the same, but instead of flipping a real coin, imagine you're flipping one, and write down your imaginary results. Let's say `head=0`, and `tail=1`, it will be easier to write down.

And the end, compare your results with those of your buddy. You'll notice that both of you will have, in average, an equal number of *0* and *1*. And indeed, as you were trying to achieve randomness, you took care of having the same number of those, because that's a requisite of randomness: as both heads and tails have fifty-fifty chance of outcome, they should appear with the same frequency.

![diceware homogeneity]({{ site.baseurl }}/assets/figures/diceware_g1.png)

However, that is not randomness, that's homogeneity. To see that, **let's group coin flips by groups of three.** For instance, if you got *head, head, tail*, it's a *001*. Now the possible outcomes are not *0* or *1*, but *000*, *001*, *010*, *011*, *100*, *101*, *110*, *111*.

Now, if you count the frequency of those outcomes, you'll notice that with a real coin, they appear in average the same number of times. However, with your imaginary coin, they're not! **Some outcomes appear more than others.**

![diceware frequency stability property]({{ site.baseurl }}/assets/figures/diceware_g3.png)

This is known as the **frequency stability property.** A coin has it, **humans don't.** That's because humans use their memory in order to keep track of previous coin outcomes, and try to compensate those in the next ones.

This is why you should not try to build a random password yourself.

*If you want more visuals on that phenomenon, check out [this video](https://www.youtube.com/watch?v=H2lJLXS3AYM), which illustrates it pretty well. Besides, you'll find the source code for the graphics of this post [here](https://raw.githubusercontent.com/CharlesAracil/charlesaracil.github.io/master/assets/python/diceware.py).*

# Build strong password with true randomness: use dices!

**Diceware** is a method for generating random passwords built by aggregation of common words from the dictionary. So instead of having a password, like `Face1eTheWc0deO|3Ts!Book`, you'll end up with a serie of random words, like `correct horse battery staple`. This is called a **passphrase.**

Passphrases are stronger than passwords when built properly, and are far easier to remember. In essence, they're just the same though, they only differ in structure, but are both keyboard typable series. As a result, they can be used systematically instead of passwords in order to login to you accounts. **Forget about passwords, use passphrases.**

*There's one exception though. If the website prevents long sequences to be used as password, you won't be able to use your passphrase. Those policies just suck, and I hope very few websites still enforce them. Anyway, do not bother, we'll introduce a workaround in the next post, or rather a great tool making these considerations irrelevant*

![xkcd diceware](http://imgs.xkcd.com/comics/password_strength.png)

*Yes, I know, some of you have already seen this very comic a thousand times, from [xkcd](https://xkcd.com/936/), but it's such a beauty a concision and clarity that it's worth one more reference...*

So, here how it works. The *Diceware* method come up with a [big list of words](http://world.std.com/~reinhold/diceware.wordlist.asc). Each word is coupled with a number. Here's a small slice of it:

| Code           | Word          |
| :------------- | :------------- |
| 21552          | crave          |
| 21553          | craw           |
| 21554          | crawl          |
| 21555          | craze          |
| 21556          | crazy          |
| 21561          | creak          |
| 21562          | cream          |

Each digit of a code is the result of a rolled dice. As a code has 5 digits, you have to throw 5 dices. For instance, if my 5 dices give me `2, 1, 5, 5 and 6`, it'd yield the word `crazy`.

Just do that a least 6 times - you could do less but 6 is the minimum recommended - and you get your final passphrase. I did it writing this post and got `verify lagoon province gala anyplace unworn`.

Assuming you're using perfectly balanced dices, outcomes are equiprobable. There's no algorithmic correlation whatsoever between a code, or its digits, and the matching word, it's just an arbitrary lookup table. As a result, all words are also equiprobable. In a hacker's perspective, it means there's no word which may appear more than other, so it gives no clue for any kind of dictionary attack. And because a long passphrase of at least 6 words shall be used, brute-force attack is also out of order.

*You'll find [here](https://www.rempe.us/diceware/#eff) an online diceware generator, just to try it out. Even though it uses https protocol and strong random number generator, it recommends to use real dices for bullet-proof diceware generation.*

If you followed my previous post, you'll argue that ordinary words aren't strong enough for password material, because they're known and because they're just lower-case alphabetical characters. Well it turns out that the size of the password built by this method and the randomness of the generated words largely overcome those considerations. As a result, *diceware* passphrases are perfectly suitable as password material.

You end up with an **easier password to both remember and type**, because it's made with words you know and maybe use on a daily basis. **And its randomness makes it very strong.**

*There is still one unsolved problem: your passphrase should still be unique for every account you have. And having a lot of Diceware passwords surely can't be remembered. But there's a solution for that: password managers! Combined with only one diceware passphrase, you'll get on almost bullet-proof password policy. Buckle-up!*

[**next milestone: password managers**](released soon)
