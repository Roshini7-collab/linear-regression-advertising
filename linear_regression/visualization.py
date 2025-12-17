import matplotlib.pyplot as plt
import seaborn as sns

def plot_relationship(x, y, xlabel, ylabel):
    """
    Plot relationship between feature and target.
    """
    plt.figure(figsize=(6,4))
    sns.scatterplot(x=x, y=y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f"{ylabel} vs {xlabel}")
    plt.show()
