# compile the list of dataframes you want to merge
data_frames = [merge2019, ks42018, census2018, cfr2018]

# do the merge

df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['URN'],
                                            how='left'), data_frames)

# if you want to fill the values that don't exist in the lines of merged dataframe simply fill with required strings as
# df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['URN'], how='left'), data_frames).fillna('void')
