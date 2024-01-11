from abc import ABC, abstractmethod


class DataCrypto(ABC):
    @abstractmethod
    def compare_value(self, value: str, encrypted_value: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def encrypt_data(self, data: str) -> str:
        raise NotImplementedError
