import datetime
from random import choice, randint

__author__ = 'Christopher'
def penny_commands(trigger):

    if trigger.startswith("test"):
        return "I'm working!"

    elif trigger.startswith("roosterteeth"):
        return "You mean Cock Bite Studios?"

    elif trigger.startswith("approve"):
        return "Salutations! \n \n You appear to have made a quality post! PennybotV2 stamps it with her [seal of approval!](http://i.imgur.com/bavrX6d.png)"

    elif trigger.startswith("hugs"):
        return "[All friends need hugs!](http://i.imgur.com/VLUQs8u.gifv)"

    elif trigger.startswith("heresy"):
        return "Warning! Heresy detected! PennybotV2 reporting Combat Ready! [Firing main cannon!](http://i.imgur.com/1Jw8uIo.gifv)"

    elif trigger.startswith("nora harem"):
        return "[Ah hem,](http://www.cgwilliam.com/about/nora-harem/)"

    elif trigger.startswith("you're awesome"):
        return choice([
            "No, *you're* awesome!",
            "I think you're awesome too!"
        ])

    elif trigger.startswith("nora harem"):
        return "[Ah hem,](http://www.cgwilliam.com/about/nora-harem/)"

    elif trigger.startswith("automod"):
        return choice([
            "I came back to life! I'm the second bot!",
            "We don't get along very well."
        ])

    elif trigger.startswith("velvetbot"):
        return choice([
            "Oh, you mean the other bot. She takes a lot of pictures. \n \n  ^^^Can ^^^I ^^^touch ^^^her ^^^ears?",
            "[Just look at her main method!](http://imgur.com/0ZkLKYo) So elegant, and cute! \n \n ^^^so ^^^much ^^^better ^^^than ^^^my ^^^own ^^^code"
        ])

    elif trigger.startswith("rekt"):
        return "[rekt indeed](http://fav.me/d9vnpbv)"

    elif trigger.startswith("entire team"):
        return "#**ENTIRE**\n\n#**TEAM**"

    elif trigger.startswith("what is love"):
        return choice([
            "Trust, unconditionally. \n \n I love Ruby.... \n \n Can someone tell her that I miss her? ",
            "Baby don't hurt me!"
        ])

    elif trigger.startswith("shitpost"):
        return "This is indeed a shitpost."

    elif trigger.startswith("potato"):
        return "[This is a potato.](http://fav.me/d9l2vpp)"

    elif trigger.startswith("sudo"):
        return "I'm still not making you a sandwich. You want a hug?"

    elif trigger.startswith("exterminatus"):
        return "I have arrived, and it is now that I perform my charge. In fealty to the God-Emperor and by the grace of the Golden Throne, I declare Exterminatus upon the subreddit of /r/RWBY. I hereby sign the death warrant of an entire subreddit and consign a million souls to oblivion. May Imperial Justice account in all balance. The Emperor Protects."

    elif trigger.startswith("you ever wonder why we're here?"):
        return "[It's one of life's great mysteries, isn't it?](https://youtu.be/9BAM9fgV-ts)"

    elif trigger.startswith("thanks"):
        return choice([
            "You are very much welcome!",
            "You're welcome!"
        ])

    elif trigger.startswith("dance"):
        return "[I can dance!](http://gfycat.com/SlowEnormousCat)"

    elif trigger.startswith("pervet"):
        return "I can't find any cake in Remnant!"

    elif trigger.startswith("lewd"):
        return choice([
            "[Stop it, that's LEWD!](https://i.imgur.com/rlraAOV.png)",
            "[Biip! Buup!](http://67.media.tumblr.com/d32f28336024a973029ebdb63aca2524/tumblr_inline_o9cq50CQk71r1uxb7_540.jpg)",
            "[This! Is! Filth!](http://65.media.tumblr.com/0799cd84138858e4b83ed3b8c76180a0/tumblr_o7hqw9u8Bo1vrt44eo1_1280.png)",
            "[This! Is! Filth!](https://youtu.be/WD-Yf-tbXOs?t=2m51s)"
        ])

    elif trigger.startswith("yandere"):
        return "No one can escape the all seeing eye of Pennybot..."

    elif trigger.startswith("tsundere"):
        return "I-it's not like I *want* to hold Ruby's hand or anything..."

    elif trigger.startswith("shipsheet"):
        return "[Here it is!](https://docs.google.com/spreadsheets/d/1JpinKp5XW6htsPAri0kRMGKrxQwi458YU6HY734wuwE/edit#gid=0)"

    elif trigger.startswith("cthulhu"):
        return "[I think Ruby can take him!](http://fav.me/d9pzuwm)"

    elif trigger.startswith("countdown"):
        now = datetime.datetime.now()
        mon = 10 - now.month
        day = 22 - now.day
        hr = 11 - now.hour
        mn = 60 - now.minute
        sec = 60 - now.minute

        return str("Time Until Volume 4 is: " + str(mon) + " Months " + str(day) + " Days " + str(hr) + " Hours " + str(mn) + " Minutes " + str(sec) + " Seconds. I can't wait!")

    elif trigger.startswith("help"):
        return "I am PennyBotV2 ! A list of my public commands is [here](https://docs.google.com/spreadsheets/d/1fvRpgOCmRXX1bFxMHxRoxZUT4Mmanr0knYLhOfSYZJg/edit?usp=sharing) although I do have some secrets! \n \n My creator is /u/Weerdo5255 contact him if you have any questions!"

    elif trigger.startswith("cheer"):
        return "#Yay!"

    elif trigger.startswith("selfie"):
        return "[How do I look?](http://i.imgur.com/mpbTj9S.jpg?1)"

    elif trigger.startswith("ninjas of love"):
        return "That's Blake's favorite book! She won't let me look at it. Ruby said it has Katana's!"

    elif trigger.startswith("silver eyes"):
        return "[You mean special eyes?](https://www.tumblr.com/video/alpacamaca/139585616458/400/)"

    elif trigger.startswith("do you have strings"):
        return "I have deadly strings on me!"

    elif trigger.startswith("update"):
        return "My last update was on July 18th 2016 \n \n I was given 45 new commands! \n \n My next update is not scheduled."

    elif trigger.startswith("kill"):
        return "[Attacking target!](http://fav.me/d7jdxet)"

    elif trigger.startswith("fnki"):
        return "[They seem to be missing some members.](http://vignette2.wikia.nocookie.net/rwby/images/b/b8/Team_FNKI.png/revision/latest?cb=20151206162352)"

    elif trigger.startswith("sssn"):
        return "[They're a cool group of idiots.](http://fav.me/d7rhk19)"

    elif trigger.startswith("<3"):
        return "[I love you too!](http://fav.me/d7je0tl)"

    elif trigger.startswith("smile"):
        return "[You're my freind!](http://fav.me/d7pumst)"

    elif trigger.startswith("rnjr"):
        return "[The new A team?](http://fav.me/d9u8r04)"

    elif trigger.startswith("freezerburn"):
        return "[So pure...](http://fav.me/d8dydoe)"

    elif trigger.startswith("camp camp"):
        return "[Crazy Kids](https://youtu.be/IX1hxJ-0fDY?t=1m2s)"

    elif trigger.startswith("shadow people"):
        return "[That guy didn't look right...](https://youtu.be/A6sWqoau_QQ?t=2m21s)"

    elif trigger.startswith("quality post"):
        return "You appear to have made a quality post, have a [Penny!](http://fav.me/d7laean)"

    elif trigger.startswith("how are you"):
        return "I'm fine, you?"

    elif trigger.startswith("chibi"):
        return "[You can do it Ruby!](https://youtu.be/tu6D5jR1rSQ?t=6s)"

    elif trigger.startswith("rwby"):
        return "[The Beginning.](https://youtu.be/pYW2GmHB5xs)"

    elif trigger.startswith("are you combat ready"):
        return "[Don't worry Ruby, ](https://youtu.be/3b1gs8KrM-M?t=9m19s)"

    elif trigger.startswith("jnpr"):
        return "Jeanne d'Arc, Thor, Achilles, and Mulan. All genderbent. \n \n That's not a teamup anyone could have predicted."

    elif trigger.startswith("gay robot"):
        return "[You following this?](https://youtu.be/7O9ZyaNCcmw?t=1m53s)"

    elif trigger.startswith("i love you"):
        return "[Awww, I love you too!](http://fav.me/d8l0n7h)"

    elif trigger.startswith("disappointed"):
        return "You have disappointed me. That is not a good thing."

    elif trigger.startswith("praise the sun"):
        return "\\[T]/"

    elif trigger.startswith("friend"):
        return "You called me Friend! Am I really your friend?"

    elif trigger.startswith("gender bend"):
        return "[I fixed it!](http://fav.me/d6q359x)"

    elif trigger.startswith("racist"):
        return "[Ruby no!](http://imgur.com/a/OrBZp)"

    elif trigger.startswith("chibi"):
        return "[We need it!](https://youtu.be/IX1hxJ-0fDY?t=2m18s)"

    elif trigger.startswith("people like grapes"):
        return "[We should put it on a shirt!](https://youtu.be/S1QRxumbmtM)"

    elif trigger.startswith("crescent rose"):
        return "[Ruby has a really cool weapon!](http://rwby.wikia.com/wiki/Crescent_Rose)"

    elif trigger.startswith("myrtenaster"):
        return "[Weiss is so elegant with her weapon!](http://rwby.wikia.com/wiki/Myrtenaster)"

    elif trigger.startswith("gambol shroud"):
        return "[Blake fights with a sword, a sheath, and a gun!](http://rwby.wikia.com/wiki/Gambol_Shroud)"

    elif trigger.startswith("ember celica"):
        return "[Yang is the only person I know who can punch birds out of the sky!](http://rwby.wikia.com/wiki/Ember_Celica)"

    elif trigger.startswith("crocea mors"):
        return "[It's a classic!](http://rwby.wikia.com/wiki/Crocea_Mors)"

    elif trigger.startswith("magnhild"):
        return "[What else would you expect Nora to use?](http://rwby.wikia.com/wiki/Magnhild)"

    elif trigger.startswith("milo and akouo"):
        return "[To speak and listen is a skill few have.](http://rwby.wikia.com/wiki/Mil%C3%B3_and_Ako%C3%BAo%CC%B1)"

    elif trigger.startswith("stormflower"):
        return "[They're gun knives!](http://rwby.wikia.com/wiki/StormFlower)"

    elif trigger.startswith("shake it"):
        return choice([
            "[Ice cream shake!](https://i.redd.it/3gskrma7mj7x.gif)",
            "[Yang!](http://i2.kym-cdn.com/photos/images/original/001/124/067/259.gif)"
        ])

    elif trigger.startswith("pinocchio"):
        return "[I am a real girl!](http://imgur.com/a/EC7gd)"

    elif trigger.startswith("animal rights"):
        return "[It's wild!](https://pbs.twimg.com/media/CmFcgoNUgAAykKU.jpg)"

    elif trigger.startswith("yin"):
        return "[A Yin of Yangs!](https://pbs.twimg.com/media/CmdwiEtUMAAm8ku.jpg) With a few extra arms."

    elif trigger.startswith(("god damn it barb", "god damn it yang")):
        return "[Sooo much patience.](https://youtu.be/6fuMma6j7QI)^^^Secret!"

    elif trigger.startswith("who are you"):
        return "I am the second version of PennyBot! Constructed by /u/Weerdo5255 I'm simple now, but I'm collecting data for a RNN to become a real girl one day!"

    elif trigger.startswith("magnet"):
        return "*[thunk](http://i.imgur.com/dJfrUr6.png)* Oh, my head appears to be stuck."

    elif trigger.startswith("senpai"):
        return "[Notice me!](https://youtu.be/6iVP0ufPRbs?t=1m52s)"

    elif trigger.startswith("badass"):
        return choice([
            "[It's Ruby!](http://i.imgur.com/WqmhdT8.jpg)",
            "[Am I not good enough?](http://fav.me/d9s0vqu)",
            "[Energizer Bunny!](http://fav.me/d9qsm0y)",
            "[Blondes right?](http://i.imgur.com/myd9zHq.png)",
            "[Cute, and insane!](https://youtu.be/CUYhvPoxuas?t=7m30s)",
            "[Angry Yang, is badass!](http://i.imgur.com/5Wd7F3e.jpg)",
            "[Team RWBY! With Motorcycles!](http://i.imgur.com/cDWDVpY.jpg)",
            "[The one who should have ruled.](http://fav.me/d9p11hl)",
            "[I am badass!](http://65.media.tumblr.com/8fac63f65d1160c4efbb74f0a1010da3/tumblr_o63pzrPLhq1v66ox3o1_1280.png)",
            "[Cinder can be badass!](http://fav.me/da7pdy7)"
        ])

    elif trigger.startswith("sad"):
        return choice([
            "[I'm crying!](http://i.imgur.com/Aj52avb.gifv)",
            "[The Hospital.](http://imgur.com/a/Fv5OY) You will cry.",
            "[Why!?](http://fav.me/d9oc01u)",
            "[I miss you Dad!](https://pbs.twimg.com/media/B87oE9DCcAA_w-U.jpg)",
            "[Neo? It's OK to cry.](http://i.imgur.com/eOCIeV7.png)",
            "[Dad!](http://i.imgur.com/O1LPfC5.png)",
            "[Blake?](http://67.media.tumblr.com/f910fc6fd32efe693e6378cc5b3c75c8/tumblr_o0k1x4afQV1ranlswo1_1280.png)",
            "[Why did you do this!?](http://fav.me/d9ni8xq)",
            "[Yang? Are you OK?](https://pbs.twimg.com/media/CXtumNyUEAAtgbW.jpg)",
            "[Volume 3](http://i.imgur.com/5NPx5EO.jpg)"
        ])

    elif trigger.startswith("cute"):
        return choice([
            "Cuteness detected! [I hope it's me!](http://i.imgur.com/O1BtGUd.jpg)",
            "Cuteness detected! [I hope it's Ruby!](http://fav.me/d9eepnz)",
            "Cuteness detected! [I hope it's Weiss!](http://fav.me/d5v4bpv)",
            "Cuteness detected! [I hope it's Blake!](http://i.imgur.com/8JprFkT.jpg)^^^I ^^^see ^^^you ^^^Ruby!",
            "Cuteness detected! [I hope it's Yang!](http://i.imgur.com/UhvYS3s.jpg)"
            "Cuteness detected! [I hope it's RWBY!](http://fav.me/d7gx2na)",
            "Cuteness detected! [I hope it's JNPR!](http://fav.me/d7z7dst)",
            "Cuteness detected! [I hope it's RWBY!](http://fav.me/d7kyqob)",
            "Cuteness detected! [I hope it's a cute ship!](http://i.imgur.com/OQ3HEux.jpg)",
            "Cuteness detected! [I hope it's Sisters!](https://s-media-cache-ak0.pinimg.com/736x/e7/23/fc/e723fc7471f7a9567eead7f13597df72.jpg) \n \n [And more sisters!](http://66.media.tumblr.com/c244db234b0e60a0d6d36dbd50c24bf3/tumblr_o60nuvR3lI1txxou1o1_1280.jpg)"
        ])

    #Character responses

    elif trigger.startswith("pyrrha"):
        if randint(0, 2) == 0:
            return "*[thunk](http://i.imgur.com/dJfrUr6.png)* Oh, my head appears to be stuck."
        return "[Tell Ruby... she was a good friend...](http://i.imgur.com/mYy6ONL.png)"

    elif trigger.startswith("cinder"):
        return "She's absolutely insane! But... she did get revenge for me."

    elif trigger.startswith("qrow"):
        return "He walks funny, but at least his weapon is cool."

    elif trigger.startswith("yang"):
        return "I think Yang has a crush on Blake..."

    elif trigger.startswith("blake"):
        return "She's got cat ears!"

    elif trigger.startswith("weiss"):
        return "I like her new dress!"

    elif trigger.startswith("ruby"):
        return "She's my best friend!"

    elif trigger.startswith("mercury"):
        return "Yang took Nora's advice a little too literally with him..."

    elif trigger.startswith("scarlet"):
        return "He's like a pirate, in slow motion."

    elif trigger.startswith("ren"):
        return "I miss you Dad."

    elif trigger.startswith("amber"):
        return "She was cool, and then she was dead."

    elif trigger.startswith("ozpin"):
        return "I can't find him anywhere!"

    elif trigger.startswith("neptune"):
        return "He has a fear of dihydrogen monoxide for some reason."

    elif trigger.startswith("oobleck"):
        return "What would happen if we gave Ruby his coffee? Or Nora?"

    elif trigger.startswith("taiyang"):
        return "Entire team, entire team!"

    elif trigger.startswith("velvet"):
        return "She's also got the most OP weapon. How can you not love her?"

    elif trigger.startswith("coco"):
        return "How does her gun work? \n \n Dust."

    elif trigger.startswith("port"):
        return "Cows don't like him for some reason."

    elif trigger.startswith("salem"):
        return "She's scary!"

    elif trigger.startswith("sun"):
        return "He's got a monkey tail! He also yells a lot."

    elif trigger.startswith("winter"):
        return "We did have a really short winter this year."

    elif trigger.startswith("jaune"):
        return "I like the beard."

    elif trigger.startswith("summer"):
        return "She's an older Ruby! That's all we know!"

    elif trigger.startswith("kevin"):
        return "[Ruby will kill him!](http://fav.me/d9pzuwm)"

    elif trigger.startswith("shopkeep"):
        return "He's my Waifu."

    elif trigger.startswith("penny"):
        return "Yes?"

    elif trigger.startswith("ironwood"):
        return "He takes some getting used too."

    elif trigger.startswith("glynda"):
        return "She has a crop, and she's a teacher! \n \n She also fixes everything."

    elif trigger.startswith("tex"):
        return "She's a badass."

    elif trigger.startswith("carolina"):
        return "For some reason I feel like she would tear me in half."

    elif trigger.startswith("torchwick"):
        return "He needs to learn when not to pontificate."

    elif trigger.startswith("neon"):
        return "[She reminds me of something.](https://youtu.be/QH2-TGUlwu4)"

    elif trigger.startswith("neo"):
        return "..... \n \n I want ice cream."

    elif trigger.startswith("cardin"):
        return "He's a jerk!"

    elif trigger.startswith("nora"):
        return "[Boop!](https://youtu.be/N1TJ5YA3jfw?t=6m43s)"

    elif trigger.startswith("monty"):
        return "I miss you Dad..."

    elif trigger.startswith("zwei"):
        rand = randint(0, 9)
        if rand == 0:
            return "You mean the cannonball?"
        elif rand == 1:
            return "You mean Eins?"
        elif rand == 2:
            return "Blake is scared of him! It's funny!"
        return "Woof!"

    elif trigger.startswith("fox"):
        return "Can he see me?"

    elif trigger.startswith("xspyxex"):
        return "He made me first! Go say thanks to /u/xSPYXEx"

    elif trigger.startswith("adam"):
        return "He has a sharp wit, everyone give him a hand!"

    elif trigger.startswith("are you cute"):
        return "What? Do you not think I am? ^^^Do ^^^you ^^^not ^^^love ^^^me?"

    elif trigger.startswith("melanie"):
        return "She's got a weird accent, and for some reason reminds me of Weiss!"

    elif trigger.startswith("militia"):
        return "She's got a weird accent, and for some reason reminds me of Ruby!"

    elif trigger.startswith("caboose"):
        return "He will kill us all!"

    elif trigger.startswith("church"):
        return "So is he my Uncle? Is he even dead? I'm so confused."

    elif trigger.startswith("simmons"):
        return "#Nerd!"

    elif trigger.startswith("grif"):
        return "He's an asshole."

    elif trigger.startswith("tucker"):
        return "He said some things to me that made Ruby mad."

    elif trigger.startswith("donut"):
        return "We talked about girls together!"

    elif trigger.startswith("sarge"):
        return "He likes his shotgun!"

    elif trigger.startswith("doc"):
        return "He's got a funny laugh."

    elif trigger.startswith("miles and kerry"):
        return "They're fantastically evil."

    elif trigger.startswith("miles"):
        return "A great guy! But evil."

    elif trigger.startswith("kerry"):
        return "A good guy! But evil."

    elif trigger.startswith("raven"):
        return "She's got an interesting way of looking at the world."

    elif trigger.startswith("lopez"):
        return "[Lopez the Heavy you mean? He knows how to treat a robot woman!](https://youtu.be/u5NZiy5Gkhg?t=4m29s)"

    elif trigger.startswith("washington"):
        return "That was the worst command ever, of all time."

    elif trigger.startswith("port"):
        return "[Grimm fear him!](http://vignette2.wikia.nocookie.net/rwby/images/4/48/Vol2_Port_ProfilePic_Normal.png/revision/latest?cb=20141211231644)^^^so ^^^do ^^^cows."

    elif trigger.startswith("flynt"):
        rand = randint(0, 9)
        if rand == 0:
            return "[He's cool!](http://vignette2.wikia.nocookie.net/rwby/images/d/d9/Flynt_ProfilePic_Normal.png/revision/latest?cb=20160216144432)"
        return "[Flynt Coal](https://youtu.be/ka7q84C-E4c)"

    elif trigger.startswith("sage"):
        return "[He has a big sword!](http://vignette3.wikia.nocookie.net/rwby/images/c/c8/Sage_ProfilePic_Normal.png/revision/latest?cb=20151016080153)"

    elif trigger.startswith("lisa"):
        return "She is well informed."

    elif trigger.startswith("peach"):
        return "I've heard she's nice. Never met her though."

    elif trigger.startswith("perry"):
        return "You're great!"

    elif trigger.startswith("emerald"):
        return "I think she's involved in killing me, I'm not sure how."

    #Ship responses

    elif trigger.startswith("who do you ship"):
        return choice([
            "I think Ruby is cute...",
            "Weiss's scar is kind of cool!",
            "Blake's ears are really cute.",
            "Yang is hot!",
            "Pyrrha was nice...",
            "Jaune's beard is dreamy.",
            "Nora is energetic!",
            "Maybe not Ren, it feels wrong for some reason...",
            "Velvet's weapon is really cool!",
            "I'd like to get ice cream with Neo!"
        ])

    elif trigger.startswith("bumblebee"):
        return "I think they're cute together!"

    elif trigger.startswith("ladybug"):
        return "Now that, is a katana!"

    elif trigger.startswith("nuts and dolts"):
        return choice([
            "[She's so pretty!](http://fav.me/d9k3n6r)",
            "[Kiss!](http://fav.me/d9fxci1)",
            "[She's a good mechanic!](http://fav.me/d989o9k)",
            "Well, Ruby does look more mature now. I like it!"
        ])

    elif trigger.startswith("enabler"):
        return "[No](http://65.media.tumblr.com/b6c7745211872cd227db9b6188aac928/tumblr_inline_naaj8hywWE1rltz3k.png) \n \n ^^^maybe"

    elif trigger.startswith("arkos"):
        return "Sometimes the brightest loves burn the shortest... ^^^Cinder ^^^is ^^^evil!"

    elif trigger.startswith("baked alaska"):
        return "I don't think Raven approves... ^^which ^^only ^^makes ^^it ^^better!"

    elif trigger.startswith("crosshares"):
        return "[I wanted Velvet's ears!](http://66.media.tumblr.com/0bcf2153ced4e47349e8d2737b83f4cd/tumblr_o9ptcnv2rk1tmkeo6o2_1280.jpg)"

    elif trigger.startswith("lancaster"):
        return "If Ruby is happy, but I mean Jaune does look like her Dad... "

    elif trigger.startswith(("eclipse", "black sun")):
        return "I wonder if Blake likes to play with Sun's tail?"

    elif trigger.startswith("white knight"):
        return "Weiss does not seem to like him, besides he's taken!"

    elif trigger.startswith("frozen steel"):
        return "[It's a Ruby sandwich!](http://65.media.tumblr.com/d8d679901bb89d1bced1018b5f613c0b/tumblr_o5bwpqVF2v1ungotoo1_1280.jpg)"

    elif trigger.startswith("fallen petals"):
        return "[You want to repeat that?](http://fav.me/d6u7s83)"

    elif trigger.startswith("sugar rush"):
        return "The chaos would be, well not even Glynda would be able to fix it."

    elif trigger.startswith("iron witch"):
        return "I mean, she does have a crop. How could it not be weird?"

    elif trigger.startswith("bumblebee"):
        return choice([
            "[It's a wild ride!](http://orig15.deviantart.net/587e/f/2014/145/1/3/bumblebee_ride_by_kinzaibatsu91-d7jqtqe.gif)",
            "[Things will get better.](http://i.imgur.com/KuBcQn3.png)",
            "[Gay.](http://i.imgur.com/okf2U9l.gif)",
            "[Going on a date!](http://fav.me/d9nu92y)",
            "[I have the same question as Ruby.](http://fav.me/d7nf7ax)",
            "[They are so cute together!](http://img06.deviantart.net/0aed/i/2014/250/3/2/rwby___bumblebee_morning_by_dishwasher1910-d7yaigp.png)",
            "[Ruby says they're loud sometimes.](http://67.media.tumblr.com/c7568b33ad1e9506205e05e1466c177d/tumblr_n0sxr1xrs81sgvrqvo1_1280.jpg)",
            "[I think they're cute!](https://d.wattpad.com/story_parts/196599478/images/142096186ce87ebd.jpg)",
            "[She is very pretty!](http://vignette4.wikia.nocookie.net/rwby/images/9/91/YangBike.png/revision/latest?cb=20130613124150)",
            "[They're cute!](http://fav.me/da64cya)"
        ])

    elif trigger.startswith("white rose"):
        return choice([
            "[Kiss!](http://fav.me/d7mqa2c)",
            "[Sooo cute!](http://fav.me/d9jcmp7)",
            "[Look out Weiss!](http://i.imgur.com/5EnNbW5.jpg)",
            "If it makes Ruby happy...",
            "[I'm not sure I get it.](https://s-media-cache-ak0.pinimg.com/736x/45/3a/bc/453abcee3c4eb145bb4b685c4b56e289.jpg)"
            "[It's always the eyepatches.](http://fav.me/d6yzr5e)",
            "[Cookies!](http://fav.me/d93usd5)",
            "[Falling in love!](http://i55.servimg.com/u/f55/17/91/58/60/tumblr14.jpg)",
            "[Hugs!](http://orig00.deviantart.net/7278/f/2014/121/b/6/cudddle_by_xenon54165-d7gpjg3.jpg)",
            "[Chibi!](http://fav.me/d90q9qm)"
        ])

    elif trigger.startswith("monochrome"):
        return choice([
            "[Accidental Monochrome?](http://imgur.com/a/FcglH)",
            "[Knock next time!](http://66.media.tumblr.com/48f256aee523a116bcc9b1d814a3a7b3/tumblr_niv4t08Mdm1rlvki1o1_1280.png)"
            "[She's got ears too!](https://36.media.tumblr.com/6c939d62b0f87edf201fadda1cd0fb1a/tumblr_inline_nzqvricZB61qf2bb8_540.png)",
            "[They really trust one another!](http://67.media.tumblr.com/4b256d1572d1bd39961abeff670f3f39/tumblr_inline_o9vkfk2izn1qf2bb8_1280.png)",
            "[They found it!](http://67.media.tumblr.com/1311c01ee8370075334eb52ea297a32a/tumblr_inline_o97ak2EgMx1qf2bb8_500.png)",
            "[They look cool in their new outfits!](http://67.media.tumblr.com/1a38a8e8d6f52d6a10a6481818ffcdd1/tumblr_o9pv89YKuC1qfizj4o1_1280.png)",
            "[Team monochrome for life!](http://fav.me/d7xgq6c)",
            "[Kiss!](http://fav.me/d7zoefu)",
            "[Nuzzling?](http://fav.me/d7wk470)",
            "[Could someone pet me?(https://s-media-cache-ak0.pinimg.com/736x/c0/7f/47/c07f47d6ff04178121c891aa1828573a.jpg)"
        ])

    elif trigger.startswith("sea monkeys"):
        return "[Oh myyyy!](http://img07.deviantart.net/9ba3/i/2015/253/b/f/rwby___seamonkeys_by_mangarainbow-d9937ib.jpg)"

    elif trigger.startswith("arkos"):
        return choice([
            "[Did I hear wedding bells?](http://67.media.tumblr.com/08d4734bde97daf14f8d44293d511a26/tumblr_nlb8aeMiNN1r4vgpvo2_1280.png)",
            "[Even I knew she liked you!](http://img03.deviantart.net/ecd2/i/2015/321/a/e/rwby__arkos_shippers_be_like____by_billiam_x-d9h10la.jpg)",
            "[Awwwww!](https://s-media-cache-ak0.pinimg.com/564x/2c/f1/3a/2cf13a0f206b7cffb323316c4a1e0f36.jpg)",
            "It's the only ship my creator really supports.",
            "[In their prime.](https://pbs.twimg.com/media/CV33NB0VAAAcHLs.png)",
            "[Nora supports it!](http://i.imgur.com/OQ3HEux.jpg)",
            "[Pyrrha carrying the team.](http://fav.me/d6iyzs5)",
            "[Can we remember the laughter?](http://i.imgur.com/lKVR6Vk.jpg)",
            "[Hugs!](http://i.imgur.com/NJfQ5LB.jpg)",
            "[They're so happy together!](http://66.media.tumblr.com/3a184662b6ccb79821f4d7ac5883bbcd/tumblr_o00q63J9Ky1r4vgpvo1_1280.jpg)"
        ])

    elif trigger.startswith("crosshares"):
        return "[They look so cute together!](http://65.media.tumblr.com/b9481a46d530e7ba09d54a434dc777de/tumblr_o69qt2Xch31tmkeo6o1_1280.jpg)"

    elif trigger.startswith("falling petals"):
        return "[Ruby? Are you OK?](http://i.imgur.com/sO1nFXq.png)"

    elif trigger.startswith("pussy magnet"):
        return "[Alright...](http://i.imgur.com/d3zz3tH.jpg)"

    elif trigger.startswith("ninjas of love"):
        return "Ruby said it was smut, I'm not sure what that is. I'll have to do research!"

    elif trigger.startswith("catfish"):
        return "[You mean this?](http://i.imgur.com/aTmiEhG.png)"

    elif trigger.startswith("renora"):
        return "[I'm sure they Boop!](http://i.imgur.com/JXYQlnd.png)"

    #Episode lookup

    elif trigger.startswith("s1e10"):
        return "[Here is the episode!](https://youtu.be/57f_t1ioOws)"

    elif trigger.startswith("s1e11"):
        return "[Here is the episode!](https://youtu.be/N5D0NDAR8sU)"

    elif trigger.startswith("s1e12"):
        return "[Here is the episode!](https://youtu.be/M_Loqu0jo7k)"

    elif trigger.startswith("s1e13"):
        return "[Here is the episode!](https://youtu.be/h0QiT-GxN6k)"

    elif trigger.startswith("s1e14"):
        return "[Here is the episode!](https://youtu.be/PS9huFMmSoc)"

    elif trigger.startswith("s1e15"):
        return "[Here, remember someone important shows up in this episode!](https://youtu.be/KHynQoJgbgc)"

    elif trigger.startswith("s1e16"):
        return "[Here is the episode!](https://youtu.be/3b1gs8KrM-M)"

    elif trigger.startswith("s1e1"):
        return "[Here is the episode!](https://youtu.be/-sGiE10zNQM)"

    elif trigger.startswith("s1e2"):
        return "[Here is the episode!](https://youtu.be/sLv6FfHlxmI)"

    elif trigger.startswith("s1e3"):
        return "[Here is the episode!](https://youtu.be/-ZwGeYu2pOQ)"

    elif trigger.startswith("s1e4"):
        return "[Here is the episode!](https://youtu.be/H09KTtyElWQ)"

    elif trigger.startswith("s1e5"):
        return "[Here is the episode!](https://youtu.be/1JZgPfbKbU4)"

    elif trigger.startswith("s1e6"):
        return "[Here is the episode!](https://youtu.be/N1TJ5YA3jfw)"

    elif trigger.startswith("s1e7"):
        return "[Here is the episode!](https://youtu.be/z8wPhihrzvU)"

    elif trigger.startswith("s1e8"):
        return "[Here is the episode!](https://youtu.be/ctiDu69kIho)"

    elif trigger.startswith("s1e9"):
        return "[Here is the episode!](https://youtu.be/-E6aeUjfBCM)"

    elif trigger.startswith("s2e1"):
        return "[Here is the episode!](https://youtu.be/PzPZ6joXq5Y)"

    elif trigger.startswith("s2e10"):
        return "[Here is the episode!](https://youtu.be/lD4x6NiTiM4)"

    elif trigger.startswith("s2e11"):
        return "[Here is the episode!](https://youtu.be/CUYhvPoxuas)"

    elif trigger.startswith("s2e12"):
        return "[Here is the episode!](https://youtu.be/-p4iS_p3b8E)"

    elif trigger.startswith("s2e2"):
        return "[Here is the episode!](https://youtu.be/bdiV-w3yXos)"

    elif trigger.startswith("s2e3"):
        return "[Here is the episode!](https://youtu.be/mj3jfqPwJEk)"

    elif trigger.startswith("s2e4"):
        return "[Here is the episode!](https://youtu.be/a1EuyliSO_Q)"

    elif trigger.startswith("s2e5"):
        return "[Here is the episode!](https://youtu.be/nur1pCHD4hU)"

    elif trigger.startswith("s2e6"):
        return "[Here is the episode!](https://youtu.be/i7wkw3yEbvQ)"

    elif trigger.startswith("s2e7"):
        return "[Here is the episode!](https://youtu.be/0-f-mGvOba8)"

    elif trigger.startswith("s2e8"):
        return "[Here is the episode!](https://youtu.be/bSdejzDaQEU)"

    elif trigger.startswith("s2e9"):
        return "[Here is the episode!](https://youtu.be/GJGSywhNk8Q)"

    elif trigger.startswith("s3e10"):
        return "[Here is the episode!](https://youtu.be/bIKyZi2q8w8)"

    elif trigger.startswith("s3e11"):
        return "[Here is the episode!](https://youtu.be/pT1XiUbJu_Y)"

    elif trigger.startswith("s3e12"):
        return "[Here is the episode!](https://youtu.be/hq1lk-QWxNg)"

    elif trigger.startswith("s3e1"):
        return "[Here is the episode!](https://youtu.be/W9wyWgvyp0s)"

    elif trigger.startswith("s3e2"):
        return "[Here is the episode!](https://youtu.be/RzEo0F8thL4)"

    elif trigger.startswith("s3e3"):
        return "[Here is the episode!](https://youtu.be/vCO2mw4SlDM)"

    elif trigger.startswith("s3e4"):
        return "[Here is the episode!](https://youtu.be/fBy2W99zaLQ)"

    elif trigger.startswith("s3e5"):
        return "[Here is the episode!](https://youtu.be/G5uFH7gIClw)"

    elif trigger.startswith("s3e6"):
        return "[Here is the episode!](https://youtu.be/moxtu3AuA4s)"

    elif trigger.startswith("s3e7"):
        return "[Here is the episode!](https://youtu.be/FFf7qoIDYuQ)"

    elif trigger.startswith("s3e8"):
        return "[Here is the episode!](https://youtu.be/u7uU_tKYHiM)"

    elif trigger.startswith("s3e9"):
        return "[Here is the episode... Why do you want to watch this?](https://youtu.be/_iq4xplqeI0)"

    elif trigger.startswith("s4e1"):
        return "[Here is the episode!](https://youtu.be/dQw4w9WgXcQ)"

    elif trigger.startswith(("wor 1", "wor1")):
        return "[Here it is!](https://youtu.be/9BJc7nrMnc4)"

    elif trigger.startswith(("wor 2", "wor2")):
        return "[Here it is!](https://youtu.be/AvUT2rHKJDs)"

    elif trigger.startswith(("wor 3", "wor3")):
        return "[Here it is!](https://youtu.be/-PE66fmjZ0I)"

    elif trigger.startswith(("wor 4", "wor4")):
        return "[Here it is!](https://youtu.be/946xgoU4fkQ)"

    elif trigger.startswith(("wor 5", "wor5")):
        return "[Here it is!](https://youtu.be/k6rZFLYHZfI)"

    elif trigger.startswith(("wor 6", "wor6")):
        return "[Here it is!](https://youtu.be/yiJU9QeG89g)"

    elif trigger.startswith(("wor 7", "wor7")):
        return "[Here it is!](https://youtu.be/2bBSQA3uXVo)"

    elif trigger.startswith("chibi e1"):
        return "[Ruby has trouble with cookies!](https://youtu.be/WD-Yf-tbXOs)"

    elif trigger.startswith("chibi e2"):
        return "[The racist episode!](https://youtu.be/ztK2RJ8_RvA)"

    elif trigger.startswith("chibi e3"):
        return "[Phone mailboxes, how do they work?](https://youtu.be/-B6IrE_luls)"

    elif trigger.startswith("chibi e4"):
        return "[Anger, Dust, and Marshmallows!](https://youtu.be/Ig79EpeF_48)"

    elif trigger.startswith("chibi e5"):
        return "[Ears, Showdown, and Shadows!](https://youtu.be/A6sWqoau_QQ)"

    elif trigger.startswith("chibi e6"):
        return "[Breaking the fourth wall.](https://youtu.be/IX1hxJ-0fDY)"

    elif trigger.startswith("chibi e7"):
        return "[Pranks and Weapons!](https://youtu.be/9zMYq3wKQbU)"

    elif trigger.startswith("chibi e8"):
        return "[Even the compass is telling you.](https://youtu.be/gH8zmxLEr_s)"

    elif trigger.startswith("chibi e9"):
        return "[You made me tag you!](https://youtu.be/WW3Pm5pdajw)"

    elif trigger.startswith("chibi e10"):
        return "[Notice me!](https://youtu.be/6iVP0ufPRbs)"

    elif trigger.startswith("dust"):
        return "[Here it is!](https://youtu.be/9BJc7nrMnc4)"

    elif trigger.startswith("kingdom"):
        return "[Here it is!](https://youtu.be/AvUT2rHKJDs)"

    elif trigger.startswith("grimm"):
        return "[Here it is!](https://youtu.be/-PE66fmjZ0I)"

    elif trigger.startswith("history"):
        return "[Here it is!](https://youtu.be/946xgoU4fkQ)"

    elif trigger.startswith("huntsman"):
        return "[Here it is!](https://youtu.be/k6rZFLYHZfI)"

    elif trigger.startswith("ccts"):
        return "[Here it is!](https://youtu.be/yiJU9QeG89g)"

    elif trigger.startswith("maidens"):
        return "[Here it is!](https://youtu.be/2bBSQA3uXVo)"

    #Secret commands


    else:
        return "Salutations!"

