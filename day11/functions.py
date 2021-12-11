import pandas as pd


def propagate_energy(df, mask):

    all_indexes, df_mask = get_high_indexes(df[mask])

    # Increment all neighbours by 1
    df = increment_neighbours(df, all_indexes)

    # Set all current flashes to None
    df[df_mask] = -1e8
    return df


def increment_neighbours(df, all_indexes):

    for coords in all_indexes:
        row = coords[0]
        col = coords[1]
        # Directly below
        try:
            new_row = row + 1
            new_col = col
            if new_row >= 0 and new_col >= 0:
                df.iloc[new_row, new_col] += 1
        except IndexError:
            pass

        # Directly above
        try:
            new_row = row - 1
            new_col = col
            if new_row >= 0 and new_col >= 0:
                df.iloc[new_row, new_col] += 1
        except IndexError:
            pass

        # Directly right
        try:
            new_row = row
            new_col = col + 1
            if new_row >= 0 and new_col >= 0:
                df.iloc[new_row, new_col] += 1
        except IndexError:
            pass

        # Directly left
        try:
            new_row = row
            new_col = col - 1
            if new_row >= 0 and new_col >= 0:
                df.iloc[new_row, new_col] += 1
        except IndexError:
            pass

        # diagnol top right
        try:
            new_row = row - 1
            new_col = col + 1
            if new_row >= 0 and new_col >= 0:
                df.iloc[new_row, new_col] += 1
        except IndexError:
            pass

        # diagnol top left
        try:
            new_row = row - 1
            new_col = col - 1
            if new_row >= 0 and new_col >= 0:
                df.iloc[new_row, new_col] += 1
        except IndexError:
            pass

        # diagnol bottom right
        try:
            new_row = row + 1
            new_col = col + 1
            if new_row >= 0 and new_col >= 0:
                df.iloc[new_row, new_col] += 1
        except IndexError:
            pass

        # diagnol bottom left
        try:
            new_row = row + 1
            new_col = col - 1
            if new_row >= 0 and new_col >= 0:
                df.iloc[new_row, new_col] += 1
        except IndexError:
            pass

    return df


def get_high_indexes(df_masked):

    df_mask = pd.Index.notnull(df_masked)
    all_indexes = []
    for j, row in df_masked.iterrows():
        for i, val in enumerate(row):
            if not pd.isnull(val):
                all_indexes.append([j, i])

    return all_indexes, df_mask
