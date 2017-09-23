import argparse
import hashlib


def hash(x, buffer_size=65536):
    '''Get file's hash

    Arguments:
        x {io.FileIO}: an open file
        buffer_size {int}: a size of chunks in which x argument will be
        readed. Defaults to 16 bytes, 2^16

    Returns:
        Hash of a given file in string representation
    '''
    sha = hashlib.sha256()
    while 1:
        data = x.read(buffer_size)
        if not data:
            break
        sha.update(data)

    return sha.hexdigest()


def rw(what, where):
    '''Read a given file, and write it into an another location, changing
    file's name to it's hash representation

    Arguments:
        what    {string}: path to a given file
        where   {string}: path to where to store hash-renamed file
    '''
    with open(what, 'rb') as f:
        data = bytearray(f.read())
        name = hash(f)

        with open(where + '/' + name, 'wb') as nf:
            nf.write(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='How to store files using hash function')
    parser.add_argument('-i', '--image', help='path to an image')

    args = parser.parse_args()
    rw(args.image, './img')
