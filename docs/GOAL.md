# Ice Prize Price — Development Goal

> **Chase the prize. Pay the price.**

Ice Prize Price is a small 2D arcade game made with Python + Pygame.

The player controls an ice ball on a slippery ice floor, collects coins, and tries to get the highest score while avoiding costly wall collisions.

## Goal

Build the game gradually, starting with a very small playable prototype and adding features version by version.

The final v1.0.0 game should have:

- Simple controls
- Slippery ice physics
- Wall bouncing
- Limited lives
- Coins
- Score
- Game Over
- Restart
- Custom visuals
- Sound effects

The game should remain small, lightweight, understandable, and fun.

---

## Core Gameplay

The basic gameplay loop is:

```text
Move the ice ball
       ↓
Find a coin
       ↓
Collect the coin
       ↓
Gain score
       ↓
Keep playing
       ↓
Hit a wall
       ↓
Lose 1 life
       ↓
Lives remaining?
   ↙          ↘
 Yes           No
  ↓             ↓
Continue     Game Over
```

## Main Mechanics

- The player moves around an ice-covered play area.
- Ice physics cause the player to keep sliding after releasing movement.
- Coins are the main reward.
- Hitting a wall costs one life.
- Wall collisions cause the player to bounce.
- A wall bounce may temporarily increase velocity.
- The game ends when all lives are lost.

---

## Controls

### PC

Both control layouts should work:

| Action | Keys |
|---|---|
| Up | `W` / `↑` |
| Down | `S` / `↓` |
| Left | `A` / `←` |
| Right | `D` / `→` |

Diagonal movement should be supported.

### Android

Use simple screen-edge touch controls:

```text
┌─────────────────────┐
│         UP          │
│                     │
│ LEFT   PLAYER   RIGHT│
│                     │
│        DOWN         │
└─────────────────────┘
```

- Top edge → Up
- Bottom edge → Down
- Left edge → Left
- Right edge → Right

A virtual joystick is not required.

---

## Screen

Initial resolution:

```python
SCREEN_SIZE = (1280, 720)
```

- Designed primarily for landscape orientation.
- The player must remain inside the playable area.
- Target: approximately 60 FPS.

---

# Version Roadmap

## v0.1.0 — Bare Minimum Prototype

### Goal

Create the smallest playable version of the game.

### Requirements

- Pygame window
- Ice-like background
- Circle player
- WASD controls
- Arrow-key controls
- Android edge-touch controls
- Diagonal movement
- Screen boundary restriction
- Direct movement

### Not included

- Ice physics
- Friction
- Wall bounce
- Lives
- Coins
- Score
- Game Over
- Assets
- Sound

### Done when

The player can start the game, move in all directions, use keyboard/touch controls, move diagonally, and stay inside the screen.

---

## v0.2.0 — Ice Physics

### Goal

Make the player behave like an object sliding on ice.

### Requirements

Add:

- Position
- Velocity
- Acceleration
- X/Y movement
- Friction
- Maximum normal speed

Movement should roughly work as:

```text
Input
 ↓
Acceleration
 ↓
Velocity
 ↓
Position
```

When input stops, the player should continue sliding and gradually slow down.

### Done when

Movement feels slippery instead of instantly stopping.

---

## v0.3.0 — Walls & Bouncing

### Goal

Make wall collisions part of the gameplay.

### Requirements

- Detect screen-wall collisions.
- Keep the player inside the screen.
- Bounce away from walls.
- Preserve the appropriate velocity direction.
- Prevent the player from getting stuck.

### Temporary Wall Boost

A wall collision may temporarily increase velocity.

Target multiplier:

**1.25× – 1.50×**

The boost must eventually return to normal movement speed.

### Done when

The player can bounce from walls and receives a temporary bounce-speed boost.

---

## v0.4.0 — Lives

### Goal

Add the main penalty for hitting walls.

### Requirements

- Start with 5 lives.
- Lose 1 life per valid wall collision.
- Bounce after the collision.
- Prevent one continuous wall contact from removing multiple lives.
- Display lives near the top-center of the screen.

Example:

```text
❤️ ❤️ ❤️ 🖤 🖤
```

### Done when

Lives are displayed, correctly decrease after collisions, and the game detects when all lives are gone.

---

## v0.5.0 — Coins

### Goal

Add the main reward.

### Requirements

- Spawn a coin inside the playable area.
- Allow the player to collect it.
- Remove the coin after collection.
- Spawn another coin.
- Do not spawn a coin directly inside the player.
- Keep coins inside the playable area.

Gameplay:

```text
Find coin
   ↓
Collect coin
   ↓
New coin
```

### Done when

The player can repeatedly collect coins.

---

## v0.6.0 — Score

### Goal

Add a visible score.

### Requirements

- Start score at `0`.
- Increase score when collecting coins.
- Display score on the HUD.
- Keep score during the current game.
- Reset score when starting a new game.

### Optional custom digit assets

