ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def apply_permutation(index, permutation, offset):
    """
    Translates the index of a character by applying both a permutation
    and a cyclic offset.  The index argument is the position at which
    the process starts and the method returns the new index after
    applying both transformations.
    """
    shifted_idx = (index + offset) % 26
    wired_letter = permutation[shifted_idx]
    target_idx = ord(wired_letter) - ord("A")
    #target_idx = ALPHABET.find(wired_letter) can also work if imported
    return (target_idx - offset) % 26


# Unit test

def test_apply_permutation():
    ROTOR = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

    assert apply_permutation(0, ROTOR, 0) == 4
    assert apply_permutation(1, ROTOR, 0) == 10
    assert apply_permutation(9, ROTOR, 1) == 12
    assert apply_permutation(2, ROTOR, 4) == 25

def invert_key(key):
    """Inverts a 26-letter key for a letter-substitution cipher.
    Args:
        key (str): the 26-letter encryption string
    Returns:
        (str): the corresponding 26-letter decryption string
    """
    # newkey = ""
    # for ch in ALPHABET:
    #     newkey += ALPHABET[key.find(ch)]
    # return newkey

    return ''.join(ALPHABET[key.find(ch)] for ch in ALPHABET)

# Unit test

def test_invert_key():
    """Tests several encryption and resulting decryption strings"""
    assert invert_key(ALPHABET) == ALPHABET
    en_key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    de_key = "KXVMCNOPHQRSZYIJADLEGWBUFT"
    assert invert_key(en_key) == de_key
    assert invert_key(de_key) == en_key


# Startup code

if __name__ == "__main__":
    test_invert_key()