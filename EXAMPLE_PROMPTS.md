# Maya AI Assistant 0.3.0 示例指令

## 1. Polygon 产品建模

创建一个科幻金属箱子。主体使用多边形立方体，四周做轻微倒角，顶部做一个凹槽。自动 UV。创建深灰色 standardSurface，Metalness 0.9，Roughness 0.25。所有对象放进 SciFiCrate_GRP。

## 2. 桌子

创建一个桌子。桌面宽 6、高 0.3、深 3，桌面中心位于 Y=3。创建四条桌腿，每条宽 0.4、深 0.4、高 3，分别命名 Table_Leg_01 到 Table_Leg_04，放在四角。最后组合到 Table_GRP。

## 3. 标准足球

在桌面中央上方制作一个标准足球，半径 1。使用十二个五边形和二十个六边形结构，五边形黑色、六边形白色，并加入轻微皮革凹凸。

## 4. NURBS 花瓶

创建一条花瓶半边轮廓 NURBS 曲线，高度约 12，底部半径约 3，瓶口半径约 1.6。然后绕 Y 轴旋转 360 度生成花瓶，命名 Vase_NURBS。

## 5. NURBS Loft 灯罩

创建 5 条由下到上逐渐缩小的 NURBS 圆形曲线，再 Loft 成一个流线型灯罩。顶部和底部分别收窄。

## 6. 图片参考建模

我添加的三张图片分别是物体正面、侧面和背面。综合三张图片建立中等精度模型，优先匹配整体比例、轮廓和主要结构。各部件合理命名并组合到 ReferenceModel_GRP。

## 7. PBR 贴图

给当前选择的模型自动 UV。使用附件 `metal_basecolor.jpg` 作为 Base Color、`metal_roughness.jpg` 作为 Roughness、`metal_metallic.jpg` 作为 Metalness、`metal_normal.jpg` 作为 Normal。创建 standardSurface 材质 Metal_MAT。

## 8. 三点布光 + Arnold

创建 RenderCam，焦距 70mm。创建 Key、Fill、Rim 三盏 Area Light。Key 为主光，Fill 强度约 Key 的 35%，Rim 从后上方照亮轮廓。Arnold 设置为 1920x1080，AA Samples 6，Diffuse 3，Specular 3。

## 9. HDRI

使用附件 `studio.hdr` 创建 Arnold SkyDome，曝光 0.5，并把它作为产品渲染环境光。

## 10. 动画

给 SoccerBall 制作 1 到 72 帧动画：第 1 帧在 (0,3,0)，第 36 帧移动到 (8,6,0) 并旋转 Y=360，第 72 帧落到 (14,1,0)。使用 Auto Tangent。播放范围 1-72，24fps。

## 11. 粒子

在原点创建 Sparks nParticle，向上定向发射，Rate 500，Speed 6，Speed Random 2，Lifespan 1.5，Radius 0.03。添加向下 Gravity 和较弱 Turbulence。

## 12. 刚体

把 Floor 设置为被动刚体，把 Ball01、Ball02 设置为主动刚体，质量 1，弹性 0.7，摩擦 0.35。添加向下重力，播放范围 1-120。

## 13. 导入本地资产

使用我添加的 `robot.fbx` 本地资产导入到当前场景，namespace 使用 robot，把新增的根节点组合到 Robot_Imported_GRP。不要修改文件本身。
