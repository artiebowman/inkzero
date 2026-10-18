# InkZero

InkZero is a practice helper for Disney Lorcana, a two-player trading card game with 60-card decks and hidden hands. A lot of what decides a game is information a player has already seen and has to hold in their head: which cards the opponent inked, which they discarded, which they revealed, and what that leaves in their deck. The tournament rules allow no notes, so the only tracker a player has at a physical table is memory. InkZero puts that tracking on a passthrough headset. For every card in the opponent's deck it draws one row: a pip per copy showing where that copy went, and the chance that card is the next draw. The rows sit on the mat under the cards they are about, or in a panel beside the mat, and they update on their own as the game moves. The player wears the headset, pins the mat once, and then plays the game the way it is always played.

The engine behind the rows is arithmetic: count what was seen, divide unseen copies by unseen cards. It is kept simple on purpose. The question this project answers is how the help should be shown so that a player can read it without looking away from the opponent. A camera that reads the table, and a learned engine that infers the opponent's deck and likely plays, are future parts that would slot in without changing the display.

The AR part is being built as my project for HCC 552, AR/VR Design and Research, at Grand Valley State University, Fall 2026. The proposal is in [`ar/docs/proposal/`](ar/docs/proposal/), as [PDF](ar/docs/proposal/InkZero_AR_Proposal_v3_2026-10-18.pdf) and Markdown.

## How it is organized

Code lives in the namespace `InkZero.<Package>`. Every name is in [`ar/docs/naming.md`](ar/docs/naming.md), with the naming rules. That file is the source of truth; the diagrams and the code follow it.

| Package | Job | Now | Future |
|---|---|---|---|
| `Perception` | Turn what happens at the table into zone changes | `ScriptedGame`: a written-down game, stepped from the laptop | `Recognition`: the camera does the same job |
| `GameData` | The data every other package reads or writes | `GameState`, `Card`, `CardZone`, `Turn`, `CardZoneChange`, `MatPosition`, `OverlayRow` | |
| `Engine` | Estimate what is hidden | `Counting`: count what was seen, divide | `MachineLearning`: learned from data |
| `Overlay` | Draw rows and counts in passthrough, pinned to the mat | `OverlayDrawer` | |

Each future swap touches one package.

## Layout

```
docs/                 project-wide notes: decisions.md
ar/                   the AR part
  docs/proposal/      the proposal, Markdown and PDF, and its figures
  docs/uml/           use case, class, sequence and package diagrams
  docs/naming.md      every package, class, field and method name, and the naming rules
  docs/scene-format.md  the scene file format, with a worked example
  docs/related-work/  the prior-work scan and search notes
  scenes/             scene files: a few turns copied from a recorded tournament game, one file each
  tools/              small scripts that are not the app: hand-check tables, log parsers
  unity/              the Unity project, from Sprint 1
```

`recognition/` and `engine/` appear when they exist.

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

## Positioning

This is a free learning tool for casual play. It is not for sanctioned events. Lorcana's tournament rules forbid notes other than lore totals, and allow electronic devices only when the device is in plain view of both players, which a headset display is not. The overlay is visible only to the player wearing the headset. In casual play the opponent knows the tool is there.

Card images and card data come from a public Lorcana card API at runtime and are shown the way deck-building sites such as Dreamborn already show them. This repo stores no card images.

## Author and license

Arthur Bowman, M.S. in Artificial Intelligence, Grand Valley State University.

The code and documents are under the [MIT License](LICENSE). Card data and images are not covered by it.

InkZero is unofficial Fan Content permitted under Ravensburger's community guidelines. Not approved or endorsed by Disney or Ravensburger. Disney Lorcana and all related characters and elements are the property of Disney and Ravensburger.
