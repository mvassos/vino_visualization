import db_helper
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    price_and_points_df = db_helper.get_price_points()

    price_and_points_df = price_and_points_df[price_and_points_df['price'] <= 200]

    all_data = db_helper.get_all_data()

    sns.set(style="whitegrid", palette="muted", color_codes=True)

    f, ax = plt.subplots(figsize=(6.5, 6.5))
    sns.despine(f, left=True, bottom=True)
    sns.scatterplot(x="price", y="points",
                    palette="ch:r=-.2,d=.3_r",
                    linewidth=0, data=price_and_points_df,
                    ax=ax)

    plt.show()





