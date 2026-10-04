# 共通VFXレシピのカタログ

特定のゲームの品目ではなく、表現する意味・主形状・素材・動き・状態管理から選ぶ共通知識。各Recipeは一つの推奨構成を具体的に示す。採用先は固有ID・範囲・速度・期間・個別調整を `projects/` の対応表へ記録する。[知識と採用先の境界](KNOWLEDGE_BOUNDARIES.md)と[制作方針](VFX_ART_DIRECTION.md)を参照する。

全てdraft。秒数・比率・個数は初稿の美術値で、実測値ではない。Resourceは必要アセットの仕様であり、完成した画像・メッシュの納品ではない。

## 武器・自然武器の攻撃

| 推奨レシピ | 主案 |
| --- | --- |
| [剣：鋭く薄い扇状の斬撃](../knowledge/recipes/weapons/weapon-sword.md) | 薄い象牙色の入力角度θ弧と一点の切断反応で、標準的な剣の切れを作る。 |
| [斧：先端の重い扇状の振り抜き](../knowledge/recipes/weapons/weapon-axe.md) | 先端が厚い弧と遅れる重い残留で、斧の刃重と振り抜きを見せる。 |
| [大剣：長く厚い扇状の斬撃](../knowledge/recipes/weapons/weapon-greatsword.md) | 長い外縁と幅広い内側の遅れで、大剣の刃渡りと慣性を表す。 |
| [鎌：途切れない円形の薙ぎ](../knowledge/recipes/weapons/weapon-scythe.md) | 細い円周を刃先に沿って一周展開し、円形攻撃の流れを保つ。 |
| [短剣：小さく鋭い刺突](../knowledge/recipes/weapons/weapon-dagger.md) | 短い針と一点の白芯で、短剣の速さと密接した接触を表す。 |
| [槍：長い軸を通す刺突](../knowledge/recipes/weapons/weapon-spear.md) | 槍先から伸びる細い軸と二本の短い側筋で、直線的な到達を見せる。 |
| [棒：しなる後流と面の打撃](../knowledge/recipes/weapons/weapon-rod.md) | 棒先の灰白の後流を短くつなぎ、接触で幅広い衝撃へ切り替える。 |
| [拳：短い拳圧と鋭い接触](../knowledge/recipes/weapons/weapon-fist.md) | 拳の前に短い圧縮形状を置き、局所の放射でパンチを締める。 |
| [大盾：面で押し込む衝撃](../knowledge/recipes/weapons/weapon-greatshield.md) | 盾の面に沿う楕円の圧力と幅広い接触で、面の打撃を伝える。 |
| [鉄扇：薄い三筋の切り返し](../knowledge/recipes/weapons/weapon-ironfan.md) | 扇の外縁から短い三筋を出し、軽い金属の切り返しを見せる。 |
| [爪：並行する三本の引っかき](../knowledge/recipes/weapons/weapon-claw.md) | 近接した三本の短い曲線を一回の動作として解放する。 |
| [牙：内へ閉じる二点の噛みつき](../knowledge/recipes/weapons/weapon-fang.md) | 上下の短い針と内向きの圧縮で、噛みつきの締まりを示す。 |
| [弓：実体の矢と短い飛翔線](../knowledge/recipes/weapons/weapon-bow.md) | 可視の矢を主役にし、射出の細い筋と短い尾で実速度の飛翔を読む。 |
| [クロスボウ：硬い射出と短いボルト](../knowledge/recipes/weapons/weapon-crossbow.md) | 鋭い一閃と短い太めのボルトで2半径R/sの機械的な射出を表す。 |
| [杖：丸い魔法核と柔らかな尾](../knowledge/recipes/weapons/weapon-staff.md) | 青白い立体の核と細い周回筋で、杖の実速度魔法弾を表す。 |
| [ワンド：小さな滴状の魔法弾](../knowledge/recipes/weapons/weapon-wand.md) | 小さな鋭い滴と短い細尾で、ワンドの1半径R/s射出を軽快に見せる。 |

## 準備・発動・飛翔・命中の構成

