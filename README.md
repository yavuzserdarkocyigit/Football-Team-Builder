# Football Team Builder

#### Description:

The Football Team Management System is a Python-based application designed to manage football players and teams. Users can register, log in, view available players, and create teams with specific constraints. The system uses various classes and functions to implement its features.

## Classes and Functions

### 1. `Player` Class

This class represents a football player and stores relevant information about the player.

- **Attributes**:
  - `_name`: The name of the player.
  - `_team`: The team the player is associated with.
  - `_stat`: The player's overall rating.
  - `_position`: The position the player plays in (e.g., midfielder, striker).
  - `_selected`: A boolean flag to indicate if the player has been selected for a team.

- **Methods**:
  - `__init__(self, name, team, stat, position)`: Initializes a new player with the given attributes.
  - Getter methods for `name`, `team`, `stat`, `position`, and `selected` properties.
  - Setter method for the `selected` property.
  - `__repr__(self)`: Returns a string representation of the player for debugging and display purposes.

### 2. `Team` Class

This class represents a football team and manages a collection of players.

- **Attributes**:
  - `_team_name`: The name of the team/user.
  - `_players`: A list that stores the players in the team.

- **Methods**:
  - `__init__(self, team_name)`: Initializes a new team with the specified name.
  - `add_player(self, *players)`: Adds one or more players to the team, ensuring no player is selected for multiple teams. If the player is already selected or the team has reached the maximum size (18 players), appropriate messages or exceptions are raised.
  - `remove_player(self, player_name)`: Removes a player from the team by name and marks the player as unselected.
  - `__str__(self)`: Returns a string representation of the team, displaying the list of players in a tabular format.

### 3. `scrap_data()` Function

This function fetches player data from an online source and returns a list of `Player` objects.

- **Process**:
  - Makes an HTTP request to a specified URL to get player data.
  - Parses the HTML response using `BeautifulSoup` to extract player information such as name, team, stat, and position.
  - Creates `Player` objects for each player and adds them to a list.
  - Returns the list of players.

### 4. `user_log_or_sign_in()` Function

This function handles user authentication, allowing users to log in or register.

- **Process**:
  - Checks command-line arguments to determine if the user is logging in (`log`) or signing up (`sign`).
  - For login, prompts the user for their email and password, checks these against stored user data in `users.csv`.
  - For registration, prompts the user for a valid email, password, and username, then stores this information in `users.csv`.
  - Displays appropriate messages for successful login, registration, or errors.

### 5. `print_unselected_players(players)` Function

This function displays a list of players who have not been selected for any team.

- **Process**:
  - Takes a list of `Player` objects as input.
  - Filters the list to include only players who are not selected (`selected` is `False`).
  - Displays the filtered list in a tabular format, showing each player's name, team, overall rating, and position.

### 6. `main()` Function

The main entry point for the application, which orchestrates the overall workflow.

- **Process**:
  - Calls `scrap_data()` to fetch and display player data.
  - Invokes `user_log_or_sign_in()` for user authentication.
  - Allows the user to manage teams by adding and removing players using the `Team` class methods.
  - Displays the state of the team after various operations.

## Unit Tests

### `test_scrap_data()`

Tests the `scrap_data()` function to ensure it correctly fetches player data.

- **Checks**:
  - Asserts that the returned list of players is not empty.
  - Asserts that all items in the list are instances of the `Player` class.

### `test_user_log_or_sign_in(capsys)`

Tests the `user_log_or_sign_in()` function for various user input scenarios.

- **Sign Up with Invalid Email**:
  - Simulates user inputs for signing up with an invalid email, followed by a valid email, password, and username.
  - Asserts that the output contains the message "Invalid email address."

- **Log In with Wrong Password**:
  - Simulates user inputs for logging in with a registered email but an incorrect password, followed by correct credentials.
  - Asserts that the output contains the message "username and/or password is wrong."

### `test_print_unselected_players(capsys)`

Tests the `print_unselected_players(players)` function to ensure it correctly filters and displays players.

- **Scenario**:
  - Creates two `Player` objects, marks one as selected, and passes them to the function.
  - Asserts that the selected player does not appear in the output.
  - Asserts that the unselected player appears in the output.

## Requirements

To run this project, you will need the following Python packages:

- `requests`: To make HTTP requests for fetching player data.
- `beautifulsoup4`: To parse HTML and extract player information.
- `tabulate`: To display data in a formatted table.
- `validator-collection`: To validate user inputs such as email addresses.
- `pyfiglet`: To create ASCII art for enhancing the terminal output.
- `pytest`: To run the test suite.

You can install these dependencies using the following command:

```bash
pip install -r requirements.txt
```

To run the tests, use pytest:

```bash
pytest test_project.py
```
