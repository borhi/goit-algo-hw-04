import math

import matplotlib.pyplot as plt


def _rot60_cw(x: float, y: float) -> tuple[float, float]:
    rad = math.radians(-60)
    c, s = math.cos(rad), math.sin(rad)
    return c * x - s * y, s * x + c * y


def koch_points(
    ax: float, ay: float, bx: float, by: float, order: int
) -> list[tuple[float, float]]:
    if order == 0:
        return [(ax, ay), (bx, by)]

    abx, aby = bx - ax, by - ay
    cx, cy = ax + abx / 3, ay + aby / 3
    dx, dy = ax + 2 * abx / 3, ay + 2 * aby / 3
    vx, vy = abx / 3, aby / 3
    rx, ry = _rot60_cw(vx, vy)
    ex, ey = cx + rx, cy + ry

    p1 = koch_points(ax, ay, cx, cy, order - 1)
    p2 = koch_points(cx, cy, ex, ey, order - 1)
    p3 = koch_points(ex, ey, dx, dy, order - 1)
    p4 = koch_points(dx, dy, bx, by, order - 1)

    return p1[:-1] + p2[:-1] + p3[:-1] + p4


def snowflake_points(order: int, size: float = 300.0) -> list[tuple[float, float]]:
    h = size * math.sqrt(3) / 2
    x0, y0 = -size / 2, -h / 3
    x1, y1 = size / 2, -h / 3
    x2, y2 = 0.0, 2 * h / 3

    s1 = koch_points(x0, y0, x1, y1, order)
    s2 = koch_points(x1, y1, x2, y2, order)
    s3 = koch_points(x2, y2, x0, y0, order)
    return s1[:-1] + s2[:-1] + s3


def draw_koch_snowflake(order: int, size: float = 300.0) -> None:
    pts = snowflake_points(order, size)
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]

    fig, ax = plt.subplots()
    ax.plot(xs, ys, color="black", linewidth=1.0)
    ax.set_aspect("equal", adjustable="box")
    ax.set_axis_off()
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")

    pad = size * 0.08
    ax.set_xlim(min(xs) - pad, max(xs) + pad)
    ax.set_ylim(min(ys) - pad, max(ys) + pad)

    plt.show()


if __name__ == "__main__":
    raw = input("Рівень рекурсії (від 0 до 7): ").strip()
    try:
        level = int(raw)
    except ValueError:
        print("Потрібне ціле число.")
        raise SystemExit(1)

    if level < 0:
        print("Рівень не може бути відʼємним.")
        raise SystemExit(1)

    if level > 7:
        print("Занадто великий рівень; обмеження 7.")
        raise SystemExit(1)

    draw_koch_snowflake(level)
