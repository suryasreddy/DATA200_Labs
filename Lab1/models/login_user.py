class LoginUser:
    def __init__(self, user_id, password, role):
        """
        Initialize the LoginUser with email_id and an *encrypted* version of the password.
        """
        self.user_id = user_id
        # Store the password in encrypted form
        self._encrypted_password = self.encrypt_password(password)
        self.password = password
        self.role = role

    def login(self, entered_password):
        """
        Decrypts the stored password and compares it with 'entered_password'.
        Returns True if login is successful, False otherwise.
        """
        stored_password = self.decrypt_password(self._encrypted_password)
        if stored_password == entered_password:
            print("Login successful.")
            return True
        else:
            print("Login failed. Incorrect password.")
            return False

    def logout(self):
        """
        Simple logout method.
        """
        print("Logout successful.")

    def change_password(self, new_password):
        """
        Encrypts and updates the stored password.
        """
        self._encrypted_password = self.encrypt_password(new_password)
        print("Password changed successfully.")

    @staticmethod
    def encrypt_password(password):
        """
        Caeser Cypher password encryption
        """
        encrypted = "".join(chr(ord(char) + 3) for char in password)
        return encrypted

    @staticmethod
    def decrypt_password(encrypted):
        """
        Reverses the simple shift-based encryption above.
        """
        decrypted = "".join(chr(ord(char) - 3) for char in encrypted)
        return decrypted

    def __str__(self):
        """
        String representation of the LoginUser object.
        (Does not reveal the decrypted password.)
        """
        return (f"LoginUser(Email_id={self.email_id}, "
                f"EncryptedPassword={self._encrypted_password})")
