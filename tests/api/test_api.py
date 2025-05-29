import pytest

# Verify that user's name can be cleared
@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''

# Check that user's first name is set to "Ivan"
@pytest.mark.check
def test_name(user):
    assert user.name == 'Ivan'

# Check that user's last name is set to "Nikitenko"
@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Nikitenko'  


