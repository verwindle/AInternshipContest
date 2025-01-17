import matplotlib.pyplot as plt
import seaborn as sns


def show_img_with_mask(img, mask, figsize=(14, 8)):
    """Shows image and mask.

    Parameters
    ----------
    img : np.ndarray
        Image.
    mask : np.ndarray
        Mask.
    figsize : tuple of 2 int, optional (default=(14, 8))
        Figure size.

    """
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    ax1.imshow(img)
    ax2.imshow(mask)
    ax1.axis("off")
    ax2.axis("off")
    plt.show()


def show_hist(df):
    plt.rcParams['figure.figsize'] = (12, 8)
    sns.set_style('darkgrid')
    sns.set_palette('RdBu')
    g = sns.FacetGrid(df.reset_index(), hue='model', height=3, aspect=2)
    g.map(plt.hist, "dice", bins=16, alpha=.7)
    g.add_legend()