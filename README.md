# frhdtools
A Python library for working with Free Rider HD Tracks.

## Introduction
Free Rider HD is an online HTML5 + JS game where users can draw bike tracks, upload them to a community of players, and rider them. ([Go try it out!](https://www.freeriderhd.com "Free Rider HD"))

When drawing a track, you can import track code from a file or from your clipboard. This library (as of now) allows you to generate that code.

## Install
Download [frhdtools-1.0.0.tar.gz](https://github.com/maxmillion18/frhdtools/blob/master/dist/frhdtools-1.0.0.tar.gz?raw=true "frhdtools-1.0.0.tar.gz"). Next, run:

`pip install /Downloads/frhdtools-1.0.0.tar.gz`

Note: replace `/Downloads` with wherever you put it.

## Usage
### Example 1: Straight Line
When you start, you'll want to import frhdtools.Track, the main track manipulation section:

```python
from frhdtools import Track
```

Next, you should create a Track class. This will hold all of your track's objects and code.

```python
my_track = Track.Track()
```

Now that you've done that, you can add a line:

```python
my_track.insLine(-40,50,100,50,'p')
```

This line goes from (-40,50) to (100,50). What is the 'p', you ask? That corresponds to the type of line. In this case, it means a physics line. More on types of lines later.

Now, lets generate our code:

```python
print(my_track.genCode())
```

This will generate the code stored in ```my_track``` and print it to stdin.
In my case, the code was this:
