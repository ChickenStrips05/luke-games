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
            print(f"✅ Found game: {folder.name}")
    print(f"\n🎮 Total valid games found: {len(games)}")
    return games

# Set your base directory
games_root = Path("games")
print("🔍 Scanning for valid games...\n")
found_games = list_valid_games(games_root)
