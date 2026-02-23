from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        print("not done yet")

    def get_strategy_name(self) -> str:
        return "AggresiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

