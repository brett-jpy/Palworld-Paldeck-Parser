# Palworld Paldeck Parser

This project allows you to parse your Palworld save files and track your Paldeck completion outside of the game.

## Project Use

* [Pal Information and Attributes](https://github.com/mlg404/palworld-paldex-api/tree/main/src) are taken from the _.json_ files in this repo.
* [.SAV to JSON conversion](https://github.com/cheahjs/palworld-save-tools)
* [AssetID to IGNs](https://palwiki.io/)

## How to Use

The `assetId_to_name.py` script gets a list of all the Pal names from [palworld-paldex-api pals.json file](https://raw.githubusercontent.com/mlg404/palworld-paldex-api/main/src/pals.json) and does a look up to get the associated AssetID name from the [Palwiki](https://palwiki.io/).

The result of the lookup are shown below. The _Reptyro-Cryst_ and _Kingpaca-Cryst_ are not found because the [Palwiki](https://palwiki.io/) refers to them as _Ice Reptyro_ and _Ice Kingpaca_. I've correct the entries in the JSON.

```py
[{'palname_ign': 'Lamball', 'asset_id': 'SheepBall'}, {'palname_ign': 'Cattiva', 'asset_id': 'PinkCat'}, {'palname_ign': 'Chikipi', 'asset_id': 'ChickenPal'}, {'palname_ign': 'Lifmunk', 'asset_id': 'Carbunclo'}, {'palname_ign': 'Foxparks', 'asset_id': 'Kitsunebi'}, {'palname_ign': 'Fuack', 'asset_id': 'BluePlatypus'}, {'palname_ign': 'Sparkit', 'asset_id': 'ElecCat'}, {'palname_ign': 'Tanzee', 'asset_id': 'Monkey'}, {'palname_ign': 'Rooby', 'asset_id': 'FlameBambi'}, {'palname_ign': 'Pengullet', 'asset_id': 'Penguin'}, {'palname_ign': 'Penking', 'asset_id': 'CaptainPenguin'}, {'palname_ign': 'Jolthog', 'asset_id': 'Hedgehog'}, {'palname_ign': 'Gumoss', 'asset_id': 'PlantSlime'}, {'palname_ign': 'Vixy', 'asset_id': 'CuteFox'}, {'palname_ign': 'Hoocrates', 'asset_id': 'WizardOwl'}, {'palname_ign': 'Teafant', 'asset_id': 'Ganesha'}, {'palname_ign': 'Depresso', 'asset_id': 'NegativeKoala'}, {'palname_ign': 'Cremis', 'asset_id': 'WoolFox'}, {'palname_ign': 'Daedream', 'asset_id': 'DreamDemon'}, {'palname_ign': 'Rushoar', 'asset_id': 'Boar'}, {'palname_ign': 'Nox', 'asset_id': 'NightFox'}, {'palname_ign': 'Fuddler', 'asset_id': 'CuteMole'}, {'palname_ign': 'Killamari', 'asset_id': 'NegativeOctopus'}, {'palname_ign': 'Mau', 'asset_id': 'Bastet'}, {'palname_ign': 'Celaray', 'asset_id': 'FlyingManta'}, {'palname_ign': 'Direhowl', 'asset_id': 'Garm'}, {'palname_ign': 'Tocotoco', 'asset_id': 'ColorfulBird'}, {'palname_ign': 'Flopie', 'asset_id': 'FlowerRabbit'}, {'palname_ign': 'Mozzarina', 'asset_id': 'CowPal'}, {'palname_ign': 'Bristla', 'asset_id': 'LittleBriarRose'}, {'palname_ign': 'Gobfin', 'asset_id': 'SharkKid'}, {'palname_ign': 'Hangyu', 'asset_id': 'WindChimes'}, {'palname_ign': 'Mossanda', 'asset_id': 'GrassPanda'}, {'palname_ign': 'Woolipop', 'asset_id': 'SweetsSheep'}, {'palname_ign': 'Caprity', 'asset_id': 'BerryGoat'}, {'palname_ign': 'Melpaca', 'asset_id': 'Alpaca'}, {'palname_ign': 'Eikthyrdeer', 'asset_id': 'Deer'}, {'palname_ign': 'Nitewing', 'asset_id': 'HawkBird'}, {'palname_ign': 'Ribbuny', 'asset_id': 'PinkRabbit'}, {'palname_ign': 'Incineram', 'asset_id': 'Baphomet'}, {'palname_ign': 'Cinnamoth', 'asset_id': 'CuteButterfly'}, {'palname_ign': 'Arsox', 'asset_id': 'FlameBuffalo'}, {'palname_ign': 'Dumud', 'asset_id': 'LazyCatfish'}, {'palname_ign': 'Cawgnito', 'asset_id': 'DarkCrow'}, {'palname_ign': 'Leezpunk', 'asset_id': 'LizardMan'}, {'palname_ign': 'Loupmoon', 'asset_id': 'Werewolf'}, {'palname_ign': 'Galeclaw', 'asset_id': 'Eagle'}, {'palname_ign': 'Robinquill', 'asset_id': 'RobinHood'}, {'palname_ign': 'Gorirat', 'asset_id': 'Gorilla'}, {'palname_ign': 'Beegarde', 'asset_id': 'SoldierBee'}, {'palname_ign': 'Elizabee', 'asset_id': 'QueenBee'}, {'palname_ign': 'Grintale', 'asset_id': 'NaughtyCat'}, {'palname_ign': 'Swee', 'asset_id': 'MopBaby'}, {'palname_ign': 'Sweepa', 'asset_id': 'MopKing'}, {'palname_ign': 'Chillet', 'asset_id': 'WeaselDragon'}, {'palname_ign': 'Univolt', 'asset_id': 'Kirin'}, {'palname_ign': 'Foxcicle', 'asset_id': 'IceFox'}, {'palname_ign': 'Pyrin', 'asset_id': 'FireKirin'}, {'palname_ign': 'Reindrix', 'asset_id': 'IceDeer'}, {'palname_ign': 'Rayhound', 'asset_id': 'ThunderDog'}, {'palname_ign': 'Kitsun', 'asset_id': 'AmaterasuWolf'}, {'palname_ign': 'Dazzi', 'asset_id': 'RaijinDaughter'}, {'palname_ign': 'Lunaris', 'asset_id': 'Mutant'}, {'palname_ign': 'Dinossom', 'asset_id': 'FlowerDinosaur'}, {'palname_ign': 'Surfent', 'asset_id': 'Serpent'}, {'palname_ign': 'Maraith', 'asset_id': 'GhostBeast'}, {'palname_ign': 'Digtoise', 'asset_id': 'DrillGame'}, {'palname_ign': 'Tombat', 'asset_id': 'CatBat'}, {'palname_ign': 'Lovander', 'asset_id': 'PinkLizard'}, {'palname_ign': 'Flambelle', 'asset_id': 'LavaGirl'}, {'palname_ign': 'Vanwyrm', 'asset_id': 'BirdDragon'}, {'palname_ign': 'Bushi', 'asset_id': 'Ronin'}, {'palname_ign': 'Beakon', 'asset_id': 'ThunderBird'}, {'palname_ign': 'Ragnahawk', 'asset_id': 'RedArmorBird'}, {'palname_ign': 'Katress', 'asset_id': 'CatMage'}, {'palname_ign': 'Wixen', 'asset_id': 'FoxMage'}, {'palname_ign': 'Verdash', 'asset_id': 'GrassRabbitMan'}, {'palname_ign': 'Vaelet', 'asset_id': 'VioletFairy'}, {'palname_ign': 'Sibelyx', 'asset_id': 'WhiteMoth'}, {'palname_ign': 'Elphidran', 'asset_id': 'FairyDragon'}, {'palname_ign': 'Kelpsea', 'asset_id': 'Kelpie'}, {'palname_ign': 'Azurobe', 'asset_id': 'BlueDragon'}, {'palname_ign': 'Cryolinx', 'asset_id': 'WhiteTiger'}, {'palname_ign': 'Blazehowl', 'asset_id': 'Manticore'}, {'palname_ign': 'Relaxaurus', 'asset_id': 'LazyDragon'}, {'palname_ign': 'Broncherry', 'asset_id': 'SakuraSaurus'}, {'palname_ign': 'Petallia', 'asset_id': 'FlowerDoll'}, {'palname_ign': 'Reptyro', 'asset_id': 'VolcanicMonster'}, {'palname_ign': 'Kingpaca', 'asset_id': 'KingAlpaca'}, {'palname_ign': 'Mammorest', 'asset_id': 'GrassMammoth'}, {'palname_ign': 'Wumpo', 'asset_id': 'Yeti'}, {'palname_ign': 'Warsect', 'asset_id': 'HerculesBeetle'}, {'palname_ign': 'Fenglope', 'asset_id': 'FengyunDeeper'}, {'palname_ign': 'Felbat', 'asset_id': 'CatVampire'}, {'palname_ign': 'Quivern', 'asset_id': 'SkyDragon'}, {'palname_ign': 'Blazamut', 'asset_id': 'KingBahamut'}, {'palname_ign': 'Helzephyr', 'asset_id': 'HadesBird'}, {'palname_ign': 'Astegon', 'asset_id': 'BlackMetalDragon'}, {'palname_ign': 'Menasting', 'asset_id': 'DarkScorpion'}, {'palname_ign': 'Anubis', 'asset_id': 'Anubis'}, {'palname_ign': 'Jormuntide', 'asset_id': 'Umihebi'}, {'palname_ign': 'Suzaku', 'asset_id': 'Suzaku'}, {'palname_ign': 'Grizzbolt', 'asset_id': 'ElecPanda'}, {'palname_ign': 'Lyleen', 'asset_id': 'LilyQueen'}, {'palname_ign': 'Faleris', 'asset_id': 'Horus'}, {'palname_ign': 'Orserk', 'asset_id': 'ThunderDragonMan'}, {'palname_ign': 'Shadowbeak', 'asset_id': 'BlackGriffon'}, {'palname_ign': 'Paladius', 'asset_id': 'SaintCentaur'}, {'palname_ign': 'Necromus', 'asset_id': 'BlackCentaur'}, {'palname_ign': 'Frostallion', 'asset_id': 'IceHorse'}, {'palname_ign': 'Jetragon', 'asset_id': 'JetDragon'}, {'palname_ign': 'Jolthog-Cryst', 'asset_id': 'Hedgehog_Ice'}, {'palname_ign': 'Mau-Cryst', 'asset_id': 'Bastet_Ice'}, {'palname_ign': 'Gobfin-Ignis', 'asset_id': 'SharkKid_Fire'}, {'palname_ign': 'Hangyu-Cryst', 'asset_id': 'WindChimes_Ice'}, {'palname_ign': 'Mossanda-Lux', 'asset_id': 'GrassPanda_Electric'}, {'palname_ign': 'Eikthyrdeer-Terra', 'asset_id': 'Deer_Ground'}, {'palname_ign': 'Incineram-Noct', 'asset_id': 'Baphomet_Dark'}, {'palname_ign': 'Leezpunk-Ignis', 'asset_id': 'LizardMan_Fire'}, {'palname_ign': 'Robinquill-Terra', 'asset_id': 'RobinHood_Ground'}, {'palname_ign': 'Pyrin-Noct', 'asset_id': 'FireKirin_Dark'}, {'palname_ign': 'Dinossom-Lux', 'asset_id': 'FlowerDinosaur_Electric'}, {'palname_ign': 'Surfent-Terra', 'asset_id': 'Serpent_Ground'}, {'palname_ign': 'Vanwyrm-Cryst', 'asset_id': 'BirdDragon_Ice'}, {'palname_ign': 'Elphidran-Aqua', 'asset_id': 'FairyDragon_Water'}, {'palname_ign': 'Kelpsea-Ignis', 'asset_id': 'Kelpie_Fire'}, {'palname_ign': 'Blazehowl-Noct', 'asset_id': 'Manticore_Dark'}, {'palname_ign': 'Relaxaurus-Lux', 'asset_id': 'LazyDragon_Electric'}, {'palname_ign': 'Broncherry-Aqua', 'asset_id': 'SakuraSaurus_Water'}, {'palname_ign': 'Reptyro-Cryst', 'asset_id': "VolcanicMonster_Ice"}, {'palname_ign': 'Kingpaca-Cryst', 'asset_id': "KingAlpaca_Ice"}, {'palname_ign': 'Mammorest-Cryst', 'asset_id': 'GrassMammoth_Ice'}, {'palname_ign': 'Wumpo-Botan', 'asset_id': 'Yeti_Grass'}, {'palname_ign': 'Jormuntide-Ignis', 'asset_id': 'Umihebi_Fire'}, {'palname_ign': 'Suzaku-Aqua', 'asset_id': 'Suzaku_Water'}, {'palname_ign': 'Lyleen-Noct', 'asset_id': 'LilyQueen_Dark'}, {'palname_ign': 'Frostallion-Noct', 'asset_id': 'IceHorse_Dark'}]
```

Second, convert your player save file to JSON using the [Palworld-Save-Tools](https://github.com/cheahjs/palworld-save-tools) repo. This can be accomplished by running `python .\convert.py C:\Users\name\Downloads\save_file.sav`

Run script _parse_paldeck.py_ which will find all the asset IDs from your save file and return the IGNs for each captured Pal.

```python
['Cattiva', 'Chikipi', 'Lifmunk', 'Foxparks', 'Fuack', 'Sparkit', 'Tanzee', 'Rooby', 'Pengullet', 'Penking', 'Jolthog', 'Gumoss', 'Vixy', 'Hoocrates', 'Teafant', 'Depresso', 'Cremis', 'Daedream', 'Rushoar', 'Nox', 'Fuddler', 'Killamari', 'Mau', 'Celaray', 'Direhowl', 'Tocotoco', 'Flopie', 'Mozzarina', 'Bristla', 'Gobfin', 'Hangyu', 'Mossanda', 'Woolipop', 'Caprity', 'Melpaca', 'Eikthyrdeer', 'Nitewing', 'Ribbuny', 'Incineram', 'Cinnamoth', 'Arsox', 'Dumud', 'Cawgnito', 'Loupmoon', 'Galeclaw', 'Robinquill', 'Gorirat', 'Beegarde', 'Elizabee', 'Grintale', 'Swee', 'Sweepa', 'Chillet', 'Univolt', 'Foxcicle', 'Pyrin', 'Reindrix', 'Rayhound', 'Kitsun', 'Dazzi', 'Lunaris', 'Dinossom', 'Surfent', 'Maraith', 'Digtoise', 'Tombat', 'Lovander', 'Flambelle', 'Vanwyrm', 'Bushi', 'Beakon', 'Ragnahawk', 'Katress', 'Wixen', 'Verdash', 'Vaelet', 'Sibelyx', 'Elphidran', 'Kelpsea', 'Azurobe', 'Cryolinx', 'Blazehowl', 'Relaxaurus', 'Broncherry', 'Petallia', 'Reptyro', 'Kingpaca', 'Mammorest', 'Wumpo', 'Warsect', 'Felbat', 'Quivern', 'Blazamut', 'Helzephyr', 'Astegon', 'Menasting', 'Anubis', 'Jormuntide', 'Suzaku', 'Grizzbolt', 'Lyleen', 'Faleris', 'Orserk', 'Shadowbeak', 'Mau Cryst', 'Mossanda Lux', 'Eikthyrdeer Terra', 'Leezpunk Ignis', 'Robinquill Terra', 'Pyrin Noct', 'Dinossom Lux', 'Surfent Terra', 'Vanwyrm Cryst', 'Kelpsea Ignis', 'Blazehowl Noct', 'Mammorest Cryst', 'Jormuntide Ignis', 'Suzaku Aqua']
```
