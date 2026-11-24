---
name: tracking-and-dolly
description: Design translating camera moves with perspective change, parallax, focus
  and dramatic motivation. Use when planning moving-camera shots.
---
# Tracking and dolly

## Inputs and deliverable

- Accept: scene geometry; start/end framing; subject path; practical constraints.
- Produce: movement path, parallax and focus plan, fallback coverage.
- If critical inputs are missing, state assumptions, distinguish planning from observed footage, and mark any untestable decision for review. Do not invent measurements, assets or runtime results.

## Decision procedure

1. Choose whether to track parallel, follow, approach, retreat or move vertically; tie motion to a reveal or relationship.
2. Plot actual camera translation relative to foreground and background; distinguish translation from zoom.
3. Calculate or estimate clearances, eyelines and subject scale at key positions; check occlusion and changing perspective.
4. Plan focus and lighting across the path, including start and end exposures; avoid promising identical perspective from different positions.
5. Define a meaningful endpoint and an alternative edited version if the move cannot be achieved.

## Diagnose and correct

A large dolly move that adds no new perspective is unnecessary. A close move may distort face or expose set edges; revise distance or use a simpler alternative.

## Output checks

- Deliver the specified artifact, with decisions tied to identifiable scenes, beats or shots when relevant.
- Show evidence or reasoning for the selected approach and at least one plausible alternative when the decision is consequential; state whether it is planned or actually observed.
- Verify the specific failure mode above is not present, or document the creative reason and the test that would demonstrate success.
- Use the original practice case below to check that the procedure produces a concrete, reviewable result rather than a definition or generic advice.

## Practice case

A camera approaches a seated person while another figure enters behind them; identify when foreground parallax and focus reveal the second figure.

## Sources and related capabilities

Read [Source notes](references/sources.md) for provenance and boundaries. Related skill IDs (optional, discover through your host or library registry): `camera-movement-intent`, `lens-and-focus`, `tracking-choreography`. No external skill is mandatory for standalone use.
