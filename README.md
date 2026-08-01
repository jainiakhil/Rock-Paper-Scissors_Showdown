# 🪨📄✂️ Rock-Paper-Scissors Showdown!

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.1%2B-green.svg)](https://www.pygame.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Welcome to **Rock-Paper-Scissors Showdown!** 💥 An autonomous battle royale simulation built in Python with Pygame, where three legendary factions clash inside an Olympic ring arena until only **ONE** faction remains standing supreme!

![Rock Paper Scissors Simulation Teaser](assets/rps_demo.gif)

> 🎬 **Want to watch the full high-definition trailer?**  
> Check out the complete video showcase: [RPS_Trailer.mp4](file:///d:/Akhil's/Creativity/My%20Work/Coding/Rock%20Paper%20Scissors/RPS_Trailer.mp4)

---

## ⚡ The Battle Mechanics

Inside the ring, 20 **Rocks** 🪨, 20 **Papers** 📄, and 20 **Scissors** ✂️ roam freely under dynamic gravitational and behavioral algorithms:

- 🪨 **Rock** hunts ✂️ **Scissors**, while fleeing from 📄 **Paper**
- 📄 **Paper** hunts 🪨 **Rock**, while fleeing from ✂️ **Scissors**
- ✂️ **Scissors** hunts 📄 **Paper**, while fleeing from 🪨 **Rock**

### 🔄 Conversion & Acceleration
- **Collision Conversion**: When an entity collides with its target, the victim is converted into the attacker's faction!
- **Speed Boost**: As a faction's population shrinks, the remaining survivors gain an exponential speed boost to turn the tide of battle!
- **Wall Bouncing**: Entites bouncing off the ring boundaries get redirected back into the heat of combat.

---

## 🕹️ Quick Start Guide

### Prerequisites
Make sure you have **Python 3.8+** installed on your system.

### 1. Clone & Navigate
```bash
git clone https://github.com/jainiakhil/Rock-Paper-Scissors_Showdown.git
cd Rock-Paper-Scissors_Showdown
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Simulation!
```bash
python main.py
```

---

## 🎮 Controls

| Action | Control |
| :--- | :--- |
| **Exit Simulation** | Press <kbd>ESC</kbd> or click window `X` |

---

## 📜 Project Structure

```
Rock-Paper-Scissors_Showdown/
├── assets/
│   ├── rps_demo.gif          # Teaser GIF preview
│   ├── rock.png              # Rock texture asset
│   ├── paper.png             # Paper texture asset
│   ├── scissors.png          # Scissors texture asset
│   ├── ring.jpg              # Arena background texture
│   ├── ring_border_2_bg.png  # Arena boundary overlay
│   └── olympics_tr.png       # Arena logo
├── main.py                   # Main Pygame simulation loop & physics engine
├── requirements.txt          # Dependencies (pygame)
├── .gitignore                # Git filtering configuration
└── README.md                 # Project documentation
```

---

## 🏆 Credits & Author

Created with ❤️ & Pygame by **Akhil Jaini**.
