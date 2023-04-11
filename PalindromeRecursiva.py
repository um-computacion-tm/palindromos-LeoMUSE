
def palindromeRecursiva(Word):
    if len(Word) <= 1:
        return True

    if Word[0] == Word[-1]:
        return palindromeRecursiva(Word[1:-1])

    else:
        return False

if __name__ == '__main__':
    pass
    