| 推奨レシピ | 主案 |
| --- | --- |
| [狙い撃ち：張り詰めた収束と強い矢](../knowledge/recipes/abilities/charged-arrow.md) | 細い照準の収束から、鋭い矢の実体と長い一本の尾へ解放する。 |
| [旋回斬撃：一周する主弧と低い風の残留](../knowledge/recipes/abilities/circular-slash.md) | 半径Rの一周する厚薄のある弧で周囲攻撃を見せる。 |
| [ファイアボール：立体の火球と鋭い着弾爆発](../knowledge/recipes/abilities/volumetric-fireball.md) | 小さな熱核・方向性のある炎殻・先細り尾・半径Rの一回の爆発を組み合わせる。 |
| [ヒール：使用者の収束と対象の上昇回復](../knowledge/recipes/abilities/targeted-healing-cast.md) | 詠唱の小さな環から、対象の回復パルスと上昇する葉へ接続する。 |
| [急所突き：一点の赤金の刺突と弱体の刻印](../knowledge/recipes/abilities/weakening-thrust.md) | 短い収束、鋭い刺突、接触から沈む弱体記号で急所を伝える。 |
| [号令：自分を押し上げる強化の解放](../knowledge/recipes/abilities/sharp-self-buff-cast.md) | 使用者自身の胸から上向きの形を解放し、攻撃強化の小さな記号へ畳む。 |
| [広域なぎ払い：横へ押し抜く主弧](../knowledge/recipes/abilities/wide-weapon-sweep.md) | 拡張射程の大きな前方弧を一枚で見せ、広い振り抜きを保持する。 |
| [地面衝撃：接地の圧縮と広がる低い波](../knowledge/recipes/abilities/ground-shockwave.md) | 接地の圧縮、正確な境界、薄い地面波、低い粉塵で重い地響きを作る。 |
| [剛腕の一撃：長い圧縮からの強い一点解放](../knowledge/recipes/abilities/charged-heavy-impact.md) | 入力進捗区間の溜めを腕の圧縮で見せ、幅広い命中と遅れる圧力で重さを作る。 |
| [強打：短く締めた強い打撃](../knowledge/recipes/abilities/accented-heavy-impact.md) | 入力進捗区間の溜めと一段強い接触を、通常打撃の形を保って作る。 |
| [呪いの眼光：眼の収束と対象の下降刻印](../knowledge/recipes/abilities/weakening-gaze.md) | 使用者の眼の小さな紫の収束から、対象の眼形・下降形へ切り替える。 |
| [再生：自分を巡る柔らかな回復](../knowledge/recipes/abilities/self-regeneration-cast.md) | 身体へ収束する薄い緑の流れから、実回復刻みの小さな上昇へ引き継ぐ。 |
| [瞬間火炎コーン：太い炎筋と短い残留](../knowledge/recipes/abilities/instant-fire-cone.md) | 半径R・入力角度θの前方形状を発動時に一度解放し、太い炎筋と短い残留で仕上げる。 |
| [鼓舞：短い上昇の鼓動と自己強化](../knowledge/recipes/abilities/soft-self-buff-cast.md) | 短い暖金の上昇で自分を強化し、小さな継続記号へ畳む。 |
| [食事による活力付与：暖かな収束と小さな継続表示](../knowledge/recipes/abilities/meal-vitality-activation.md) | 対象の胸へ穀粒の形を収束し、暖金の上昇から小さな長寿命の活力表示へ移る。 |

## 回復・強化・弱体の状態表示

| 推奨レシピ | 主案 |
| --- | --- |
| [継続HP回復：葉の識別と実回復パルス](../knowledge/recipes/states/periodic-health-restoration.md) | ミント色の短い付与と、葉の識別・実回復刻みの小さな上昇を組み合わせる。 |
| [強調HP回復：二段の付与と葉の識別](../knowledge/recipes/states/enhanced-health-restoration.md) | ポーションと同じHP言語を保ち、付与の二段の上昇と三枚の葉で上位品を読む。 |
| [食事由来の活力：暖かな攻撃強化](../knowledge/recipes/states/meal-vitality.md) | 穀粒の上昇と暖金の小さな上向き記号で、食事由来の活力を示す。 |
| [継続MP回復：結晶の識別と内向きの脈動](../knowledge/recipes/states/periodic-mana-restoration.md) | 青い結晶の収束と小さな周回で、HPとは異なるMP回復を示す。 |
| [上質な回復：真珠の縁と二重環](../knowledge/recipes/states/premium-restoration-burst.md) | 真珠色の身体縁と二重の細い環・上昇光で、短い回復を特別に見せる。 |
| [食事由来のHP回復：暖かな葉の上昇](../knowledge/recipes/states/food-health-restoration.md) | 少数の小さな葉と柔らかな緑の縁で、食材摂取による短い回復を示す。 |
| [回復と活力：独立した二つの状態表示](../knowledge/recipes/states/restoration-and-vitality.md) | 緑の回復と暖金の強化を同時に付与し、実状態期間は強化だけを残す。 |
| [対象への短い回復：一度の明瞭な上昇](../knowledge/recipes/states/targeted-restoration-burst.md) | 対象のミントの輪郭と一本にまとまる葉の上昇で実状態期間の回復を示す。 |
| [攻撃低下：欠けた下降記号](../knowledge/recipes/states/attack-reduction.md) | 暗紫の短い付与と、欠けた下向き山形二枚で攻撃低下を示す。 |
| [鋭い自己強化：上向きの解放](../knowledge/recipes/states/sharp-self-empowerment.md) | 自分の胸の強い短い解放から、小さな暖金の上向き記号へ移る。 |
| [自己再生：身体を巡る柔らかな回復](../knowledge/recipes/states/self-regeneration.md) | 少数の葉が身体外縁を昇り、実回復刻みで小さく輝く自己再生。 |
| [強い攻撃低下：二重の下降記号](../knowledge/recipes/states/strong-attack-reduction.md) | 濃い紫の二段の沈み込みと二重の下降記号で、強い攻撃低下を読む。 |
| [休息回復：静かなHP・MPの識別](../knowledge/recipes/states/rest-health-and-mana.md) | 葉と結晶を小さく並べ、実回復刻みだけに柔らかな脈動を付ける。 |
| [柔らかな自己強化：軽い上昇の鼓動](../knowledge/recipes/states/soft-self-empowerment.md) | 柔らかな暖金の付与から、二枚の上向き記号で実状態期間の自己強化を示す。 |

