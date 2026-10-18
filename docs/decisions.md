# Decisions

One line per decision, newest at the bottom. The reason stays short. The proposal in `ar/docs/proposal/` has the long version.

| Date | Decision | Why |
|---|---|---|
| 2026-09 | InkZero has three parts: recognition, engine, AR. HCC 552 builds the AR part. | Each part is its own problem. The course has room for one. |
| 2026-10-11 | The research question is about the display, not the engine. | The engine belongs to another part. Keeping it simple keeps the display question the one being answered. |
| 2026-10-11 | Build both placements, on the mat and on a panel, and compare them. | Each has a known strength. The comparison is the contribution. |
| 2026-10-11 | The demo is a scripted game stepped from the laptop, not a camera. | Recognition is future work. A script gives every pip and number a known answer to check. |
| 2026-10-14 | Track the mat, not the cards. A printed mat with a position for each card. | Four corner pinches pin the mat. Every overlay is measured from them. |
| 2026-10-17 | Four packages: Perception, GameData, Engine, Overlay. | Each future swap (recognition, a learned engine) touches one package. |
| 2026-10-17 | Every name is in `ar/docs/naming.md`, with 13 naming rules. | One source of truth. Diagrams and code follow it. |
| 2026-10-17 | Tokens are out of scope. | They arrived with the set released 2026-10-16, after the design was set. |
| 2026-10-18 | Scenes are copied from recorded tournament games, not authored. | I did not pick a board that flatters the overlay. |
| 2026-10-18 | One repo, `inkzero`, with the AR part in `ar/`. | Claims the name. Recognition and engine get folders when they exist. |
| 2026-10-18 | Card images come from a public Lorcana card API at runtime. None are stored in the repo. | Deck sites already show them this way. The project is free and for learning. |
| 2026-10-18 | The proposal PDF is built on the Mac. | The CSS asks for Helvetica. Linux falls back to Liberation Sans. |
| 2026-10-18 | MIT license for the code. Card data and images are not covered. | The usual choice for a free tool. |
