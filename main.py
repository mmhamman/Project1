#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "CDC045DF-724E-4E86-A2D1-A374D5E5636A",
  "name": "Butterfly Effect",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631503631401,
  "passages": [
    {
      "name": "Bedroom",
      "tags": "",
      "id": "1",
      "text": "You wake up exhausted from the night before. \n-Too many videogames- \nYou think to yourself but it's ok because it's a Sunday and you have all day ahead of you.\n\n[[NEXT->Bedroom2]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "Bedroom2",
          "original": "[[NEXT->Bedroom2]]"
        }
      ],
      "hooks": [],
      "cleanText": "You wake up exhausted from the night before. \n-Too many videogames- \nYou think to yourself but it's ok because it's a Sunday and you have all day ahead of you."
    },
    {
      "name": "Bedroom2",
      "tags": "",
      "id": "2",
      "text": "You look over at your clock.\n-12:00????-\nYou remember you and your friend Mark were going to the cave to hang out. That would be pretty fun or you could blow him off to play more Life is Weird. It's this cool game you got for your FunStation 4 about your choices and how they affect the story and based on your choices the game will have different outcomes. What was I talking about? Oh yea, what do you wanna do?\n\n[[PLAY->Bedroom3]]\n[[FRIEND->CaveEntrance]]",
      "links": [
        {
          "linkText": "PLAY",
          "passageName": "Bedroom3",
          "original": "[[PLAY->Bedroom3]]"
        },
        {
          "linkText": "FRIEND",
          "passageName": "CaveEntrance",
          "original": "[[FRIEND->CaveEntrance]]"
        }
      ],
      "hooks": [],
      "cleanText": "You look over at your clock.\n-12:00????-\nYou remember you and your friend Mark were going to the cave to hang out. That would be pretty fun or you could blow him off to play more Life is Weird. It's this cool game you got for your FunStation 4 about your choices and how they affect the story and based on your choices the game will have different outcomes. What was I talking about? Oh yea, what do you wanna do?"
    },
    {
      "name": "Bedroom3",
      "tags": "",
      "id": "3",
			"score": -10,
      "text": "Wow you are really lazy I can't believe you picked this option! Don't leave your friend waiting!\n\n[[NEXT->CaveEntrance]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "CaveEntrance",
          "original": "[[NEXT->CaveEntrance]]"
        }
      ],
      "hooks": [],
      "cleanText": "Wow you are really lazy I can't believe you picked this option! Don't leave your friend waiting!"
    },
    {
      "name": "CaveEntrance",
      "tags": "",
      "id": "4",
      "text": "After a bit of a walk, just enough to realize you never had breakfast, you make it to the cave entrance. You see your friend waving. He is slightly taller than you with silver eyes and dark hair.\nFriend: Hey sleepyhead! About time you rolled around! I was getting worried something bad had happened.\nYou: Like what?\nFriend: I don't know maybe your mom did something about your videogame addiction. Were you up late again?\nYou: Guilty.\nYour friend shrugs his shoulders and then motions to the cave entrance. \nFriend: Ready to tackle the cave? My dad always said something was special about this place. Almost as if the cave chose us to be here today rather than ourselves.\nYou: Ugh you're weirding me out come one let's get this over with.\n\n[[ENTER->Cave]]",
      "links": [
        {
          "linkText": "ENTER",
          "passageName": "Cave",
          "original": "[[ENTER->Cave]]"
        }
      ],
      "hooks": [],
      "cleanText": "After a bit of a walk, just enough to realize you never had breakfast, you make it to the cave entrance. You see your friend waving. He is slightly taller than you with silver eyes and dark hair.\nFriend: Hey sleepyhead! About time you rolled around! I was getting worried something bad had happened.\nYou: Like what?\nFriend: I don't know maybe your mom did something about your videogame addiction. Were you up late again?\nYou: Guilty.\nYour friend shrugs his shoulders and then motions to the cave entrance. \nFriend: Ready to tackle the cave? My dad always said something was special about this place. Almost as if the cave chose us to be here today rather than ourselves.\nYou: Ugh you're weirding me out come one let's get this over with."
    },
    {
      "name": "Cave",
      "tags": "",
      "id": "5",
      "text": "You walk into the cave with your friend behind you. The cave is dark and moist. The only light is from the entrance. After hearing your friend's shaky breathing you quickly realize he was hoping you wouldn't have came so he didn't have to go in. After surveying the area you see a faint glimmer in a corner and deeper into the cave their is a ledge.\n\n[[GLIMMER->Glimmer]]\n[[LEDGE->Ledge]]",
      "links": [
        {
          "linkText": "GLIMMER",
          "passageName": "Glimmer",
          "original": "[[GLIMMER->Glimmer]]"
        },
        {
          "linkText": "LEDGE",
          "passageName": "Ledge",
          "original": "[[LEDGE->Ledge]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the cave with your friend behind you. The cave is dark and moist. The only light is from the entrance. After hearing your friend's shaky breathing you quickly realize he was hoping you wouldn't have came so he didn't have to go in. After surveying the area you see a faint glimmer in a corner and deeper into the cave their is a ledge."
    },
    {
      "name": "Glimmer",
      "tags": "",
      "id": "6",
      "text": "You inch closer to the glimmer and see a bottle! It has a note inside do you want to read it?\n\n[[READ->Note]]\n[[BACK->Cave1]]",
      "links": [
        {
          "linkText": "READ",
          "passageName": "Note",
          "original": "[[READ->Note]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Cave1",
          "original": "[[BACK->Cave1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You inch closer to the glimmer and see a bottle! It has a note inside do you want to read it?"
    },
    {
      "name": "Ledge",
      "tags": "",
      "id": "7",
      "text": "You walk towards the ledge and notice there's a giant hole. You try to look deeper inside but see nothing, it's too dark. Maybe if you just got a little closer.... [This will end exploration of this area]\n\n[[BACK->Cave1]]\n[[APPROACH->EndOFLedge]]",
      "links": [
				{
					"linkText": "BACK",
          "passageName": "Cave1",
          "original": "[[BACK->Cave1]]"
				},
				{
					"linkText": "APPROACH",
          "passageName": "EndOFLedge",
          "original": "[[APPROACH->EndOFLedge]]"
				}
			],
      "hooks": [],
      "cleanText": "You walk towards the ledge and notice there's a giant hole. You try to look deeper inside but see nothing, it's too dark. Maybe if you just got a little closer.... [This will end exploration of this area]"
    },
    {
      "name": "Note",
      "tags": "",
      "id": "8",
      "text": "You unfurl the note from inside the bottle after taking it out.\nTo all who read this note: DO NOT GO ANY FURTHER. There is something weird about this cave. From the ledge I could hear talking from deep inside the cave and deep in the hole I could make out silhouettes of inhuman figures, some would call them monsters.\nFriend: OOOo spooky! Are you creeped out? Because I'm not. No sir, not me at all.\n\n[[BACK->Glimmer]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Glimmer",
          "original": "[[BACK->Glimmer]]"
        }
      ],
      "hooks": [],
      "cleanText": "You unfurl the note from inside the bottle after taking it out.\nTo all who read this note: DO NOT GO ANY FURTHER. There is something weird about this cave. From the ledge I could hear talking from deep inside the cave and deep in the hole I could make out silhouettes of inhuman figures, some would call them monsters.\nFriend: OOOo spooky! Are you creeped out? Because I'm not. No sir, not me at all."
    },
    {
      "name": "Cave1",
      "tags": "",
      "id": "9",
      "text": "Friend: You're not leaving yet are you? You are staying here and if you want to leave let me go first please. I gotta.... make sure it's safe.\n\n[[GLIMMER->Glimmer]]\n[[LEDGE->Ledge]]",
      "links": [
        {
          "linkText": "GLIMMER",
          "passageName": "Glimmer",
          "original": "[[GLIMMER->Glimmer]]"
        },
        {
          "linkText": "LEDGE",
          "passageName": "Ledge",
          "original": "[[LEDGE->Ledge]]"
        }
      ],
      "hooks": [],
      "cleanText": "Friend: You're not leaving yet are you? You are staying here and if you want to leave let me go first please. I gotta.... make sure it's safe."
    },
    {
      "name": "EndOFLedge",
      "tags": "",
      "id": "10",
      "text": "You peer over the ledge and look deeper and deeper into the hole. You notice two little jewel like glimmers shine and then-\nHUH?? They moved! \nFriend: Did you see that??\nUnknown: Want a closer look?\nAs soon as you hear that somewhat familiar but unidentifiable voice you also hear your friend let out a giant scream. He was pushed off the ledge.\nUnknown: H-hey! What are you doing here?\nYou also get pushed off by the mysterious figure.\n\n[[NEXT->BottomOfHole]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "BottomOfHole",
          "original": "[[NEXT->BottomOfHole]]"
        }
      ],
      "hooks": [],
      "cleanText": "You peer over the ledge and look deeper and deeper into the hole. You notice two little jewel like glimmers shine and then-\nHUH?? They moved! \nFriend: Did you see that??\nUnknown: Want a closer look?\nAs soon as you hear that somewhat familiar but unidentifiable voice you also hear your friend let out a giant scream. He was pushed off the ledge.\nUnknown: H-hey! What are you doing here?\nYou also get pushed off by the mysterious figure."
    },
    {
      "name": "BottomOfHole",
      "tags": "",
      "id": "11",
      "text": "???: Hey bud are you ok?\nYou slowly get up. You look beneath your feet and see a patch of flowers blocked your fall. upon examining your surroundings you see a dark figure.\n???: You can talk right?\nThe dark figure gets closer and you finally can identify it. It's a monster! Scaly and blue with horns! Yellow glowing eyes peer into your soul. What are you going to do?\n\n[[ATTACK->BottomOfHoleAttack]]\n[[TALK->BottomOfHoleTalk]]",
      "links": [
        {
          "linkText": "ATTACK",
          "passageName": "BottomOfHoleAttack",
          "original": "[[ATTACK->BottomOfHoleAttack]]"
        },
        {
          "linkText": "TALK",
          "passageName": "BottomOfHoleTalk",
          "original": "[[TALK->BottomOfHoleTalk]]"
        }
      ],
      "hooks": [],
      "cleanText": "???: Hey bud are you ok?\nYou slowly get up. You look beneath your feet and see a patch of flowers blocked your fall. upon examining your surroundings you see a dark figure.\n???: You can talk right?\nThe dark figure gets closer and you finally can identify it. It's a monster! Scaly and blue with horns! Yellow glowing eyes peer into your soul. What are you going to do?"
    },
    {
      "name": "BottomOfHoleAttack",
      "tags": "",
      "id": "12",
      "text": "You throw a swift punch and knock the monster to the ground.\n???: Nice t-to m-meet you too pal.\nThe monster slowly gets up using it's long sharp claws.\n???: I just want to talk.\nYou think about it for a second and decide it would be too socially awkward to run away because he's such a nice guy.\nWilbur: I'm Wilber. I've already met your sidehook but I want to know more about you like your name.\nYou tell Wilbur your name and he steps back and thinks for a second.\nWilbur: I'll call you Slippy after my brother's favorite videogame character and that sick barrel roll you did off the ledge up there!\n\n[[NEXT->BottomOfHole1]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "BottomOfHole1",
          "original": "[[NEXT->BottomOfHole1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You throw a swift punch and knock the monster to the ground.\n???: Nice t-to m-meet you too pal.\nThe monster slowly gets up using it's long sharp claws.\n???: I just want to talk.\nYou think about it for a second and decide it would be too socially awkward to run away because he's such a nice guy.\nWilbur: I'm Wilber. I've already met your sidehook but I want to know more about you like your name.\nYou tell Wilbur your name and he steps back and thinks for a second.\nWilbur: I'll call you Slippy after my brother's favorite videogame character and that sick barrel roll you did off the ledge up there!"
    },
    {
      "name": "BottomOfHoleTalk",
      "tags": "",
      "id": "13",
      "text": "You: H-hi\n???: Do you have a lot of friends in school? You don't seem very extroverted.\nYou: I fell off the ledge.\n???: I'm near sighted, but I'm not blind you fell right in front of me. Where are my manners??\nYou: I don't know did you check your pockets?\nHe gives you a weird look because your pun wasn't funny and you kinda regret not punching him.\nWilbur: My name's Wilbur. We'll work on whatever that was. Anyways, how does the name Slippy sound? I got my inspiration from that sick barrel roll you did down the slope.\n\n[[NEXT->BottomOfHole1]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "BottomOfHole1",
          "original": "[[NEXT->BottomOfHole1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You: H-hi\n???: Do you have a lot of friends in school? You don't seem very extroverted.\nYou: I fell off the ledge.\n???: I'm near sighted, but I'm not blind you fell right in front of me. Where are my manners??\nYou: I don't know did you check your pockets?\nHe gives you a weird look because your pun wasn't funny and you kinda regret not punching him.\nWilbur: My name's Wilbur. We'll work on whatever that was. Anyways, how does the name Slippy sound? I got my inspiration from that sick barrel roll you did down the slope."
    },
    {
      "name": "BottomOfHole1",
      "tags": "",
      "id": "14",
      "text": "-Slippy-\nYou slowly collect your thoughts and you remember everything.\nYou: Wait! Did anyone else fall down here?\nWilbur: Nope, just you Slippy\nYou: I was with a friend of mine and we fell down the hole. I guess we fell down different passages.\nWilbur: I should've known you came from above ground since you are a human. We look so different.\nYou examine his scaly body noting his tail and claws and horns and glowing yellow eyes. They remind you of what you saw when you peered into the hole. \nWilbur: I'm afraid there's only one way back up. Through the demon king's castle.\nYou: D-demon king??\nWilbur: Oh he's a total softy. He doesn't take too kindly to humans though so I guess your fear is justified.\n\n[[NEXT->BottomOfHole2]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "BottomOfHole2",
          "original": "[[NEXT->BottomOfHole2]]"
        }
      ],
      "hooks": [],
      "cleanText": "-Slippy-\nYou slowly collect your thoughts and you remember everything.\nYou: Wait! Did anyone else fall down here?\nWilbur: Nope, just you Slippy\nYou: I was with a friend of mine and we fell down the hole. I guess we fell down different passages.\nWilbur: I should've known you came from above ground since you are a human. We look so different.\nYou examine his scaly body noting his tail and claws and horns and glowing yellow eyes. They remind you of what you saw when you peered into the hole. \nWilbur: I'm afraid there's only one way back up. Through the demon king's castle.\nYou: D-demon king??\nWilbur: Oh he's a total softy. He doesn't take too kindly to humans though so I guess your fear is justified."
    },
    {
      "name": "BottomOfHole2",
      "tags": "",
      "id": "15",
      "text": "Wilbur: I can tell this is a lot to process but I'll help you out I made a promise to an old friend that I would help little guys like you. I'll teach you how to survive out here. \nYou breath a sigh of relief. All you need now is to find your friend and Wilbur will help you guys out.\nWilbur: My first bit of advice is this. Even though I'm a nice guy, others don't share my views. Whether you CHOOSE to fight off these types of monsters or befriend them is up to you, just remember, your choices have consequences. Now come on don't be shy I'm your official tour guide to the realm of monsters!\n\n[[NEXT->MushroomForest]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "MushroomForest",
          "original": "[[NEXT->MushroomForest]]"
        }
      ],
      "hooks": [],
      "cleanText": "Wilbur: I can tell this is a lot to process but I'll help you out I made a promise to an old friend that I would help little guys like you. I'll teach you how to survive out here. \nYou breath a sigh of relief. All you need now is to find your friend and Wilbur will help you guys out.\nWilbur: My first bit of advice is this. Even though I'm a nice guy, others don't share my views. Whether you CHOOSE to fight off these types of monsters or befriend them is up to you, just remember, your choices have consequences. Now come on don't be shy I'm your official tour guide to the realm of monsters!"
    },
    {
      "name": "MushroomForest",
      "tags": "",
      "id": "16",
      "text": "You follow Wilbur though some tight fitting caves and pop out of a huge expanse. It's a forrest but instead of trees it's... mushrooms? I guess it is still a cave after all but taking a deep breath in it feels like fresh air.\nWilbur: This is Mushroom Forrest! If you wanna see my house we can go down that path or if you hate sidequests and fun, we can go straight ahead.\n\n[[PATH->House]]\n[[STRAIGHT->MushroomForestExit]]",
      "links": [
        {
          "linkText": "PATH",
          "passageName": "House",
          "original": "[[PATH->House]]"
        },
        {
          "linkText": "STRAIGHT",
          "passageName": "MushroomForestExit",
          "original": "[[STRAIGHT->MushroomForestExit]]"
        }
      ],
      "hooks": [],
      "cleanText": "You follow Wilbur though some tight fitting caves and pop out of a huge expanse. It's a forrest but instead of trees it's... mushrooms? I guess it is still a cave after all but taking a deep breath in it feels like fresh air.\nWilbur: This is Mushroom Forrest! If you wanna see my house we can go down that path or if you hate sidequests and fun, we can go straight ahead."
    },
    {
      "name": "House",
      "tags": "",
      "id": "17",
      "text": "You walk down the path and approach a log-uh I mean mushroom..? cabin. Wilbur skips up to the door and knocks comically loud and fast. You hear a mysterious unknown voice scream at the top of it's lungs.\nWilbur: Uh oh gotta go.\nHe quickly opens the door which apparently was unlocked and he runs inside. You can't chase him fast enough and end up alone in his living room.\n\n[[NEXT->HouseLiving]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "HouseLiving",
          "original": "[[NEXT->HouseLiving]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk down the path and approach a log-uh I mean mushroom..? cabin. Wilbur skips up to the door and knocks comically loud and fast. You hear a mysterious unknown voice scream at the top of it's lungs.\nWilbur: Uh oh gotta go.\nHe quickly opens the door which apparently was unlocked and he runs inside. You can't chase him fast enough and end up alone in his living room."
    },
    {
      "name": "HouseLiving",
      "tags": "",
      "id": "18",
      "text": "You see a kitchen/dining room to your front and on the side there are 2 doors. One is slightly ajar to the right and the other to the left has a bunch of signs that say no entry and a-what is that?-banana..? nailed to the door. \n\n[[KITCHEN->Kitchen]]\n[[RIGHT->OrvilleRoom]]\n[[LEFT->Knock]]",
      "links": [
        {
          "linkText": "KITCHEN",
          "passageName": "Kitchen",
          "original": "[[KITCHEN->Kitchen]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "OrvilleRoom",
          "original": "[[RIGHT->OrvilleRoom]]"
        },
        {
          "linkText": "LEFT",
          "passageName": "Knock",
          "original": "[[LEFT->Knock]]"
        }
      ],
      "hooks": [],
      "cleanText": "You see a kitchen/dining room to your front and on the side there are 2 doors. One is slightly ajar to the right and the other to the left has a bunch of signs that say no entry and a-what is that?-banana..? nailed to the door."
    },
    {
      "name": "Kitchen",
      "tags": "",
      "id": "19",
      "text": "You walk into the kitchen/dining room area and immediately spot a bunch of bananas on the counter and table. Only heaven knows what's in the fridge, probably more bananas. Maybe check out what's in that room with the open door?\n\n[[BACK->HouseLiving]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "HouseLiving",
          "original": "[[BACK->HouseLiving]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the kitchen/dining room area and immediately spot a bunch of bananas on the counter and table. Only heaven knows what's in the fridge, probably more bananas. Maybe check out what's in that room with the open door?"
    },
    {
      "name": "OrvilleRoom",
      "tags": "",
      "id": "20",
      "text": "You slowly appraoch the open door and see a shadowy figure inside. You walk into the room and before you can introduce yourself, the shadowy figure lunges at you.\n???: I'll kill you!\nYou let out a scream and before you can have your life flash before your eyes the figure stops.\n???: Ew. What are you cosplaying as, a human?\nYou: Uh, I am a human?\nThe figure stares at you in horror. While he is in shock you examine him and realize he looks very similar to Wilbur taller and red. This must be his brother.\nWilbur: Hey Orville, this is my new friend.\nOrville: YOU BROUGHT A HUMAN HOME?\nWibur: Well technically he chose to come here of his own volition so I followed him while walking in front of him.\n\n[[NEXT->OrvilleRoom1]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "OrvilleRoom1",
          "original": "[[NEXT->OrvilleRoom1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You slowly appraoch the open door and see a shadowy figure inside. You walk into the room and before you can introduce yourself, the shadowy figure lunges at you.\n???: I'll kill you!\nYou let out a scream and before you can have your life flash before your eyes the figure stops.\n???: Ew. What are you cosplaying as, a human?\nYou: Uh, I am a human?\nThe figure stares at you in horror. While he is in shock you examine him and realize he looks very similar to Wilbur taller and red. This must be his brother.\nWilbur: Hey Orville, this is my new friend.\nOrville: YOU BROUGHT A HUMAN HOME?\nWibur: Well technically he chose to come here of his own volition so I followed him while walking in front of him."
    },
    {
      "name": "Knock",
      "tags": "",
      "id": "21",
      "text": "You knock on the door carefully avoiding the banana and you hear a lot of fumbling around but inevitably no one answers. You roll your eyes as you realize this is Wilbur's room and he's probably cleaning it because he didn't expect you to try this sidequest.\n\n[[BACK->HouseLiving]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "HouseLiving",
          "original": "[[BACK->HouseLiving]]"
        }
      ],
      "hooks": [],
      "cleanText": "You knock on the door carefully avoiding the banana and you hear a lot of fumbling around but inevitably no one answers. You roll your eyes as you realize this is Wilbur's room and he's probably cleaning it because he didn't expect you to try this sidequest."
    },
    {
      "name": "OrvilleRoom1",
      "tags": "",
      "id": "22",
      "text": "Orville: I'm going to throw up. The demon king is going to kill us.\nWilbur: Nah he's a big softy. Well except to humans so I guess your fear is justified.\nYou roll your eyes as you figure out just exactly what it means to be a human in a monster's world.\nOrville: What do you even plan to do with him? He sticks out like a sore thumb.\nWilbur: I was looking for my banana costume but SOMEONE took it.\nYou: How many bananas do you have?\nWilbur: There was a sale at the banana store, I couldn't resist.\nOrville: Did you check in your closet?\nWilbur: No? That's where I keep all my banana-related clothing, why would it be in there.\nYou let out a light chuckle and when Wilbur gives you another weird look like before and you realize he was being serious.\nWilbur: Also I'm taking him to the demon king to let him back to human world.\nOrville grows pale. \nOrville: No, I'm gonna report him. We can't risk this again you are lucky you came away with your head when you-know-what happened.\nWilbur: Plllllllleeeeeaaaasssseee. I'll give you a banana if you don't.\nYou look around as Orville reaches for his phone. You spot a sword and realize this is your moment. You can attack him or try to convince him to not report you. What will you do?\n\n[[TALK->OrvilleRoomTalk]]\n[[ATTACK->OrvilleRoomAttack]]",
      "links": [
        {
          "linkText": "TALK",
          "passageName": "OrvilleRoomTalk",
          "original": "[[TALK->OrvilleRoomTalk]]"
        },
        {
          "linkText": "ATTACK",
          "passageName": "OrvilleRoomAttack",
          "original": "[[ATTACK->OrvilleRoomAttack]]"
        }
      ],
      "hooks": [],
      "cleanText": "Orville: I'm going to throw up. The demon king is going to kill us.\nWilbur: Nah he's a big softy. Well except to humans so I guess your fear is justified.\nYou roll your eyes as you figure out just exactly what it means to be a human in a monster's world.\nOrville: What do you even plan to do with him? He sticks out like a sore thumb.\nWilbur: I was looking for my banana costume but SOMEONE took it.\nYou: How many bananas do you have?\nWilbur: There was a sale at the banana store, I couldn't resist.\nOrville: Did you check in your closet?\nWilbur: No? That's where I keep all my banana-related clothing, why would it be in there.\nYou let out a light chuckle and when Wilbur gives you another weird look like before and you realize he was being serious.\nWilbur: Also I'm taking him to the demon king to let him back to human world.\nOrville grows pale. \nOrville: No, I'm gonna report him. We can't risk this again you are lucky you came away with your head when you-know-what happened.\nWilbur: Plllllllleeeeeaaaasssseee. I'll give you a banana if you don't.\nYou look around as Orville reaches for his phone. You spot a sword and realize this is your moment. You can attack him or try to convince him to not report you. What will you do?"
    },
    {
      "name": "OrvilleRoomTalk",
      "tags": "",
      "id": "23",
			"score": 10,
      "text": "You: Please don't report me!\nOrville pasuses. \nOrville: Why?\nYou: I uh, didn't think I'd get this far.\nEveryone is confused as you let out an embarrassing chuckle.\nWilbur: I made a promise to help Slippy so I will.\nOrville: You named it??\nOrville sighs and sits next to a pile of swords.\nWilbur: Come one bro, all you have to do is sit here and keep practicing for the royal guard. My actions don't effect you we're monsters, not humans.\nYou feel slightly insulted now but relieved as talking seems to have worked.\nWilbur: Come on slippy, let's get you home.\nOrville: You better come home tonight!\nAs Wilbur motions you to leave he hugs Orville and whispers something to him. I think it's time to leave.\n\n[[BACK->HouseLeave]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "HouseLeave",
          "original": "[[BACK->HouseLeave]]"
        }
      ],
      "hooks": [],
      "cleanText": "You: Please don't report me!\nOrville pasuses. \nOrville: Why?\nYou: I uh, didn't think I'd get this far.\nEveryone is confused as you let out an embarrassing chuckle.\nWilbur: I made a promise to help Slippy so I will.\nOrville: You named it??\nOrville sighs and sits next to a pile of swords.\nWilbur: Come one bro, all you have to do is sit here and keep practicing for the royal guard. My actions don't effect you we're monsters, not humans.\nYou feel slightly insulted now but relieved as talking seems to have worked.\nWilbur: Come on slippy, let's get you home.\nOrville: You better come home tonight!\nAs Wilbur motions you to leave he hugs Orville and whispers something to him. I think it's time to leave."
    },
    {
      "name": "OrvilleRoomAttack",
      "tags": "",
      "id": "24",
			"score": -10,
      "text": "You grab the sword and lunge at Orville as he did you. This time, however, you didn't stop. As you swing Orville vanishes out of thin air. Is this how monsters die?\nWilbur: Why did you do that?\nYou: I had to! He was gonna report me!\nWilbur sighs and motions you to follow him.\nWilbur: Come on Slippy, we need to go.\nIt's almost frustrating how little he cares about his own brother to just walk away like that.\nWilbur: Must one of those kinda runs.\n\n[[FOLLOW->MushroomForestExitEvil]]",
      "links": [
        {
          "linkText": "FOLLOW",
          "passageName": "MushroomForestExitEvil",
          "original": "[[FOLLOW->MushroomForestExitEvil]]"
        }
      ],
      "hooks": [],
      "cleanText": "You grab the sword and lunge at Orville as he did you. This time, however, you didn't stop. As you swing Orville vanishes out of thin air. Is this how monsters die?\nWilbur: Why did you do that?\nYou: I had to! He was gonna report me!\nWilbur sighs and motions you to follow him.\nWilbur: Come on Slippy, we need to go.\nIt's almost frustrating how little he cares about his own brother to just walk away like that.\nWilbur: Must one of those kinda runs."
    },
    {
      "name": "MushroomForestExitEvil",
      "tags": "",
      "id": "25",
      "text": "You and Wilbur share a quiet tense walk over to the next destination. You look ahead and notice a gate.\nWilbur: 2,000 years ago, humans and monsters lived together. Monsters have certain qualities that humans find repulsive and the monsters that humans couldn't tame like dogs simply got thrown into this prison. Ever since then the royal family keeps all monsters in here lest the humans return to exact their revenge.\nYou think for a moment as you desperately want to show him humans aren't all like that but you are more of a monster than him.\nWilbur: I guess I understand why now.\nYou: You don't have to help me.\nWilbur gets frustrated.\nWilbur: Yes I do, I made a promise.\n\n[[NEXT->CastleGatesEvil]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "CastleGatesEvil",
          "original": "[[NEXT->CastleGatesEvil]]"
        }
      ],
      "hooks": [],
      "cleanText": "You and Wilbur share a quiet tense walk over to the next destination. You look ahead and notice a gate.\nWilbur: 2,000 years ago, humans and monsters lived together. Monsters have certain qualities that humans find repulsive and the monsters that humans couldn't tame like dogs simply got thrown into this prison. Ever since then the royal family keeps all monsters in here lest the humans return to exact their revenge.\nYou think for a moment as you desperately want to show him humans aren't all like that but you are more of a monster than him.\nWilbur: I guess I understand why now.\nYou: You don't have to help me.\nWilbur gets frustrated.\nWilbur: Yes I do, I made a promise."
    },
    {
      "name": "HouseLeave",
      "tags": "",
      "id": "26",
      "text": "You follow Wilbur out of the house and wave bye to Orville who is smiling and waving back. I think you made a friend.\nWilbur: How was that little sidequest? Fun right? Let's go back on the path to the castle.\n\n[[NEXT->MushroomForestExit]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "MushroomForestExit",
          "original": "[[NEXT->MushroomForestExit]]"
        }
      ],
      "hooks": [],
      "cleanText": "You follow Wilbur out of the house and wave bye to Orville who is smiling and waving back. I think you made a friend.\nWilbur: How was that little sidequest? Fun right? Let's go back on the path to the castle."
    },
    {
      "name": "MushroomForestExit",
      "tags": "",
      "id": "27",
      "text": "You go straight through the forest and after a bit of walking you see large gates.\nWilbur: These are the castle gates. There's a town and then inside the castle there is a staircase that leads straight to the human world.\nYou: Maybe I can show you my world and my house!\nWilbur: Heh I wish. Everyone knows monsters were banished to this underground world. \nYou: What?\nWilbur: 2,000 years ago, humans and monsters lived together. Monsters have certain qualities that humans find repulsive and the monsters that humans couldn't tame like dogs simply got thrown into this prison. Ever since then the royal family keeps all monsters in here lest the humans return to exact their revenge. You don't seem so bad though.\nYou: That's crazy I never knew any of that?\nWilbur: That surprising. Maybe that's why Harry got out so easily.\nYou: Harry?\nWilbur: Oh yea he was this real tall monkey looking like creature, he had huge feet.\nYou: Bigfoot?\nWilbur: hehe that's what we called him in gradeschool how did you know?\nYou: Just uh guessing...\n\n[[NEXT->CastleGates]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "CastleGates",
          "original": "[[NEXT->CastleGates]]"
        }
      ],
      "hooks": [],
      "cleanText": "You go straight through the forest and after a bit of walking you see large gates.\nWilbur: These are the castle gates. There's a town and then inside the castle there is a staircase that leads straight to the human world.\nYou: Maybe I can show you my world and my house!\nWilbur: Heh I wish. Everyone knows monsters were banished to this underground world. \nYou: What?\nWilbur: 2,000 years ago, humans and monsters lived together. Monsters have certain qualities that humans find repulsive and the monsters that humans couldn't tame like dogs simply got thrown into this prison. Ever since then the royal family keeps all monsters in here lest the humans return to exact their revenge. You don't seem so bad though.\nYou: That's crazy I never knew any of that?\nWilbur: That surprising. Maybe that's why Harry got out so easily.\nYou: Harry?\nWilbur: Oh yea he was this real tall monkey looking like creature, he had huge feet.\nYou: Bigfoot?\nWilbur: hehe that's what we called him in gradeschool how did you know?\nYou: Just uh guessing..."
    },
    {
      "name": "CastleGates",
      "tags": "",
      "id": "28",
      "text": "You walk through 2 large doors and walk into a town with all different kinds of monsters. Some large and hairy and others small and slimy. A parade of skeletons dances by and before you can question how that's even possible Wilbur darts past you.\nWilbur: They're having a banana sale at the banana store!\nYou let out a sigh and wonder how many more times this will happen. You see a grandious door which is being guarded by a rather large goblin. You contemplate waiting for Wilbur but he looks pretty absorbed in the bananas because he's a bad guide. You are a decent guy why not try mingling with the skeletons?\n\n[[BANANA->BananaStore]]\n[[GOBLIN->Door]]\n[[TALK->Skeleton]]",
      "links": [
        {
          "linkText": "BANANA",
          "passageName": "BananaStore",
          "original": "[[BANANA->BananaStore]]"
        },
        {
          "linkText": "GOBLIN",
          "passageName": "Door",
          "original": "[[GOBLIN->Door]]"
        },
        {
          "linkText": "TALK",
          "passageName": "Skeleton",
          "original": "[[TALK->Skeleton]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk through 2 large doors and walk into a town with all different kinds of monsters. Some large and hairy and others small and slimy. A parade of skeletons dances by and before you can question how that's even possible Wilbur darts past you.\nWilbur: They're having a banana sale at the banana store!\nYou let out a sigh and wonder how many more times this will happen. You see a grandious door which is being guarded by a rather large goblin. You contemplate waiting for Wilbur but he looks pretty absorbed in the bananas because he's a bad guide. You are a decent guy why not try mingling with the skeletons?"
    },
    {
      "name": "CastleGatesEvil",
      "tags": "",
      "id": "29",
      "text": "You walk through two huge gates. It's a ghost town. Not a single person. You breath a sigh of relief as you don't want to have to kill more monsters.\nWilbur: Here we are Slippy. Why don't you explore for a little bit. I'll wait for you by the castle gates.\n\n[[NEXT->Town]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "Town",
          "original": "[[NEXT->Town]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk through two huge gates. It's a ghost town. Not a single person. You breath a sigh of relief as you don't want to have to kill more monsters.\nWilbur: Here we are Slippy. Why don't you explore for a little bit. I'll wait for you by the castle gates."
    },
    {
      "name": "BananaStore",
      "tags": "",
      "id": "30",
      "text": "You approach the banana store and peer inside. Wilbur has more bananas than he can hold. He's gonna be there for awhile.\n\n[[BACK->CastleGate1]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "CastleGate1",
          "original": "[[BACK->CastleGate1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You approach the banana store and peer inside. Wilbur has more bananas than he can hold. He's gonna be there for awhile."
    },
    {
      "name": "Door",
      "tags": "",
      "id": "31",
      "text": "You approach the door and the large goblin steps forward.\nGoblin: What business do you have here?\nYou: I wish to speak to the demon king.\nGoblin: Hehe you must have a deathwish to see him dressed as a human.\nYou: I am a human.\nThe Goblin stands there in awe for a second.\nGoblin: Ok so I'm gonna radio my supervisor I'm not sure how to handle this kind of situation.\nYou: By all means, I would hate to make you job harder.\nYou and the goblin exchange an awkward forced smile as he walks off to get his radio.\n\n[[NEXT->Door1]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "Door1",
          "original": "[[NEXT->Door1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You approach the door and the large goblin steps forward.\nGoblin: What business do you have here?\nYou: I wish to speak to the demon king.\nGoblin: Hehe you must have a deathwish to see him dressed as a human.\nYou: I am a human.\nThe Goblin stands there in awe for a second.\nGoblin: Ok so I'm gonna radio my supervisor I'm not sure how to handle this kind of situation.\nYou: By all means, I would hate to make you job harder.\nYou and the goblin exchange an awkward forced smile as he walks off to get his radio."
    },
    {
      "name": "Skeleton",
      "tags": "",
      "id": "32",
      "text": "You approach the skeletons.\nYou: Did you know skeletons get extremely lonely becuase they have no body?\nThe skeletons look at eachother and whisper a bit and look back at you angry.\nSkeleton 1: That's really messed up dude.\nSkeleton 2: Yea where are your friends meatbag??\nSkeleton 3: What a jerk dude. Now I don't want to go to the bonequet.\nSkeleton 1: Don't mind him amigo, he probably has some sort of bone deformity to make him look like that.\nYou feel more insulted than them but because you were the aggressor you sulk away.\n\n[[BACK->CastleGate1]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "CastleGate1",
          "original": "[[BACK->CastleGate1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You approach the skeletons.\nYou: Did you know skeletons get extremely lonely becuase they have no body?\nThe skeletons look at eachother and whisper a bit and look back at you angry.\nSkeleton 1: That's really messed up dude.\nSkeleton 2: Yea where are your friends meatbag??\nSkeleton 3: What a jerk dude. Now I don't want to go to the bonequet.\nSkeleton 1: Don't mind him amigo, he probably has some sort of bone deformity to make him look like that.\nYou feel more insulted than them but because you were the aggressor you sulk away."
    },
    {
      "name": "CastleGate1",
      "tags": "",
      "id": "33",
      "text": "Banana store, gate guarded by a goblin, or mingle with the skeletons?\n\n[[BANANA->BananaStore]]\n[[GOBLIN->Door]]\n[[TALK->Skeleton]]",
      "links": [
        {
          "linkText": "BANANA",
          "passageName": "BananaStore",
          "original": "[[BANANA->BananaStore]]"
        },
        {
          "linkText": "GOBLIN",
          "passageName": "Door",
          "original": "[[GOBLIN->Door]]"
        },
        {
          "linkText": "TALK",
          "passageName": "Skeleton",
          "original": "[[TALK->Skeleton]]"
        }
      ],
      "hooks": [],
      "cleanText": "Banana store, gate guarded by a goblin, or mingle with the skeletons?"
    },
    {
      "name": "Door1",
      "tags": "",
      "id": "34",
      "text": "After awhile the goblin lumbers back.\nGoblin: Ok so I talked to my manager and I have to kill you.\nYou: Ah ok understandable- Wait what??\nGoblin: Sorry, company policy. You seem like a nice guy but I have a real shot at grunt manager and this will really boost my chances.\nYou: Please don't hurt me!\nGoblin: Wow you really are a human. Us goblins are really weak, we attack in gameshow trivia. If you lose you die.\nYou: Why do you guard doors then?\nGoblin: Listen pal, I don't make the rules. Get ready for Jeopardy!\n\n[[NEXT->Question1]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "Question1",
          "original": "[[NEXT->Question1]]"
        }
      ],
      "hooks": [],
      "cleanText": "After awhile the goblin lumbers back.\nGoblin: Ok so I talked to my manager and I have to kill you.\nYou: Ah ok understandable- Wait what??\nGoblin: Sorry, company policy. You seem like a nice guy but I have a real shot at grunt manager and this will really boost my chances.\nYou: Please don't hurt me!\nGoblin: Wow you really are a human. Us goblins are really weak, we attack in gameshow trivia. If you lose you die.\nYou: Why do you guard doors then?\nGoblin: Listen pal, I don't make the rules. Get ready for Jeopardy!"
    },
    {
      "name": "Question1",
      "tags": "",
      "id": "35",
      "text": "Goblin: Question 1! Which US president delivered the Gettysberg address?\nA: George Washington\nB: Abraham Lincoln\nC: Betty White (It's gonna happen)\nD: Barack Obama\nYou: How would you even know this?\nGoblin: Don't think about it!\n\n[[A->Death]]\n[[B->Question2]]\n[[C->Death]]\n[[D->Death]]",
      "links": [
        {
          "linkText": "A",
          "passageName": "Death",
          "original": "[[A->Death]]"
        },
        {
          "linkText": "B",
          "passageName": "Question2",
          "original": "[[B->Question2]]"
        },
        {
          "linkText": "C",
          "passageName": "Death",
          "original": "[[C->Death]]"
        },
        {
          "linkText": "D",
          "passageName": "Death",
          "original": "[[D->Death]]"
        }
      ],
      "hooks": [],
      "cleanText": "Goblin: Question 1! Which US president delivered the Gettysberg address?\nA: George Washington\nB: Abraham Lincoln\nC: Betty White (It's gonna happen)\nD: Barack Obama\nYou: How would you even know this?\nGoblin: Don't think about it!"
    },
    {
      "name": "Death",
      "tags": "",
      "id": "36",
			"score": -1,
      "text": "You died! Respawn?\n\n[[RESPAWN->Door1]]",
      "links": [
        {
          "linkText": "RESPAWN",
          "passageName": "Door1",
          "original": "[[RESPAWN->Door1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You died! Respawn?"
    },
    {
      "name": "Question2",
      "tags": "",
      "id": "37",
			"score": 10,
      "text": "Goblin: Question 2! How long does a day last on Uranus?\nA: 17 Hours\nB: 24 Hours (duh!)\nC: 3 times as long as a day on mercury\nD: A year\nYou: You guys know about Uranus??\n\n[[A->Question3]]\n[[B->Death]]\n[[C->Death]]\n[[D->Death]]",
      "links": [
        {
          "linkText": "A",
          "passageName": "Question3",
          "original": "[[A->Question3]]"
        },
        {
          "linkText": "B",
          "passageName": "Death",
          "original": "[[B->Death]]"
        },
        {
          "linkText": "C",
          "passageName": "Death",
          "original": "[[C->Death]]"
        },
        {
          "linkText": "D",
          "passageName": "Death",
          "original": "[[D->Death]]"
        }
      ],
      "hooks": [],
      "cleanText": "Goblin: Question 2! How long does a day last on Uranus?\nA: 17 Hours\nB: 24 Hours (duh!)\nC: 3 times as long as a day on mercury\nD: A year\nYou: You guys know about Uranus??"
    },
    {
      "name": "Question3",
      "tags": "",
      "id": "38",
			"score": 10,
      "text": "Goblin: Ok nerd, here's one you can't google!\nGoblin: Question 3! What's the demon king's real name?\nA: Matthew\nB: Jason\nC: Markus\nD: Alexander\nYou: How am I supposed to know that??\nGoblin: Hehe sounds like I'm about to become a manager.\n\n[[A->Death]]\n[[B->Death]]\n[[C->Goblin]]\n[[D->Death]]",
      "links": [
        {
          "linkText": "A",
          "passageName": "Death",
          "original": "[[A->Death]]"
        },
        {
          "linkText": "B",
          "passageName": "Death",
          "original": "[[B->Death]]"
        },
        {
          "linkText": "C",
          "passageName": "Goblin",
          "original": "[[C->Goblin]]"
        },
        {
          "linkText": "D",
          "passageName": "Death",
          "original": "[[D->Death]]"
        }
      ],
      "hooks": [],
      "cleanText": "Goblin: Ok nerd, here's one you can't google!\nGoblin: Question 3! What's the demon king's real name?\nA: Matthew\nB: Jason\nC: Markus\nD: Alexander\nYou: How am I supposed to know that??\nGoblin: Hehe sounds like I'm about to become a manager."
    },
    {
      "name": "Goblin",
      "tags": "",
      "id": "39",
			"score": 10,
      "text": "Goblin: You jerk! You just kept dying and guessing!\nYou: No I didn't I just know someone else with that name!\nGoblin: Ahhhh you are clearly superior you will be my boss one day my 5th grade teacher was riiiiiigggghhhtttttt. . ..\nThe goblin stumbles around in faux agony and then hides behind a bush.\nGoblin: Wait! I'll just take you to the demon king and get the reward from the head honcho! I'll be famous!\nYou: No don't!\nYou think back to your earlier conversation. If he's that weak you can take him. Wanna try?\n\n[[FIGHT->GoblinEvil]]\n[[TAlK->GoblinGood]]",
      "links": [
        {
          "linkText": "FIGHT",
          "passageName": "GoblinEvil",
          "original": "[[FIGHT->GoblinEvil]]"
        },
        {
          "linkText": "TALK",
          "passageName": "GoblinGood",
          "original": "[[TALK->GoblinGood]]"
        }
      ],
      "hooks": [],
      "cleanText": "Goblin: You jerk! You just kept dying and guessing!\nYou: No I didn't I just know someone else with that name!\nGoblin: Ahhhh you are clearly superior you will be my boss one day my 5th grade teacher was riiiiiigggghhhtttttt. . ..\nThe goblin stumbles around in faux agony and then hides behind a bush.\nGoblin: Wait! I'll just take you to the demon king and get the reward from the head honcho! I'll be famous!\nYou: No don't!\nYou think back to your earlier conversation. If he's that weak you can take him. Wanna try?"
    },
    {
      "name": "GoblinEvil",
      "tags": "",
      "id": "40",
			"score": -10,
      "text": "You attack the goblin and easily beat him into submission. He fades away into smoke. He's gone. You look around and so is everyone else. What was once a bustling town was now a ghost town. You can't focus on that now though. What's done is done. Time to go home.\nWilbur: Hey Slippy where'd everyone go?\nYou: Uh I don't know! Don't ask me!\nWilbur: Geez dude calm down. Here, the castle gates are open. Let's go inside.\n\n[[NEXT->FortressEntranceEvil]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "FortressEntranceEvil",
          "original": "[[NEXT->FortressEntranceEvil]]"
        }
      ],
      "hooks": [],
      "cleanText": "You attack the goblin and easily beat him into submission. He fades away into smoke. He's gone. You look around and so is everyone else. What was once a bustling town was now a ghost town. You can't focus on that now though. What's done is done. Time to go home.\nWilbur: Hey Slippy where'd everyone go?\nYou: Uh I don't know! Don't ask me!\nWilbur: Geez dude calm down. Here, the castle gates are open. Let's go inside."
    },
    {
      "name": "GoblinGood",
      "tags": "",
      "id": "41",
			"score": 10,
      "text": "You: Please don't sir! I just want to go home and see my family!\nGoblin: Y-You're right I'm sorry. I can't let my greed end another's life. Please accept my apology and go ahead.\nHe motions you ahead and a familiar face runs through the crowd with more bananas than you can count stored in incredibly creative ways.\nWilbur: Heya Slippy! Sorry, the banana store was having a sale!\nYou sigh a little bit but motion Wilbur to go first since he's your terrible guide and you need to find the thrown room.\nWilbur: Let's go!\nGoblin: Good luck kid!\nYou and the goblin exchange a much more genuine smile than before and then you enter the castle to finally face this demon king.\n\n[[NEXT->FortessEntranceGood]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "FortessEntranceGood",
          "original": "[[NEXT->FortessEntranceGood]]"
        }
      ],
      "hooks": [],
      "cleanText": "You: Please don't sir! I just want to go home and see my family!\nGoblin: Y-You're right I'm sorry. I can't let my greed end another's life. Please accept my apology and go ahead.\nHe motions you ahead and a familiar face runs through the crowd with more bananas than you can count stored in incredibly creative ways.\nWilbur: Heya Slippy! Sorry, the banana store was having a sale!\nYou sigh a little bit but motion Wilbur to go first since he's your terrible guide and you need to find the thrown room.\nWilbur: Let's go!\nGoblin: Good luck kid!\nYou and the goblin exchange a much more genuine smile than before and then you enter the castle to finally face this demon king."
    },
    {
      "name": "FortressEntranceEvil",
      "tags": "",
      "id": "42",
      "text": "You follow Wilbur into the halls of the demon king. It's empty. This is your moment. When the times strikes you'll end him and finally go home.\nWilbur: I know what you did.\nYou: Did what?\nWilbur: You're digusting. I finally understand why the demon king hates humans. They really are vile and disgusting creatures.\nYou: I had to!\nWilbur: No one has to do anything. Especially kill.\nOn that note, it's time to face you destiny.\n\n[[NEXT->ThroneRoomEvil]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "ThroneRoomEvil",
          "original": "[[NEXT->ThroneRoomEvil]]"
        }
      ],
      "hooks": [],
      "cleanText": "You follow Wilbur into the halls of the demon king. It's empty. This is your moment. When the times strikes you'll end him and finally go home.\nWilbur: I know what you did.\nYou: Did what?\nWilbur: You're digusting. I finally understand why the demon king hates humans. They really are vile and disgusting creatures.\nYou: I had to!\nWilbur: No one has to do anything. Especially kill.\nOn that note, it's time to face you destiny."
    },
    {
      "name": "FortessEntranceGood",
      "tags": "",
      "id": "43",
      "text": "You follow Wilbur into the mighty halls of the demon king. Oddly enough, there are no portraits of the demon king nor are there any statues or any depictions of the demon king. Wilbur walks slowly through the halls to give you time to admire their magnitude. This is the first time he's been a good guide. There are a lot of guards around the place. They are tall mighty human shaped figures with the heads of eagles. Easily 7 feet tall and just as magnificent as the halls they roam.\nWilbur: The throne room is just up ahead. Anything you wanna know about the demon king before you meet him?\n\n[[YES->QuestionDemonKing]]\n[[NO->ThroneRoom]]",
      "links": [
        {
          "linkText": "YES",
          "passageName": "QuestionDemonKing",
          "original": "[[YES->QuestionDemonKing]]"
        },
        {
          "linkText": "NO",
          "passageName": "ThroneRoom",
          "original": "[[NO->ThroneRoom]]"
        }
      ],
      "hooks": [],
      "cleanText": "You follow Wilbur into the mighty halls of the demon king. Oddly enough, there are no portraits of the demon king nor are there any statues or any depictions of the demon king. Wilbur walks slowly through the halls to give you time to admire their magnitude. This is the first time he's been a good guide. There are a lot of guards around the place. They are tall mighty human shaped figures with the heads of eagles. Easily 7 feet tall and just as magnificent as the halls they roam.\nWilbur: The throne room is just up ahead. Anything you wanna know about the demon king before you meet him?"
    },
    {
      "name": "Town",
      "tags": "",
      "id": "44",
      "text": "You look and see an abandoned banana store, Wilbur standing by the castle gates, and what looks to be footprints. What will you do?\n\n[[BANANA->BananaEvil]]\n[[WILBUR->DoorEvil]]\n[[FOOTPRINTS->FootPrints]]",
      "links": [
        {
          "linkText": "BANANA",
          "passageName": "BananaEvil",
          "original": "[[BANANA->BananaEvil]]"
        },
        {
          "linkText": "WILBUR",
          "passageName": "DoorEvil",
          "original": "[[WILBUR->DoorEvil]]"
        },
        {
          "linkText": "FOOTPRINTS",
          "passageName": "FootPrints",
          "original": "[[FOOTPRINTS->FootPrints]]"
        }
      ],
      "hooks": [],
      "cleanText": "You look and see an abandoned banana store, Wilbur standing by the castle gates, and what looks to be footprints. What will you do?"
    },
    {
      "name": "BananaEvil",
      "tags": "",
      "id": "45",
      "text": "You drift over to the banana store. Theres banans and random junk all over the place. It's almost like everyone up and vanished.\n\n[[BACK->Town]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Town",
          "original": "[[BACK->Town]]"
        }
      ],
      "hooks": [],
      "cleanText": "You drift over to the banana store. Theres banans and random junk all over the place. It's almost like everyone up and vanished."
    },
    {
      "name": "DoorEvil",
      "tags": "",
      "id": "46",
      "text": "You walk over to Wilbur by the giant pair of doors that lead to the castle of the great demon king.\nWilbur: I bet you're wondering where everyone went huh?\nYou: Kinda yea, I figured it was abandoned.\nWilbur: Now it is.\nWilbur opens the door and walks inside. I guess follow him?\n\n[[NEXT->FortessEntranceOrville]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "FortessEntranceOrville",
          "original": "[[NEXT->FortessEntranceOrville]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk over to Wilbur by the giant pair of doors that lead to the castle of the great demon king.\nWilbur: I bet you're wondering where everyone went huh?\nYou: Kinda yea, I figured it was abandoned.\nWilbur: Now it is.\nWilbur opens the door and walks inside. I guess follow him?"
    },
    {
      "name": "FootPrints",
      "tags": "",
      "id": "47",
      "text": "You walk over to the footprints and examine them. They look like human footprints but almost as if they were missing flesh. So a skeleton I guess? They could've made great friends I bet.\n\n[[BACK->Town]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Town",
          "original": "[[BACK->Town]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk over to the footprints and examine them. They look like human footprints but almost as if they were missing flesh. So a skeleton I guess? They could've made great friends I bet."
    },
    {
      "name": "FortessEntranceOrville",
      "tags": "",
      "id": "48",
      "text": "You follow Wilbur into the halls of the demon king. It's empty. As you follow Wilbur to the throne room you feel the full force of guilt.\nWilbur: The demon king really was right. Humans are vile creatures.\nYou: I'm sorry.\nWilbur: Sorry doesn't bring him back.\nYou: I don't know what came out of me.\nWilbur: You weren't possessed by anything. There is no nasty entity controlling you. You are that entity.\nOn that note, you should just shut up. It's time to end the demon king.\n\n[[NEXT->ThroneRoomOrville]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "ThroneRoomOrville",
          "original": "[[NEXT->ThroneRoomOrville]]"
        }
      ],
      "hooks": [],
      "cleanText": "You follow Wilbur into the halls of the demon king. It's empty. As you follow Wilbur to the throne room you feel the full force of guilt.\nWilbur: The demon king really was right. Humans are vile creatures.\nYou: I'm sorry.\nWilbur: Sorry doesn't bring him back.\nYou: I don't know what came out of me.\nWilbur: You weren't possessed by anything. There is no nasty entity controlling you. You are that entity.\nOn that note, you should just shut up. It's time to end the demon king."
    },
    {
      "name": "QuestionDemonKing",
      "tags": "",
      "id": "49",
      "text": "Here are the questions you can ask Wilbur.\nA: What is the demon king like?\nB: Why is he called the demon king?\nC: Why does he hate humans?\nD: Is his real name Markus?\n\n[[A->AnswerA]]\n[[B->AnswerB]]\n[[C->AnswerC]]\n[[D->AnswerD]]\n[[BACK->FortessEntranceGood]]",
      "links": [
        {
          "linkText": "A",
          "passageName": "AnswerA",
          "original": "[[A->AnswerA]]"
        },
        {
          "linkText": "B",
          "passageName": "AnswerB",
          "original": "[[B->AnswerB]]"
        },
        {
          "linkText": "C",
          "passageName": "AnswerC",
          "original": "[[C->AnswerC]]"
        },
        {
          "linkText": "D",
          "passageName": "AnswerD",
          "original": "[[D->AnswerD]]"
        },
        {
          "linkText": "BACK",
          "passageName": "FortessEntranceGood",
          "original": "[[BACK->FortessEntranceGood]]"
        }
      ],
      "hooks": [],
      "cleanText": "Here are the questions you can ask Wilbur.\nA: What is the demon king like?\nB: Why is he called the demon king?\nC: Why does he hate humans?\nD: Is his real name Markus?"
    },
    {
      "name": "ThroneRoom",
      "tags": "",
      "id": "50",
      "text": "You open the door to a peaceful serene garden. In the middle a tall figure in golden robes slowly turns your way.\nDemon King: Hello human.\nHe examines you. His eyes cold as steel. He knows he is better than you and he gets extremely close by bending forward. His dark hair covers his silver eyes before he backs away and resumes his royal stance.\nDemon King: What do you want child?\nYou turn to Wilbur for help frozen in fear but he's gone. It's just you and the demon king.\nDemon King: All humans in my chambers want only one thing. To leave. Am I correct?\nYou: Yes sir. I fell down here with my friend and I heard this is my only way out.\nDemon King: Some friend you are. Why did you leave your friend behind?\nWill you tell the truth or lie?\n\n[[TRUTH->ThroneRoomTruth]]\n[[LIE->ThroneRoomLie]]",
      "links": [
        {
          "linkText": "TRUTH",
          "passageName": "ThroneRoomTruth",
          "original": "[[TRUTH->ThroneRoomTruth]]"
        },
        {
          "linkText": "LIE",
          "passageName": "ThroneRoomLie",
          "original": "[[LIE->ThroneRoomLie]]"
        }
      ],
      "hooks": [],
      "cleanText": "You open the door to a peaceful serene garden. In the middle a tall figure in golden robes slowly turns your way.\nDemon King: Hello human.\nHe examines you. His eyes cold as steel. He knows he is better than you and he gets extremely close by bending forward. His dark hair covers his silver eyes before he backs away and resumes his royal stance.\nDemon King: What do you want child?\nYou turn to Wilbur for help frozen in fear but he's gone. It's just you and the demon king.\nDemon King: All humans in my chambers want only one thing. To leave. Am I correct?\nYou: Yes sir. I fell down here with my friend and I heard this is my only way out.\nDemon King: Some friend you are. Why did you leave your friend behind?\nWill you tell the truth or lie?"
    },
    {
      "name": "AnswerA",
      "tags": "",
      "id": "51",
      "text": "Wilbur: He's a human. He's very kind and always helps people and doesn't see himself as a king. Rumor has it that he's the first human to enter the monster world. He always gives his possessions away and makes sure all monster kind is taken care of and fed. He just doesn't like humans.\n\n[[BACK->QuestionDemonKing]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "QuestionDemonKing",
          "original": "[[BACK->QuestionDemonKing]]"
        }
      ],
      "hooks": [],
      "cleanText": "Wilbur: He's a human. He's very kind and always helps people and doesn't see himself as a king. Rumor has it that he's the first human to enter the monster world. He always gives his possessions away and makes sure all monster kind is taken care of and fed. He just doesn't like humans."
    },
    {
      "name": "AnswerB",
      "tags": "",
      "id": "52",
      "text": "Wilbur: I'm not quite sure. Maybe he thought it would fit in with the aesthetic of being a monster. He's a huge softy so I tend not to see him as a huge big bad intimidating demon.\n\n[[BACK->QuestionDemonKing]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "QuestionDemonKing",
          "original": "[[BACK->QuestionDemonKing]]"
        }
      ],
      "hooks": [],
      "cleanText": "Wilbur: I'm not quite sure. Maybe he thought it would fit in with the aesthetic of being a monster. He's a huge softy so I tend not to see him as a huge big bad intimidating demon."
    },
    {
      "name": "AnswerC",
      "tags": "",
      "id": "53",
      "text": "Wilbur: He says it's because they are untrustworthy and vile. He says he lost faith in humans when he came here and that the monsters here are so kind when they took him in that he vowed to extreminate every human that dare enter monster territory.\n\n[[BACK->QuestionDemonKing]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "QuestionDemonKing",
          "original": "[[BACK->QuestionDemonKing]]"
        }
      ],
      "hooks": [],
      "cleanText": "Wilbur: He says it's because they are untrustworthy and vile. He says he lost faith in humans when he came here and that the monsters here are so kind when they took him in that he vowed to extreminate every human that dare enter monster territory."
    },
    {
      "name": "AnswerD",
      "tags": "",
      "id": "54",
      "text": "Wilbur: Yea how did you know that?\n\n[[BACK->QuestionDemonKing]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "QuestionDemonKing",
          "original": "[[BACK->QuestionDemonKing]]"
        }
      ],
      "hooks": [],
      "cleanText": "Wilbur: Yea how did you know that?"
    },
    {
      "name": "ThroneRoomEvil",
      "tags": "",
      "id": "55",
      "text": "You walk into the throne room and see the demon king. He is tall and has dark hair. He slowly turns to you but you immediately take the chance to attack him. He easily dodges and kicks you against the wall.\nDemon King: Foolish boy. Such an action is a sign that the human world has not changed. You are so corrupted by violence that you try to attack me? You truly are disgusting.\nThe demon king leans in close. His silver eyes pierce your soul. \nDemon King: You have changed old friend. The world of monsters has judged you and found you guilty. You see, the realm of monsters is not like that of humans. As part of the curse that locks all monster-kind here we are forever stuck in a loop. Our history is doomed to repeat forever. In this timeline you have chosen violence.\nYou finally realize who the demon king really is.\nDemon King: I can tell by your reaction you know exactly who I am. I am not your mark however. I am a Mark from a timeline where my actions were tried and true, as such I was judged and rewarded with my position.\n\n[[NEXT->ThroneRoomEvil1]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "ThroneRoomEvil1",
          "original": "[[NEXT->ThroneRoomEvil1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the throne room and see the demon king. He is tall and has dark hair. He slowly turns to you but you immediately take the chance to attack him. He easily dodges and kicks you against the wall.\nDemon King: Foolish boy. Such an action is a sign that the human world has not changed. You are so corrupted by violence that you try to attack me? You truly are disgusting.\nThe demon king leans in close. His silver eyes pierce your soul. \nDemon King: You have changed old friend. The world of monsters has judged you and found you guilty. You see, the realm of monsters is not like that of humans. As part of the curse that locks all monster-kind here we are forever stuck in a loop. Our history is doomed to repeat forever. In this timeline you have chosen violence.\nYou finally realize who the demon king really is.\nDemon King: I can tell by your reaction you know exactly who I am. I am not your mark however. I am a Mark from a timeline where my actions were tried and true, as such I was judged and rewarded with my position."
    },
    {
      "name": "ThroneRoomOrville",
      "tags": "",
      "id": "56",
      "text": "You walk into the throne room and see the demon king. He is tall and has dark hair. He slowly turns to you but you immediately take the chance to attack him. He easily dodges and kicks you against the wall.\nDemon King: Foolish boy. Such an action is a sign that the human world has not changed. You are so corrupted by violence that you try to attack me? You truly are disgusting.\nThe demon king leans in close. His silver eyes pierce your soul. \nDemon King: You have changed old friend. The world of monsters has judged you and found you guilty. You see, the realm of monsters is not like that of humans. As part of the curse that locks all monster-kind here we are forever stuck in a loop. Our history is doomed to repeat forever. In this timeline you have chosen violence.\nYou finally realize who the demon king really is.\nDemon King: I can tell by your reaction you know exactly who I am. I am not your mark however. I am a Mark from a timeline where my actions were tried and true, as such I was judged and rewarded with my position.\n\n[[NEXT->ThroneRoomOrville1]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "ThroneRoomOrville1",
          "original": "[[NEXT->ThroneRoomOrville1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the throne room and see the demon king. He is tall and has dark hair. He slowly turns to you but you immediately take the chance to attack him. He easily dodges and kicks you against the wall.\nDemon King: Foolish boy. Such an action is a sign that the human world has not changed. You are so corrupted by violence that you try to attack me? You truly are disgusting.\nThe demon king leans in close. His silver eyes pierce your soul. \nDemon King: You have changed old friend. The world of monsters has judged you and found you guilty. You see, the realm of monsters is not like that of humans. As part of the curse that locks all monster-kind here we are forever stuck in a loop. Our history is doomed to repeat forever. In this timeline you have chosen violence.\nYou finally realize who the demon king really is.\nDemon King: I can tell by your reaction you know exactly who I am. I am not your mark however. I am a Mark from a timeline where my actions were tried and true, as such I was judged and rewarded with my position."
    },
    {
      "name": "ThroneRoomTruth",
      "tags": "",
      "id": "57",
			"score": 5,
      "text": "You: I left him behind because I was selfish and abandoned him.\nThe demon king smirks.\nDemon King: I know. You are no different than all humans. Although I appreciate you honesty, you must pay for your kind's sins.\nYou: But I didn't do anything evil! It's not my fault humans treated you badly!\nThe demon king slowly walks around his garden smelling the flowers and examining the vegetables he grew. You look up and notice the sun shines down directly onto his garden.\nDemon King: You claim innocence yet do nothing to stop evil actions? You abandon your friend and lecture me on morals? You watch and commit abuses yourself and live among monsters and still don't recognize who the real monster is?\n\n[[NEXT->ThroneRoom1]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "ThroneRoom1",
          "original": "[[NEXT->ThroneRoom1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You: I left him behind because I was selfish and abandoned him.\nThe demon king smirks.\nDemon King: I know. You are no different than all humans. Although I appreciate you honesty, you must pay for your kind's sins.\nYou: But I didn't do anything evil! It's not my fault humans treated you badly!\nThe demon king slowly walks around his garden smelling the flowers and examining the vegetables he grew. You look up and notice the sun shines down directly onto his garden.\nDemon King: You claim innocence yet do nothing to stop evil actions? You abandon your friend and lecture me on morals? You watch and commit abuses yourself and live among monsters and still don't recognize who the real monster is?"
    },
    {
      "name": "ThroneRoomLie",
      "tags": "",
      "id": "58",
			"score": -5,
      "text": "You: I-I tried looking for him but I assumed the worst had happened so I continued on.\nThe demon king gets in your face extremely quickly. With his robes still in the air from his dash, he leans into your ear.\nDemon King: Don't lie to me boy. I own this domain and see all that happens within it.\nYou clench your fists and start to tear up but quickly wipe them away as he backs off.\nDemon King: All humans are so vile and disgusting. You live among monsters and do not yet see that you are the true monster.\n\n[[NEXT->ThroneRoom1]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "ThroneRoom1",
          "original": "[[NEXT->ThroneRoom1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You: I-I tried looking for him but I assumed the worst had happened so I continued on.\nThe demon king gets in your face extremely quickly. With his robes still in the air from his dash, he leans into your ear.\nDemon King: Don't lie to me boy. I own this domain and see all that happens within it.\nYou clench your fists and start to tear up but quickly wipe them away as he backs off.\nDemon King: All humans are so vile and disgusting. You live among monsters and do not yet see that you are the true monster."
    },
    {
      "name": "ThroneRoom1",
      "tags": "",
      "id": "59",
      "text": "You take a deep breath and look at him and it finally clicks in your head.\nYou: Mark?\nThe demon king laughs.\nDemon King: Yes, but not your Mark. You see, the realm of monsters is not like that of humans. As part of the curse that locks all monster-kind here we are forever stuck in a loop. Our history is doomed to repeat forever. Though I have not been called that for ages, I am a version of Mark that has walked a tried and true path. The realm of monsters has judged you and seen your path. As such, you will be permitted to leave. I will give you the option to stay as the monsters have taken a liking to you.\nYou turn around and see Wilbur and his brother Orville and the goblin standing in the entrance. The demon king smiles. What will it be friend?\n\n[[STAY->GoodEndingStay]]\n[[LEAVE->GoodEndingLeave]]\n[[DELETETHISONE->SecretEnding]]",
      "links": [
        {
          "linkText": "STAY",
          "passageName": "GoodEndingStay",
          "original": "[[STAY->GoodEndingStay]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "GoodEndingLeave",
          "original": "[[LEAVE->GoodEndingLeave]]"
        },
        {
          "linkText": "SECRET",
          "passageName": "SecretEnding",
          "original": "[[DELETETHISONE->SecretEnding]]"
        }
      ],
      "hooks": [],
      "cleanText": "You take a deep breath and look at him and it finally clicks in your head.\nYou: Mark?\nThe demon king laughs.\nDemon King: Yes, but not your Mark. You see, the realm of monsters is not like that of humans. As part of the curse that locks all monster-kind here we are forever stuck in a loop. Our history is doomed to repeat forever. Though I have not been called that for ages, I am a version of Mark that has walked a tried and true path. The realm of monsters has judged you and seen your path. As such, you will be permitted to leave. I will give you the option to stay as the monsters have taken a liking to you.\nYou turn around and see Wilbur and his brother Orville and the goblin standing in the entrance. The demon king smiles. What will it be friend?"
    },
    {
      "name": "GoodEndingStay",
      "tags": "",
      "id": "60",
			"score": 20,
      "text": "You: I want to stay. These monsters are my family they did everything they could to bring me here and sacrificed a lot. Since everything is doomed to repeat, there will be another version of me right? He can leave. Me? I want to stay.\nMark: A wise choice friend.\nMark smiles. Wilburs motions you forward and you all leave the throne room going back to the entrance. What started as a cave exploration was an exploration of what it means to be a true friend.\n\nGOOD ENDING: Type SECRET at an important choice for the true ending!",
      "links": [],
      "hooks": [],
      "cleanText": "You: I want to stay. These monsters are my family they did everything they could to bring me here and sacrificed a lot. Since everything is doomed to repeat, there will be another version of me right? He can leave. Me? I want to stay.\nMark: A wise choice friend.\nMark smiles. Wilburs motions you forward and you all leave the throne room going back to the entrance. What started as a cave exploration was an exploration of what it means to be a true friend.\n\nGOOD ENDING: Type SECRET at an important choice for the true ending!"
    },
    {
      "name": "GoodEndingLeave",
      "tags": "",
      "id": "61",
			"score": 20,
      "text": "You: I want to leave. Wilbur and everyone else will be invaluable friends but since everything is doomed to repeat, for the sake of my other copies, I should go home. Another version of me will stay. Me? I should go.\nMark: A wise choice friend.\nMark smiles and opens the door. The sun shines through. For the first time in awhile, you can smell the fresh air. It's time to go home.\nAll of your friends smile and wave as you walk away.\nWilbur: Do you think he'll ever come back?\nMark: He always does.\n\nGOOD ENDING: Type SECRET at an important choice for the true ending!",
      "links": [],
      "hooks": [],
      "cleanText": "You: I want to leave. Wilbur and everyone else will be invaluable friends but since everything is doomed to repeat, for the sake of my other copies, I should go home. Another version of me will stay. Me? I should go.\nMark: A wise choice friend.\nMark smiles and opens the door. The sun shines through. For the first time in awhile, you can smell the fresh air. It's time to go home.\nAll of your friends smile and wave as you walk away.\nWilbur: Do you think he'll ever come back?\nMark: He always does.\n\nGOOD ENDING: Type SECRET at an important choice for the true ending!"
    },
    {
      "name": "SecretEnding",
      "tags": "",
      "id": "62",
			"score": 50,
      "text": "You: Why can't you guys come too?\nMark looks surprised.\nWilbur: Monsters in the human world?\nMark is in deep thought.\nWilbur: This human was pretty cool. I trust him.\nMark: Maybe your coming was a sign that the curse is broken. Shall we test the morals of humans once again?\nMark walks forward and hand in hand, you all open and walk through the door to the outside.\n\nTRUE ENDING",
      "links": [],
      "hooks": [],
      "cleanText": "You: Why can't you guys come too?\nMark looks surprised.\nWilbur: Monsters in the human world?\nMark is in deep thought.\nWilbur: This human was pretty cool. I trust him.\nMark: Maybe your coming was a sign that the curse is broken. Shall we test the morals of humans once again?\nMark walks forward and hand in hand, you all open and walk through the door to the outside.\n\nTRUE ENDING"
    },
    {
      "name": "ThroneRoomEvil1",
      "tags": "",
      "id": "63",
      "text": "You: What's gonna happen to me?\nMark: You will be punished. For killing innocent monsters you will be the front guard of the cave. All who the cave beckons, you must push so they may be judged. This is your duty. Even if it is yourself.\nYou: What if I don't.\nMark laughs.\nMark: You don't make the choice. The cave controls you now, you must simply observe as it uses you.\nYou start to feel dizzy and slowly black out.\nMark: Goodbye, old friend.\n\n[[NEXT->BadEnding]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "BadEnding",
          "original": "[[NEXT->BadEnding]]"
        }
      ],
      "hooks": [],
      "cleanText": "You: What's gonna happen to me?\nMark: You will be punished. For killing innocent monsters you will be the front guard of the cave. All who the cave beckons, you must push so they may be judged. This is your duty. Even if it is yourself.\nYou: What if I don't.\nMark laughs.\nMark: You don't make the choice. The cave controls you now, you must simply observe as it uses you.\nYou start to feel dizzy and slowly black out.\nMark: Goodbye, old friend."
    },
    {
      "name": "BadEnding",
      "tags": "",
      "id": "64",
			"score": -20,
      "text": "You wake up in a cave and see 2 children over by the ledge. One of the children is gazing deep into the cave and distracted.\nChild 1: Did you see that??\nYou: Want a closer look?\nThe child screams on his way down the cave. The other child turns around and it's you. The cave is in control now.\nYou: H-hey! What are you doing here?\nIt's too late you push the other child down.\n\nBAD ENDING",
      "links": [],
      "hooks": [],
      "cleanText": "You wake up in a cave and see 2 children over by the ledge. One of the children is gazing deep into the cave and distracted.\nChild 1: Did you see that??\nYou: Want a closer look?\nThe child screams on his way down the cave. The other child turns around and it's you. The cave is in control now.\nYou: H-hey! What are you doing here?\nIt's too late you push the other child down.\n\nBAD ENDING"
    },
    {
      "name": "ThroneRoomOrville1",
      "tags": "",
      "id": "65",
      "text": "You: What's gonna happen to me?\nMark: You will be punished. For killing Orville you must atone by living out Wilbur's life and forever will you watch you brother be killed, other times you won't but everytime you die you will play the cruel game of lottery again. Such is fate. But your promise is to always bring the human to me no matter what.\nYou start to feel dizzy and slowly black out.\nMark: Goodbye, old friend.\n\n[[NEXT->BadEnding2]]",
      "links": [
        {
          "linkText": "NEXT",
          "passageName": "BadEnding2",
          "original": "[[NEXT->BadEnding2]]"
        }
      ],
      "hooks": [],
      "cleanText": "You: What's gonna happen to me?\nMark: You will be punished. For killing Orville you must atone by living out Wilbur's life and forever will you watch you brother be killed, other times you won't but everytime you die you will play the cruel game of lottery again. Such is fate. But your promise is to always bring the human to me no matter what.\nYou start to feel dizzy and slowly black out.\nMark: Goodbye, old friend."
    },
    {
      "name": "BadEnding2",
      "tags": "",
      "id": "66",
			"score": -20,
      "text": "You're on an evening stroll and suddenly a child falls in front of you.\\\nYou: Hey bud are you ok?\n\nBAD ENDING",
      "links": [],
      "hooks": [],
      "cleanText": "You're on an evening stroll and suddenly a child falls in front of you.\\\nYou: Hey bud are you ok?\n\nBAD ENDING"
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		#print("Moves: " + str(moves) + ", Score: " + str(score))
		print("Moves: {}, Score: {}".format(moves, score))
		print(current_location["cleanText"] + "\n")
		for link in current_location["links"]:
			if link["linkText"] != "SECRET":
				print(link["linkText"])

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "Bedroom"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves += 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score += current_location["score"]
	render(current_location, score, moves)
	response = get_input()


print("Thanks for playing!")