```text
0.png
1.png
2.png
3.png
4.png
5.png
6.png
7.png
8.png
9.png
```

### Done when

The score is visible and updates correctly.

---

## v0.7.0 — Game Over

### Goal

Complete the basic gameplay loop.

### Requirements

When:

```text
Lives = 0
```

show:

```text
GAME OVER
```

Also:

- Stop normal gameplay.
- Show final score.
- Provide a restart option.

### Done when

The complete loop works:

```text
Start
 ↓
Move
 ↓
Collect coins
 ↓
Lose lives
 ↓
Lives = 0
 ↓
Game Over
 ↓
Restart
```

---

## v0.8.0 — Visual Assets

### Goal

Replace prototype shapes with custom artwork.

### Planned assets

```text
assets/
├── background/
│   └── ice.png
│
├── player/
│   └── ice-ball.png
│
├── coins/
│   └── coin.png
│
└── ui/
    ├── heart-full.png
    ├── heart-empty.png
    ├── game-over.png
    └── digits/
        ├── 0.png
        ├── 1.png
        ├── ...
        └── 9.png
```

Assets should be original, self-created, AI-generated for the project, or properly licensed.

### Done when

The main prototype shapes have been replaced with intended artwork.

---

## v0.9.0 — Sound

### Goal

Add audio feedback.

### Planned sounds

- Coin collection
- Wall collision
- Life lost
- Game Over

### Requirements

- Reasonable volume.
- Avoid uncontrollable sound overlap.
- Use properly licensed audio.

### Done when

Important gameplay actions have appropriate sound feedback.

---

# v1.0.0 — First Complete Release

### Goal

Create the first complete and polished version of Ice Prize Price.

### Required Features

- [ ] Playable ice ball
- [ ] WASD controls
- [ ] Arrow-key controls
- [ ] Android touch controls
- [ ] Diagonal movement
- [ ] Ice physics
- [ ] Acceleration
- [ ] Velocity
- [ ] Friction
- [ ] Maximum speed
- [ ] Wall collision
- [ ] Wall bouncing
- [ ] Temporary wall boost
- [ ] Lives
- [ ] Heart HUD
- [ ] Coins
- [ ] Score
- [ ] Game Over
- [ ] Game restart
- [ ] Custom visual assets
- [ ] Sound effects
- [ ] Stable gameplay

## Definition of Done

The game can be played from start to finish without debug features.

The complete gameplay loop works reliably:

```text
START
  ↓
CONTROL PLAYER
  ↓
FIND COIN
  ↓
COLLECT COIN
  ↓
+ SCORE
  ↓
CONTINUE PLAYING
  ↓
WALL COLLISION
  ↓
-1 LIFE
  ↓
LIVES > 0?
 ↙       ↘
YES       NO
 ↓         ↓
PLAY     GAME OVER
           ↓
        RESTART
```

---

# Future Versions

These features are not required for v1.0.0.

They may be added later if they improve the game.

| Version | Possible Features |
|---|---|
| v1.1.0 | High scores, local save |
| v1.2.0 | Difficulty progression |
| v1.3.0 | Multiple coins, coin values, combos |
| v1.4.0 | Power-ups |
| v1.5.0 | Particles, animations, visual polish |
| v2.0.0 | Levels, obstacles, new environments, game modes |

The game should not become unnecessarily complicated just to increase its version number.

---

# Technical Requirements

## Language

**Python**

## Main Library

**Pygame**

## Dependencies

Keep dependencies minimal.

Initial project should ideally require only:

```text
pygame
```

## Performance

Target:

**60 FPS**

The game should remain lightweight and avoid unnecessary per-frame work.

---

# Current Status

**Current Version:** `v0.1.0`

**Current Goal:** Build the basic playable ice-ball movement prototype.

## v0.1.0 Checklist

- [x] Pygame window
- [x] Ice-like background
- [x] Circle player
- [ ] WASD controls
- [ ] Arrow-key controls
- [x] Android edge-touch controls
- [x] Diagonal movement
- [x] Screen boundary restriction

## Later Features

- [ ] Ice physics
- [ ] Friction
- [ ] Wall bouncing
- [ ] Temporary wall boost
- [ ] Lives
- [ ] Coins
- [ ] Score
- [ ] Game Over
- [ ] Visual assets
- [ ] Sound
- [ ] High score

---

# Versioning

Use:

**MAJOR.MINOR.PATCH**

Examples:

```text
v0.1.0
v0.2.0
v0.3.0
v1.0.0
```

- **MAJOR** — Major redesign or breaking change
- **MINOR** — New gameplay feature
- **PATCH** — Bug fix or small improvement


---

# Final Goal

Build a small arcade game centered around:

```text
Simple controls
      +
Slippery physics
      +
Risky movement
      +
Collectible coins
      +
Limited lives
      =
Ice Prize Price
```

The game should be simple to learn, satisfying to control, and small enough to understand and maintain.

> **Chase the prize. Pay the price.**