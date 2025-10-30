"""CLI UI helpers for Survival Island.

This module contains rendering and input helpers so `game_loop.py` can be
very small and focused on orchestration.
"""

import os
from typing import Dict

# ANSI color codes
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_BLUE = "\033[94m"
COLOR_CYAN = "\033[96m"
COLOR_MAGENTA = "\033[95m"

BAR_CHAR = "█"
EMPTY_CHAR = "-"
BAR_WIDTH = 30

# Per-action metadata (color + emoji)
ACTION_META: Dict[str, Dict[str, str]] = {
    "fish": {"color": COLOR_BLUE, "emoji": "🎣"},
    "sleep": {"color": COLOR_MAGENTA, "emoji": "😴"},
    "find_water": {"color": COLOR_CYAN, "emoji": "💧"},
    "explore": {"color": COLOR_YELLOW, "emoji": "🧭"},
}

# Event type metadata
EVENT_META: Dict[str, Dict[str, str]] = {
    "rain": {"color": COLOR_BLUE, "emoji": "🌧️"},
    "animal": {"color": COLOR_YELLOW, "emoji": "🐾"},
    "resource": {"color": COLOR_GREEN, "emoji": "🌿"},
}



def color_for_value(value: int, gauge_type: str = "energy") -> str:
    # Hunger/Thirst: 0 = vert, 100 = rouge
    # Energy: 0 = rouge, 100 = vert
    if gauge_type in ["hunger", "thirst"]:
        if value <= 40:
            return COLOR_GREEN
        if value <= 70:
            return COLOR_YELLOW
        return COLOR_RED
    else:  # energy
        if value <= 40:
            return COLOR_RED
        if value <= 70:
            return COLOR_YELLOW
        return COLOR_GREEN



def render_slider(value: int, width: int = BAR_WIDTH, gauge_type: str = "energy") -> str:
    pct = max(0, min(100, int(value)))
    filled = int(round((pct / 100.0) * width))
    bar = BAR_CHAR * filled + EMPTY_CHAR * (width - filled)
    color = color_for_value(pct, gauge_type)
    return f"{color}[{bar}]{COLOR_RESET} {pct}%"


def render_header(player) -> None:
    print()
    print("=" * 60)
    print(f"Player: {player.name}    Day: {player.days_survived}")
    print("=" * 60)
    print()


def prompt_start(game) -> None:
    import os
    import glob

    saves_dir = "saves"
    save_files = glob.glob(os.path.join(saves_dir, "*.json"))
    if save_files:
        print("Available saves:")
        for idx, f in enumerate(save_files, 1):
            print(f"  {idx}. {os.path.basename(f)[:-5]}")
        choice = input("Enter the number to load a save, or press Enter to start a new game: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(save_files):
            path = save_files[int(choice)-1]
            if game.load_game_from_file(path):
                print(f"Loaded saved game from {path}.")
                return
            print("Failed to load save — starting new game.")

    name = input("Enter player name (or press Enter for 'Survivor'): ").strip() or "Survivor"
    game.start_new_game(name)


def prompt_save(game, default_path: str = "savegame.json") -> None:
    """Prompt user to save the current game to a JSON file."""
    if not game or not game.get_player():
        print("No game in progress to save.")
        return

    player = game.get_player()
    filename = f"{player.name}.json"
    default_path = os.path.join("saves", filename)
    choice = input(f"Save current game to file? (y/n) [default: {default_path}] ").strip().lower()
    if choice != "y":
        return

    path = input(f"Enter save file path (default: {default_path}): ").strip() or default_path
    ok = game.save_game(path)
    if ok:
        print(f"Game saved to {path}.")
    else:
        print("Failed to save game.")


def choose_and_apply_action(am, player) -> None:
    actions = am.get_actions_desc()
    keys = list(actions.keys())
    print()
    print("Available actions:")
    print()
    for i, key in enumerate(keys, start=1):
        meta = ACTION_META.get(key, {})
        color = meta.get("color", "")
        emoji = meta.get("emoji", "")
        print(f" {i}. {key} - {actions[key]} {color}{emoji}{COLOR_RESET}")
        print()
    print(" s. Show state    q. Quit")
    print()

    choice = input("Choose action (number/name/Enter to skip): ").strip().lower()
    if not choice:
        return
    if choice == "q":
        raise KeyboardInterrupt
    if choice == "s":
        # caller will re-render state
        return

    # allow number or name
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(keys):
            key = keys[idx]
        else:
            print("Invalid action number.")
            return
    else:
        key = choice
        if key not in keys:
            print("Invalid action name.")
            return

    # dispatch to ActionManager methods by key
    meta = ACTION_META.get(key, {})
    color = meta.get("color", "")
    emoji = meta.get("emoji", "")

    if key == "fish":
        am.execute_fish_action(player)
        print(f"{color}{emoji} You went fishing.{COLOR_RESET}")
    elif key == "sleep":
        am.execute_sleep_action(player)
        print(f"{color}{emoji} You rested and regained energy.{COLOR_RESET}")
    elif key == "find_water":
        am.execute_find_water_action(player)
        print(f"{color}{emoji} You searched for water.{COLOR_RESET}")
    elif key == "explore":
        # Need to pass event_manager, so we return a flag to main
        return "explore"
    else:
        action = am.actions.get(key)
        if action:
            action.execute(player)
            print(f"{color}{emoji} Performed {action.name}.{COLOR_RESET}")
        else:
            print("Unknown action.")


def display_event(res: dict) -> None:
    print()
    if not isinstance(res, dict):
        print(res)
        print()
        return
    event_type = res.get("event_type")
    event_name = res.get("event_name") or "Event"
    message = res.get("message") or "An event occurred"

    meta = EVENT_META.get(event_type, {})
    color = meta.get("color", "")
    emoji = meta.get("emoji", "")

    print(f"\n{color}{emoji} [{event_name}] {message}{COLOR_RESET}")
