def count():
    from pathlib import Path

    def is_valid_game_folder(folder: Path) -> bool:
        if not folder.is_dir():
            return False
        contents = list(folder.iterdir())
        return (
            len(contents) == 1 and
            contents[0].is_file() and
            contents[0].name.lower() == "index.html"
        )

    def list_valid_games(root: Path):
        games = []
        for folder in root.rglob("*"):
            if is_valid_game_folder(folder):
                games.append(folder)
                print(f"✅ Found game: {folder.name} in {folder.parent}")
        print(f"\n🎮 Total valid games found: {len(games)}")
        return games

    # Set your base directory
    games_root = Path("games")
    print("🔍 Scanning for valid games...\n")
    found_games = list_valid_games(games_root)


def sort():
    from bs4 import BeautifulSoup
    from collections import defaultdict

    # Sample HTML input again after kernel reset
    html = """
<div class="game-grid">
<div class="game-box">
    <a href="/games/action/time-shooter"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1GgC47YHMF93s8lFPpwq5Jl0QjPoO6OiWOA&s"
        alt="Time Shooter Series" />Time Shooter Series</a>
</div>
<div class="game-box">
    <a href="/games/arcade/slope"><img
        src="https://play-lh.googleusercontent.com/uJn2i9h7KxYQarC_c3K4qH6o7gLtflFnhD_dN14MNkzHJ1NeNFzCL69jpB5mT0vCoQs"
        alt="Slope" />Slope</a>
</div>
<div class="game-box">
    <a href="/games/racing/moto-x3m"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzMLxgJq1x3mIES73AsS6AuTKZTuug9nVuoQ&s"
        alt="Moto X3M" />Moto X3M</a>
</div>
<div class="game-box">
    <a href="/games/arcade/run-3"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdqWWJZJnzyA7AyATROGtMzE5uV1yFmT13Pw&s"
        alt="Run 3" />Run 3</a>
</div>
<div class="game-box">
    <a href="/games/racing/survival-race"><img src="https://watchdocumentaries.com/wp-content/uploads/survival-race-game.jpg"
        alt="Survival Race" />Survival Race</a>
</div>
<div class="game-box">
    <a href="/games/simulator/cookie-clicker"><img src="https://upload.wikimedia.org/wikipedia/en/0/06/Cookie_Clicker_logo.png"
        alt="Cookie Clicker" />Cookie Clicker</a>
</div>
<div class="game-box">
    <a href="/games/racing/drift-hunters"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ71Gd0HQjdZ6BcHphNEvh1rLhYLL3V-_tSjw&s"
        alt="Drift Hunters" />Drift Hunters</a>
</div>
<div class="game-box">
    <a href="/games/drive-mad"><img
        src="https://play-lh.googleusercontent.com/7l3WAPbei9MXrxnCzImpXi2VxjEBtgDl0htwvTnA-YqpJAuQJPpSiby1oB8LZMgD0IAy"
        alt="Drive Mad" />Drive Mad</a>
</div>
<div class="game-box">
    <a href="/games/simulator/duck-clicker"><img src="https://img.itch.zone/aW1nLzE0ODU1ODQ1LnBuZw==/original/IfCy77.png"
        alt="Duck Clicker" />Duck Clicker</a>
</div>
<div class="game-box">
    <a href="/games/action/spear-warzone"><img
        src="https://1games.io/data/image/game/spear-warzone/banner/spear-wazone-1200x1200.png"
        alt="Spear Warzone" />Spear Warzone</a>
</div>
<div class="game-box">
    <a href="/games/action/crazy-cattle-3d"><img src="https://kbhgames.com/wp-content/uploads/2025/05/Crazy-Cattle-3D.jpg"
        alt="Crazy Cattle 3D" />Crazy Cattle 3D
    </a>
</div>
<div class="game-box">
    <a href="/games/action/basketball-frvr"><img
        src="https://img.poki-cdn.com/cdn-cgi/image/quality=78,width=1200,height=1200,fit=cover,f=png/5aae527bebe68094c3d3276387150197.png"
        alt="Basketball FRVR" />Basketball FRVR</a>
</div>
<div class="game-box">
    <a href="/games/racing/hover-racer-drive"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkthRBqa43q0fy7dkkasxXwZbK7I2PvsVJlQ&s"
        alt="Hover Racer Drive" />Hover Racer Drive</a>
</div>
<div class="game-box">
    <a href="/games/strategy/escaping-the-prison"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_us-FoQoSP4m9wJjqoeJSuRWThnj7LOJjgw&s"
        alt="Escaping the Prison" />Escaping the Prison</a>
</div>
<div class="game-box">
    <a href="/games/arcade/dinosaur-game"><img
        src="https://play-lh.googleusercontent.com/iiIJq5JmLFYNI1bVz4IBHyoXs508JcEzHhOgau69bnveF9Wat51-ax9LMPVOlneKwqg"
        alt="Dinosaur Game" />Dinosaur</a>
</div>
<div class="game-box">
    <a href="/games/racing/hill-climb-racing"><img
        src="https://play-lh.googleusercontent.com/N0UxhBVUmx8s7y3F7Kqre2AcpXyPDKAp8nHjiPPoOONc_sfugHCYMjBpbUKCMlK_XUs"
        alt="Hill Climb Racing" />Hill Climb Racing</a>
</div>
<div class="game-box">
    <a href="/games/action/ragdoll-archers"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPgKROebbMUje45RYS-FkBGVWfhgcLrsnFcQ&s"
        alt="Ragdoll Archers" />Ragdoll Archers</a>
</div>
<div class="game-box">
    <a href="/games/arcade/slope-2"><img src="https://1games.io/data/image/game/slope-2/banner/slope-2_1200x1200.png"
        alt="Slope 2" />Slope 2</a>
</div>
<div class="game-box">
    <a href="/games/arcade/geometry-dash-lite"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbnu4fRE-vqOhHPCK1w-L1wtPUrYRmXFrCEQ&s"
        alt="Geometry Dash Lite" />Geometry Dash Lite</a>
</div>
<div class="game-box">
    <a href="/games/arcade/under-the-red-sky"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYUBT9PxKg9R838IKPRd7H-e80EsPPhKnxYw&s"
        alt="Under The Red Sky" />Under The Red Sky</a>
</div>
<div class="game-box">
    <a href="/games/racing/madalin-stunt-cars-2"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQusfyO2aA-RIpYzKsPPyPXI5wWtGkSTN4CHA&s"
        alt="Madalin Stunt Cars 2" />Madalin Stunt Cars 2</a>
</div>
<div class="game-box">
    <a href="/games/strategy/creative-kill-chamber"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvUpG1sUxY_hNrTqOXaseRqDbgqHuFtDpgxQ&s"
        alt="Creative Kill Chamber" />Creative Kill Chamber</a>
</div>
<div class="game-box">
    <a href="/games/strategy/creative-kill-chamber-2"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5ba3S_wQH-4vpRNquuhNxIvVa6Ax7owRYRQ&s"
        alt="Creative Kill Chamber 2" />Creative Kill Chamber 2</a>
</div>
<div class="game-box">
    <a href="/games/action/tunnel-rush"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTS0Ja02fwjrD3RqkAnHIGLCG_Tuzwg5bTs1Q&s"
        alt="Tunnel Rush" />Tunnel Rush</a>
</div>
<div class="game-box">
    <a href="/games/action/head-soccer-2023"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtpImwxBfrVDqm27BAW_onIL5UYsCugaFKMA&s"
        alt="Head Soccer 2023" />Head Soccer 2023</a>
</div>
<div class="game-box">
    <a href="/games/simulator/hole-io"><img
        src="https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000069917/28c5a57b2711d70dbeb4dd55155691e8135a3069bad3455547392878c0162861"
        alt="Hole.io" />Hole.io</a>
</div>
<div class="game-box">
    <a href="/games/action/gun-blood"><img
        src="https://play-lh.googleusercontent.com/74HrzSgWFO3JIIIg2kbKafeETZW7gkh2PGeC4fRAYICNg29X3uelbr6OzR080GI-AhK-"
        alt="Gun Blood" />Gun Blood</a>
</div>
<div class="game-box">
    <a href="/games/action/funny-shooter-2"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScUXBTe2dQvh7aq3RT4P3fmWgRkTqaMIuP2g&s"
        alt="Funny Shooter 2" />Funny Shooter 2</a>
</div>
<div class="game-box">
    <a href="/games/action/getaway-shootout"><img src="https://htmlxm.github.io/thumb/getaway-shootout.png"
        alt="Getaway Shootout" />Getaway Shootout</a>
</div>
<div class="game-box">
    <a href="/games/arcade/ballistic"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNe8Cx74egEh0VAfHM-SRx3OQWtFSrq1bMiA&s"
        alt="Ballistic" />Ballistic</a>
</div>
<div class="game-box">
    <a href="/games/arcade/le-flip-3d"><img
        src="https://play-lh.googleusercontent.com/sMpJpTPMtTMr9tfusBtbWIz_h2UdX3iwx8Ea4w6vJ-0vyFILvpIMj_JvwVSeS6Xq0bg"
        alt="Bottle Flip 3D" />Bottle Flip 3D</a>
</div>
<div class="game-box">
    <a href="/games/action/bullet-force"><img
        src="https://play-lh.googleusercontent.com/d8XjgRT_XjvsNK6gHye4em45MjUa2WAUnT9y5oFDM-Z_95_uOjevcD3gbvc8vBIBGw=w526-h296-rw"
        alt="Bullet Force" />Bullet Force</a>
</div>
<div class="game-box">
    <a href="/games/arcade/snake"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG_sstbZV02TGbsIwoJvvPpSut1OpWw52WMw&s"
        alt="Snake" />Snake</a>
</div>
<div class="game-box">
    <a href="/games/simulator/monkey-mart"><img src="https://i.ytimg.com/vi/KsyQBXdkAuM/maxresdefault.jpg"
        alt="Monkey Mart" />Monkey Mart</a>
</div>
<div class="game-box">
    <a href="/games/simulator/papas-pizzeria"><img
        src="https://papaspizzeria.io/data/image/options/papas-pizzeria-game-banner.jpg"
        alt="Papa's Pizzeria" />Papa's Pizzeria</a>
</div>
<div class="game-box">
    <a href="/games/simulator/paper-io-2"><img
        src="https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000068359/73341197ab2f46b0b68c46bd610bcd65ba490045423c918e4a9f199cd7584e20"
        alt="Paper.io 2" />Paper.io 2</a>
</div>
<div class="game-box">
    <a href="/games/racing/smash-karts"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxBphEzA60TR726i8NCfCzTddE26HT1UFENA&s"
        alt="Smash Karts" />Smash Karts</a>
</div>
<div class="game-box">
    <a href="/games/simulator/pou"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROKI39uSxoQ0v8SOJqlXnBqiQMgjlYWODQ6w&s"
        alt="Pou" />Pou</a>
</div>
<div class="game-box">
    <a href="/games/arcade/crossy-road"><img src="https://upload.wikimedia.org/wikipedia/en/7/71/Crossy_Road_icon.jpeg"
        alt="Crossy Road" />Crossy Road</a>
</div>
<div class="game-box">
    <a href="/games/strategy/bloons-td-6"><img
        src="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/960090/header.jpg?t=1738893448"
        alt="Bloons TD 6" />Bloons TD 6</a>
</div>
<div class="game-box">
    <a href="/games/simulator/bitlife"><img src="https://static.wikia.nocookie.net/jacksepticeye/images/c/cf/BitLife_logo.png"
        alt="Bitlife" />Bitlife</a>
</div>
<div class="game-box">
    <a href="/games/action/fortnite"><img
        src="https://cdn.glitch.global/21e48a88-8990-46c8-9dc5-259bb27daa0a/Capture.PNG?v=1748021224132"
        alt="Fortnite" /><em>"Fortnite"</em></a>
</div>
<div class="game-box">
    <a href="/games/racing/eggy-car"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3AihY6tU2_XRZ0CU2ZrE6v5qDzgKjkqfKOQ&s"
        alt="Eggy Car" />Eggy Car</a>
</div>
<div class="game-box">
    <a href="/games/action/1v1-lol"><img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCFCA_8XDRi81Dmw7f-woSa_X4XBXdx-q-4Q&s"
        alt="1v1.lol" />1v1.lol</a>
</div>
<div class="game-box">
    <a href="/games/simulator/idle-breakout"><img
        src="https://img.itch.zone/aW1hZ2UvMzI5MTMxLzE4MDAxNDYucG5n/original/bo9BNe.png" alt="Idle Breakout" />Idle
    Breakout</a>
</div>
<div class="game-box">
    <a href="/games/simulator/idle-mining-empire"><img
        src="https://www.mortgagecalculator.org/money-games/idle-mining-empire/idle-mining-empire.png"
        alt="Idle Mining Empire" />Idle Mining Empire</a>
</div>
<div class="game-box">
    <a href="/games/arcade/subway-surfers"><img src="https://upload.wikimedia.org/wikipedia/en/a/aa/Subway_Surfers.jpg"
        alt="Subway Surfers" />Subway Surfers</a>
</div>
<div class="game-box">
    <a href="/games/simulator/ant-art-tycoon"><img
        src="https://img.poki-cdn.com/cdn-cgi/image/quality=78,width=314,height=314,fit=cover,f=auto/b6c5f4345a8bfc1325319666882840e9.png"
        alt="Ant Art Tycoon" />Ant Art Tycoon</a>
</div>
<div class="game-box">
    <a href="/games/arcade/fruit-ninja"><img src="https://www.coolmathgames.com/sites/default/files/FruitNinja_OG-Logo.jpg"
        alt="Fruit Ninja" />Fruit Ninja</a>
</div>
<div class="game-box">
    <a href="/games/simulator/stick-merge"><img
        src="https://play-lh.googleusercontent.com/yQSKk-7dE2D45ZY70ghdGjGxzRwKQU_TDoy-1LBal2pjJ3wSKOMptCWRq9hgJdI-GVw"
        alt="Stick Merge" />Stick Merge</a>
</div>
<div class="game-box">
    <a href="/games/action/boxing-random"><img src="https://www.onlinegames.io/media/posts/473/Boxing-Random.jpg"
        alt="Boxing Random" />Boxing Random</a>
</div>
<div class="game-box">
    <a href="/games/strategy/stickman-hook"><img
        src="https://img.poki-cdn.com/cdn-cgi/image/quality=78,width=314,height=314,fit=cover,f=auto/99e090d154caf30f3625df7e456d5984.png"
        alt="Stickman Hook" />Stickman Hook</a>
</div>
<div class="game-box">
    <a href="/games/action/rooftop-snipers"><img
        src="https://img.gamepix.com/games/rooftop-snipers/cover/rooftop-snipers.png" alt="Rooftop Snipers" />Rooftop
    Snipers</a>
</div>
<div class="game-box">
    <a href="/games/action/gunspin"><img src="https://static.keygames.com/4/113974/98896/1024x1024/gunspin.webp"
        alt="GunSpin" />GunSpin</a>
</div>
<div class="game-box">
    <a href="/games/action/stickman-army-the-resistance"><img src="https://play-lh.googleusercontent.com/jcOyPcmM2vjbh7ALN6taninGoskE4n9F-R6HgvrcEVs9AGQfYhjLU0VZ21ksuKxN1g"
        alt="Stickman Army" />Stickman Army, The Resistance</a>
</div>
<div class="game-box">
    <a href="/games/action/stickman-fighter-epic-battles"><img src="https://play-lh.googleusercontent.com/-p6yzlvqe2yK-d5ye_wFVxXBpzzjz030hNOzzn74GakefmjavvRoNOLj_5RFBy379J7Y"
        alt="Stickman Army" />Stickman Fighter, Epic Battles</a>
</div>
<div class="game-box">
    <a href="/games/strategy/little-alchemy-2"><img src="https://static1.srcdn.com/wordpress/wp-content/uploads/2024/09/little-alchemy-a-lot-of-items-in-scene.jpg"
        alt="Little Alchemy 2" />Little Alchemy 2</a>
</div>
</div>
"""

    # Parse the HTML and extract game info
    soup = BeautifulSoup(html, "html.parser")
    game_boxes = soup.select(".game-box")

    games = []
    for box in game_boxes:
        a_tag = box.find("a")
        href = a_tag["href"]
        category = href.split("/")[2]  # extract category from URL
        name = a_tag.text.strip()
        games.append((category, name, str(box)))  # store category, name, original HTML

    # Sort and group the games by category and name
    games.sort(key=lambda x: (x[0].lower(), x[1].lower()))
    grouped_html = defaultdict(list)
    for cat, name, html_box in games:
        grouped_html[cat].append(html_box)

    # Construct the sorted HTML output
    final_html = ""
    for cat in sorted(grouped_html.keys()):
        final_html += f"<!-- Category: {cat} -->\n"
        final_html += "\n".join(grouped_html[cat]) + "\n\n"

    print(final_html)


sort()