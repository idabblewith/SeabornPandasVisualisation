from helpers import *

# Data structure:
# year, category, prize, motivation, prize_share, laureate_type, full_name, birth_date,
# birth_city, birth_country, birth_country_current, sex, organization_name,
# organization_city, organization_country, ISO


def day_078():
    df_data = pd.read_csv("./nobel_prize_data.csv")
    # print(df_data)
    # print(df_data.info())
    # print(df_data.head())
    # print(df_data.isna().values.any()) # check if na values present (PRESENT)
    # print(df_data.duplicated().values.any()) # check for duplicates (NONE)
    # print(df_data.isna().sum()) # count nas (A LOT)

    ################# fixing types #################
    # date
    df_data.birth_date = pd.to_datetime(df_data.birth_date)

    # change prize share to percentage type new column
    separated_values = df_data.prize_share.str.split("/", expand=True)
    numerator = pd.to_numeric(separated_values[0])
    denomenator = pd.to_numeric(separated_values[1])
    df_data["share_pct"] = numerator / denomenator

    ################# Charts #################

    ################# 1a (Male to Female Ratio) #################
    # biology = df_data.sex.value_counts()
    # fig = px.pie(
    #     labels=biology.index,
    #     values=biology.values,
    #     title="Percentage of Male vs. Female Winners",
    #     names=biology.index,
    #     hole=0.4,
    # )

    # fig.update_traces(textposition="inside", textfont_size=15, textinfo="percent")
    # fig.show()  # women make up only 6.21%

    ################# 1b (Print first three female winners, and multiple winners) #################
    # ftf = df_data[df_data.sex == "Female"].sort_values("year", ascending=True)[
    #     :3
    # ]  # first three females winners
    # print(ftf.full_name)

    # is_winner = df_data.duplicated(subset=["full_name"], keep=False)
    # multiple_winners = df_data[is_winner]
    # print(
    #     f"There are {multiple_winners.full_name.nunique()}"
    #     " winners who were awarded the prize more than once."
    # )
    # col_subset = ["year", "category", "laureate_type", "full_name"]
    # print(multiple_winners[col_subset])

    ################# 2 (Prizes per category) #################
    # prizes_per_category = df_data.category.value_counts()
    # v_bar = px.bar(
    #     x=prizes_per_category.index,
    #     y=prizes_per_category.values,
    #     color=prizes_per_category.values,
    #     color_continuous_scale="Aggrnyl",
    #     title="Number of Prizes Awarded per Category",
    # )

    # v_bar.update_layout(
    #     xaxis_title="Nobel Prize Category",
    #     coloraxis_showscale=False,
    #     yaxis_title="Number of Prizes",
    # )
    # v_bar.show()
    # economics = df_data[df_data.category == "Economics"].sort_values("year")[:3]

    ################# 3 (Sex by Category) #################

    # cat_men_women = df_data.groupby(["category", "sex"], as_index=False).agg(
    #     {"prize": pd.Series.count}
    # )
    # cat_men_women.sort_values("prize", ascending=False, inplace=True)
    # v_bar_split = px.bar(
    #     x=cat_men_women.category,
    #     y=cat_men_women.prize,
    #     color=cat_men_women.sex,
    #     title="Number of Prizes Awarded per Category split by Men and Women",
    # )

    # v_bar_split.update_layout(
    #     xaxis_title="Nobel Prize Category", yaxis_title="Number of Prizes"
    # )
    # v_bar_split.show()

    ################# 4a (Frequency of Prizes) #################
    # prize_per_year = df_data.groupby(by="year").count().prize
    # moving_average = prize_per_year.rolling(window=5).mean()
    # plt.figure(figsize=(16, 8), dpi=200)
    # plt.title("Number of Nobel Prizes Awarded per Year", fontsize=18)
    # plt.yticks(fontsize=14)
    # plt.xticks(ticks=np.arange(1900, 2021, step=5), fontsize=14, rotation=45)

    # ax = plt.gca()  # get current axis
    # ax.set_xlim(1900, 2020)

    # ax.scatter(
    #     x=prize_per_year.index,
    #     y=prize_per_year.values,
    #     c="dodgerblue",
    #     alpha=0.7,
    #     s=100,
    # )

    # ax.plot(
    #     prize_per_year.index,
    #     moving_average.values,
    #     c="crimson",
    #     linewidth=3,
    # )

    # plt.show()

    ################# 4b (Percentage Share of Prize) #################

    # yearly_avg_share = df_data.groupby(by="year").agg({"share_pct": pd.Series.mean})
    # share_moving_average = yearly_avg_share.rolling(window=5).mean()
    # plt.figure(figsize=(16, 8), dpi=200)
    # plt.title("Number of Nobel Prizes Awarded per Year", fontsize=18)
    # plt.yticks(fontsize=14)
    # plt.xticks(ticks=np.arange(1900, 2021, step=5), fontsize=14, rotation=45)

    # ax1 = plt.gca()
    # ax2 = ax1.twinx()

    # ax1.set_xlim(1900, 2020)

    # # Can invert axis
    # ax2.invert_yaxis()

    # ax1.scatter(
    #     x=prize_per_year.index,             #uncomment lines 93 & 94
    #     y=prize_per_year.values,
    #     c="dodgerblue",
    #     alpha=0.7,
    #     s=100,
    # )

    # ax1.plot(
    #     prize_per_year.index,
    #     moving_average.values,
    #     c="crimson",
    #     linewidth=3,
    # )

    # ax2.plot(
    #     prize_per_year.index,
    #     share_moving_average.values,
    #     c="grey",
    #     linewidth=3,
    # )

    # plt.show()

    ################# 5a (Top Awarded Countries) #################

    # top_countries = df_data.groupby(["birth_country_current"], as_index=False).agg(
    #     {"prize": pd.Series.count}
    # )

    # top_countries.sort_values(by="prize", inplace=True)
    # top20_countries = top_countries[-20:]

    # h_bar = px.bar(
    #     x=top20_countries.prize,
    #     y=top20_countries.birth_country_current,
    #     orientation="h",
    #     color=top20_countries.prize,
    #     color_continuous_scale="Viridis",
    #     title="Top 20 Countries by Number of Prizes",
    # )

    # h_bar.update_layout(
    #     xaxis_title="Number of Prizes", yaxis_title="Country", coloraxis_showscale=False
    # )
    # h_bar.show()

    ################# 5b (Top Awarded Countries MAP) #################
    # df_countries = df_data.groupby(
    #     ["birth_country_current", "ISO"], as_index=False
    # ).agg({"prize": pd.Series.count})
    # df_countries.sort_values("prize", ascending=False)

    # world_map = px.choropleth(
    #     df_countries,
    #     locations="ISO",
    #     color="prize",
    #     hover_name="birth_country_current",
    #     color_continuous_scale=px.colors.sequential.matter,
    # )

    # world_map.update_layout(
    #     coloraxis_showscale=True,
    # )

    # world_map.show()

    ################# 6 (Countries by # Prizes & Category) #################

    # cat_country = df_data.groupby(
    #     ["birth_country_current", "category"], as_index=False
    # ).agg({"prize": pd.Series.count})
    # cat_country.sort_values(by="prize", ascending=False, inplace=True)
    # print(cat_country)

    # # uncomment lines 163-168
    # # change column names
    # merged_df = pd.merge(cat_country, top20_countries, on="birth_country_current")

    # merged_df.columns = [
    #     "birth_country_current",
    #     "category",
    #     "cat_prize",
    #     "total_prize",
    # ]
    # merged_df.sort_values(by="total_prize", inplace=True)

    # cat_cntry_bar = px.bar(
    #     x=merged_df.cat_prize,
    #     y=merged_df.birth_country_current,
    #     color=merged_df.category,
    #     orientation="h",
    #     title="Top 20 Countries by Number of Prizes and Category",
    # )

    # cat_cntry_bar.update_layout(xaxis_title="Number of Prizes", yaxis_title="Country")
    # cat_cntry_bar.show()

    ################# 7 (Countries Prizers over Time) #################

    # prize_by_year = df_data.groupby(
    #     by=["birth_country_current", "year"], as_index=False
    # ).count()
    # prize_by_year = prize_by_year.sort_values("year")[
    #     ["year", "birth_country_current", "prize"]
    # ]

    # cumulative_prizes = (
    #     prize_by_year.groupby(by=["birth_country_current", "year"])
    #     .sum()
    #     .groupby(level=[0])
    #     .cumsum()
    # )
    # cumulative_prizes.reset_index(inplace=True)

    # l_chart = px.line(
    #     cumulative_prizes,
    #     x="year",
    #     y="prize",
    #     color="birth_country_current",
    #     hover_name="birth_country_current",
    # )

    # l_chart.update_layout(xaxis_title="Year", yaxis_title="Number of Prizes")

    # l_chart.show()

    ################# 8 (Top Organisations) #################
    # top20_orgs = df_data.organization_name.value_counts()[:20]
    # top20_orgs.sort_values(ascending=True, inplace=True)

    # org_bar = px.bar(
    #     x=top20_orgs.values,
    #     y=top20_orgs.index,
    #     orientation="h",
    #     color=top20_orgs.values,
    #     color_continuous_scale=px.colors.sequential.haline,
    #     title="Top 20 Research Institutions by Number of Prizes",
    # )

    # org_bar.update_layout(
    #     xaxis_title="Number of Prizes",
    #     yaxis_title="Institution",
    #     coloraxis_showscale=False,
    # )
    # org_bar.show()

    ################# 9 (Top Research Cities) #################
    # top20_org_cities = df_data.organization_city.value_counts()[:20]
    # top20_org_cities.sort_values(ascending=True, inplace=True)
    # city_bar2 = px.bar(
    #     x=top20_org_cities.values,
    #     y=top20_org_cities.index,
    #     orientation="h",
    #     color=top20_org_cities.values,
    #     color_continuous_scale=px.colors.sequential.Plasma,
    #     title="Which Cities Do the Most Research?",
    # )

    # city_bar2.update_layout(
    #     xaxis_title="Number of Prizes", yaxis_title="City", coloraxis_showscale=False
    # )
    # city_bar2.show()

    ################# 10 (Top Birth Cities) #################

    # top20_cities = df_data.birth_city.value_counts()[:20]
    # top20_cities.sort_values(ascending=True, inplace=True)
    # city_bar = px.bar(
    #     x=top20_cities.values,
    #     y=top20_cities.index,
    #     orientation="h",
    #     color=top20_cities.values,
    #     color_continuous_scale=px.colors.sequential.Plasma,
    #     title="Where were the Nobel Laureates Born?",
    # )

    # city_bar.update_layout(
    #     xaxis_title="Number of Prizes",
    #     yaxis_title="City of Birth",
    #     coloraxis_showscale=False,
    # )
    # city_bar.show()

    ################# SUNBURST CHART #################

    country_city_org = df_data.groupby(
        by=["organization_country", "organization_city", "organization_name"],
        as_index=False,
    ).agg({"prize": pd.Series.count})

    country_city_org = country_city_org.sort_values("prize", ascending=False)

    burst = px.sunburst(
        country_city_org,
        path=["organization_country", "organization_city", "organization_name"],
        values="prize",
        title="Where do Discoveries Take Place?",
    )

    burst.update_layout(
        xaxis_title="Number of Prizes", yaxis_title="City", coloraxis_showscale=False
    )

    burst.show()

    ################# 11 (Winning Age - Various Charts) #################

    # birth_years = df_data.birth_date.dt.year
    # df_data["winning_age"] = df_data.year - birth_years

    # plt.figure(figsize=(8, 4), dpi=200)
    # sbr.histplot(data=df_data, x=df_data.winning_age, bins=30)
    # plt.xlabel("Age")
    # plt.title("Distribution of Age on Receipt of Prize")
    # plt.show()

    # plt.figure(figsize=(8, 4), dpi=200)
    # with sbr.axes_style("whitegrid"):
    #     sbr.regplot(
    #         data=df_data,
    #         x="year",
    #         y="winning_age",
    #         lowess=True,
    #         scatter_kws={"alpha": 0.4},
    #         line_kws={"color": "black"},
    #     )

    # plt.show()

    # plt.figure(figsize=(8, 4), dpi=200)
    # with sbr.axes_style("whitegrid"):
    #     sbr.boxplot(data=df_data, x="category", y="winning_age")

    # plt.show()

    # with sbr.axes_style("whitegrid"):
    #     sbr.lmplot(
    #         data=df_data,
    #         x="year",
    #         y="winning_age",
    #         row="category",
    #         lowess=True,
    #         aspect=2,
    #         scatter_kws={"alpha": 0.6},
    #         line_kws={"color": "black"},
    #     )
    # plt.show()

    # with sbr.axes_style("whitegrid"):
    #     sbr.lmplot(
    #         data=df_data,
    #         x="year",
    #         y="winning_age",
    #         hue="category",
    #         lowess=True,
    #         aspect=2,
    #         scatter_kws={"alpha": 0.5},
    #         line_kws={"linewidth": 5},
    #     )

    # plt.show()


day_078()
