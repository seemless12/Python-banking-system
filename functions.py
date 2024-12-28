
def generate_account_number():
    """Generate a random 10-digit Account number"""
    return ''.join(random.choices(string.digits, k=10))

def generate_password():
    """Generate a random 8-character Password"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
