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
	render_stats,
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

			# Advance game state via controller
			status_msg = game.game_loop()
			if status_msg:
				print(f"\n{status_msg}")
				break

			# Trigger and display event via UI helper
			res = em.trigger_daily_event(player)
			if res:
				display_event(res)

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