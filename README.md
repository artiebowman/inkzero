# InkZero

InkZero is a project I conceived before I applied to the M.S. in Artificial Intelligence at Grand Valley State University. It is a practice helper for Disney Lorcana, a two-player trading card game. During a game, it shows the player where each copy of the opponent's cards has gone and the chance each card is the next draw, while they play a normal game.

The project has three parts:

- **Recognition.** The camera reads the table and turns what happens into zone changes. Future work.
- **Engine.** Works out what is likely hidden from what was seen. The first version counts and divides.
- **AR.** Draws the help on a passthrough headset, either on the mat under each card or in a panel beside it.

`ar/` is the AR part. I am building it as my project for HCC 552, AR/VR Design and Research, Fall 2026. The proposal is in [`ar/InkZero_AR_Proposal_v3_2026-10-18.pdf`](ar/InkZero_AR_Proposal_v3_2026-10-18.pdf). The other two parts get folders when they exist.

## Layout

```
ar/
  InkZero_AR_Proposal_v3_2026-10-18.md   the proposal, source
  InkZero_AR_Proposal_v3_2026-10-18.pdf  the proposal, as submitted
  README.md                              what the AR part is and how it is organized
  figures/                               the proposal figures, SVG and PNG
    class_index.md                       every package, class, field and method name, and the naming rules
    scene_example.md                     the scene file format, with a worked example
  uml/                                   use case, class, sequence and package diagrams
```

## Positioning

This is a free learning tool for casual play. It is not for sanctioned events. Lorcana's tournament rules forbid notes other than lore totals, and allow electronic devices only when the device is in plain view of both players, which a headset display is not. The overlay is visible only to the player wearing the headset. In casual play the opponent knows the tool is there.

No card art is reproduced in this repo or in the overlay; the overlay draws marks and numbers. Ravensburger, the company behind Lorcana, publishes guidelines for community use, and this project follows them.

InkZero is unofficial Fan Content permitted under Ravensburger's community guidelines. Not approved or endorsed by Disney or Ravensburger. Disney Lorcana and all related characters and elements are the property of Disney and Ravensburger.

## Author

Arthur Bowman, M.S. in Artificial Intelligence, Grand Valley State University.
