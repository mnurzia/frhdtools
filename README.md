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
Obviously, when you start, you'll want to import frhdtools:

```python
import frhdtools
```
