---
layout: post
title: Double authentication
ref: double-authentication
lang: fr
---

How your password being stolen can not be a big deal.

Using *double-authentication* to protect your password manager, you can avoid the *single point of failure*, so that even if your password gets stolen, your password database would still be safe. Here's how it works.

## Principle

Double-authentication is similar to having two keyholes: you'll need two keys in order to open the door. If a thief came out, he'd require both keys to enter your home.

With double-authentication, these two keys are your **passphrase** and a **software of hardware device.** This device will feed your system with unique identification *tokens* - basically codes - that the device and **only** the device knows.

As a result, to open your system, you'll need both **something you know** - your passphrase - and **something you have** - your device.

That way, if a hacker guesses what you know, he still won't have what you have. And if he steals what you have, he still wouldn't have guessed what you know.

## Software double-authentication

Software double-authentication is the easiest way to setup double-authentication, because it does not require any specific hardware.

Concretely, it can be an app on your smartphone. For instance, *Gmail* offers double-authentication for its web service through [Google Authentificator](https://support.google.com/accounts/answer/1066447?hl=fr), and [Steam Guard](https://support.steampowered.com/kb_article.php?ref=4020-ALZM-5519#what) provides protection for the *Steam* video game platform.

Both behaviours are simple: they generate a single-use code, periodically refresh, namely every 30 seconds.

![Google authentificator]({{ site.baseurl }}/assets/screenshots/screenshot-double-auth-google_aut.png)

With double-authentication setup, next time you want to connect to your account, **you'll be asked for both your passphrase and this single-use code.**

In a security perspective, it means that even if your passphrase gets stolen, your account would still be safe, because the hacker won't have this single-use code. And if your phone gets stolen, the hacker won't access your account either, because he doesn't have your passphrase.

And that's even more powerful: if the hacker manages to steal your passphrase and one single-use code - not the phone, just one code - he would have to use them in the next 30 seconds, before the single-use code gets refreshed. Which is a very short timing.

To summarize, the hacker would basically need to steal both your passphrase and your phone, and use them **before you noticed it** and change your account settings. That's kind of tricky even for good hackers.

Software double-authentication is very efficient, that's why it's used in a lot of critical system and fully-fledged companies.

However, there's one drawback: it relies on the safety of your phone. If your phone gets hacked, your codes could be compromised without you even knowing it. That's where hardware double-authentication prevails.

## Hardware double-authentication

Hardware double-authentication works exactly the same as double-authentication - at least at a user level, technical details defer - but instead of having an app feeding you with codes, you have a specific hardware device doing all the heavy-lifting for you.

I'll just focus on one specific device, because it's fully fledged, used among top-level companies, and because it's the one I use. It's called a **Yubikey**, from the [Yubico](https://www.yubico.com/) company. It's worth between 20$ and 40$, depending on the model, which can seem a little expensive, but considering what it does, it's not that much.

![Yubikey from Yubico]({{ site.baseurl }}/assets/screenshots/screenshot-double-auth-yubikey.png)

As you can see, it looks like a standard USB key, and you plug it in your computer the same way. It is recognised automatically as a USB device.

However, it is not used to store any data, and it can't because it's a **read-only** device, which means that no one can write data on it, so that **it cannot be tampered with.**

It works by generating an **authentication response** when asked to. When you configure your system with it, you first register your *Yubikey* into it, to say *"That's my Yubikey, it's mine, and it will assert I'm the one using my system"*. Next time you log into your system, it will ask you to plug your yubikey, so that the system and the *Yubikey* can communicate. The *Yubikey* will then validate your identity to your system, which will let you in. Providing you also enter your passphrase of course...

*I can't be more precise without being too technical, but for those who wants to know, they are lots of protocols to achieve such feature. Yubikeys handle static passwords, Yubikey OTP, OATH/HOTP, OATH/TOTP, PIV-Compliant Smart Card, OpenPGP and FIDO U2F. ([source](https://www.yubico.com/products/yubikey-hardware/))*

If you remember from my [previous post]({% post_url 2016-11-12-Password_manager %}), the login screen of Keepass looks like this, when configured with double-authentication:

![Yubikey from Yubico]({{ site.baseurl }}/assets/screenshots/screenshot-keepass-login.png)

You can see it with its two rows: *Master Password* and *Key File*. Again, it means that to access the database, you'll need to know and type-in your passphrase, and have your *Yubikey* plugged into your computer. This protection is the most secure solution I know, secure enough to be applied in highly critical structures. I would trust this technology with my bank credentials. And I actually do.


## Summary of a good security policy

To summarize all we've said in previous posts, here is a proposition of what might be a good security policy:

* do not create passwords yourself!
* create **only one custom made passphrase** using the *Diceware* method
* install a **password manager**
* protect it using **double-authentication**
* have your password manager create and use passwords for you

*That's it! As always, perfect security doesn't exist. Hackers always find new exploits to crack systems. And you might have a breach in your system you didn't know about. However, setting up this policy, you're at least doing everything you could to prevent such disasters. And besides, you've avoided the burden of manual password management, trusting a very efficient security tool for that. Now forget about the crap the media and governments tell you about your home security, try those techniques and tell me what you think of them!*
