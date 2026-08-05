
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)




# read file
dataSet = pd.read_csv('team_stats_2003_2023.csv')








def typeStats():
    print("Here are the available statistics to chose from: \n 1) win/loss ratio \n 2) Total points \n 3) Total yards \n 4) Total touchdowns \n 5) Turnovers")




def totalStats(dS, team, year, x):
    if x == 1:
        teamData = dS[(dS['year'] == year) & (dS['team'] == team)]
        wins = teamData['wins'].values[0]
        loses = teamData['losses'].values[0]
        print("The win/loss ratio for the", year, team, "is", int(wins), '-', int(loses))
    elif x == 2:
        teamData = dS[(dS['year'] == year) & (dS['team'] == team)]
        wins = teamData['points'].values[0]
        print("The total points for the", year, team, "is", wins)
    elif x ==3:
        teamData = dS[(dS['year'] == year) & (dS['team'] == team)]
        yards = teamData['total_yards'].values[0]
        print("The total yards for the", year, team, "is", yards)
    elif x ==4:
        teamData = dS[(dS['year'] == year) & (dS['team'] == team)]
        touchdowns = teamData['rush_td'].values[0] + teamData['pass_td'].values[0]
        print("The total number of touchdowns for the", year, team, "is", touchdowns)
    elif x ==5:
        teamData = dS[(dS['year'] == year) & (dS['team'] == team)]
        turnovers = teamData['turnovers'].values[0]
        print("The total amount of turnovers for the", year, team, "is", turnovers)


# specifies colors associated with each team for overall graph
# AI was used to find colors for teams
team_colors = {
    "New England Patriots": "midnightblue",
    "Miami Dolphins": "aqua",
    "Buffalo Bills": "royalblue",
    "New York Jets": "forestgreen",
    "Baltimore Ravens": "darkviolet",
    "Cincinnati Bengals": "orangered",
    "Pittsburgh Steelers": "gold",
    "Cleveland Browns": "sienna",
    "Indianapolis Colts": "dodgerblue",
    "Tennessee Titans": "skyblue",
    "Jacksonville Jaguars": "darkcyan",
    "Houston Texans": "firebrick",
    "Kansas City Chiefs": "crimson",
    "Denver Broncos": "darkorange",
    "Las Vegas Raiders": "dimgray",
    "Los Angeles Chargers": "lightgoldenrodyellow",
    "Philadelphia Eagles": "darkslategray",
    "Dallas Cowboys": "steelblue",
    "Washington Commanders": "maroon",
    "New York Giants": "mediumblue",
    "Green Bay Packers": "darkgreen",
    "Minnesota Vikings": "mediumpurple",
    "Chicago Bears": "darkslateblue",
    "Detroit Lions": "deepskyblue",
    "Carolina Panthers": "deepskyblue",
    "New Orleans Saints": "peru",
    "Tampa Bay Buccaneers": "firebrick",
    "Atlanta Falcons": "red",
    "Seattle Seahawks": "teal",
    "San Francisco 49ers": "darkred",
    "Arizona Cardinals": "darkred",
    "Los Angeles Rams": "blue",
    # Historical names
    "Washington Redskins": "maroon",
    "Washington Football Team": "maroon",
    "St. Louis Rams": "blue",
    "San Diego Chargers": "lightgoldenrodyellow",
    "Oakland Raiders": "dimgray"
}


#Overall comparison of wins
def comp_of_wins():
# groups dataset by sum of all wins in relation to team
    comparison_of_wins = dataSet.groupby('team')['wins'].sum().sort_values(ascending=False).reset_index()
