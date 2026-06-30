from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import (
    GeomVertexFormat, GeomVertexData, GeomVertexWriter,
    Geom, GeomTriangles, GeomNode,
)


class CubeDemo(ShowBase):
    def __init__(self):
        super().__init__()
        self.disableMouse()
        self.camera.setPos(0, -30, 12)
        self.camera.lookAt(0, 0, 0)

        cube_np = self.render.attachNewNode(self.build_cube())
        cube_np.setTwoSided(True)
        self.cube = cube_np

        self.enableMouse()
        self.taskMgr.add(self.spin_task, "SpinCubeTask")

    def build_cube(self):
        fmt = GeomVertexFormat.getV3c4()
        vdata = GeomVertexData("cube", fmt, Geom.UHStatic)
        vdata.setNumRows(24)

        vertex = GeomVertexWriter(vdata, "vertex")
        color = GeomVertexWriter(vdata, "color")

        faces = [
            ([(1, -1, -1), (1, 1, -1), (1, 1, 1), (1, -1, 1)], (0.9, 0.2, 0.2, 1)),
            ([(-1, 1, -1), (-1, -1, -1), (-1, -1, 1), (-1, 1, 1)], (0.2, 0.9, 0.2, 1)),
            ([(1, 1, -1), (-1, 1, -1), (-1, 1, 1), (1, 1, 1)], (0.2, 0.2, 0.9, 1)),
            ([(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1)], (0.9, 0.9, 0.2, 1)),
            ([(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)], (0.9, 0.2, 0.9, 1)),
            ([(1, -1, -1), (-1, -1, -1), (-1, 1, -1), (1, 1, -1)], (0.2, 0.9, 0.9, 1)),
        ]

        tris = GeomTriangles(Geom.UHStatic)
        v_index = 0
        for verts, col in faces:
            for v in verts:
                vertex.addData3(*v)
                color.addData4(*col)
            tris.addVertices(v_index, v_index + 1, v_index + 2)
            tris.addVertices(v_index, v_index + 2, v_index + 3)
            v_index += 4

        geom = Geom(vdata)
        geom.addPrimitive(tris)
        node = GeomNode("cube")
        node.addGeom(geom)
        return node

    def spin_task(self, task):
        self.cube.setHpr(task.time * 40, task.time * 25, 0)
        return Task.cont


if __name__ == "__main__":
    app = CubeDemo()
    app.run()