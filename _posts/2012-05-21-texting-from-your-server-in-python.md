---
title: Texting from a Computer in Python
author: Patrick Fuller
layout: post
permalink: /texting-from-your-server-in-python/
categories:
  - Coding
---

Here's a script to send a text message in Python. It uses the standard library and
is very straightforward. It utilizes the fact that most major carriers allow texting
via email (ie. by [SMTP](http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol),
so nothing more is needed than an email account and a desired target.

In my work, I use it to tell me when my computational simulations are done running.
Also, it can send to any phone number and can be put in an infinite loop; days of
fun, right there.

{% gist 8390767 texter.py %}
