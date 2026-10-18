# InkZero AR — names: rules, packages, classes, functions

Every name below was chosen by Artie on 2026-10-17. This file is the source of truth; the diagrams and the code follow it.

## Naming rules (reuse on the next project)

1. **Classes and functions start with a capital** (`ScriptedGameLoader`, `LoadScriptedGame()`). **Fields start lowercase** (`turnNumber`). Standard C#.
2. **Private fields get a leading underscore** (`_laptopPort`). Microsoft's .NET style; marks "mine, internal."
3. **Everything lives in a namespace**: `InkZero.<Package>`. Hover in the editor and it says `InkZero.GameData.GameState` vs `UnityEngine.Transform`. That is how you tell your names from Unity's.
4. **A name says what the thing does**, not how hard it was (`Counting`, not `Simple`) and not what it will become.
5. **Name the package for its real job; nest the stand-in inside it** (`Perception/ScriptedGame` now, `Perception/Recognition` later).
6. **A class carries its folder's name when it is that folder's main thing** (`ScriptedGameLoader`, `CountingEngine`, `OverlayDrawer`).
7. **No shortening** (`MachineLearning`, not `ML`; `cardCopy`, never bare `copy`).
8. **Collision checks, every name**: Unity/C# words (`Input`, `Renderer`, `Scene`, `Script`, `Display`, `Model`), Meta words (`Link`), ML words (`Model`), and the **Lorcana rulebook**. A rulebook word is allowed only when it means the same thing the rules mean (`zone`, `turn`, `deck`, `draw`, `inkwell` yes; `move`, `location`, `card state` no).
9. **One word, one meaning**: zone = where a card is by the rules; area = a region of the mat; position = one spot in an area; counts = tallies; the percentage is the only statistic.
10. **Functions that run when something happens start with `On`** (`OnLaptopCommand`). Unity convention.
11. **One verb per pipeline stage**: load → step → build → draw.
12. **Type singular, list plural** (`Turn` / `turns`, `CardZone` / `cardZones`).
13. **Reading a function call**: `DrawOverlay(overlayRows, gameCounts)` is two separate inputs handed over, not one (x, y) point. The parentheses list deliveries; they do not pair the inputs together.

## Namespace and folder layout

```
InkZero/
  Perception/          sense: turn what happens at the table into zone changes
    ScriptedGame/        demo stand-in: a written-down game, stepped from the laptop
    Recognition/         future: camera does the same job
  GameData/            the data every other package reads or writes
  Engine/              think: estimate what is hidden
    Counting/            now: count what was seen, divide
    MachineLearning/     future: learned from data, method not yet chosen
  Overlay/             act: draw rows and counts in passthrough
```

## Perception / ScriptedGame

**ScriptedGameLoader** — runs once at startup; reads the scripted-game file and fills GameState.
- `_scriptedGameFile` — where the file sits inside the build.
- `LoadScriptedGame(gameState)` — reads both deck lists, the mat positions, and every turn into the GameState it is handed.

**TurnStepper** — the demo's remote control; steps the scripted game one turn at a time.
- `_laptopPort` — the USB serial connection to the laptop (not Quest Link).
- `OnLaptopCommand(command)` — runs when "next" or "back" arrives: calls `NextTurn()` or `PreviousTurn()`, then `BuildOverlayRows()`, then `DrawOverlay()`.

## Perception / Recognition (future, empty)
The camera version of ScriptedGame: video in, CardZoneChanges out.

## GameData

