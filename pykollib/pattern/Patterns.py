"""
This module holds all of the regular expression patterns that pykol uses. It makes sense
to store them all in the same place since many patterns are used by multiple requests.
The 'patterns' data object is a dictionary mapping patternId to pattern. If pattern is a tuple,
then the first element of the tuple should be the pattern while the second element is a flag
to pass to re.compile (like re.DOTALL).
"""

import re

patterns = {
    # General patterns.
    "whitespace": r"([\t ]+)",
    "results": r"<b>Results:<\/b><\/td><\/tr><tr><td[^<>]*><center><table><tr><td>(.*?)</td></tr></table></center></td></tr>",
    "htmlComment": r"<!--.*?-->",
    "htmlTag": r"<[^>]*?>",
    # Login-related patterns.
    "accountPwd": r'var pwdhash = "([0-9a-f]+)";',
    "accountId": r"var playerid = ([0-9]+);",
    "accountName": r'<a [^<>]*href="charsheet\.php">(?:<b>)?([^<>]+)<',
    "loginChallenge": r'name="?challenge"?\s+value="?([0-9a-f]+)"?',
    # Item-related patterns.
    "menuItem": r'<input type=radio name=whichitem value="?(-?[0-9]+)"?></td><td><img .*? onclick=\'descitem\("?([^"]+)"?\);\'>',
    "gainMeat": r'<td><img src="[^"]*meat\.gif"[^>]*><\/td><td[^>]*>You gain ([0-9,]*?) Meat\.<\/td>',
    "loseMeat": r"You lose ([0-9,]*?) Meat",
    "isCocktailcraftingIngredient": (r"<br>\(Cocktailcrafting ingredient\)<br>"),
    "isCookingIngredient": r"<br>\(Cooking ingredient\)<br>",
    "isJewelrymakingComponent": r"<br>\(Jewelrymaking component\)<br>",
    "isMeatsmithingComponent": r"<br>\(Meatsmithing component\)<br>",
    "inventorySingleItem": r"<img [^>]*descitem\(([0-9]+)[^>]*></td><td[^>]*><b[^>]*>([^<>]+)</b>&nbsp;<span><\/span>",
    "inventoryMultipleItems": r"<img [^>]*descitem\(([0-9]+)[^>]*></td><td[^>]*><b[^>]*>([^<>]+)</b>&nbsp;<span>\(([0-9]+)\)<\/span>",
    "itemAutosell": r"<br>Selling Price: <b>(\d*) Meat\.<\/b>",
    "itemImage": r'\/images\.kingdomofloathing\.com\/itemimages\/(.*?)"',
    "itemName": r"<b>(.+?)<\/b>",
    "itemType": r"<br>Type: <b>([^<]*)<.*\/b><br>",
    "tooFull": r"You're too full to eat that\.",
    "tooDrunk": r"You're way too drunk already\.",
    "notBooze": r"That's not booze\.",
    "notFood": r"That's not something you can eat\.",
    # Message-related patterns.
    "brickMessage": r"\/\/images\.kingdomofloathing\.com\/adventureimages\/(brokewin|bigbrick)\.gif",
    "candyHeartMessage": r"\/\/images\.kingdomofloathing\.com\/otherimages\/heart\/hearttop\.gif",
    "coffeeMessage": r"\/\/images\.kingdomofloathing\.com\/otherimages\/heart\/cuptop\.gif",
    "fullMessage": (
        '<tr><td[^>]*><input type=checkbox name="sel([0-9]+)".*?<b>[^<]*<\/b> <a href="showplayer\.php\?who=([0-9]+)">([^<]*)<\/a>.*?<b>Date:<\/b>([^<]*?)</b>.*?<blockquote>(.*?)<\/blockquote>',
        re.DOTALL,
    ),
    "userInHardcoreRonin": r"<center><table><tr><td>That player cannot receive Meat or items from other players right now\.",
    "userIgnoringUs": r"<center><table><tr><td>This message could not be sent, because you are on that player's ignore list\.<\/td><\/tr><\/table><\/center>",
    "userInvalid": r"<td>Invalid PlayerID.</td>",
    "notEnoughItemsToSend": r"<center><table><tr><td>You don't have enough of one of the items you're trying to send\.<\/td><\/tr><\/table><\/center>",
    "messageSent": r"<td><center>Message sent\.<\/center><\/td>",
    "kmailNotSentUserTrendy": r"<center><table><tr><td>That player would never use something as old and outmoded as",
    "weAreIgnoringUser": r"<td>This message could not be sent, because that player is on your ignore list\.<\/td>",
    # Error patterns.
    "notEnoughItems": r"(?:<td>You haven't got that many\.<\/td>)|(?:You don't have the item you're trying to use\.)|(?:You don't have the item you're trying to equip\.)",
    # Chat patterns.
    "chatChannel": r'^<font color="?#?\w+"?>\[([^<>]+)\]<\/font> ',
    "chatMessage": r'<b><a target="?mainpane"? href="showplayer\.php\?who=(-?[0-9]+)"><font color="?#?\w+"?>([^<>]+)<\/font>(?:<\/b>|<\/a>|:)* (.*)$',
    "chatEmote": r'<b><i><a target="?mainpane"? href="showplayer\.php\?who=([0-9]+)"><font color="?#?\w+"?>([^<>]+)<\/b><\/font><\/a> (.*)<\/i>$',
    "privateChat": r'<a target="?mainpane"? href="showplayer\.php\?who=([0-9]+)"><font color="?blue"?><b>([^)]+) \(private\):<\/b><\/font><\/a> <font color="?blue"?>(.*)</font>$',
    "chatNewKmailNotification": r'<a target="?mainpane"? href="messages\.php"><font color="?green"?>New message received from <a target="?mainpane"? href=\'showplayer\.php\?who=([0-9]+)\'><font color="?green"?>([^<>]+)<\/font><\/a>\.<\/font><\/a>$',
    "chatLink": r'<a target="?_blank"? href="([^"]+)"><font color="?blue"?>\[link\]<\/font><\/a> ',
    "chatWhoResponse": r"<table><tr><td class=tiny><center><b>Players in (?:this channel|channel \w+):",
    "chatWhoPerson": r'<a (?:class="([^"]+)" )?target="?mainpane"? href="showplayer\.php\?who=([0-9]+)"><font color="?#?\w+"?>([^<>]+)<\/font><\/a>',
    "chatLinkedPlayer": r"<a style='color: #?\w+' href='showplayer\.php\?who=([0-9]+)' target=mainpane>([^<]+)<\/a>",
    "newChatChannel": r"<font color=[^>]+>You are now talking in channel: ([^\,]+?)\.<p><p>(.*?)</font>",
    "chatListenResponse": r"<font color=[^>]+>Currently listening to channels:(.*?<b>.*?</b>.*?)</font>",
    "chatListenCurrent": r"<br>&nbsp;&nbsp;<b>(.*?)</b>",
    "chatListenOthers": r"&nbsp;&nbsp;([^<>]*?)<br>",
    "chatStartListen": r"<font color=[^>]+>Now listening to channel: ([^>]+)</font>",
    "chatStopListen": r"<font color=[^>]+>No longer listening to channel: ([^>]+)</font>",
    "chatMultiLineStart": r'<b><a target="?mainpane"? href="showplayer\.php\?who=(-?[0-9]+)"><font color="?#?\w+"?>([^<>]+)<\/font><\/b><\/a>:$',
    "chatMultiLineEmote": r'<b><i><a target="?mainpane"? href="showplayer\.php\?who=(-?[0-9]+)"><font color="?#?\w+"?>([^<>]+)<\/b><\/font><\/a>$',
    "outgoingPrivate": r'<font color="?blue"?><b>private to <a class=nounder target="?mainpane"? href="?showplayer.php\?who=([0-9]+)"?><font color="?blue"?>(.*?)</font></a></b>:(.*?)</font></br>',
    "chatPlayerLoggedOn": r"<font color=green><a target=mainpane href=\'showplayer\.php\?who=([0-9]+)\'><font color=green><b>([^<>]+)<\/b><\/font><\/a> logged on\.<\/font>$",
    "chatPlayerLoggedOff": r"<font color=green><a target=mainpane href=\'showplayer\.php\?who=([0-9]+)\'><font color=green><b>([^<>]+)<\/b><\/font><\/a> logged off\.<\/font>$",
    "chatTalkieFrequency": r"<font color=green>The frequency is (.*?), Mr. Rather\.<\/font>",
    "chatCarnival": r'<font color="?green"?>(?:.*?)testlove=([0-9]+)\'>consult Madame Zatara about your relationship<\/a> with ([^<>]+?)\.<\/font>',
    # Clan dungeon patterns.
    "dungeonActivity": r"(?:^|<blockquote>|<br>|<br><b>|<b>)([^<>]+) \(#([0-9,]+)\) ((?:[^<>](?!(?:\([0-9]+ turns?\))))+)(?: \(([0-9,]+) turns?\))?",
    "dungeonLootDistribution": r"(?:<blockquote>|<br>)([^<>]+) \(#([0-9,]+)\) distributed <b>([^<>]+)</b> to ([^<>]+) \(#([0-9,]+)\)<br>",
    "dungeonPreviousRun": r'<tr><td class="?small"?>([^<>]+)&nbsp;&nbsp;<\/td><td class="?small"?>([^<>]+)&nbsp;&nbsp;<\/td><td class="?small"?>([^<>]+)&nbsp;&nbsp;<\/td><td class="?small"?>([0-9,]+)<\/td><td class="?tiny"?>\[<a href="clan_raidlogs\.php\?viewlog=([0-9]+)">view logs<\/a>\]<\/td><\/tr>',
    "dungeonLogType": r"<div id=[^>]+><center><b>([^:]+):<!--[^:]+:([0-9]+)--></b><p><table[^>]+><tr><td[^>]+>(.*?)</table></div>",
    "dungeonLogStatus": r"<center>(.*?)<b>([0-9]+)<\/b> (.*?).</center>",
    "dungeonLogCategory": r"<b>([^<>]+):?<\/b><blockquote>(.*?)<\/blockquote>",
    "imprisonedByChums": r"^(.*) has been imprisoned by the C\. H\. U\. M\.s!$",
    "freedFromChums": r"^(.*) has rescued (.*) from the C\. H\. U\. M\.s\.$",
    "chefExplosion": r"Smoke begins to pour from the head of your chef-in-the-box. It begins to vibrate noisily, spits out a few dishes at random, and then explodes\.",
    # Stat, Substat, Leveling, HP, and MP patterns. Will fail in Haiku Dungeon.
    "muscleGainLoss": r"You (gain|lose) ([0-9,]+) (?:Beefiness|Fortitude|Muscleboundness|Strengthliness|Strongness)",
    "mysticalityGainLoss": r"You (gain|lose) ([0-9,]+) (?:Enchantedness|Magicalness|Mysteriousness|Wizardliness)",
    "moxieGainLoss": r"You (gain|lose) ([0-9,]+) (?:Cheek|Chutzpah|Roguishness|Sarcasm|Smarm)",
    "musclePointGainLoss": r"You (gain|lose) (a|some) Muscle points?",
    "mystPointGainLoss": r"You (gain|lose) (a|some) Mysticality points?",
    "moxiePointGainLoss": r"You (gain|lose) (a|some) Moxie points?",
    "levelGain": r"You gain (a|some) (?:L|l)evels?",
    "hpGainLoss": r"You (gain|lose) ([0-9,]+) hit points?",
    "mpGainLoss": r"You (gain|lose) ([0-9,]+) (?:Muscularity|Mana|Mojo) (?:P|p)oints?",
    # Drunkenness, Adventures, and Effect patterns.
    "gainDrunk": r"You gain ([0-9]+) Drunkenness",
    "gainAdventures": r"You gain ([0-9,]+) Adventures",
    "gainEffect": r"<td valign=center class=effect>You acquire an effect: <b>(.*?)</b><br>\(duration: ([0-9,]+) Adventures\)</td>",
    # Meatpasting patterns.
    "noMeatForMeatpasting": r"<td>You don't have enough Meat to make that many\.</td>",
    # Store patterns.
    "meatSpent": r"You spent ([0-9,]+) Meat",
    "noMeatForStore": r"(?:You can't afford that many of that item)|(?:You can't afford that item)|(?:You can't afford to purchase that)",
    "invalidStore": r"You've been sent back here by some kind of bug",
    "notSoldHere": r"(?:This store doesn't sell that item)|(?:Invalid item selected)",
    "storeInventory": r'<tr class="deets" rel="([0-9]+)" after="([0-9]+)">(.*?)<b>(.*?)</b></td><td valign="center" align="center">([0-9]+)</td(.*?)name="price\[([0-9]+)\]" value="([0-9,]+)"(.*?)name="limit\[[0-9]+\]" value="([0-9]+)"(.*?)cheapest: ([0-9]+)</span>',
    # Hermit patterns.
    "noTrinkets": r"You don't have enough stuff",
    "noHermitPermits": r"You don't have enough Hermit Permits to trade for that many",
    "notEnoughClovers": r"you are able to infer that he doesn't have enough clovers to make that trade",
    "notHermitItem": r"The Hermit doesn't have that item",
    # Adventure patterns.
    "twiddlingThumbs": r"You twiddle your thumbs\.",
    "userShouldNotBeHere": r"(?:>You shouldn't be here\.<)|(?:)>This is not currently available to you\.<",
    "monsterName": r"<span id='monname'>(.*?)<\/span>",
    "choiceIdentifier": r'<input type="?hidden"? name="?whichchoice"? value="?([0-9]+)"?>',
    "choiceName": r"<b>([^<>]+?)<\/b><\/td><\/tr>",
    "noncombatName": r"<center><table><tr><td><center><b>([^<>]+)<\/b><br><img",
    "fightWon": r"<center>You win the fight!<!--WINWINWIN--><p>",
    "fightLost": r"<p>You lose\. +You slink away, dejected and defeated\.<p>",
    "usedBarrel": r"KOMPRESSOR does not smash",
    "noAdventures": r"You're out of adventures",
    # Rumpus Room patterns.
    "rumpusRoomFurniture": r"rump([0-9])_([0-9])\.gif",
    # Mall search patterns.
    "mallItemSearchResult": r'<tr class="graybelow(.*?)<\/tr>',
    "mallItemSearchDetails": r'<a[^<>]*href="mallstore\.php\?whichstore=(?P<storeId>[0-9]+)&searchitem=(?P<itemId>[0-9]+)&searchprice=(?P<price>[0-9]+)"><b>(?P<storeName>.*?)<\/b><\/a>[^<>]*<\/td><td[^<>]*>(?P<quantity>[0-9,]+)<\/td><td[^<>]*>(?:&nbsp;)*(?P<limit>[0-9,]*)[^<>]*<\/td>',
    "nextLink": r"\[<a [^>]*start=([0-9]+)[^>]*>next</a>\]",
    "mallItemHeader": r"<tr class=.blackabove. id=.item_([0-9]+)[^0-9]>",
    # Mall purchase patterns.
    "cantAffordItem": r"<td>You can't afford that item\.<\/td>",
    "mallNoItemAtThatPrice": r"<td>This store doesn't have that item at that price\.",
    "cantBuyItemIgnoreList": r"<td>That player will not sell to you, because you are on his or her ignore list\.<\/td>",
    "mallHitLimit": r"You may only buy ([0-9,]+) of this item per day from this store\. You have already purchased ([0-9,]+) in the last 24 hours\.",
    # Canadia patterns.
    "noAdvInstitue": r">You don't have that many Adventures\.  Take off, eh\?<",
    "invalidAdvInstitute": r">That doesn't make any sense, you hoser\.<",
    # Guild patterns.
    "skillNotTrainable": r">Invalid skill selected\.<",
    "skillTooWeak": r">You're not powerful enough to train that skill\.<",
    "skillTooPoor": r">You can't afford to train that skill\.<",
    "skillLearned": r">You learn a new skill: <b>(.*?)</b>",
    "skillHaveAlready": r">You've already got that skill\.<",
    # Equipment patterns
    "currentHat": r"Hat</a>:</td><td><img src=\"[^\"]+\" class=hand onClick='descitem\(([0-9]+)\)'",
    "currentWeapon": r"Weapon</a>:</td><td><img src=\"[^\"]+\" class=hand onClick='descitem\(([0-9]+)\)'",
    "currentOffhand": r"Offhand</a>:</td><td><img src=\"[^\"]+\" class=hand onClick='descitem\(([0-9]+)\)'",
    "currentShirt": r"Shirt</a>:</td><td><img src=\"[^\"]+\" class=hand onClick='descitem\(([0-9]+)\)'",
    "currentPants": r"Pants</a>:</td><td><img src=\"[^\"]+\" class=hand onClick='descitem\(([0-9]+)\)'",
    "currentAcc": r"Accessory</a>:</td><td><img src=\"[^\"]+\" class=hand onClick='descitem\(([0-9]+)\)'",
    "currentAcc1": r"Accessory</a>&nbsp;1:</td><td><img src=\"[^\"]+\" class=hand onClick='descitem\(([0-9]+)\)'",
    "currentAcc2": r"Accessory</a>&nbsp;2:</td><td><img src=\"[^\"]+\" class=hand onClick='descitem\(([0-9]+)\)'",
    "currentAcc3": r"Accessory</a>&nbsp;3:</td><td><img src=\"[^\"]+\" class=hand onClick='descitem\(([0-9]+)\)'",
    "currentFam": r"Familiar</a>:</td><td><img src=\"[^\"]+\" class=hand onClick='descitem\(([0-9]+)\)'",
    # Ascension History patterns.
    "fullAscension": r'</tr><td[^>]*>([0-9]+).*?</td><td[^>]*>([0-9/]+).*?</td><td[^>]*><span[^>]*>([0-9,]+).*?</span>.*?</td><td[^>]*><img [^>]*title="(.*?)"[^>]*></td><td[^>]*>(.*?)</td><td[^>]*>(<span[^>]*>)?([0-9,]+)(</span>)?</td><td[^>]*>(<span[^>]*>)?([0-9,]+)(</span>)?</td><td[^>]*>(?:<img [^>]*title="(.*?)"[^>]*>)?</td><td[^>]*>(<img [^>]*title="(.*?)"[^>]*>|<img src="http://images\.kingdomofloathing\.com/otherimages/spacer.gif" width=30 height=30>)(<img [^>]*title="(.*?)"[^>]*>|</td>)',
    "familiarAscension": r"^(.*?) \(([0-9.]+)%\)",
    "playerName": r"Ascension History \(<a[^>]*><font[^>]*>(.*?)<\/font><\/a>\)",
    # Clan patterns.
    "clanName": r'<a href="clan_hall\.php">([^<>]*)<\/a>',
    "clanCredo": r"<textarea name=newcredo[^<>]*>([^<>]*)</textarea>",
    "clanWebsite": r'<input type=text class=text name=website value="([^"]*)" size=60 maxlength=255>',
    "clanAcceptingApps": r"<p>Your clan is currently accepting applications\.<br>",
    "clanRankContainer": r"<select name=level[0-9]+>(.*?)<\/select>",
    "clanRank": r"<option value=([0-9]+)(?: selected)?>(.*?) \(&deg;([0-9]+)\)<\/option>",
    "clanWhitelistMember": r"""<tr><td><input type=hidden name=(?:player[0-9]+|who) value=[0-9]+><a href='showplayer\.php\?who=(?P<userId>[0-9]+)' class=nounder><b>(?P<userName>[^<>]+)</b> \(#[0-9]+\)<\/a><\/td><td>(?:<select.*?<option value=(?P<clanRankId>[0-9]+) selected>.*?<\/select>|(?P<clanRankName>[^<>]+))<\/td><td>(?:<input type=text class=text size=[0-9]+ name=title[0-9]+ value=")?(?P<clanTitle>[^<>]*)(?:">)?<\/td>""",
    "clanLogEntry": r">(?P<date>[0-9/]+, [0-9:]+(?:AM|PM)): (?:<a class=nounder href=\'showplayer\.php\?who=[0-9]+\'>)?(?P<userName>[^<>]+) \(#(?P<userId>[0-9]+)\)(?:<\/a>)? (?P<action>.*?)(?=<br>)",
    "clanLogFax": r"faxed in a (?P<monsterName>.*)$",
    "clanLogAttack": r"launched an attack against (?P<clanName>.*)\.$",
    "clanLogWhitelistAdd": r"added <a class=nounder href=\'showplayer\.php\?who=[0-9]+\'>(?P<userName>.*) \(#(?P<userId>[0-9]+)\)<\/a> to the clan\'s whitelist\.$",
    "clanLogPlayerJoinedAnotherClan": r"joined another clan\.$",
    "clanLogPlayerJoinedClanWhitelist": r"was accepted into the clan \(whitelist\)$",
    "clanLogStashItemAdd": r"added (?P<quantity>[0-9,]+) (?P<itemName>.*)\.$",
    "clanLogStashItemRemove": r"took (?P<quantity>[0-9,]+) (?P<itemName>.*)\.$",
    "clanLogMeatSpentArmy": r"spent (?P<meat>[0-9,]+) Meat on the clan army\.$",
    "clanLogChangedRank": r"changed Rank for <a class=nounder href=\'showplayer\.php\?who=[0-9]+\'>(?P<userName>.*) \(#(?P<userId>[0-9]+)\)<\/a>\.$",
    "clanLogChangedTitle": r"changed title for <a class=nounder href=\'showplayer\.php\?who=[0-9]+\'>(?P<userName>.*) \(#(?P<userId>[0-9]+)\)<\/a>\. \((?P<clanTitle>.*)\)$",
    # Search player Patterns
    "searchPlayers": r'showplayer\.php\?who=([0-9]+)">([^<]*)<\/a>',
    # Traveling Trader Patterns
    "traderNotTradingForThatItem": r"<td>The trader is not trading for that item\.<\/td>",
    "traderCantTradeForThatMany": r"<td>You can\'t trade for that many ",
    "traderNotEnoughWads": r"<td>You don\'t have enough twinkly wads to trade for that many ",
    # Crimbo Patterns
    "crimboItemIsNotCandy": r"<td>That's not candy!<\/td>",
    "crimboNotEnoughCandy": r"<td>You don't have that much candy!<\/td>",
    "crimboCandyCreditsReceived": r"That gives you ([0-9,]+) Candy Credits?\.  You can trade in your",
    "crimboInvalidGift": r"<td>Invalid gift selected\.  Bah Humbug!<\/td>",
    "crimboInvalidPlayer": r"<td>Sorry, I couldn't find the player ",
    "crimboUserAlreadyReceivedGift": r"<td>The factory workers inform you that your intended recipient already has one of those\.<\/td>",
    # Nash Crosby's Still Patterns
    "wrongStillProfession": r"<td>No still for you\.<\/td>",
    "invalidStillItem": r"<td>Nash Crosby doesn\'t want anything to do with that item\.<\/td>",
    "stillItemNotFound": r"<td>You don\'t have that many of that item, Chief.<\/td>",
    "stillMaxLimit": r"<td>The still can\'t handle that much action today\.<\/td>",
    # Bounty Hunter Hunter patterns.
    "easyBountyAvailable": r'<input type=hidden name=action value=takelow><input class=button type=submit value="I\'ll Get These">',
    "hardBountyAvailable": r'<input type=hidden name=action value=takehigh><input class=button type=submit value="I\'ll Get These">',
    "specialBountyAvailable": r'<input type=hidden name=action value=takespecial><input class=button type=submit value="I\'ll Get These">',
    "easyBountyActive": r'<input class=button type=submit value="I Give Up!"><input type=hidden name=action value=giveup_low>',
    "hardBountyActive": r'<input class=button type=submit value="I Give Up!"><input type=hidden name=action value=giveup_high>',
    "specialBountyActive": r'<input class=button type=submit value="I Give Up!"><input type=hidden name=action value=giveup_special>',
    "bountyChosen": r"Come back when you've gotten the goods",
    # Wok related patterns.
    "dontHaveItemsForWok": r"<td>You don't have the materials for that amount of wokkage\.</td>",
    "dontHaveAdventuresForWok": r"<td>You don't have that many adventures left\.",
    "noWokAccess": "What wok are you tokking about\?",
    "dontHaveSkillForWok": r"<td>You don't have the skill necessary",
    # Sept 2013 Mall interface patterns
    "dontHaveEnoughOfItem": r"<td>You don't have enough of those",
    "dontHaveThatItem": r"<td>You don't have that item.([0-9]+)",
    "itemAddedSuccessfully": r"<td>\(([0-9]+)\) (.*) for ([0-9,]+) meat each",
    "dontHaveThatManyInStore": "You don't have that many in your store.",
    "itemTakenSuccessfully": "You acquire",
    "mallPricesUnlimited": r"<tr><td>unlimited:</td><td><b>([0-9,]+)</b> x([0-9]+).*?</td><td><b>([0-9,]+)</b> x([0-9]+).*?</td><td><b>([0-9,]+)</b> x([0-9]+).*?</td><td><b>([0-9,]+)</b> x([0-9]+).*?</td></tr>",
    "mallPricesLimited": r"<tr><td>limited:</td><td><b>([0-9,]+)</b>\(([0-9]+)/day\) x([0-9]+).*?</td><td><b>([0-9,]+)</b>\(([0-9]+)/day\) x([0-9]+).*?</td><td><b>([0-9,]+)</b>\(([0-9]+)/day\) x([0-9]+).*?</td></tr>",
    "mallPriceNotUpdated": "Nothing updated",
    "mallTransactions": r"([1-9][1-9]/[1-9][1-9]/[1-9][1-9] [1-9][1-9]:[1-9][1-9]:[1-9][1-9]) <a class=nounder href=\"showplayer.php\?who=([0-9]+)\"><b>(.*?)<\/b><\/a> bought ([0-9]+) \((.*?)\) for ([0-9]+) Meat.<br>",
    # Trade related patterns
    "traderIgnoringUs": r"<td>You can't make an offer to a player who has placed you on his or her ignore list\.",
    "traderIsInRoninHC": r"<td>That player cannot receive Meat or items from other players\.",
    "traderHasNotEnoughMeat": r"<td>You don't have that much Meat\.",
    "traderHasNotEnoughItems": r"<td>You don't have enough of one of the items you're trying to send.",
    "traderBannedFromChat": r"<td>You can't send offers while you're banned from the chat\.",
    "tradeSentSuccessfully": r"<td>Your trade offer has been sent\.",
    "tradeResponseSentSuccessfully": r"Pending Responses \(Outgoing\)",
    "tradeCancelledSuccessfully": r"Offer cancelled\.",
}
