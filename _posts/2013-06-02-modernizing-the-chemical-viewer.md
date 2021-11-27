---
title: Modernizing the Chemical Viewer
thumbnail: nu_100_blender.png
layout: post
permalink: /modernizing-the-chemical-viewer/
---

![](/assets/2013-06-02-modernizing-the-chemical-viewer/nu_100_blender.png)

**tl;dr:** *Check out [this program](http://patrickfuller.github.io/imolecule/).
If you like source code, [here's the github repo](https://github.com/patrickfuller/imolecule).*

I wrote a web-based chemical visualizer and format converter. I did this to help
out experimentally oriented co-workers, and I chose to build it with cutting-edge
tools primarily to stay entertained as I wrote it. That being said, I think I
made something that is somewhat neat and, more importantly, has the potential to
be *really* neat. In this post, I'm going to explain why this viewer is different
than the hundreds of other chemical programs out there (hint: it's because it uses
that "cutting edge" part), and then go on to try to convince some of you to go out
and use this as a base to make something awesome. Before doing that, let's start
at the beginning:

## The State of Chemical Software

To put it bluntly, most of the end-user chemical software out there is behind a
paywall and/or becoming dated. Programs like [ChemDraw](http://www.cambridgesoft.com/Ensemble_for_Chemistry/ChemDraw/)
are on every chemist's computer, and institutions are paying steep fees for
something that could be replicated over a caffeine-addled weekend. This standard
is so deeply rooted into the field of chemistry that people generally don't
realize that they have other options.

However, there are some truly amazing open-source chemistry libraries out there.
These projects (ie. [openbabel](http://openbabel.org/wiki/Main_Page), [RDKit](http://www.rdkit.org/))
are very useful to computer savvy people, but are often too complex for experimental
chemists to pick up and use. While I have found some great projects using these
as their back end (ex. [Avogadro](http://sourceforge.net/projects/avogadro/)),
they are few and far between.

Additionally, the chemical programs out there aren't poised to take advantage
of the new age of web apps and cloud servers (exception: [ChemWriter](http://metamolecular.com/chemwriter/)).
The workflow of the chemist of the future won't consist of downloading/installing/updating
software and waiting for programs to load. Rather, everything they need will run
right in their browser. This will enable a ton of interesting new capabilities - more
on this later.

## What I Wrote and Why it's Different

For the sake of speed, the open-source chemistry libraries out there are written
in a fast compiled language - usually C++. While speed is important, it comes
with trade offs. In the case of code modernization, the standard web stack
historically has not interfaced easily with a compiled language. There's good
reason for this: when you navigate to a web site, your browser does the work
of HTML / javascript rendering, which frees up the server to serve many other
clients. However, a compiled language, in its desire to be close to the
machinery of a computer, is stuck on the server.

There is a solution to this issue, which involves setting up something referred
to as a "socket" for auxiliary communication. Historically, this was prohibitively
difficult to do between client-side javascript and a server. Fortunately, things
have changed. (Update June 2014: This has gotten MUCH easier). Most browsers now
support HTML5 and the [WebSocket](http://www.websocket.org/) protocol. This
allows many possibilities beyond standard HTTP requests, enabling programming
patterns that were previously not possible. Using the [Tornado](http://www.tornadoweb.org/en/stable/)
web framework simplifies Python-Javascript websocket communication, and then
Python can interface with compiled server-side software.

Here's the upshot: not only can we communicate between browser windows and the
server, we can also split computational effort between the client and the server.
While this isn't good for your typical website-delivering server, this opens up
a world of opportunity for internal servers with small user bases (ie. most
science-oriented groups).

In this vein, my chemical viewer program is a very small sample of what we can
do with this socket connection. In its current state, all file conversion work
is done on the server, and the (client) browser is only responsible for
rendering the output. By dropping a file in the browser, you run code on the
server. Imagine if this server was a high-end computer of the type sitting
around many labs, and say this code had the function to run full MD simulations.
If the output of these simulations was relevant to an experimental chemist,
and the front-end program was designed well, they could run otherwise complex
code on a fast server with the click of a button. You could even expand on
this approach with something like cloud supercomputing, enabling a chemist to
run multi-core simulations in real time.

## In Conclusion

This program can interface with existing chemical software, and does not require
installation. Right now, I have only interfaced with Open Babel and RDKit, but
this could be expanded to simulation libraries (ie. LAMMPS), linear algebra
packages (ie. numpy), and, you know, everything else. If so motivated, a
computational chemist could literally code himself out of his own job. I like that.
