#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gear_calc.py —— 标准直齿轮分度圆直径计算

公式：
    d = m × z

符号说明：
    d —— 分度圆直径，单位 mm
    m —— 模数（module），单位 mm，国标标准值如 0.5 / 1 / 1.25 / 1.5 / 2 / 2.5 / 3 ...
    z —— 齿数，正整数

关于「标准直齿轮」：
    指采用标准模数、标准压力角 20°、齿顶高系数 1、顶隙系数 0.25 的
    正常齿制渐开线直齿圆柱齿轮。分度圆是设计、加工、测量的基准圆：
    齿距 p = π·m，齿厚 = 齿槽宽 = p/2，分度圆上压力角为 20°。

用法：
    python gear_calc.py 2 20     # 模数 2，齿数 20 → d = 40 mm
    python gear_calc.py          # 不带参数则进入交互输入模式
"""

import sys


def pitch_diameter(module, teeth):
    """计算标准直齿轮的分度圆直径，返回单位 mm。

    参数：
        module —— 模数 m，单位 mm，必须大于 0
        teeth  —— 齿数 z，必须为正整数

    返回：
        分度圆直径 d = m × z，单位 mm

    异常：
        ValueError —— 模数 ≤ 0 或齿数不是正整数时抛出
    """

    # ---------- 第一步：参数合法性检查 ----------
    # 先在算之前把非法输入挡住，避免算出看似正常其实无意义的结果。
    if not isinstance(module, (int, float)) or isinstance(module, bool):
        raise ValueError("模数必须是数字，当前为 %r" % (module,))
    if module <= 0:
        raise ValueError("模数必须大于 0，当前为 %g" % module)

    if isinstance(teeth, bool) or not isinstance(teeth, int):
        # 齿数只允许整数，2.5 个齿没有物理意义
        raise ValueError("齿数必须是正整数，当前为 %r" % (teeth,))
    if teeth <= 0:
        raise ValueError("齿数必须大于 0，当前为 %d" % teeth)

    # ---------- 第二步：套公式 d = m × z ----------
    # 分度圆直径与齿数成正比：模数相同的一对齿轮啮合，
    # 只要齿数相同，分度圆直径就相同，这是能正确啮合的前提。
    return module * teeth


def main(argv):
    """命令行入口：解析参数 → 调用计算 → 打印结果。

    argv 为 sys.argv，形如 ["gear_calc.py", "2", "20"]。
    返回进程退出码：0 成功，1 输入不合法，2 参数格式错误。
    """

    # ---------- 情况一：命令行正好给了两个参数（模数、齿数）----------
    if len(argv) == 3:
        try:
            module = float(argv[1])   # 模数允许小数，如 1.5
            teeth = int(argv[2])      # 齿数必须是整数
        except ValueError:
            print("参数格式错误：用法 python gear_calc.py <模数> <齿数>", file=sys.stderr)
            return 2

    # ---------- 情况二：一个参数都没给，进入交互模式 ----------
    elif len(argv) == 1:
        print("标准直齿轮分度圆直径计算  d = m × z")
        try:
            module = float(input("请输入模数 m（mm）：").strip())
            teeth = int(input("请输入齿数 z：").strip())
        except (ValueError, EOFError):
            print("输入的不是数字，请重新运行。", file=sys.stderr)
            return 2

    # ---------- 情况三：参数数量不对（如只给了一个）----------
    else:
        print("参数数量错误：用法 python gear_calc.py <模数> <齿数>", file=sys.stderr)
        return 2

    # ---------- 计算并输出 ----------
    try:
        d = pitch_diameter(module, teeth)
    except ValueError as error:          # 把函数里的校验错误转成友好提示
        print("输入错误：%s" % error, file=sys.stderr)
        return 1

    # %g 让 2.0 显示成 2，2.5 原样显示；结果保留两位小数便于抄进图纸
    print("模数 m = %g mm，齿数 z = %d" % (module, teeth))
    print("分度圆直径 d = m × z = %g × %d = %.2f mm" % (module, teeth, d))
    return 0


# 只有直接运行本文件时才执行 main；被其它脚本 import 时不会自动跑
if __name__ == "__main__":
    sys.exit(main(sys.argv))
