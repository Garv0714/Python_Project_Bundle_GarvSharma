def ask_user_preferences():
    print("\n🔧 Custom Password Configuration:")
    length = int(input("📏 Desired length (8 to 32 recommended): "))

    use_upper = input("🅰️ Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("🔡 Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("🔢 Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("🔣 Include symbols? (y/n): ").lower() == 'y'

    if not any([use_upper, use_lower, use_digits, use_symbols]):
        print("❌ Error: You must include at least one character type.")
        return ask_user_preferences()

    start_cap = input("⚡ Must start with a capital letter? (y/n): ").lower() == 'y'

    return length, use_upper, use_lower, use_digits, use_symbols, start_cap


def generate_password(length, upper, lower, digits, symbols, must_start_cap):
    chars = ''
    if upper: chars += string.ascii_uppercase
    if lower: chars += string.ascii_lowercase
    if digits: chars += string.digits
    if symbols: chars += string.punctuation

    if must_start_cap:
        first_char = random.choice(string.ascii_uppercase)
        rest = ''.join(random.choice(chars) for _ in range(length - 1))
        password = first_char + rest
    else:
        password = ''.join(random.choice(chars) for _ in range(length))

    return password


def get_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    score = min(score, 4)

    return ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"][score]


def save_log(password, strength):
    with open("._pgenlog", "a") as log:
        log.write(f"{password} | {strength}\n")


def main():
    print("🔐 Welcome to Garv's Intelligent Password Forge 🔥")

    length, upper, lower, digits, symbols, must_start_cap = ask_user_preferences()
    password = generate_password(length, upper, lower, digits, symbols, must_start_cap)
    strength = get_strength(password)

    print(f"\n✅ Generated Password: {password}")
    print(f"🔒 Strength Level: {strength}")

    copy = input("📋 Copy password to clipboard? (y/n): ").lower()
    if copy == 'y':
        pyperclip.copy(password)
        print("📎 Password copied to clipboard!")

    save_log(password, strength)
    print("✅ Done. Password securely created.\n")


if __name__ == "__main__":
    try:
        import pyperclip
    except ImportError:
        print("⚠️ pyperclip module not found. Install it using 'pip install pyperclip'")
        exit()

    main()