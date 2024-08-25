from project import scrap_data, user_log_or_sign_in, print_unselected_players, Player, Team
import sys
from io import StringIO
import pytest,re

def test_scrap_data():
    players = scrap_data()
    assert len(players) > 0
    assert all(isinstance(player, Player) for player in players)

def test_user_log_or_sign_in(capsys):
    sys.argv = ["project.py", "sign"]
    sys.stdin = StringIO("invalid-email@@..com\nvalid@gmail.com\npassword123\nusername\n")
    user_log_or_sign_in()
    captured = capsys.readouterr()
    output = captured.out.strip()
    matches = re.search("Invalid email address.", output)
    assert matches is not None

    sys.argv = ["project.py", "log"]
    sys.stdin = StringIO("test@example.com\nwrongpassword\ntest@example.com\npassword123\n")
    user_log_or_sign_in()
    captured = capsys.readouterr()
    output = captured.out.strip()
    matches = re.search("username and/or password is wrong.", output)
    assert matches is not None


def test_print_unselected_players(capsys):
    players = [
        Player("Player 1", "Team A", "85", "CM"),
        Player("Player 2", "Team B", "90", "ST")
    ]

    players[0].selected = True

    print_unselected_players(players)
    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "Player 1" not in output
    assert "Player 2" in output
