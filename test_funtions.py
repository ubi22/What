from fn import hello_who,salary
def test_hellp_who():
    assert hello_who("Jonn") == "Hello Jonn"
    assert hello_who("Jonn") == "Hello Jonn лОх"
    assert hello_who("Jonn") == "Hello Jonn"
    assert hello_who("Jonn") == "Hello Jonn лОх"

def test_salary():
    assert salary(2, 5) == 10
    assert salary(2, 5) == 10
    assert salary(2, 5) == 10

