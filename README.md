# Image to Hash

Small research project: attempt to solve a question "how to store images".


## Problem

You want to store image, or effectively, any other files on a server. Things
which you most likely will concern are:

* Security
* Consistent naming
* Name collisions
* Reduce # of duplicates


## Solution

Due to the nature of widespread compression algorithms for images, each image
may have many instances. Trivially, a number of instances depends on image's origin, its purpose.
For examples images on Instagram has usually only one instance due to its nature:
sharing personal photos. However, images on Pinterest have a high repetition rate
because Pinterest is about sharing, and people share a lot.

Therefore we can **store images using a hash string representation as a name.**


## Proof of Concept

Let's take one instance of an image and store it in different places.

1. [Image on Google Drive](https://drive.google.com/open?id=0B1rsXetG2YsjNjJfWjJuMGR2d1E)
2. [Image on Dropbox](https://www.dropbox.com/s/kko780u7qypseo0/original_image.jpg?dl=0)
3. [Image on GitHub](https://github.com/pvlbzn/itoh/raw/master/img/original_image.jpg)
4. [Image on Imgur](https://i.imgur.com/AhfqaQW.jpg)

After, let's save them back on a disk in a separate directory adding prefixes
about their origin.

```
sha256

Imgur:      975aa7f42346a406dcfa0dfef408d45f389795a4d16b12c4a9eda861da29d474
Dropbox:    c380db894d40144b9cc91f9821ae4833085df10201313be1f32b5c3f41038c3d
GDrive:     cc26a121692fd12b356f783ed7f863da0f6dc478cb074570dde87fda929bd04a
GitHub:     cc26a121692fd12b356f783ed7f863da0f6dc478cb074570dde87fda929bd04a
Original:   cc26a121692fd12b356f783ed7f863da0f6dc478cb074570dde87fda929bd04a
```

Original, GitHub, Google Drive versions are identical, while Imgur uses compression
as well as some kind of similar naming techniques, as can be inferred from the image's
name.


#### Hashing Algorithm

It is better to prefer [Blake2](https://blake2.net/) algorithm, due to its speed
and interface advantages. In the code, [`./itoh.py`](https://github.com/pvlbzn/itoh/blob/master/itoh.py)
blake2s aliased to blake.


## Conclusion

Hashing method for sure can solve the naming problem with not much of an overhead.
Depending on the nature of your application it also may save considerable space
on duplicates, however, if service used mostly for unique content, such as Instagram,
hashing won't save any space.

However, hashing always has a probability of a collision. Therefore it is not
a good idea to have only hashing check. In case of collision, some additional
comparison algorithm may be used together with a sanity check assertions.

For example, if two images have the same hash *and* the same size, then they are
the same.
