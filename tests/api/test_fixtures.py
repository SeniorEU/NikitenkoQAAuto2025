import pytest

# Check that user's first name is "Ivan"
@pytest.mark.check
def test_change_name(user):
    assert user.name == 'Ivan'

# Check that user's last name is "Nikitenko"
@pytest.mark.check    
def test_change_second_name(user):
    assert user.second_name == 'Nikitenko'