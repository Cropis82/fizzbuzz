from fizzbuzz import fizzbuzz

def test_base():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(13) == 13

def test_fizz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(9) == "Fizz"

def test_buzz():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(25) == "Buzz"

def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"

def esegui_test(test, nome_test):
    try:
        test()
        print(f"{nome_test} ok")
        return True
    except AssertionError:
        print(f"{nome_test} fallito")
        return False
    
def run_test():
    print("\n=== AVVIO TEST ===\n")
    test_ok = 0
    test_ok += 1 if esegui_test(test_base, "test_base") else 0
    test_ok += 1 if esegui_test(test_fizz, "test_fizz") else 0
    test_ok += 1 if esegui_test(test_buzz, "test_buzz") else 0
    test_ok += 1 if esegui_test(test_fizzbuzz, "test_fizzbuzz") else 0
    print(f"\n=== TEST COMPLETATI ===")
    print(f"Test superati: {test_ok}/4" )
run_test()