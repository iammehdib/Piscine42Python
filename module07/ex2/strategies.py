from abc import ABC, abstractmethod

from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    ...


class BattleStrategy(ABC):

    name = "battle"

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool: ...

    @abstractmethod
    def act(self, creature: Creature) -> None: ...

    def _reject(self, creature: Creature) -> None:
        raise InvalidStrategyError(
            f"Invalid Creature '{creature.name}' "
            f"for this {self.name} strategy"
        )


class NormalStrategy(BattleStrategy):

    name = "normal"

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    name = "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        attack = creature.attack
        if not isinstance(creature, TransformCapability):
            self._reject(creature)
            return
        print(creature.transform())
        print(attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):

    name = "defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        attack = creature.attack
        if not isinstance(creature, HealCapability):
            self._reject(creature)
            return
        print(attack())
        print(creature.heal())