**GameState** — where every copy of every card is right now, as the player saw it. The only class that changes during play. (The judge's word.)
- `turnNumber` — which turn we are on.
- `cardZones[card][cardCopy]` — a CardZone for each copy of each card.
- `positionOnMat[card][cardCopy]` — which MatPosition a copy sits in, if it is on the mat.
- `handCount`, `loreCount` — from the scripted-game file; the mat cannot tell you these.
- `inkwellCount`, `deckCount`, `discardCount` — counted from positions.
- `NextTurn()` — applies the next Turn's zone changes and counts; `turnNumber` + 1.
- `PreviousTurn()` — undoes them; `turnNumber` − 1.

**Card** — one line of the opponent's deck list.
- `cardName`, `cardCopiesInDeck` (1–4), `cardType` (enum **CardType**: character, action, song, item, location), `inkCost`.
- Design note: in the demo `cardCopiesInDeck` is known from the script. In real use nobody hands you the list, so it is either the worst-case assumption (4) or an inference the engine makes. The field name stays true either way: how many copies the system believes are in the deck.

**CardZone** (enum: a fixed list of allowed values) — which zone a copy went to, as last seen. The rulebook's zones plus one.
- `Hand`, `Deck`, `Discard`, `Inkwell`, `InPlay`, `Blank`.
- These are the rulebook's physical zones (Comprehensive Rules 8.2–8.6) plus Blank. The sixth rulebook zone, the bag (8.7), is where triggered abilities wait; it is not a place on the mat and has no pip. `Hand` covers a card seen by a reveal or returned to hand from the table.
- The first four plus Blank are the five pips. `InPlay` has no pip: the card is on the table and its row is drawn under it. `Blank` = not seen yet: in the opponent's hand, still in their deck, or put into the inkwell face-down by a card effect. (A normal ink is revealed, Tournament Rules 5.5. Unknown cards on the table come from effect-inks such as Judy Hopps, On the Case, and from Boost, which puts the top card of the deck face-down under a character.) An unknown card is written in the script as `unknown`; it fills a position, leaves the unseen total if it came from the deck, and moves no pip. A face-down card is not in play.

**Turn** — one turn of play, as the script describes it.
- `turnNumber`, `zoneChanges` (a list of CardZoneChange), `handCount`, `loreCount` at the end of the turn.

**CardZoneChange** — one copy of one card going from one zone to another. ("Move" is avoided: in Lorcana, moving means moving a character to a location.)
- `card`, `cardCopyNumber` (1–4), `from`, `to` — each end is a MatPosition or a CardZone (hand and deck are zones, not spots on the mat).

**MatPosition** — one marked spot on the printed mat.
- `matPositionName` — printed on the mat and used in the script: `play-3`, `inkwell-7`, `deck`, `discard`.
- `matArea` — which region of the mat: `PlayArea`, `InkwellArea`, `DeckArea`, `DiscardArea` (enum **MatArea**).
- `matPositionMillimeters` — across and down from the mat's corner, in mm.

**OverlayRow** — everything drawn for one card.
- `card`, `pips` (one CardZone per copy), `nextDrawOdds` (unseen copies ÷ unseen cards; unseen copies = Blank + Deck copies of that card; unseen cards = deckSize − copies in Inkwell, Discard, InPlay or revealed Hand − effect-placed face-down cards; in practice the deck plus the unrevealed hand), `matPositionsInPlay` (where to draw the row under copies on the table).

## Engine / Counting

**CountingEngine** — turns GameState into OverlayRows by counting.
- `deckSize` — 60.
- `BuildOverlayRows(gameState)` — one OverlayRow per card in the deck list. Deterministic: same GameState in, same rows out.

## Engine / MachineLearning (future, empty)
`MachineLearningEngine`: GameState → likely deck list and likely plays. Method chosen when it is built.

## Overlay

**OverlayDrawer** — draws the rows and the counts in passthrough, anchored to the mat. The contribution.
- `placement` — `OnMat` or `OnPanel` (enum **OverlayPlacement**). The switch the test plan flips.
- `matCorners` — the four pinned corner points.
- `PinMat(corners)` — setup: takes the four corner pinches. Pinning is the gesture; anchoring is what it produces.
- `DrawOverlay(overlayRows, gameCounts)` — once per turn: draws the per-card rows and the five-number counts strip. Rows come from the engine, counts from GameState; they are drawn side by side, not derived from each other.

## Words that are NOT class names, used in prose
- **scene** — one staged moment copied from a tournament game. In code a scene is a scripted game (`ScriptedGame`).
- **overlay** — rows plus counts strip, whichever placement.
- **pip** — one icon per copy, drawn from a CardZone. Display labels use the short player words ("ink", "disc"); code uses the rulebook zone names (`Inkwell`, `Discard`).
- **figure notes** — one # at the start of each note; wrapped lines indent under it with no #; panel captions get no #.
