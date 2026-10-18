# InkZero AR — scene file format, example

One scene = one text file. Three sections: decks, start, turns.
Plain text, one item per line, so it can be typed by hand from a stream recording.

```
# scene-02.txt
# Lorcana Challenge NA 2026, round 2, turns 4–7, opponent's side only
# Opponent's copy of the mat is mirrored; position names are the opponent's positions.

[deck]
# name | cardCopiesInDeck | type | ink cost
Maleficent - Exultant Spellcaster | 4 | character | 1
Rafiki - Mystical Fighter        | 4 | character | 1
Toulouse - Rough and Tumble      | 4 | character | 2
Arthur - Novice Blacksmith       | 3 | character | 2
Cheshire Cat - Inexplicable      | 4 | character | 3
Strength of a Raging Fire        | 4 | song      | 3
# ... one line per distinct card, until 60

[start]
# where every copy is when the scene opens. Anything not listed is blank.
turn = 4
lore = 3
hand = 5
Maleficent - Exultant Spellcaster | 1 | play-1
Maleficent - Exultant Spellcaster | 2 | inkwell-1
Rafiki - Mystical Fighter        | 1 | inkwell-2
Toulouse - Rough and Tumble      | 1 | inkwell-3
Toulouse - Rough and Tumble      | 2 | discard
Arthur - Novice Blacksmith       | 1 | inkwell-4
Cheshire Cat - Inexplicable      | 1 | hand      # seen by a reveal before the scene opens

[turn 5]
# one zone change per line: card | cardCopy | from | to
# "hand" and "deck" are not positions on the mat, they are zones
Cheshire Cat - Inexplicable | 1 | hand | play-2
Rafiki - Mystical Fighter   | 2 | hand | inkwell-5
lore = 5

[turn 6]
Maleficent - Exultant Spellcaster | 1 | play-1 | discard
Strength of a Raging Fire         | 1 | hand   | discard
Cheshire Cat - Inexplicable       | 2 | deck   | hand      # revealed by an effect
lore = 7

[turn 7]
Cheshire Cat - Inexplicable | 2 | hand | play-3
Arthur - Novice Blacksmith  | 2 | hand | inkwell-6
unknown                     | - | deck | inkwell-7      # effect inked the top card face-down; fills the position, no pip moves
hand = 4
lore = 7
```

## What the loader does with it

- `[deck]` builds the `Card[]` list. `cardCopiesInDeck` sets how many pips each card gets.
- `[start]` sets `GameState` for the opening turn. Every copy not named is `Blank`. A `| hand` here means seen in hand already.
- Each `[turn n]` is a list of `CardZoneChange`s. `NextTurn()` applies the next block; `PreviousTurn()` undoes it.
- A `to` of `inkwell-k`, `discard`, `play-k` sets that copy's `CardZone` and `MatPosition`. A `play-k` destination sets `InPlay`, the zone with no pip.
- A `to` of `hand` sets `Hand` (seen by a reveal). A `to` of `deck` sets `Deck`. In code a scene is a `ScriptedGame`.
- A `from` of `hand` on a card whose copy was `Blank` is fine: the zone change itself is the first sighting.
- A card of `unknown` going to `inkwell-k` (an effect-ink) or to `play-k` (Boost: top card of the deck face-down under that character) fills that position without touching any card's pip. An unknown from `deck` leaves the unseen total; an unknown to `inkwell-k` adds one to `inkwellCount`. A face-down card is not in play (Comprehensive Rules glossary).
- `hand =`, `lore =` lines set counts directly, since the script knows them from the stream.
- Deck count = 60 − everything placed. Inkwell and discard counts come from the positions.

## Why plain text

- Typed by hand while scrubbing a stream recording. No tool needed.
- Diffs cleanly in git.
- Readable in the proposal and the repo README.
