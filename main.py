"""Point d'entrée principal du Survival Island Game."""

import sys
import os
import time

# Ensure project root is importable as `src`
sys.path.insert(0, os.path.dirname(__file__))

from src.controllers.game import Game
from src.controllers.action_manager import ActionManager
from src.controllers.event_manager import EventManager
from src.ui.cli import (
    prompt_start,
    render_header,
    render_slider,
    choose_and_apply_action,
    display_event,
    prompt_save,
)


def main() -> None:
	game = Game()
	am = ActionManager()
	em = EventManager()

	prompt_start(game)
	player = game.get_player()

	try:
		while True:
			render_header(player)
			print("Hunger :", render_slider(player.hunger, gauge_type="hunger"))
			print("Thirst :", render_slider(player.thirst, gauge_type="thirst"))
			print("Energy :", render_slider(player.energy, gauge_type="energy"))

			# check end conditions after rendering so UI always visible
			if player.check_game_over():
				print()
				print("Game Over: You died from lack of vital resources!")
				print()
				break
			if game.check_victory():
				print()
				print("Victory: You survived 30 days on the island!")
				print()
				break

			try:
				print()
				action_result = choose_and_apply_action(am, player)
				print()
			except KeyboardInterrupt:
				print()
				print("Quitting game...")
				print()
				break

			# If player chose 'explore', trigger event
			if action_result == "explore":
				print()
				event_res = am.execute_explore_action(player, em)
				if event_res:
					display_event(event_res)
				print()

			# Advance game state via controller
			status_msg = game.game_loop()
			if status_msg:
				print()
				print(f"{status_msg}")
				print()
				break

			# Trigger and display event via UI helper
			res = em.trigger_daily_event(player)
			if res:
				print()
				display_event(res)
				print()

			time.sleep(0.1)

	except KeyboardInterrupt:
		print("\nInterrupted. Exiting.")
	finally:
		# Offer to save the game on exit, unless running on Windows (user preference)
		try:
			if os.name != 'nt':
				prompt_save(game)
		except Exception:
			pass


if __name__ == "__main__":
	main()