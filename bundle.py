#!/usr/bin/env python3
import zipfile
import os
from glob import glob

filedir = os.path.dirname(os.path.realpath(__file__))
compressionType = zipfile.ZIP_DEFLATED


def find_all_required_files(dir: str, ex: str) -> list:
    required = [y for x in os.walk(dir) for y in glob(os.path.join(x[0], ex or "*"))]
    return list(filter(lambda v: v.find("__pycache__") == -1, required))


class Mapping:
    _from: str
    _to: str

    def __init__(self, _from: str, _to: str):
        self._from = _from
        self._to = _to

    def __str__(self):
        return "{} -> {}".format(self._from, self._to)

    @property
    def to(self):
        return self._to

    @property
    def pfrom(self):
        return self._from


def createMapping(p: str):
    return Mapping(p, os.path.relpath(p, filedir))


def find_all_files() -> list:
    base = list([os.path.realpath(filedir + "/diskrita.desktop")])
    source = find_all_required_files("diskrita", "*.py")
    lib = find_all_required_files("diskrita/dsdk/lib", "discord_game_sdk*")
    base.extend(source)
    base.extend(lib)

    base = map(createMapping, base)
    return list(base)


def info(mapping: Mapping) -> zipfile.ZipInfo:
    i = zipfile.ZipInfo()
    i.filename = mapping.to
    i.compress_type = compressionType
    return i


def copy_file(mapping: Mapping, zip: zipfile.ZipFile) -> None:
    print("Copying file: " + str(mapping))
    input = open(mapping.pfrom, "r+b")
    i = info(mapping)
    output = zip.open(i, "w", None)
    for z in input:
        output.write(z)


def get_output_file():
    path = os.path.realpath(filedir + "/build/diskrita.zip")
    parent = os.path.dirname(path)
    if not os.path.exists(parent):
        os.makedirs(parent)
    return path


def start():
    files = find_all_files()
    output = zipfile.ZipFile(get_output_file(), "w", zipfile.ZIP_BZIP2)
    created = dict()
    for mapping in files:
        dir: str = os.path.dirname(mapping.to)
        if dir and dir not in created:
            output.write(dir)
            created[dir] = True
            print("Created directory {}".format(dir))
        copy_file(mapping, output)


if __name__ == "__main__":
    start()
