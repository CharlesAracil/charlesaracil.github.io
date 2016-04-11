---
layout: post
title: How computers don't store passwords
ref: how-computers-dont-store-passwords
lang: en
---

Hackers can't steal passwords, because passwords aren't stored anywhere... in theory anyway .

It means that even if a hacker get full access to your computer, or your online account, he still won't be able to know your password. That's because **your computer does not need to know your password, it only has to certify you entered the correct one.** And as counter-intuitive as it may be, a computer can tell even if it doesn't know your password. It only requires its `hash code`.

---

## Hashing principle

---

A hash is like a fingerprint, its a unique identifier of your password, computed from it. **Two different passwords have completely different hashes**, even if these passwords differ only by one character. The hashing process uses what is called a `one-way function`.

> "In computer science, a one-way function is a function that is easy to compute on every input, but hard to invert given the image of a random input."
– [wikipedia.org](https://en.wikipedia.org/wiki/One-way_function)

Said in simpler terms, a one-way function is a transformation that can't be undone easily. For instance, a jigsaw puzzle is a one-way function, because it's very easy to take the full image and break it into pieces, but very hard to put all the pieces back together to rebuild the puzzle. As another instance, Sudoku grids are one-way functions too, they are [easy to build](http://www.wikihow.com/Create-a-Sudoku), but hard to solve.

It's worth mentioning that *"hard"* is a relative term, as it depends on what or who is assigned the task. Processing an image is very easy for a human being but very hard for a computer, while multiplication and division are very difficult for a human being, and easy for a computer. Jigsaw Puzzles and Sudokus are one-way functions for human beings, but aren't for computers, which can solve them quite easily.

*This hardness is related to [computational complexity](https://en.wikipedia.org/wiki/Computational_complexity_theory), but it's a whole topic in itself and we won't be discussing it here.*

Hashing algorithms are a subset of one-way functions. They are hard to solve for both human beings and computers, and they also have a `non-collision property`, which means that every input will give a different result. In our case, it ensures that **two different passwords will have two different hashes.**

Computers can use several hashing algorithms, the best known being `Message Digest 5 (MD5)` and `Secure Hash Algorithm (SHA)`. Both of them consist in taking an input, like a password, and applying a series of mathematical operations to turn this input into a *fixed-length hexadecimal string*, a string constituted with digits and characters from *A* to *F*. Here are some examples of passwords and their corresponding hashes using both *MD5* and *SHA*:

| Passwords            | Hash with MD5        | Hash with SHA-512  |
| -------------------- | -------------------- | ------------------ |
| 123                  | 202cb962ac59075...   | 3c9909afec25354... |
| 124                  | c8ffe9a587b126f...   | 813d00895b26351... |
| Ghostbuster          | 202cb962ac59075...   | 5ce72e772ca8135... |
| Superman123          | b40b8f862d816d6...   | 9b1c3c6c94a42f4... |

*If you want to check it out for yourself, I'd recommand [onlinemd5.com](http://onlinemd5.com/), a user-friendly online hash generator.*

Computing a hash from a password is very easy, but guessing the password from its hash is almost impossible, providing the password is strong enough.

![hash transformation]({{ site.baseurl }}/images/password-certification-hashing.png)

**This property is the cornerstone of password certification.**

---

## Password certification

---

Password certification is the process your computer do in order to verify the password you type-in matches with your account.

For the sake of clarity, let's set a scenario where you create an account on your favorite operating system, like when you boot it for the first time, and then log-in to this newly created account. The scheme will be the same for password certification on online services.

First, the operating system ask you to choose your password. After a bit of thinking, you come up with `Ghostbuster`, which is actually a very weak password, but it's just to make things clearer than using a complex password. Anyway, you type-in your password, and here's what happens under the hood:

![password-certification-creation]({{ site.baseurl }}/images/password-certification-creation.png)

Your password is processed by a hashing algorithm, like those we discussed earlier. The generated hash is then stored in memory, and your password... **completely destroyed and forgotten!** Your operating system doesn't remember your password anymore, and it could not get it back even if it wanted to.

Now it's time to login. Say you misspelled your password once before entering it correctly. Here's again what happens under the hood:

![password-certification-login]({{ site.baseurl }}/images/password-certification-login.png)

Each time you enter a password, your operating system computes its hash, and then compare it with the stored one:

* if hashes aren't equals, it means the password you entered is not the same as the one you set previously, so your system will deny your access.
* if hashes are equals, it means you entered the correct password, and the system can let you in.

Again, **the system never needed your password to certify the one you typed-in**, because it only used hashes. Besides, a system can't mix up two different passwords, because they necessarily have two different hashes.

---

## Limitation in password length

---

You may have noticed on several online services that the length of passwords is limited. Yet we just said that they don't need to remember your password, because they only use its hash, which is a fixed-size string.

Consequently, **there is no need to limit the size of passwords,** as they won't end on any storage... *unless they do.*

In real life, some services do store your passwords, which is a very very bad habit, because if a hacker breaks into their system, they'll most likely look for passwords. How easy they'll find them depends on whether encryption is used to protect these passwords:

* **best case**, encryption is used, and a hacker won't be able to get your passwords, unless either your password is weak or the encryption has a flaw.
* **worst case** - the one you should always consider when dealing with security - encryption is not used, so your passwords are stored in plain text, and a hacker just has to read it and use it.

This password length requirement is not exclusive to some small unknown onlines services. Famous ones have it, like *Paypal* or *Ebay*. The reason for that is unclear.

Optimistically, the reason could be technical. These companies may not have upgraded their application form for a while, or just use a static size string to store temporarily your password, to be hashed afterwards. *Ebay* currently limits the length to 64 characters. It may be a compromise between a long enough password pleasing almost every users, and not having to deal with dynamic size strings in their internal engine, which might require an extra setup, although I doubt it. In that case, the password may not be stored, but we can't know for sure without further investigation.

Storing your password could also be used to send it back to you when you forget it, but it's surely a dumb idea. Unless you set up encryption, like with [GnuPG](https://www.gnupg.org/), **email communications aren't encrypted at all,** which means all emails you send or receive travel the network in plain text, so everyone sniffing your traffic is able to read those emails without further effort. A listener could then get your password and use it. Lost password recovery should always be handled using a [temporary one time reset URL](https://www.owasp.org/index.php/Forgot_Password_Cheat_Sheet#Step_3.29_Send_a_Token_Over_a_Side-Channel).

So next time you see such forms, email the company and ask them what do they need your password for...

---

## Glimpse of life

---

I've recently registered to a french e-commerce website. Right after registration was complete, I received an email. How pleased I was when I realized the email contained the password I'd just chosen!

![screenshot-password-send-after-subscription.png]({{ site.baseurl }}/images/screenshot-password-send-after-subscription.png)

The mail was even enlivened with advices on how to keep your credentials safe... this is like the pot calling the kettle black.

I can't figure out any interest of such email. I asked the staff behind the website, but did not get any response. After a quick research, I found out that it seems to be a widespread habit. The website [plaintextoffenders.com](http://plaintextoffenders.com/) references a whole bunch of them, with passwords just... lying there.

*These security flaws are like anti-social behaviours: there because no one actively care. Each time you see them, don't leave before sending an email to the suitable staff. They might ignore some of them, but not a lot of them.*

***next milestone: from strong password building to oblivion (coming soon)***

