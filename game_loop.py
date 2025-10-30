"""
Interactive game loop for Survival Island with colored actions and events.

- Each action has a distinct color and emoji.
- Events are shown with a color and emoji according to their type.

Run from the project root so `src` is importable.
"""

import sys
import os
import time

# Ensure project root is importable as `src`
sys.path.insert(0, os.path.dirname(__file__))

from src.controllers.game import Game
from src.controllers.action_manager import ActionManager
from src.controllers.event_manager import EventManager

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
ACTION_META = {
    "fish": {"color": COLOR_BLUE, "emoji": "🎣"},
    "sleep": {"color": COLOR_MAGENTA, "emoji": "😴"},
    "find_water": {"color": COLOR_CYAN, "emoji": "💧"},
}

# Event type metadata
EVENT_META = {
    "rain": {"color": COLOR_BLUE, "emoji": "🌧️"},
    "animal": {"color": COLOR_YELLOW, "emoji": "🐾"},
    "resource": {"color": COLOR_GREEN, "emoji": "🌿"},
}


def color_for_value(value: int) -> str:
    if value >= 60:
        return COLOR_GREEN
    if value >= 30:
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


def prompt_start(game: Game) -> None:
    choice = input("Load saved game? (y/n) ").strip().lower()
    if choice == "y":
        # example saved data used for demo/test
        save_data = {
            "name": "SavedPlayer",
            "hunger": 50,
            "thirst": 50,
            "energy": 50,
            "days_survived": 29,
            "is_alive": True,
        }
        if game.load_game(save_data):
            print("Loaded saved game.")
            return
        print("Failed to load save — starting new game.")

    name = input("Enter player name (or press Enter for 'Survivor'): ").strip() or "Survivor"
    game.start_new_game(name)


def choose_and_apply_action(am: ActionManager, player) -> None:
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


def process_day(game: Game, em: EventManager) -> None:
    player = game.get_player()
    # natural evolution increments days_survived
    player.natural_evolution()

    # trigger an event
    res = em.trigger_daily_event(player)
    if res:
        # res should be a dict; EventManager now attaches event_type and event_name
        event_type = res.get("event_type")
        event_name = res.get("event_name") or "Event"
        message = res.get("message") or "An event occurred"

        meta = EVENT_META.get(event_type, {})
        color = meta.get("color", "")
        emoji = meta.get("emoji", "")

        print(f"\n{color}{emoji} [{event_name}] {message}{COLOR_RESET}")


def main() -> None:
    game = Game()
    am = ActionManager()
    em = EventManager()

    prompt_start(game)
    player = game.get_player()

    try:
        while True:
            render_header(player)
            render_stats(player)

            # check end conditions after rendering so UI always visible
            if player.check_game_over():
                print("\nGame Over: You died from lack of vital resources!")
                break
            if game.check_victory():
                print("\nVictory: You survived 30 days on the island!")
                break

            try:
                choose_and_apply_action(am, player)
            except KeyboardInterrupt:
                print("\nQuitting game...")
                break

            process_day(game, em)
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")

    print("\nFinal state:")
    for k, v in game.get_game_state().items():
        print(f" - {k}: {v}")


if __name__ == "__main__":
    main()
import sys
import os
import time

# Ensure project root is importable as `src`
sys.path.insert(0, os.path.dirname(__file__))

from src.controllers.game import Game
from src.controllers.action_manager import ActionManager
from src.controllers.event_manager import EventManager

# ANSI color codes
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"

BAR_CHAR = "█"
EMPTY_CHAR = "-"
BAR_WIDTH = 30


def color_for_value(value: int) -> str:
    if value >= 60:
        return COLOR_GREEN
    if value >= 30:
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


def prompt_start(game: Game) -> None:
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


def choose_and_apply_action(am: ActionManager, player) -> None:
    actions = am.get_actions_desc()
    keys = list(actions.keys())
    print("\nAvailable actions:")
    for i, key in enumerate(keys, start=1):
        print(f" {i}. {key} - {actions[key]}")
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
    if key == "fish":
        am.execute_fish_action(player)
        print("You went fishing.")
    elif key == "sleep":
        am.execute_sleep_action(player)
        print("You slept/rested.")
    elif key == "find_water":
        am.execute_find_water_action(player)
        print("You searched for water.")
    else:
        action = am.actions.get(key)
        if action:
            action.execute(player)
            print(f"Performed {action.name}.")
        else:
            print("Unknown action.")


def process_day(game: Game, em: EventManager) -> None:
    player = game.get_player()
    # natural evolution increments days_survived
    player.natural_evolution()

    # trigger an event
    res = em.trigger_daily_event(player)
    if res:
        print(f"\n[Event] {res.get('message', 'An event occurred')}")


def main() -> None:
    game = Game()
    am = ActionManager()
    em = EventManager()

    prompt_start(game)
    player = game.get_player()

    try:
        while True:
            render_header(player)
            render_stats(player)

            # check end conditions after rendering so UI always visible
            if player.check_game_over():
                print(f"\n \033[91mGame Over: You died from lack of vital resources!\033[0m")
                break
            if game.check_victory():
                print(f"\n \033[92mVictory: You survived 30 days on the island!\033[0m")
                break

            try:
                choose_and_apply_action(am, player)
            except KeyboardInterrupt:
                print("\nQuitting game...")
                break

            process_day(game, em)
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")

    print("\nFinal state:")
    for k, v in game.get_game_state().items():
        print(f" - {k}: {v}")


if __name__ == "__main__":
    main()