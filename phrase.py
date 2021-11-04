
def test_phrase_len():
    phrase = input("Set a phrase: ")
    expect_number = 15
    assert len(phrase) <= expect_number, "Длина фразы привышает 15 символов"
