import bcrypt


class HashingData:
    def __init__(self):
        self.salt = bcrypt.gensalt()

    def validate_data(self, plain_data: str, hashed_data: str) -> bool:
        return bcrypt.checkpw(plain_data.encode(), hashed_data.encode())

    def get_hashed_data(self, data: str) -> str:
        bytes_data = data.encode()
        return bcrypt.hashpw(bytes_data, self.salt).decode()
