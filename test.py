import numpy as np
import matplotlib.pyplot as plt


# 2次元直交座標の[0, 1] × [0, 1] 内の点列を返す
def random_xy(pixel):
    # 分布を偏らせるために長さの違う一様分布をつくる
    s = int(num_dot/4)
    if (pixel == "int"):
        x1 = rng.integers(low=0, high=i, size=s)/i - 1
        x2 = rng.integers(low=i, high=2*i, size=3*s)/i - 1
        y1 = rng.integers(low=0, high=i, size=3*s)/i - 1
        y2 = rng.integers(low=i, high=2*i, size=s)/i - 1
    elif (pixel == 'float'):
        x1 = rng.random(s) * (-1)
        x2 = rng.random(3*s) * 1
        y1 = rng.random(3*s) * (-1)
        y2 = rng.random(s) * 1

    else:
        print('Error: random_xy')
        return ''

    # くっつける　片方シャッフルして[0, 1] × [0, 1] 内にばら撒く
    x = np.hstack([x1, x2])
    rng.shuffle(x)
    y = np.hstack([y1, y2])

    return x, y


# 点列のうち、原点からの距離が０より大きく１より小さいものを選ぶ。2次元極座標に変換し、rとcos θを返す
def r_cos(x, y):
    if ((len(x) > 0) & (len(y) > 0)):
        r = np.sqrt(x**2 + y**2)
        idx = ((r > 0) & (r <= 1))
        x = x[idx]
        y = y[idx]
        r = r[idx]
        cos = x/r

        return x, y, r, cos, len(x)

    else:
        print('Error: r_cos')
        return ''


# 軸周りの共通設定
def plot_settings(ax, aspect):
    for a in [ax[0][0], ax[0][2], ax[1][0], ax[1][2]]:
        # 縦横比
        a.set_aspect(aspect)
        # 上と右の枠を消す
        a.spines['top'].set_visible(False)
        a.spines['right'].set_visible(False)

    # 左の枠をずらす
    ax[0][0].spines['left'].set_position(('outward', 5))
    # 下の軸、目盛り線、目盛りラベルを消す
    ax[0][0].tick_params(labelbottom=False, bottom=False)
    ax[0][0].spines['bottom'].set_visible(False)

    ax[0][2].spines['left'].set_visible(False)
    ax[0][2].tick_params(
        labelbottom=False, bottom=False, labelleft=False, left=False)
    ax[0][2].tick_params(labelleft=False, left=False)
    ax[0][2].spines['bottom'].set_visible(False)

    ax[1][0].spines['left'].set_position(('outward', 5))
    ax[1][0].spines['bottom'].set_position(('outward', 5))

    ax[1][2].spines['left'].set_visible(False)
    ax[1][2].tick_params(labelleft=False, left=False)
    ax[1][2].spines['bottom'].set_position(('outward', 5))


# X × Y 上に点列を表示
def plot_xy(x_i, y_i, len_i, x_f, y_f, len_f):
    f, ax = plt.subplots(
        2, 4, gridspec_kw={'width_ratios': (1, 0.05, 1, 0.05)})

    # グラフたち
    ax[0][0].scatter(x_i, y_i, s=0.1)
    ax[0][2].scatter(x_f, y_f, s=0.1)
    im_i = ax[1][0].hist2d(x_i, y_i, cmap='Blues', bins=30)
    im_f = ax[1][2].hist2d(x_f, y_f, cmap='Blues', bins=30)

    # カラーバー
    f.colorbar(im_i[3], cax=ax[1][1])
    f.colorbar(im_f[3], cax=ax[1][3])

    # いらないとこは何も表示しない
    ax[0][1].set_axis_off()
    ax[0][3].set_axis_off()

    # title, label
    ax[0][0].set_title(f'int (N={len_i})', x=0.5, y=1.01)
    ax[0][2].set_title(f'float (N={len_f})', x=0.5, y=1.01)
    ax[0][0].set_ylabel('y')
    ax[1][0].set_ylabel('y')
    ax[1][0].set_xlabel('x')
    ax[1][2].set_xlabel('x')

    # 軸周り
    for a in [ax[0][0], ax[0][2], ax[1][0], ax[1][2]]:
        # 範囲指定
        a.set_xlim([-1, 1])
        a.set_ylim([-1, 1])
    plot_settings(ax, aspect=1)

    # subplot間隔調整
    plt.subplots_adjust(wspace=0, hspace=0.3)
    plt.savefig('xy.png', dpi=400)
    # plt.show()


# R × cos θ 上に点列を表示
def plot_r_cos(r_i, cos_i, len_i, r_f, cos_f, len_f):
    f, ax = plt.subplots(
        2, 4, gridspec_kw={'width_ratios': (1, 0.05, 1, 0.05)})

    # グラフたち
    ax[0][0].scatter(cos_i, r_i, s=0.1)
    ax[0][2].scatter(cos_f, r_f, s=0.1)
    im_i = ax[1][0].hist2d(cos_i, r_i, cmap='Blues', bins=15)
    im_f = ax[1][2].hist2d(cos_f, r_f, cmap='Blues', bins=15)

    # カラーバー
    f.colorbar(im_i[3], cax=ax[1][1])
    f.colorbar(im_f[3], cax=ax[1][3])

    # いらないとこは何も表示しない
    ax[0][1].set_axis_off()
    ax[0][3].set_axis_off()

    # title, label
    ax[0][0].set_title(f'int (N={len_i})', x=0.5, y=1.01)
    ax[0][2].set_title(f'float (N={len_f})', x=0.5, y=1.01)
    ax[0][0].set_ylabel('speed')
    ax[1][0].set_ylabel('speed')
    ax[1][0].set_xlabel('cos '+r'$\theta$')
    ax[1][2].set_xlabel('cos '+r'$\theta$')

    # 軸周り
    for a in [ax[0][0], ax[0][2], ax[1][0], ax[1][2]]:
        a.set_xlim([-1, 1])
        a.set_ylim([0, 1])
    plot_settings(ax, aspect=2)

    plt.subplots_adjust(wspace=0, hspace=0.3)
    plt.savefig('r_cos.png', dpi=400)
    # plt.show()


# main
def main():
    x_i, y_i = random_xy('int')
    x_i, y_i, r_i, cos_i, len_i = r_cos(x_i, y_i)

    x_f, y_f = random_xy('float')
    x_f, y_f, r_f, cos_f, len_f = r_cos(x_f, y_f)

    plot_xy(x_i, y_i, len_i, x_f, y_f, len_f)
    plot_r_cos(r_i, cos_i, len_i, r_f, cos_f, len_f)


# 直接実行の時だけ実行する
if __name__ == '__main__':

    # 繰り返し回数
    num_dot = 2**13

    # 刻み幅（格子点の粗さ）
    i = 2**5

    # 乱数生成用
    rng = np.random.default_rng(42)

    # 実行部分
    main()
