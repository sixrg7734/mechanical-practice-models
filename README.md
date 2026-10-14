# mechanical-practice-models

> 机械建模练习仓库 · 工具：FreeCAD

## 项目简介

这是我在大一阶段自学机械建模的练习仓库，用来记录从零开始使用 FreeCAD 完成零件建模的完整过程。

- 每个零件都保留可编辑的源文件（`.FCStd`），便于修改尺寸、复用特征
- 同时导出 STEP / STL 与工程图，练习「建模 → 出图 → 导出」的完整流程
- 现阶段重点是草图约束与基础特征，不追求复杂曲面
- 仓库里另外收录了 3D 打印 BOM 清单、机械制图学习笔记和一个齿轮计算小脚本

![项目总览](images/overview.svg)

## 零件清单

| 序号 | 零件名称 | 模型文件 | 关键特征 | 状态 |
| :--: | --- | --- | --- | :--: |
| 1 | L型固定支架 | `models/l-bracket.FCStd` | 拉伸、打孔、圆角 | 已完成 |
| 2 | 带孔垫片 | `models/washer.FCStd` | 圆形轮廓、孔阵列 | 已完成 |

### 1. L型固定支架

![L型固定支架](images/l-bracket.svg)

用于板材连接的基础角件，也是我练习「两个方向尺寸同时约束」的第一个零件。

- 建模思路：先画 L 形封闭草图，再整体拉伸
- 关键尺寸：臂长、板厚、安装孔中心距
- 练习要点：草图完全约束、孔特征定位、边缘圆角过渡
- 3D 打印建议：PETG，板厚 4 mm，沿折角竖直方向摆放

### 2. 带孔垫片

![带孔垫片](images/washer.svg)

薄板类零件，主要用来练习圆形轮廓与孔的定位方式。

- 建模思路：外圆拉伸后用草图定位孔位
- 关键尺寸：外径、内孔直径、孔分布圆直径
- 练习要点：对称约束、环形阵列、厚度参数化
- 3D 打印建议：PETG，厚度 2 mm，100% 填充

## 使用软件

| 项目 | 说明 |
| --- | --- |
| 建模软件 | [FreeCAD](https://www.freecad.org/) 1.0 |
| 常用工作台 | Sketcher、Part Design、TechDraw |
| 导出格式 | STEP（`.step`）、STL（`.stl`） |
| 运行环境 | Windows |
| 脚本环境 | Python 3.6+（只用标准库，无需安装依赖） |

## 仓库目录结构

```
mechanical-practice-models/
├── models/                     # FreeCAD 源文件（.FCStd），可直接打开编辑
│   ├── l-bracket.FCStd
│   └── washer.FCStd
├── exports/                    # 导出文件：STEP / STL
├── drawings/                   # TechDraw 导出的工程图（PDF / SVG）
├── images/                     # README 配图（当前为占位图，替换成自己的截图即可）
│   ├── overview.svg
│   ├── l-bracket.svg
│   └── washer.svg
├── docs/
│   └── 机械制图学习笔记.md      # 草图 / 拉伸 / 打孔 / 尺寸标注笔记
├── bom.md                      # 3D 打印 BOM 清单
├── gear_calc.py                # 分度圆直径计算脚本
├── .gitignore                  # 忽略 FreeCAD 自动保存、备份、日志等临时文件
├── .dshignore                  # 避免 AI 工具读取大体积模型文件
└── README.md
```

> `models/`、`exports/`、`drawings/` 目前只有说明文件，模型做好后按目录放进去即可。

## 文档与脚本

| 文件 | 内容 |
| --- | --- |
| [bom.md](bom.md) | L型固定支架、带孔垫片的 3D 打印 BOM：推荐材料、建议厚度、用途备注 |
| [docs/机械制图学习笔记.md](docs/机械制图学习笔记.md) | 入门笔记：草图绘制、拉伸特征、打孔、尺寸标注 |
| [gear_calc.py](gear_calc.py) | 标准直齿轮分度圆直径计算，公式 `d = m × z` |

### 齿轮脚本用法

```bash
python gear_calc.py 2 20     # 模数 2、齿数 20 → d = 40.00 mm
python gear_calc.py          # 不带参数则进入交互输入模式
```

也可以在自己的代码里调用：`from gear_calc import pitch_diameter`

## 后续学习计划

- [x] 草图绘制与尺寸约束
- [x] 拉伸、打孔等基础特征
- [ ] 装配体建模与装配约束
- [ ] 用表达式实现参数化尺寸联动
- [ ] TechDraw 输出规范工程图（三视图 + 尺寸 + 标题栏）
- [ ] 放样、扫掠等进阶特征
- [ ] 3D 打印自己设计的零件并验证尺寸
- [ ] 完成一对直齿轮的参数化建模

## 关于

- 作者：大一学生
- 用途：机械建模练习记录，欢迎交流指正
- 联系：（邮箱 / QQ）
- 许可：学习用途，可自由参考
