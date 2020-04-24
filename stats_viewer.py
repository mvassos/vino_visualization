import db_helper
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from operator import itemgetter
import math


def price_vs_points(pp_data):

    sns.set(style="whitegrid", palette="muted", color_codes=True)

    f, ax = plt.subplots(figsize=(6.5, 6.5))
    sns.despine(f, left=True, bottom=True)
    sns.scatterplot(x="price", y="points",
                    palette="ch:r=-.2,d=.3_r",
                    linewidth=0, data=pp_data,
                    ax=ax)

    plt.show()


def country_analysis(cntry_data):

    countries_dict = {}
    count = 0

    for index, row in cntry_data.iterrows():
        country = row['country']
        score = row['points']
        price = row['price']

        if count == 1000:
            break

        if math.isnan(price):
            continue

        count += 1

        if country not in countries_dict.keys():
            countries_dict[country] = (1, score, price, score, price)
            # tuple keys: 'entries', 'score_sum', 'price_sum', 'score_avg', 'price_avg'

        else:
            old_tuple = countries_dict[country]
            new_tuple = (old_tuple[0]+1, old_tuple[1]+score, old_tuple[2]+price, (old_tuple[1]+score)/(old_tuple[0]+1),
                         (old_tuple[2]+price)/(old_tuple[0]+1))

            update_dict = {country: new_tuple}
            countries_dict.update(update_dict)

    print(len(countries_dict.keys()))
    print(countries_dict)
    print('{} total entries'.format(count))

    score_ordered_dict = sorted(countries_dict.items(), key=lambda x: countries_dict[x][1], reverse=True)
    #price_ordered_dict = sorted(countries_dict.items(), key=lambda x: x[2], reverse=True)

    print(score_ordered_dict[:10])
    #print(price_ordered_dict[:10])


if __name__ == '__main__':

    price_and_points_df = db_helper.get_price_points()
    price_and_points_df = price_and_points_df[price_and_points_df['price'] <= 200]

    all_data = db_helper.get_all_data()

    # price_vs_points(price_and_points_df)
    country_analysis(all_data)








