frhdtools
=========

A Python library for working with Free Rider HD Tracks.

|pip stable| |type sdist| |license MIT|

Introduction
------------

Free Rider HD is an online HTML5 + JS game where users can draw bike
tracks, upload them to a community of players, and ride them. (`Go try
it out!`_)

When drawing a track, you can import track code from a file or from your
clipboard. This library (as of now) allows you to generate that code.

Install
-------

Fire up a terminal and run:

``pip install frhdtools``

You should be good to go.

Usage
-----

Example 1: Straight Line
~~~~~~~~~~~~~~~~~~~~~~~~

When you start, you’ll want to import frhdtools:

.. code:: python

    import frhdtools

Next, you should create a Track class. This will hold all of your
track’s objects and code.

.. code:: python

    my_track = frhdtools.Track.Track()

Now that you’ve done that, you can add a line:

.. code:: python

    my_track.insLine(-40,50,100,50,'p')

This line goes from (-40,50) to (100,50). What is the ‘p’, you ask? That
corresponds to the type of line. In this case, it means a physics line.
More on types of lines later.

Now, lets generate our code:

.. code:: python

    print(my_track.genCode())

| This will generate the code stored in ``my_track`` and print it to
  stdout.
| In my case, the code was this:

.. code:: python

    -18 1i 34 1i,###

Don’t worry what the code means just yet. First let’s plug it into FRHD
to see if it works.

In the Track Editor, click “Import” at the top of the editor:

.. figure:: https://raw.githubusercontent.com/maxmillion18/frhdtools/master/images/example1/frhdimport.png
   :alt: Click Import at the top of the screen.


Then paste in your generated code at the window that pops up.

After it loads your file, the track should look **exactly** like this:

.. figure:: https://raw.githubusercontent.com/maxmillion18/frhdtools/master//images/example1/frhdexample1.png
   :alt: The imported track.

Wondering about the helmet? It’s just swag.

Congratulations! You’ve just finished you first line segment. It will
get easier, I promise. :wink:

Example 2: Scenery Line
~~~~~~~~~~~~~~~~~~~~~~~

Remember how I mentioned that there were different types of lines? Well
here’s what they are.

In the last example we used a physics line. The rider can interact and ride on those.

In this example you’ll make a **scenery line**. A scenery line is a line
that the rider cannot ride on. It is purely just for scenery. Also,
scenery lines are gray instead of black.

It’s really easy to make a scenery line. Instead of using the code from
last time:

.. code:: python

    import frhdtools
    my_track = frhdtools.Track.Track()
    my_track.insLine(-40,50,100,50,'p')
    print(my_track.genCode())

We change the ‘p’ to an ‘s’ in my\_track.insLine:

.. code:: python

    import frhdtools
    my_track = frhdtools.Track.Track()
    my_track.insLine(-40,50,100,50,'s')
    print(my_track.genCode())

(FYI: The code should be ``#-18 1i 34 1i,##``)

Now, when you plug the code into FRHD, you will get this:

.. figure:: https://raw.githubusercontent.com/maxmillion18/frhdtools/master/images/example2/frhdexample2.png
   :alt: A scenery line.

Note: the rider will fall through the line as it does not have physics.
This is normal.

Now you have made a scenery line. Great!

Example 3: Boost
~~~~~~~~~~~~~~~~

In this example, you will learn how to make a boost powerup.

To start, let's take our code from the first example:

.. code:: python

    import frhdtools
    my_track = frhdtools.Track.Track()
    my_track.insLine(-40,50,100,50,'p')
    print(my_track.genCode())

and add my_track.insBoost(90,-10,90)

.. code:: python

    import frhdtools
    my_track = frhdtools.Track.Track()
    my_track.insLine(-40,50,100,50,'p')
    my_track.insBoost(90,10,90)
    print(my_track.genCode())

This will spawn a boost powerup at (90,10). It will be rotated 90 degrees.

** By the way, the code should look like this: ``-18 1i 34 1i,##B 2q a 2q,#``

Plug that into FRHD, and you're left with this:

.. figure:: https://raw.githubusercontent.com/maxmillion18/frhdtools/master/images/example3/boost.gif
   :alt: A boost powerup.

Example 4: Bomb
~~~~~~~~~~~~~~~

In this example, you'll learn how to spawn a bomb powerup. Bombs explode when you touch them.

So, to get started we'll take our code from our first example and add my_track.insBomb():

.. code:: python

    import frhdtools
    my_track = frhdtools.Track.Track()
    my_track.insLine(-40,50,100,50,'p')
    my_track.insBomb(90,10)
    print(my_track.genCode())

That code makes a bomb at (90,10), which are the same coordinates from the last example.

Go ahead and put that into FRHD:
.. figure:: https://raw.githubusercontent.com/maxmillion18/frhdtools/master/images/example4/bomb.gif
   :alt: A Bomb.

.. _Go try it out!: https://www.freeriderhd.com

.. |pip stable| image:: https://img.shields.io/badge/pip-stable-green.svg
.. |type sdist| image:: https://img.shields.io/badge/type-sdist-blue.svg
.. |license MIT| image:: https://img.shields.io/badge/license-MIT-blue.svg
