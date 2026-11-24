---
name: camera-angle-projection
description: Use simplified top and elevation views to estimate camera placement,
  framing and feasibility. Use when previsualizing or planning coverage.
---
# Camera angle projection

## Inputs and deliverable

- Accept: set dimensions or approximate geometry; subject positions; format; desired frame.
- Produce: camera placement diagram, viewpoint limits, assumptions and validation step.
- If critical inputs are missing, state assumptions, distinguish planning from observed footage, and mark any untestable decision for review. Do not invent measurements, assets or runtime results.

## Decision procedure

1. Establish a common coordinate system and dimensioned or estimated floor plan; record camera and subjects in world space.
2. Choose viewing direction and field of view, drawing the frame's horizontal boundaries from camera position; use elevation or height estimates to check vertical framing.
3. Check which objects overlap, which surfaces are visible and whether the camera position is physically plausible.
4. For multiple angles, preserve geometry and update camera not the world; test with rough 3D or on-location framing if available.
5. Label approximate dimensions and lens assumptions; do not present a sketch as surveyed or optically calibrated.

## Diagnose and correct

If a reverse frame requires a camera through a wall, revise layout, choose another view or explicitly plan a virtual/set modification.

## Output checks

- Deliver the specified artifact, with decisions tied to identifiable scenes, beats or shots when relevant.
- Show evidence or reasoning for the selected approach and at least one plausible alternative when the decision is consequential; state whether it is planned or actually observed.
- Verify the specific failure mode above is not present, or document the creative reason and the test that would demonstrate success.
- Use the original practice case below to check that the procedure produces a concrete, reviewable result rather than a definition or generic advice.

## Practice case

A narrow corridor requires an OTS and wide view; draw a feasible camera plan and note which wall might need removal in a constructed set.

## Sources and related capabilities

Consult [Approximate camera projection](references/projection-example.md) for additional technique details when relevant. Read [Source notes](references/sources.md) for provenance and boundaries. Related skill IDs (optional, discover through your host or library registry): `location-geography`, `lens-and-focus`, `storyboard-design`. No external skill is mandatory for standalone use.
