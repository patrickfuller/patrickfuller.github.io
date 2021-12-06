---
title: Improving reproducibility in computational literature
thumbnail: nist.png
layout: post
permalink: /nist-workshop/
---

I was invited to be a speaker at *2014 NIST Workshop on Atomistic Simulations for Industrial Applications*. As the one 20-something invited to present alongside professors that I consider to be top of the field, this was a daunting meeting.

I focused on where I viewed my youth as a unique strength: providing a view of the future. The future is going to need reproducible scripts alongside published literature. We always put math equations in our papers but none of us actually run these equations. We trust third-party libraries to implement the math properly. However, I've often found that our view of how software math works versus its actual implementation is very different.

It will no longer be good enough for labs to publish simulation results without the same in-depth review rigor required of our experimental colleagues.

Instead, we should submit papers with a single reproducible script that can calculate the simulation results. In the case of these simulations being computationally expensive, a simpler version will be provided to show the software working. In the case of the simulations being stochastic, a random seed will be provided and the expected result included in the script.

These are simple steps that the software community has adopted long ago. It's time for us to adopt these same practices.
