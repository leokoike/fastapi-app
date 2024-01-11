from abc import ABC, abstractmethod


class TokenResolver(ABC):
    @abstractmethod
    def generate_token(self, data: dict) -> str:
        raise NotImplementedError

    @abstractmethod
    def decode_token(self, token: str) -> dict:
        raise NotImplementedError
