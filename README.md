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
When you start, you'll want to import frhdtools:

```python
import frhdtools
```

Next, you should create a Track class. This will hold all of your track's objects and code.

```python
my_track = frhdtools.Track.Track()
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

This will generate the code stored in ```my_track``` and print it to stdout.
In my case, the code was this:

```python
-18 1i 34 1i,###
```

Don't worry what the code means just yet. First let's plug it into FRHD to see if it works.

In the Track Editor, click "Import" at the top of the editor:

![Click Import at the top of the screen.](/images/example1/frhdimport.png)

Then paste in your generated code at the window that pops up.

After it loads your file, the track should look **exactly** like this:

![The imported track.](/images/example1/frhdexample1.png)

Wondering about the helmet? It's just swag.

Congratulations! You've just finished you first line segment. It will get easier, I promise. :wink:
