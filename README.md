# Ice Prize Price

> **Chase the prize. Pay the price.**

**Ice Prize Price** is a small 2D arcade game made with **Python + Pygame**.

You control an ice ball on a slippery ice floor. Your goal is to collect coins and get the highest score you can.

The catch is simple:

> **Hitting the walls costs you lives.**

The slippery movement makes the game harder to control than a normal movement-based game. You have to think ahead, manage your momentum, and decide how much risk you are willing to take to reach a coin.

## 🎮 Game Logic

The core idea is:

```text
Control the ice ball
        ↓
Slide around the ice
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
Lose a life + bounce
        ↓
Lives remaining?
     ↙       ↘
   YES        NO
    ↓          ↓
Continue    Game Over
               ↓
            Restart
```

The walls are not just boundaries. They are part of the risk/reward system.

A wall collision costs a life, but bouncing from a wall can also give the player a temporary speed boost.

So the player may sometimes choose a risky movement path to reach a prize faster.

That's the main idea behind the name:

> **Chase the prize. Pay the price.**

## 🕹️ Controls

### PC

| Action | Keys |
|---|---|
| Up | `W` / `↑` |
| Down | `S` / `↓` |
| Left | `A` / `←` |
| Right | `D` / `→` |

Diagonal movement is supported.

### Android

The game is planned to use simple screen-edge touch controls:

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

## 🧊 Movement

The player is meant to feel like an object moving on ice.

In the early prototype, movement is direct.

As development continues, the movement will become velocity-based:

```text
Input
  ↓
Acceleration
  ↓
Velocity
  ↓
Position
  ↓
Friction
```

This means the ice ball should continue sliding after the player releases the controls and gradually slow down.

The physics are intended to feel good and predictable rather than perfectly simulate real-world ice.

## 🪙 Risk & Reward

Coins are the main reward.

The player collects coins to increase their score, while walls create the main danger.

This creates a simple decision:

> **How much risk should I take to get the prize?**

The game is not intended to be complicated. Most of the gameplay comes from combining simple controls with slippery movement and risky wall collisions.

## 🛠️ Development

Ice Prize Price is being developed **incrementally, version by version**.

The project starts with the smallest playable prototype and gradually adds the mechanics needed for the complete game.

The planned progression is:

```text
v0.1.0 → Basic movement
    ↓
v0.2.0 → Ice physics
    ↓
v0.3.0 → Walls + bouncing
    ↓
v0.4.0 → Lives
    ↓
v0.5.0 → Coins
    ↓
v0.6.0 → Score
    ↓
v0.7.0 → Game Over
    ↓
v0.8.0 → Visual assets
    ↓
v0.9.0 → Sound
    ↓
v1.0.0 → First complete release
```

Each version should add a meaningful feature while keeping the game playable and understandable.

### Development Goal

The complete development plan, gameplay requirements, version roadmap, technical requirements, and current status are maintained in:

**[`GOAL.md`](docs/GOAL.md)**

`GOAL.md` is the main development reference for the project.

It describes what each version is intended to add and what the project is ultimately trying to become.

## 🎯 v1.0.0

`v1.0.0` is planned to be the **first complete release** of Ice Prize Price.

It is expected to bring the core ideas together:

- Playable ice ball
- Keyboard controls
- Android touch controls
- Slippery ice physics
- Friction and momentum
- Wall bouncing
- Temporary wall boost
- Lives
- Coins
- Score
- Game Over
- Restart
- Custom visual assets
- Sound effects
- Stable gameplay

The exact development requirements and definition of done for `v1.0.0` are maintained in [`GOAL.md`](docs/GOAL.md).

## 🚀 Future Development

After `v1.0.0`, the game may be expanded with features such as:

- High scores
- Difficulty progression
- Multiple coins
- Power-ups
- Particles and visual effects
- Multiple levels
- Obstacles
- New environments
- Additional game modes
- More advanced physics

These are **not part of the initial core game**.

The game should only become bigger when new features actually make it more fun or interesting.

## 💡 Design Philosophy

Ice Prize Price is intentionally designed to stay **small, lightweight, understandable, and fun**.

The goal is not to build a huge game with endless features.

The goal is to make a simple idea work well:

```text
Simple controls
      +
Slippery movement
      +
Risky walls
      +
Collectible prizes
      +
Limited lives
      =
Ice Prize Price
```

> **Chase the prize. Pay the price.**