## 摂取・飲用のカテゴリ表現

| 推奨レシピ | 主案 |
| --- | --- |
| [回復液の飲用：滴の短い収束](../knowledge/recipes/consumption/liquid-remedy-use.md) | 清潔な小さな滴二個と短い白芯を、口元・手元から胸へ寄せる。 |
| [魔力回復液の飲用：小さな結晶の収束](../knowledge/recipes/consumption/mana-remedy-use.md) | 澄んだ淡青の結晶三個を胸へ内向きに収束する。 |
| [上質な回復液の飲用：真珠と暖金の収束](../knowledge/recipes/consumption/premium-remedy-use.md) | 真珠の小点四個が暖金の小弧を描いて胸へ収束する。 |
| [柔らかな食材の摂取：白黄の丸い光点](../knowledge/recipes/consumption/soft-protein-consumption.md) | 乳白の丸い光点二個と淡黄の小点を、一回だけ口元から低く上昇させる。 |
| [米・穀物の摂取：小さな穀粒の束](../knowledge/recipes/consumption/grain-consumption.md) | 象牙白の長円三粒を一束にまとめ、口元から上昇して胸へ収束する。 |
| [泡のある飲料：短い泡抜けと琥珀の弧](../knowledge/recipes/consumption/foamy-beverage-consumption.md) | クリームの丸点三個と薄い琥珀の小弧を、一度だけ口元から上昇して消す。 |
| [肉系の食材：暖白の短い上昇](../knowledge/recipes/consumption/savory-protein-consumption.md) | 暖白の細い点二個と小さな土金の点を、低く一度だけ上昇させる。 |
| [魚系の食材：銀の小片と淡青の縁](../knowledge/recipes/consumption/aquatic-protein-consumption.md) | 淡銀の小片三個とごく薄い青の縁を、口元から胸へ短く寄せる。 |
| [温かい料理：低い湯気と暖金の小点](../knowledge/recipes/consumption/warm-meal-consumption.md) | 低い暖白の湯気二本と小さな暖金の点を、口元・器の上から短く昇らせる。 |
| [衣のある料理：少数の暖金の欠片](../knowledge/recipes/consumption/crispy-food-consumption.md) | 暖金の角片四個を小さく弾き、一度だけ消す。 |
| [芋の食事：丸い暖白の二点](../knowledge/recipes/consumption/starchy-food-consumption.md) | 丸い暖白の小点二個を低く上昇し、一束へまとまる形にする。 |

## 共通の接触

| 推奨レシピ | 主案 |
| --- | --- |
| [切断方向を保つ斬撃の命中](../knowledge/recipes/impacts/impact-cut.md) | 短い切り線・接触の小さな白芯・法線方向の少数片で切断の瞬間を示す。 |
| [一点へ刺さる刺突の命中](../knowledge/recipes/impacts/impact-pierce.md) | 攻撃軸の細い白芯、短い圧縮環、背後へ抜ける小片で一点接触を強調する。 |
| [押し込んで弾ける打撃の命中](../knowledge/recipes/impacts/impact-blunt.md) | 幅広い接触星と薄い圧縮波で、打撃の面と重量を示す。 |
| [火炎が触れた対象の小さな熱反応](../knowledge/recipes/impacts/impact-fire-contact.md) | 局所の橙の熱い縁と少数の火の粉で、火炎の接触を示す。 |

## 候補比較の初期レシピ

[火球の核比較](../knowledge/recipes/fireball-readable-core.md)と[魔法球の核比較](../knowledge/recipes/magic-orb-readable-core.md)は核の複数候補を示す。核から炎殻・尾・着弾まで選んだ具体的な主案は上の立体火球Recipeを使う。

## 採用例

[DungeonInnの対応表](../projects/dungeon-inn/CATALOG.md)は、武器16・スキル15・状態14・消費アイテム16を、共通Recipeとゲーム固有の調整値へ対応付ける。対応表は共通知識の索引へ登録しない。
