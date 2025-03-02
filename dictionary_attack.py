import itertools
import string


def dictionary_attack(username, password, dictionary):
    print("\n[+] Performing Dictionary Attack...")
    dictionary_set = set(word.strip() for word in dictionary)  # Use a set for faster lookups
    if password in dictionary_set:
        print(f"[SUCCESS] Password cracked! Username: {username}, Password: {password}")
        return True
    print("[FAILED] Dictionary attack unsuccessful.")
    return False


def brute_force_attack(username, password):
    print("\n[+] Performing Brute Force Attack...")
    chars = string.ascii_letters  # A-Z, a-z
    attempt_count = 0
    for attempt in itertools.product(chars, repeat=5):
        attempt = ''.join(attempt)
        attempt_count += 1
        if attempt == password:
            print(f"[SUCCESS] Password cracked! Username: {username}, Password: {password} (Attempts: {attempt_count})")
            return True
    print(f"[FAILED] Brute force attack unsuccessful after {attempt_count} attempts.")
    return False


def main():
    try:
        username = input("Enter username: ")  # Using input but handling error
    except OSError:
        print("[ERROR] Input not supported. Using default username.")
        username = "test_user"

    password = "pA5sW"  # Hardcoded correct password (Consider securing it)
    dictionary = ["admin", "password", "12345", "letmein", "qwerty", "pA5sW"]  # Example dictionary

    if not dictionary_attack(username, password, dictionary):
        brute_force_attack(username, password)


if __name__ == "__main__":
    main()
