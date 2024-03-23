import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from tqdm import tqdm
warnings.filterwarnings('ignore')

start_date = '2014-01-01'
end_date = '2024-03-23'

def freq_plot(data, frame, thres, days) :
    plt.bar(
        frame.index,
        frame,
        edgecolor = 'none',
        color = 'gray'
    )
    plt.grid(False)
    plt.ylabel('Frequency')
    data['Adj Close'].plot(secondary_y = True, color = 'darkorange', alpha = 0.75)
    plt.grid(False)
    plt.xlabel(f'frequency after {days} days from -{thres}% Cumulative Return')
    plt.title(f'Frequency of signal | {days} Days | -{thres}% Cum.Return')
    plt.show()
    return None

def cumulative_return_plot(data, thres, days) -> None:
    sns.histplot(
        data,
        bins=50,
        alpha=0.75,
        edgecolor = 'none',
        kde = True,
        stat = "density"
    )
    plt.ylim([0, 15])
    plt.xlim([-1, 1])
    plt.axvline(0, color = 'k', ls = '--', alpha = 0.5)
    plt.xlabel(f'Returns after {days} days from -{thres}% Cumulative Return')
    plt.ylabel('Frequency')
    plt.title(f'Distribution of Returns | {days} Days | -{thres}% Cum.Return')
    plt.grid(False)
    filename = f'./figure/returns_distribution_{thres}per_{days}days.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')  # dpi는 해상도를 지정하고, bbox_inches='tight'는 여백을 최소화합니다.
    plt.show()
    return None

def getStats(ret_list):
    mean = ret_list.mean()[0]
    std = ret_list.std()[0]
    skew = ret_list.skew()[0]
    kurt = ret_list.kurt()[0]
    return [mean, std, skew, kurt]

def getStatFrame(day_list, column_list):
    day_df = pd.DataFrame()
    for i in day_list:
        day_df = pd.concat(
            [day_df, pd.Series(getStats(i))],
            axis=1
        )
    day_df.index = ['mean', 'std', 'skew', 'kurt']
    day_df.columns = column_list
    day_df = day_df.T

    return day_df

def show_stats_plot(dataframe, days, column_list) -> None:
    plt.figure(figsize=(8, 8))
    plt.subplot(2, 2, 1)
    plt.bar(getStatFrame(dataframe, column_list).index, getStatFrame(dataframe, column_list)['mean'], width=0.5, alpha=0.5)
    plt.grid(False)
    plt.axhline(0)
    plt.title('mean')
    plt.subplot(2, 2, 2)
    plt.bar(getStatFrame(dataframe, column_list).index, getStatFrame(dataframe, column_list)['std'], width=0.5, alpha=0.5)
    plt.grid(False)
    plt.axhline(0)
    plt.title('standard dev')
    plt.subplot(2, 2, 3)
    plt.bar(getStatFrame(dataframe, column_list).index, getStatFrame(dataframe, column_list)['skew'], width=0.5, alpha=0.5)
    plt.grid(False)
    plt.axhline(0)
    plt.title('skewness')
    plt.subplot(2, 2, 4)
    plt.bar(getStatFrame(dataframe, column_list).index, getStatFrame(dataframe, column_list)['kurt'], width=0.5, alpha=0.5)
    plt.grid(False)
    plt.axhline(0)
    plt.title('kurtosis')
    plt.tight_layout()
    filename = f'./figure/distribution_{days}days.png'
    plt.suptitle(f'sim_days : {days} | market : S&P500 | start : {start_date} | end : {end_date}')
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')  # dpi는 해상도를 지정하고, bbox_inches='tight'는 여백을 최소화합니다.
    plt.show()
    return None


def show_stats_plot_percent(dataframe, thresh, column_list) -> None:
    plt.figure(figsize=(8, 8))
    plt.subplot(2, 2, 1)
    plt.bar(getStatFrame(dataframe, column_list).index, getStatFrame(dataframe, column_list)['mean'], width=0.5, alpha=0.5)
    plt.grid(False)
    plt.xticks(rotation=90)
    plt.axhline(0)
    plt.title('mean')
    plt.subplot(2, 2, 2)
    plt.bar(getStatFrame(dataframe, column_list).index, getStatFrame(dataframe, column_list)['std'], width=0.5, alpha=0.5)
    plt.grid(False)
    plt.xticks(rotation=90)
    plt.axhline(0)
    plt.title('standard dev')
    plt.subplot(2, 2, 3)
    plt.bar(getStatFrame(dataframe, column_list).index, getStatFrame(dataframe, column_list)['skew'], width=0.5, alpha=0.5)
    plt.grid(False)
    plt.xticks(rotation=90)
    plt.axhline(0)
    plt.title('skewness')
    plt.subplot(2, 2, 4)
    plt.bar(getStatFrame(dataframe, column_list).index, getStatFrame(dataframe, column_list)['kurt'], width=0.5, alpha=0.5)
    plt.grid(False)
    plt.xticks(rotation=90)
    plt.axhline(0)
    plt.title('kurtosis')
    plt.tight_layout()
    filename = f'./figure/distribution_{thresh}percent.png'
    plt.suptitle(f'sim_thresh : {thresh} | market : S&P500 | start : {start_date} | end : {end_date}')
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')  # dpi는 해상도를 지정하고, bbox_inches='tight'는 여백을 최소화합니다.
    plt.show()
    return None