# sets visual aspects of graph (colors, size, etc)
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'wins', y = 'team', data = comparison_of_wins, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
# sets name of graph
    plt.title("NFL Team Wins (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
# sets x label
    plt.xlabel("Total Wins")
# sets y label
    plt.ylabel("Team")
# shows graph
    plt.show()




# Rest of the graphs are done in a similar fashion to comp_of_wins
# If any major adjustments are made, they will be pointed out via comment


#Overall comparison of losses
def comp_of_losses():
    comparison_of_losses = dataSet.groupby('team')['losses'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'losses', y = 'team', data = comparison_of_losses, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Team Losses (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Total Losses")
    plt.ylabel("Team")
    plt.show()


#Overall Win/Loss Percentage
def win_loss_perc():
# groups dataset by AVERAGE of win/loss % in relation to team
# this is different than previous graphs, which found the SUM
    overall_wins_v_losses = dataSet.groupby('team')['win_loss_perc'].mean().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'win_loss_perc', y = 'team', data = overall_wins_v_losses, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Team Win Loss Percentage (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Win / Loss Percentage")
    plt.ylabel("Team")
    plt.show()


#Overall Points For
def points_for():
    overall_points = dataSet.groupby('team')['points'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'points', y = 'team', data = overall_points, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Team Points (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Points")
    plt.ylabel("Team")
    plt.show()


#Overall Points Against
def points_against():
    overall_points_against = dataSet.groupby('team')['points_opp'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'points_opp', y = 'team', data = overall_points_against, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Team Points Against (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Points Against")
    plt.ylabel("Team")
    plt.show()


#Overall Points Differential
def points_different():
    overall_points_against = dataSet.groupby('team')['points_diff'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'points_diff', y = 'team', data = overall_points_against, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Team Points Differential (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Points Differential")
    plt.ylabel("Team")
    plt.show()


#Overall average margin of victory
def av_margin_victory():
    overall_margin_of_victory = dataSet.groupby('team')['mov'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'mov', y = 'team', data = overall_margin_of_victory, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Margin of Victory (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Margin of Victory")
    plt.ylabel("Team")
    plt.show()


#Overall Games Played
def games_played():
    overall_games_played = dataSet.groupby('team')['g'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'g', y = 'team', data = overall_games_played, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Games Played (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Total Games Played")
    plt.ylabel("Team")
    plt.show()


#Overall Offensive Yards Gained
def offen_yards_gained():  


    overall_off_yards_gained = dataSet.groupby('team')['total_yards'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'total_yards', y = 'team', data = overall_off_yards_gained, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Offensive Yards Gained (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Offensive Yards Gained")
    plt.ylabel("Team")
    plt.show()
#Overall Offensive Plays Ran
def offen_plays_ran():  
    overall_off_plays_ran = dataSet.groupby('team')['plays_offense'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'plays_offense', y = 'team', data = overall_off_plays_ran, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Offensive Plays Ran (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Offensive Plays Ran")
    plt.ylabel("Team")
    plt.show()


#Overall Yards Per Offense Play
def yds_per_off_play():  
    overall_yds_per_off = dataSet.groupby('team')['yds_per_play_off'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'yds_per_play_off', y = 'team', data = overall_yds_per_off, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Yards Per Offense Play (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Yards Per Offense Play")
    plt.ylabel("Team")
    plt.show()


#Overall Turnover Lost
def turnover_lost():
    overall_turnover_lost = dataSet.groupby('team')['turnovers'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'turnovers', y = 'team', data = overall_turnover_lost, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Turnover Lost (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Turnover Lost")
    plt.ylabel("Team")
    plt.show()


#Overall Fumble Lost
def fumble_lost():
    overall_fumble_lost = dataSet.groupby('team')['fumbles_lost'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'fumbles_lost', y = 'team', data = overall_fumble_lost, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Fumbles Lost (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Fumbles Lost")
    plt.ylabel("Team")
    plt.show()


#Overall First Downs Gained
def first_downs_gained():
    overall_first_downs_gained = dataSet.groupby('team')['first_down'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'first_down', y = 'team', data = overall_first_downs_gained, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams First Downs Gained (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("First Downs Gained")
    plt.ylabel("Team")
    plt.show()


#Overall Passes Completed
def passes_completed():
    overall_passes_completed = dataSet.groupby('team')['pass_cmp'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'pass_cmp', y = 'team', data = overall_passes_completed, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Passes Completed (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Passes Completed")
    plt.ylabel("Team")
    plt.show()


#Overall Pass Attempts
def pass_attempts():
    overall_pass_attempts = dataSet.groupby('team')['pass_att'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'pass_att', y = 'team', data = overall_pass_attempts, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Pass Attempts (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Pass Attempts")
    plt.ylabel("Team")
    plt.show()


#Overall Passing Yards
def passing_yds():
    overall_passing_yards = dataSet.groupby('team')['pass_yds'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'pass_yds', y = 'team', data = overall_passing_yards, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Passing Yards (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Passing Yards")
    plt.ylabel("Team")
    plt.show()


#Overall Passing TDs
def passing_tds():  
    overall_passing_tds = dataSet.groupby('team')['pass_td'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'pass_td', y = 'team', data = overall_passing_tds, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Passing Touchdowns (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Passing TDs")
    plt.ylabel("Team")
    plt.show()


#Overall Interceptions Thrown
def intercept_thrown():
    overall_interceptions_thrown = dataSet.groupby('team')['pass_int'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'pass_int', y = 'team', data = overall_interceptions_thrown, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Interceptions Thrown (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Interceptions")
    plt.ylabel("Team")
    plt.show()


#Overall Net Yards Gained Per Pass Attempt
def net_yds_gained_ppa():
# groups dataset by AVERAGE of Net Yards Gained in relation to team
# this is different than previous graphs, which found the SUM
    overall_net_yards_ppa = dataSet.groupby('team')['pass_net_yds_per_att'].mean().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'pass_net_yds_per_att', y = 'team', data = overall_net_yards_ppa, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Net Yards Gained Per Pass Attempt (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Yards Gained Per Pass Attempt")
    plt.ylabel("Team")
    plt.show()


#Overall Passing First Downs Gained
def passing_first_downs_gained():
    overall_passing_fds_gained = dataSet.groupby('team')['pass_fd'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'pass_fd', y = 'team', data = overall_passing_fds_gained, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Passing First Downs Gained (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Passing First Downs Gained")
    plt.ylabel("Team")
    plt.show()


#Overall Rushing Attempts
def rushing_attempts():
    overall_rushing_attempts = dataSet.groupby('team')['rush_att'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'rush_att', y = 'team', data = overall_rushing_attempts, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Rushing Attempts (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Rushing Attempts")
    plt.ylabel("Team")
    plt.show()


#Overall Rushing Yards
def rushing_yds():
    overall_rushing_yards = dataSet.groupby('team')['rush_yds'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'rush_yds', y = 'team', data = overall_rushing_yards, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Rushing Yards (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Rushing Yards")
    plt.ylabel("Team")
    plt.show()


#Overall Rushing TDs
def rushing_tds():
    overall_rushing_tds = dataSet.groupby('team')['rush_td'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'rush_td', y = 'team', data = overall_rushing_tds, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Rushing Touchdowns (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Rushing TDs")
    plt.ylabel("Team")
    plt.show()


#Overall Rushing Yards Per Attempt
def rushing_yds_pa():
    overall_rushing_yds_per_att = dataSet.groupby('team')['rush_yds_per_att'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'rush_yds_per_att', y = 'team', data = overall_rushing_yds_per_att, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Rushing Yards Per Attempt (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Rushing Yards Per Attempt")
    plt.ylabel("Team")
    plt.show()


#Overall Rushing First Downs
def rushing_fds():
    overall_rushing_first_downs = dataSet.groupby('team')['rush_fd'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'rush_fd', y = 'team', data = overall_rushing_first_downs, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Rushing First Downs (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Rushing First Downs")
    plt.ylabel("Team")
    plt.show()


#Overall Penalties Committed
def penalties_ct():
    overall_penalties_committed = dataSet.groupby('team')['penalties'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'penalties', y = 'team', data = overall_penalties_committed, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Penalties Committed (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Penalties Committed")
    plt.ylabel("Team")
    plt.show()


#Overall Penalty Yards Committed
def penalty_yds_ct():
    overall_penalty_yards_committed = dataSet.groupby('team')['penalties_yds'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'penalties_yds', y = 'team', data = overall_penalty_yards_committed, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Penalty Yards Committed (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Penalty Yards Committed")
    plt.ylabel("Team")
    plt.show()


#Overall First Downs by Penalty
def fd_by_penalty():
    overall_fd_by_penalty = dataSet.groupby('team')['pen_fd'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'pen_fd', y = 'team', data = overall_fd_by_penalty, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams First Downs by Penalty (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("First Downs by Penalty")
    plt.ylabel("Team")
    plt.show()


#Overall Percentage of Drives Ending in Score
def pct_driving_end_score():
# groups dataset by MEAN of % of drives, in relation to team
# this is different than previous graphs, which found the SUM
    overall_pct_drives_score = dataSet.groupby('team')['score_pct'].mean().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'score_pct', y = 'team', data = overall_pct_drives_score, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Percent of Drives Ending in a Score (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Percent of Drives Ending in a Score")
    plt.ylabel("Team")
    plt.show()


#Overall Percentage of Drives Ending in Turnover
def pct_driving_end_to():
# groups dataset by AVERAGE of % of drives ending in TO, in relation to team
# this is different than previous graphs, which found the SUM
    overall_pct_drives_to = dataSet.groupby('team')['turnover_pct'].mean().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'turnover_pct', y = 'team', data = overall_pct_drives_to, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Percent of Drives Ending in a Turnover (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Percent of Drives Ending in a Turnover")
    plt.ylabel("Team")
    plt.show()


#Overall Expected Points Contributed by Offense
def expt_pts_contributed_offense():
    overall_expected_pts_offense = dataSet.groupby('team')['exp_pts_tot'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'exp_pts_tot', y = 'team', data = overall_expected_pts_offense, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Expected Points Contributed by Offense (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Expected Points Contributed by Offense")
    plt.ylabel("Team")
    plt.show()


#Overall Tied Games: ties
def tied():
    overall_tied_games = dataSet.groupby('team')['ties'].sum().sort_values(ascending=False).reset_index()
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize = (12, 8))
    sns.barplot(x = 'ties', y = 'team', data = overall_tied_games, palette = team_colors)
    fig.patch.set_facecolor('lightgray')
    ax.set_facecolor('white')
    plt.title("NFL Teams Tied Games (2003 - 2023 Seasons)", fontsize = 24, fontweight = "bold")
    plt.xlabel("Tied Games")
    plt.ylabel("Team")
    plt.show()


def ifStatements(input):
    if (input == 1):
            comp_of_wins()
           
    elif (input == 2):
            comp_of_losses()
    elif (input == 3):
            win_loss_perc()
    elif (input == 4):
            points_for()
    elif (input == 5):
            points_against()
    elif (input == 6):
            points_different()
    elif (input == 7):
            av_margin_victory()
    elif (input == 8):
            games_played()
    elif (input == 9):
            offen_yards_gained()
    elif (input == 11):
            yds_per_off_play()
    elif (input == 12):
            turnover_lost()
    elif (input == 13):
            fumble_lost()
    elif (input == 14):
            first_downs_gained()
    elif (input == 15):
            passes_completed()
    elif (input == 16):
            pass_attempts()
    elif (input == 17):
            passing_yds()
    elif (input == 18):
            passing_tds()
    elif (input == 19):
            intercept_thrown()
    elif (input == 20):
            net_yds_gained_ppa()
    elif (input == 21):
            passing_first_downs_gained()
    elif (input == 22):
            rushing_attempts()
    elif (input == 23):
            rushing_yds()
    elif (input == 24):
            rushing_tds()
    elif (input == 25):
            rushing_yds_pa()
    elif (input == 26):
            rushing_fds()
    elif (input == 27):
            penalties_ct()
    elif (input == 28):
            penalty_yds_ct()
    elif (input == 29):
            fd_by_penalty()
    elif (input == 30):
            pct_driving_end_score()
    elif (input == 31):
            pct_driving_end_to()
    elif (input == 32):
            expt_pts_contributed_offense()
    elif (input == 33):
            tied()
    elif (input == 10):
            offen_plays_ran()








def main():
    dataSet = pd.read_csv('team_stats_2003_2023.csv')
    askAgain = 1
    try:
        while askAgain != 0:
            #Ask again is a loop that only breaks when the user does not want anymore statistics
            askAgain = int(input("What would you like to do? \n 1) See graphs of the overall NFL \n 2) See stats for specific teams \n 3) End Session\n"))
            #If they want to see the graphs...
            if askAgain == 1:
                graphLoop = 2
                #Graph loop is a loop that only breaks when the user wants to either see the menu or close out
                while graphLoop != 0:
                    inpt = int(input("What graph would you like to see (Answer with Number Value) :\n 1) Overall comparison of wins: wins \n 2)Overall comparison of losses \n 3)Overall Win/Loss Percentage: \n 4)Overall Points for: \n 5)Points Against: \n 6)points differential: \n 7)average margin of victory: \n 8)Overall Games Played: \n 9)Overall Offensive Yards Gained: \n 10)Overall Offensive Plays Ran \n 11)Overall Team Turnover Lost \n 12)Overall Team Fumble Lost \n 13)Overall First Downs Gained \n 14)Overall Passes Completed \n 15)Overall Pass Attempts \n 16)Overall Passing Yards \n 17)Overall Passing TDs \n 18)Overall Interceptions Thrown \n 19)Overall Net Yards Gained Per Pass Attempt \n 20)Overall Passing First Downs Gained \n 21)Overall Rushing Attempts \n 22)Overall Rushing Yards \n 23)Overall Rushing TDs \n 24)Overall Rushing Yards Per Attempt \n 25)Overall Rushing First Downs \n 26)Overall Penalties Committed \n 27)Overall Penalty Yards Committed \n 28)Overall First Downs by Penalty \n 29)Overall Percentage of Drives Ending in Score \n 30)Overall Percentage of Drives Ending in Turnover \n 31)Overall Expected Points Contributed by Offense \n 32)Overall Tied Games \n 33) Overall Offensive Plays Ran\n"))
                    ifStatements(inpt)
                    graphLoop = int(input("Would you like to see another graph (1) \n see stats for a specific team (2) \n or close out (0)\n"))
                    if graphLoop == 0:
                        print("Have a good day!\n")
                        exit()
                    elif graphLoop == 2:
                     askAgain = 2
                     graphLoop = 0
            #If they want to see individual team stats...
            elif askAgain == 2:
                print("These are the NFL teams:", dataSet['team'].unique())
                teamName = str(input("What team's stats would you like to see?: \n"))
                teamYear = int(input("What season would you like to see? (2003 - 2023): \n"))
                typeStats()
                statType = int(input("What # stat would you like to see? type 0 to end session: \n"))
                while statType != 0:
                    totalStats(dataSet, teamName, teamYear, statType)
                    print(" ")
                    typeStats()
                    statType = int(input("\nWhat # stat would you like to see? Type 0 to end session, type 6 to go back to main menu: \n"))
                    if statType == 0:
                        askAgain = 0
                    elif statType == 6:
                        statType = 0
                    else:
                        askAgain = 1
            elif askAgain == 3:
                print("Have a good day!\n")
                exit()
            else:
                print("Invalid answer, Please try again.\n")
                askAgain = 1
    #If the input is not an int...
    except ValueError:
            print("Have a good day!\n")
            exit()
main()



