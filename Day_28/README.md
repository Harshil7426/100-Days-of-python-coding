## 👉 Day 28 Challenge
# BATTLE GAME
Use Day 27's character generator for this project...to build an automated game battle system!

- Add return functions to your character's health and strength statuses from Day 27's project.
- Generate two different characters and store their data (health and strength stats, character type, name, etc.).
- Use a while True loop to simulate those two characters battling.
- Roll one six-sided dice for both characters. The character who rolls the higher amount wins that round.
- The winner of that round (the one who rolled the higher number) will give damage to the other character by doing the following:
- Find the difference between the strength of both opponents and add one.
- Take that amount away from the loser's health.
- At the end of each round, check the stats of each character to ensure neither of them have died yet.
- When one character dies (they run out of health), declare a winner of the battle!
- To keep this battle from looking hideous between rounds use time.sleep to pause between rounds os.system("clear") to ensure the - screen clears between battles.
- Extra points for the use of emojis, colors, or even sound code!   

Example:
<div style="border: 2px solid #ccc; padding: 10px;border-radius:20px"> 

  ⚔️ BATTLE TIME ⚔️

Name your Legend:
Arthur the Magnificent
Character Type (Human, Elf, Wizard, Orc): 
Elf

Arthur the Magnificent
HEALTH: 13
STRENGTH: 18

Who are they battling?

Name your Legend:
Sheila the Almighty
Character Type (Human, Elf, Wizard, Orc): 
Human

Sheila the Almighty
HEALTH: 40
STRENGTH: 26

*clear screen here*

⚔️ BATTLE TIME ⚔️

The battle begins!

Arthur wins the first blow
Sheila takes a hit, with 8 damage

Arthur the Magnificent
HEALTH: 13

Sheila the Almighty
HEALTH: 32

And they're both standing for the next round!

*clear screen here*

⚔️ BATTLE TIME ⚔️

The battle continues!

Sheila wins round 2
Arthur takes a hit, with 8 damage

Arthur the Magnificent
HEALTH: 5

Sheila the Almighty
HEALTH: 32

And they're both standing for the next round!

*clear screen here*

⚔️ BATTLE TIME ⚔️

The battle continues!

Sheila wins round 3
Arthur takes a hit, with 8 damage

Arthur the Magnificent
HEALTH: -3

Sheila the Almighty
HEALTH: 32

Oh no Arthur the Mighty has died!

Sheila the Almighty destroyed Arthur the Magnificent in 3 rounds!

</div>
