from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class PasswordAuth(Authentication):
    def login(self):
        print("Logged in using password.")

    def logout(self):
        print("Logged out from password authentication.")

class OTPAuth(Authentication):
    def login(self):
        print("Logged in using OTP.")

    def logout(self):
        print("Logged out from OTP authentication.")

for auth in [PasswordAuth(), OTPAuth()]:
    auth.login()
    auth.logout()
