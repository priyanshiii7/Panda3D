# Panda3D Spinning Cube Demo

A minimal Panda3D scene built from scratch in Python — no external `.egg`/`.bam`
model files required. Useful as a quick, honest demonstration of Panda3D
fundamentals for an interview or portfolio link.

## What it demonstrates
- **Procedural geometry**: builds a cube mesh face-by-face using
  `GeomVertexData` / `GeomVertexWriter` / `GeomTriangles` (the low-level
  Panda3D mesh API), rather than loading a pre-made asset.
- **Lighting**: one `AmbientLight` + one `PointLight` attached to the scene
  graph (`render`).
- **Animation**: a `taskMgr` task that rotates the cube continuously using
  elapsed time (`task.time`), the standard Panda3D animation pattern.
- **Camera control**: starts at a fixed pose, then hands off to Panda3D's
  built-in mouse-orbit/zoom/pan camera (`enableMouse()`).

## Run it
```bash
pip install panda3d
python spinning_cube.py
```
A window opens with a colored, rotating cube. Click-drag with the mouse to
orbit the camera; scroll to zoom.

## Why this exists
Built as a same-day learning exercise to get hands-on with Panda3D's scene
graph, Geom/GeomNode mesh API, and task manager — the three things most
Panda3D apps (games, visualizations, simulations) are built on top of.

## Next steps to extend it
- Swap the procedural cube for a loaded `.bam`/`.egg`/`.gltf` model via
  `self.loader.loadModel(...)`.
- Add keyboard-driven movement (`self.accept("arrow_up", ...)`).
- Add a `CollisionTraverser` for physics/collision detection.
