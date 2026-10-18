# InkZero AR

The AR part of InkZero: a passive overlay on a passthrough headset that shows a Lorcana player where each copy of the opponent's cards has gone and the chance each card is the next draw. Built for HCC 552, AR/VR Design and Research, Grand Valley State University, Fall 2026. The full plan is in the proposal, [PDF](InkZero_AR_Proposal_v3_2026-10-18.pdf) or [Markdown](InkZero_AR_Proposal_v3_2026-10-18.md).

## What is here

- `InkZero_AR_Proposal_v3_2026-10-18.md` and `.pdf`: the proposal. The PDF is what was submitted; the Markdown is its source.
- `figures/`: the proposal figures as SVG (source) and PNG (rendered). `fig3` is a Dreamborn screenshot that does not exist yet; the PDF carries a placeholder.
- `figures/class_index.md`: every package, class, field and method name, with the 13 naming rules. This file is the source of truth. The diagrams and the code follow it.
- `figures/scene_example.md`: the scene file format, with a worked example. A scene is a few turns copied from a recorded tournament game, written as plain text so it can be typed by hand from a stream.
- `uml/`: four UML diagrams, drafted before the code and expected to change with it. Use case for the demo, class diagram, sequence diagram for one turn, package diagram.

## The four packages

Code lives in the namespace `InkZero.<Package>`.

| Package | Job | Now | Future |
|---|---|---|---|
| `Perception` | Turn what happens at the table into zone changes | `ScriptedGame`: a written-down game, stepped from the laptop | `Recognition`: the camera does the same job |
| `GameData` | The data every other package reads or writes | `GameState`, `Card`, `CardZone`, `Turn`, `CardZoneChange`, `MatPosition`, `OverlayRow` | |
| `Engine` | Estimate what is hidden | `Counting`: count what was seen, divide | `MachineLearning`: learned from data |
| `Overlay` | Draw rows and counts in passthrough, pinned to the mat | `OverlayDrawer` | |

Each future swap touches one package.

## Timeline

- Sprint 1, Oct 20 to Nov 11: one scene, rows and counts on the mat, loaded from a file and stepped from the laptop. Shown live at the checkpoint.
- Sprint 2, Nov 12 to Dec 7: three scenes, rows and counts on the mat and in a panel, the four checks (correctness, latency, stability, readability) run and written up.

The Unity project is not in the repo yet. It lands here when Sprint 1 starts.
