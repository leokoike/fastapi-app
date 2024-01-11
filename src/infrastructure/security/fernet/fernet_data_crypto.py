from cryptography.fernet import Fernet
from src.domain.security.data_crypto import DataCrypto


class FernetDataCrypto(DataCrypto):
    def __init__(self, key: str) -> None:
        self.key: bytes = key.encode()
        self.fernet: Fernet = Fernet(key=self.key)

    def compare_value(
        self,
        value: str,
        encrypted_value: str,
    ) -> None:
        if self.fernet.encrypt(value.encode()).decode() != encrypted_value:
            raise Exception

    def encrypt_data(
        self,
        data: str,
    ) -> str:
        return self.fernet.encrypt(data.encode()).decode()
