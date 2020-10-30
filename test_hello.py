import hello

def test_inputUserChoice():
    name = "Karen"
    assert name == hello.name, "Name returned was not those given"

def test_createMessage():
    message = "Hello Karen"
    assert message == hello.createMessage(hello.name), "Message returned does not match"

# def test_blank_input
#     with pytest.raises(AssertionError):
#         name = hello.name(None)