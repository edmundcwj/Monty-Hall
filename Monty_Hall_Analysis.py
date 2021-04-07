import pandas as pd


def print_values(results):
    df = pd.DataFrame(results)
    df = df.rename(columns={0: 'Prior', 1: 'Posterior', 2: 'Result'})

    prior_group = df.groupby('Prior')
    posterior_group = df.groupby(['Prior', 'Posterior'])

    print("""
        Distribution of Prior Selections p(A)
        """)
    print(prior_group.count()["Result"])

    print("""
        Distribution of Posterior Selections p(A|B)
        Note, this is NOT the distribution of WINNING,
        only the rate at which each value is selected
        """)

    print(posterior_group.count()["Result"])

    print("""
        Data on wins
        """)

    winrate = df.groupby(['Result']).count()['Posterior']

    print(f"""
            Wins:{winrate[1]} 
            Losses: {winrate[0]} 
            Winrate: {winrate[1] / (winrate[1] + winrate[0])}
            """)

    print("""
        Wins by Posterior Selection
        """)

    print(calculate_winrate(posterior_group))


def calculate_winrate(groupby_structure):
    win_df = groupby_structure.count().join(groupby_structure.sum(), rsuffix='win')
    win_df.rename(inplace=True, columns={'Result': 'Trials', 'Resultwin': 'Wins'})
    win_df = win_df[['Trials', 'Wins']]
    win_df['Winrate'] = win_df['Wins'] / win_df['Trials']
    return win_df
