# InkZero

InkZero is a practice helper for Disney Lorcana, a two-player trading card game. While a player plays a normal game, it shows them where each copy of the opponent's cards has gone and the chance each card is the next draw. I conceived it before I applied to the M.S. in Artificial Intelligence at Grand Valley State University, and it is one of the reasons I applied.

## The three parts

| Part | Job | Status |
|---|---|---|
| Recognition | The camera reads the table and turns what happens into zone changes. | Future. |
| Engine | Works out what is likely hidden from what was seen. | The first version counts and divides. It ships inside the AR part. |
| AR | Draws the help on a passthrough headset, on the mat under each card or in a panel beside it. | In progress: my project for HCC 552, AR/VR Design and Research, Fall 2026. |

The proposal is in [`ar/docs/proposal/`](ar/docs/proposal/), as [PDF](ar/docs/proposal/InkZero_AR_Proposal_v3_2026-10-18.pdf) and Markdown.

## Layout

```
docs/            project-wide notes: decisions.md
ar/              the AR part (see ar/README.md)
  docs/          the proposal, its figures and build, the UML diagrams, the naming index, the scene format
  scenes/        scene files: a few turns copied from a recorded game, one file each
  tools/         small scripts that are not the app: hand-check tables, log parsers
  unity/         the Unity project, from Sprint 1
```

`recognition/` and `engine/` appear when they exist.

## Getting started

There is nothing to run yet. Read the proposal. The Unity project lands in `ar/unity/` when Sprint 1 starts on October 20, 2026, and this section will say how to build and run the demo.

## Building the proposal PDF

The PDF is built from the Markdown on a Mac, because the stylesheet asks for Helvetica and Linux falls back to another face. Rebuild it before committing a change to the Markdown.

```
pip install markdown playwright && python3 -m playwright install chromium
python3 ar/docs/proposal/build/build_html.py && python3 ar/docs/proposal/build/build_pdf.py
```

## Positioning

This is a free learning tool for casual play. It is not for sanctioned events. Lorcana's tournament rules forbid notes other than lore totals, and allow electronic devices only when the device is in plain view of both players, which a headset display is not. The overlay is visible only to the player wearing the headset. In casual play the opponent knows the tool is there.

Card images and card data come from a public Lorcana card API at runtime and are shown the way deck-building sites such as Dreamborn already show them. This repo stores no card images. The project is free, makes no money, and is for learning. Ravensburger, the company behind Lorcana, publishes guidelines for community use, and this project follows them.

InkZero is unofficial Fan Content permitted under Ravensburger's community guidelines. Not approved or endorsed by Disney or Ravensburger. Disney Lorcana and all related characters and elements are the property of Disney and Ravensburger.

## Author and license

Arthur Bowman, M.S. in Artificial Intelligence, Grand Valley State University.

The code and documents are under the [MIT License](LICENSE). Card data and images are not covered by it.
