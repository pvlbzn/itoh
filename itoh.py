import argparse
import hashlib


def hash(what, sha=False, blake=False, buffer_size=1 << 16):
    '''Get a file's hash string. Uses sha256 or blake2s algorithm.

    Arguments:
        what: path to an image
        sha: sha256 hashing algorithm
        blake: blake2s hashing algorithm
        buffer_size: size of a chunk by which file will be readed

    Returns:
        Hash of a given file in a string representation
    '''
    if not sha and not blake:
        raise AssertionError('no hashing algorithm specified')

    if sha:
        algorithm = hashlib.sha256()

    if blake:
        algorithm = hashlib.blake2s()

    with open(what, 'rb') as x:
        buff = x.read(buffer_size)
        while len(buff) > 0:
            algorithm.update(buff)
            buff = x.read(buffer_size)

    return algorithm.hexdigest()


def blake(what):
    '''Hash file using blake2s algorithm'''
    return hash(what, blake=True)


def sha(what):
    '''Hash file using sha256 algorithm'''
    return hash(what, sha=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='How to store files using hash function')
    parser.add_argument('-i', '--image', help='path to an image')

    args = parser.parse_args()
    print(sha(args.image))
