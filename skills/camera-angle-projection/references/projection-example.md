# Approximate camera projection

Modern, original application of the camera-placement and projection ideas in Katz (KT 29–30, 98–109, 350–369).

For a rectilinear camera with active sensor width `w` and focal length `f`, horizontal field of view is `2 * atan(w / (2*f))`. A virtual camera may expose horizontal field of view directly. At a subject plane perpendicular to the viewing direction a distance `d` away, the approximate horizontal span is `2*d*tan(FOV/2)`. Use consistent units and radians in calculation. This simplified estimate ignores distortion, focus breathing, nonperpendicular planes and crop changes.

Example: a nominal 36 mm sensor width with a 50 mm lens gives roughly 39.6 degrees horizontal field of view. At 3 m, the plane spans roughly 2.16 m. This only predicts coverage of a plane; it does not imply a particular emotional look. The relative size and shape relationships depend on camera placement. Change viewpoint first if perspective is wrong, then frame using field of view.

Make a top-view sketch using camera position and boundary rays. Use the actual output frame shape and vertical field of view to check height and headroom. If geometry is estimated, label it. Compare with a test render or measured framing before locking the shot.
