---
title: Characterizing MOF Diffusion
thumbnail: fcs.png
layout: post
permalink: /characterizing-mof-diffusion/
---

![](/assets/2012-04-08-characterizing-mof-diffusion/fcs.png)

My first paper in graduate school was published in Angewandte Chemie a few months
ago. Check it out [here](http://onlinelibrary.wiley.com/doi/10.1002/anie.201108492/abstract;jsessionid=41D8D98E1E325B5D7DAD39F5D1DB0D51.d03t01)!

Metal-organic frameworks, or MOFs, are amazing little crystals capable of storing
natural gas, carbon dioxide, and many other chemicals. While research in this field
has expanded dramatically in the last few years, topics have been experiment-driven.
This is a great pursuit, but inefficient workflow. With the use of models, experimentalists
can chose MOFs based off of known or estimated properties, rather than wasting months
of time using brute-force approaches.

So, we saw a need to characterize and model MOFs. The paper outlines that molecules
enter and leave MOFs through [reaction-diffusion](http://en.wikipedia.org/wiki/Reaction%E2%80%93diffusion_system)
kinetics. Basically, molecules slowly wiggle their way into the crystals, but
occasionally get stuck ("adsorbed") onto internal MOF surfaces.

We combined mathematical modeling with experiments using [confocal microscopy](http://en.wikipedia.org/wiki/Confocal_microscopy)
and [fluorescence correlation spectroscopy](http://en.wikipedia.org/wiki/Fluorescence_correlation_spectroscopy),
and were able to experimentally derive parameters that quantify this molecule-entering-crystal
system.

I know it's not exciting work, but this kind of stuff is amazingly useful for experiments
in the field. It means that, rather than having to test multiple crystals for a
certain property, someone can simply choose one. If I save even one person a few
months of mundane work, I'll be happy.

## Update (3 Sept)

We had a followup paper on this topic, which was also published in Angewandte.
We extended the idea of reaction-diffusion processes in MOFs to spatially control
how nanoparticles deposit in a crystal. We found that we could make a system exhibiting
periodic precipitation in three dimensions. I started calling them "Liesegang cores",
as they're basically three-dimensional [Liesegang rings](http://en.wikipedia.org/wiki/Liesegang_rings).
It didn't catch on.

Anyway, I thought this was cool as the model predicted parameter sets (ie. MOF size,
salt concentration, time of exposure) before any experiments were even started.
It shows how robust reaction-diffusion equations really are.

I'm at a loss trying to come up with an application for this exact system. I've
heard whispers of semi-conductors, optical projectors, and sensors, but I have my
doubts on all of those. Regardless, it solidifies the strength of reaction-diffusion
models in MOFs. In case there were doubters before or something.

I would love to see reaction-diffusion models used to test methane cycling in a
natural gas tank. It'd be interesting to see how MOF size and shape affects the
filling and un-filling of a MOF tank, especially in the case of time-dependent
boundary conditions.
