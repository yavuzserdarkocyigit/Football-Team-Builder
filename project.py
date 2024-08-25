import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from validator_collection import validators
import csv
import sys
from pyfiglet import Figlet

class Player:
    def __init__(self, name, team, stat, position):
        self._name = name
        self._team = team
        self._stat = stat
        self._position = position
        self._selected = False

    @property
    def name(self):
        return self._name

    @property
    def team(self):
        return self._team

    @property
    def stat(self):
        return self._stat

    @property
    def position(self):
        return self._position

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value

    def __repr__(self):
        return f"Player(Name: {self._name}, Team: {self._team}, Stat: {self._stat}, Position: {self._position})"

class Team:
    def __init__(self, team_name):
        self._team_name = team_name
        self._players = []

    def add_player(self, *players):
        for player in players:
            if player.selected:
                print((f"{player.name} has already been selected for another team."))
                continue
            if len(self._players) < 18:
                self._players.append(player)
                player.selected = True
            else:
                raise ValueError("This team already has 18 players.")

    def remove_player(self, player_name):
        for player in self._players:
            if player.name == player_name:
                player.selected = False
                self._players.remove(player)
                return
        raise ValueError(f"No player named {player_name} in the team.")

    def __str__(self):
        table = [[player.name, player.position, player.stat] for player in self._players]
        headers = ["Name", "Position", "Overall"]
        return tabulate(table, headers, tablefmt = "grid")

def main():
    players = scrap_data()
    print("\nAll Players:")
    print_unselected_players(players)

    user_log_or_sign_in()

    team1 = Team("Dream Team")
    try:
        team1.add_player(players[0], players[1], players[2])
        print("\nTeam after adding 3 players:")
        print(team1)

        team1.add_player(players[0])

    except ValueError:
        print("Not allowed to add same player to your team.")

    team1.remove_player(players[0].name)
    print("\nTeam after removing a player:")
    print(team1)


def scrap_data():
    players_data =[]
    up_to_page = 1
    for page in range(up_to_page + 1):
        url = "https://www.futwiz.com/en/fc24/career-mode/players?page=" + str(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        player_rows = soup.find_all("tr", class_= "table-row")

        #player data
        for row in player_rows:
            name_tag = row.find("p", class_= "name")
            if name_tag:
                name = name_tag.find("b").text.strip()

            team_tag = row.find("p", class_= "team")
            if team_tag:
                team = team_tag.text.strip()

            stat_tag = row.find("td", class_= "statCol")
            if stat_tag:
                stat = stat_tag.text.strip()

            position_tag = row.find_all("td", class_= "statCol")[2]
            if position_tag:
                position = position_tag.text.strip()

            player = Player(name, team, stat, position)
            players_data.append(player)

    return players_data

def user_log_or_sign_in():
    if len(sys.argv) == 2:
        logged = False
        while logged == False:
            if sys.argv[1] == "log":
                email = input("email: ").strip()
                password = input("password: ").strip()
                with open("users.csv", "r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if email == row["email"] and password == row["password"]:
                            f = Figlet(font='speed')
                            print(f.renderText("Welcome!"))
                            logged = True
                    if logged == False:
                        print("username and/or password is wrong.")

            elif sys.argv[1] == "sign":
                email = input("email: ").strip()
                try:
                    validators.email(email)
                    password = input("password: ").strip()
                    username = input("Create a username: ")
                    with open("users.csv", "a") as file:
                        writer = csv.DictWriter(file, fieldnames = ["username", "email", "password"])
                        writer.writerow({"username": username, "email": email, "password": password})
                    logged = True

                except ValueError:
                    print("Invalid email address.")

    else:
        sys.exit("Please just type 'log' or 'sign'")

def print_unselected_players(players):
    unselected_players = [player for player in players if not player.selected]
    table = [[player.name, player.team, player.stat, player.position] for player in unselected_players]
    headers = ["Name", "Team", "Overall", "Position"]
    print(tabulate(table, headers, tablefmt = "grid"))

if __name__ == "__main__":
    main()
