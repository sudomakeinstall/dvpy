from collections import namedtuple


def read_obj(file_name):
    f = open(file_name, "r")
    vertices = []
    faces = []
    for l in f:

        if l.startswith("v"):
            vertices.append(l.split()[1:])

        if l.startswith("f"):
            faces.append(l.split()[1:])

    Mesh = namedtuple("Mesh", "vertices faces")

    return Mesh(vertices, faces)
