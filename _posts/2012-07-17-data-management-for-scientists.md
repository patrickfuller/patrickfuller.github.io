---
title: Data Management for Scientists
image: binary.png
layout: post
permalink: /data-management-for-scientists/
---

![](/img/binary.png)

I've spent the last few months working with the folks at Codecademy to create a
[tutorial](http://www.codecademy.com/courses/4fa071f79953310003008791?) targeted
at experimentalists. It covers what I have found to be the most commonly-encountered-but-easily-solvable
problem in experimental science: data management. Especially with older machines,
data is often generated in non-ideal formats. The data might present itself in
obscure text files, or maybe you only need every *n*th datapoint. Regardless, the
usual solution that I've seen is for a scientist to spend hours manually copying
and pasting important information. Not only is this dangerous - translational errors
are a real thing - but it's miserably boring.

This issue came up in the work behind one of my earlier papers. In one set of
experiments, we wanted to view the motion of a single dye molecule in various
metal-organic framework crystals. Amazingly, this task can be accomplished through
an approach called [fluorescence correlation spectroscopy](http://en.wikipedia.org/wiki/Fluorescence_correlation_spectroscopy),
or FCS. This method can monitor the fluorescence intensity of a small volume (think
sub-micron) over time, providing information on flow. In a very dilute system,
the approach can monitor the volume around single molecules, which allows us to
extrapolate data on different time scales - we can observe Brownian motion, adsorption
kinetics, and diffusion.

The resultant data of a set of experiments comes out looking like
[this large text file](https://dl.dropboxusercontent.com/u/5295849/sample_mof_data.fcs)
(I don't know if I have rights to the raw data, so I've mangled the values. I have,
however, attempted to keep the underlying trends the same.). We needed to autocorrelate
the data and fit to models to ascertain diffusion and adsorption coefficients, but
we obviously couldn't do that in its current form. We moved the data to Excel using
the approach described in the Codecademy tutorial, and were then able to fit our
models. Victory.

If anyone has any questions or comments about the Codecademy tutorial or the underlying
FCS experiments, feel free to ask!
