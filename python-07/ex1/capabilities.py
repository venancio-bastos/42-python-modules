import abc


class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self, target: str | None = None) -> str:
        pass


class TransformCapability(abc.ABC):
    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass
