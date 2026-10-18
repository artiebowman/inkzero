# InkZero AR

The AR part of InkZero: a passive overlay on a passthrough headset that shows a Lorcana player where each copy of the opponent's cards has gone and the chance each card is the next draw. Built for HCC 552, AR/VR Design and Research, Grand Valley State University, Fall 2026. The full plan is the proposal, [PDF](docs/proposal/InkZero_AR_Proposal_v3_2026-10-18.pdf) or [Markdown](docs/proposal/InkZero_AR_Proposal_v3_2026-10-18.md).

## The four packages

Code lives in the namespace `InkZero.<Package>`. Every name is in [`docs/naming.md`](docs/naming.md), with the naming rules. That file is the source of truth; the diagrams and the code follow it.

| Package | Job | Now | Future |
|---|---|---|---|
| `Perception` | Turn what happens at the table into zone changes | `ScriptedGame`: a written-down game, stepped from the laptop | `Recognition`: the camera does the same job |
| `GameData` | The data every other package reads or writes | `GameState`, `Card`, `CardZone`, `Turn`, `CardZoneChange`, `MatPosition`, `OverlayRow` | |
| `Engine` | Estimate what is hidden | `Counting`: count what was seen, divide | `MachineLearning`: learned from data |
| `Overlay` | Draw rows and counts in passthrough, pinned to the mat | `OverlayDrawer` | |

Each future swap touches one package.

## Folders

- `docs/proposal/`: the proposal as Markdown and PDF, its figures (`figures/`, SVG source and PNG), and the scripts that build the PDF (`build/`).
- `docs/uml/`: use case, class, sequence and package diagrams, drafted before the code and expected to change with it.
- `docs/naming.md`: every package, class, field and method name, and the 13 naming rules.
- `docs/scene-format.md`: the scene file format, with a worked example.
- `docs/related-work/`: the prior-work scan and search notes.
- `scenes/`: the scene files. A scene is a few turns copied from a recorded tournament game, written as plain text so it can be typed by hand from a stream. Empty until the games are picked.
- `tools/`: small scripts that are not the app, such as the hand-check table for the Correctness check. Empty until Sprint 1.
- `unity/`: the Unity project. Lands when Sprint 1 starts.

## Running the demo

Not yet. Sprint 1 ends with one scene stepped from the laptop, and this section will say how to build the app, load it on the Quest, pin the mat and step turns.

## How it is checked

Four checks, run on three scenes with the overlay on the mat and on the panel:

- Correctness: pips and numbers match hand-checked answers for every turn of every scene.
- Latency: milliseconds from the turn command to the redrawn overlay.
- Stability: how far on-mat rows drift off their cards over ten minutes, against a ruler on the mat.
- Readability: reads at a glance, yes or no, against a short checklist. Glare is on the checklist.

## Timeline

- Sprint 1, Oct 20 to Nov 11, 2026: one scene, rows and counts on the mat, loaded from a file and stepped from the laptop. Shown live at the checkpoint.
- Sprint 2, Nov 12 to Dec 7, 2026: three scenes, rows and counts on the mat and in a panel, the four checks run and written up.
