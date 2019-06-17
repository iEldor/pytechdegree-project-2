import common  # common function library
import logging
from constants import TEAMS, PLAYERS
from copy import deepcopy
from datetime import datetime
from random import randint
from statistics import mean

APP_NAME = "Basketball Team Statistics"

logging.basicConfig(filename='app.log', level=logging.DEBUG)


def distribute_players(player_list, team_list):
    clean_list = []
    while player_list:
        for team in team_list:
            random_selection = randint(0, len(player_list) - 1)
            player = player_list[random_selection]
            player['team'] = team
            player['guardians'] = player['guardians'].split(' and ')
            player['height'] = int(player['height'][:2])
            player['experience'] = True if player['experience'] == 'YES' else False
            clean_list.append(player_list.pop(random_selection))
    return clean_list


def get_player_count(team_name):
    return len([player for player in final_list if player['team'] == team_name])


def check_balancing_successful():
    counts = [get_player_count(team) for team in teams]
    counts = set(counts)
    if len(counts) == 1:
        matches = True
        logging.info("{}: Team Balancing completed successfully. Each team has {} players".format(datetime.today(),counts))
    else:
        logging.warning("{}: Team Balancing completed unsuccessfully. Teams have {} players".format(datetime.today(),counts))


def get_player_names(team_name):
    names = [player['name'] for player in final_list if player['team'] == team_name]
    return ", ".join(names)


def get_other_counts(team_name, key, value):
    return len([player for player in final_list if player['team'] == team_name and player[key] == value])


def get_avg_height(team_name):
    height = mean([player['height'] for player in final_list if player['team'] == team_name])
    return round(height, 2)


def get_guardians(team_name):
    guardians = [", ".join(player['guardians']) for player in final_list if player['team'] == team_name]
    guardians = set(guardians)
    return ", ".join(guardians)


def display_team_list(team_list):
    common.print_title("List of Teams with Statistics")
    counter = 1
    for team in team_list:
        print("{}) {}".format(counter, team))
        counter += 1
    print("\n0) To RETURN to the Main Menu")


def display_team_stat(team_name):
    common.clear_screen()
    common.print_title("Displaying Team Statistics for: {}".format(team_name))
    print("Number of Players: {}".format(get_player_count(team_name)))
    print("\nPlayers: {}".format(get_player_names(team_name)))
    print("\nNumber of Newbies: {}".format(get_other_counts(team_name, "experience", False)))
    print("\nNumber of Pros: {}".format(get_other_counts(team_name, "experience", True)))
    print("\nAverage Height: {}".format(get_avg_height(team_name)))
    print("\nGuardians: {}".format(get_guardians(team_name)))


def start_app():
    logging.info("{}: Application Started".format(datetime.today()))
    common.clear_screen()
    while True:
        common.print_title("Welcome to {}".format(APP_NAME))
        option_selected = common.display_menu("""Please select from available menu options e.g. 1:

1) Display Team Statistics
2) Quit
""")
        try:
            option_selected = int(option_selected)
            if option_selected == 1:
                common.clear_screen()
                sub_menu = True
                while sub_menu:
                    display_team_list(teams)
                    option_selected = common.display_menu("")
                    try:
                        option_selected = int(option_selected)
                        if option_selected < 0 or option_selected > len(teams):
                            raise ValueError
                        elif option_selected == 0:
                            common.clear_screen()
                            sub_menu = False
                        else:
                            team = teams[option_selected-1]
                            display_team_stat(team)
                            input("\nPress ENTER to continue ... ")
                            common.clear_screen()
                    except ValueError:
                        common.invalid_entry(option_selected)
                        continue
            elif option_selected == 2:
                print()
                common.print_title("Thank you for using {}!".format(APP_NAME))
                logging.info("{}: Application Closed".format(datetime.today()))
                break
            else:
                raise ValueError
        except ValueError:
            common.invalid_entry(option_selected)
            continue


if __name__ == "__main__":
    teams = deepcopy(TEAMS)
    players = deepcopy(PLAYERS)
    pros = [player for player in players if player["experience"] == "YES"]
    newbies = [player for player in players if player["experience"] == "NO"]
    final_list = []
    final_list.extend(distribute_players(pros, teams))
    final_list.extend(distribute_players(newbies, teams))
    check_balancing_successful()
    start_app()
