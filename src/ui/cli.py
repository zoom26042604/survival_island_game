"""CLI UI helpers for Survival Island.

This module contains rendering and input helpers so `game_loop.py` can be
very small and focused on orchestration.
"""
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
}

# Event type metadata
EVENT_META: Dict[str, Dict[str, str]] = {
    "rain": {"color": COLOR_BLUE, "emoji": "🌧️"},
    "animal": {"color": COLOR_YELLOW, "emoji": "🐾"},
    "resource": {"color": COLOR_GREEN, "emoji": "🌿"},
}


def color_for_value(value: int) -> str:
    # Lower values are better now (0=healthy, 100=death).
    if value <= 40:
        return COLOR_GREEN
    if value <= 70:
        return COLOR_YELLOW
    return COLOR_RED


def render_slider(value: int, width: int = BAR_WIDTH) -> str:
    pct = max(0, min(100, int(value)))
    filled = int(round((pct / 100.0) * width))
    bar = BAR_CHAR * filled + EMPTY_CHAR * (width - filled)
    color = color_for_value(pct)
    return f"{color}[{bar}]{COLOR_RESET} {pct}%"


def render_header(player) -> None:
    print("\n" + "=" * 60)
    print(f"Player: {player.name}    Day: {player.days_survived}")
    print("=" * 60)


def render_stats(player) -> None:
    print("Hunger :", render_slider(player.hunger))
    print("Thirst :", render_slider(player.thirst))
    print("Energy :", render_slider(player.energy))


def prompt_start(game) -> None:
    choice = input("Load saved game? (y/n) ").strip().lower()
    if choice == "y":
        # example saved data used for demo/test
        save_data = {
            "name": "SavedPlayer",
            "hunger": 50,
            "thirst": 50,
            "energy": 50,
            "days_survived": 5,
            "is_alive": True,
        }
        if game.load_game(save_data):
            print("Loaded saved game.")
            return
        print("Failed to load save — starting new game.")

    name = input("Enter player name (or press Enter for 'Survivor'): ").strip() or "Survivor"
    game.start_new_game(name)


def choose_and_apply_action(am, player) -> None:
    actions = am.get_actions_desc()
    keys = list(actions.keys())
    print("\nAvailable actions:")
    for i, key in enumerate(keys, start=1):
        meta = ACTION_META.get(key, {})
        color = meta.get("color", "")
        emoji = meta.get("emoji", "")
        print(f" {i}. {key} - {actions[key]} {color}{emoji}{COLOR_RESET}")
    print(" s. Show state    q. Quit")

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
    else:
        action = am.actions.get(key)
        if action:
            action.execute(player)
            print(f"{color}{emoji} Performed {action.name}.{COLOR_RESET}")
        else:
            print("Unknown action.")


def display_event(res: dict) -> None:
    if not isinstance(res, dict):
        print(res)
        return
    event_type = res.get("event_type")
    event_name = res.get("event_name") or "Event"
    message = res.get("message") or "An event occurred"

    meta = EVENT_META.get(event_type, {})
    color = meta.get("color", "")
    emoji = meta.get("emoji", "")

    print(f"\n{color}{emoji} [{event_name}] {message}{COLOR_RESET}")
