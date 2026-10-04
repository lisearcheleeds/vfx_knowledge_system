# DungeonInn：共通知識の採用対応表

[受領仕様](INPUT.md)と[美術方針](ART_DIRECTION.md)に基づく採用案。[BINDINGS.json](BINDINGS.json)に全61対象のゲーム契約・採用Recipe・レイヤー調整を記録する。共通知識は汎用の形・構成・技法として登録し、固有IDや時間はこのフォルダに置く。

共通Recipeは具体的な主案を持つ。候補・代替は自動採用しない。Recipeはdraft。火球の射出・飛翔・着弾はUnity Previewで制作・撮影し、[制作記録](runs/fireball-2026-10-04.md)へ知見を保存した。矩形面の欠点と、内部構造・ゲーム接続・性能測定が残る。他対象は未実装。ナレッジIDは実行時EffectIdではない。

## 通常攻撃：16種

| 対象 | 採用する共通知識 | このゲームの契約 |
| --- | --- | --- |
| 剣 | [recipe/weapon-sword](../../knowledge/recipes/weapons/weapon-sword.md) | 通常攻撃：扇形90度。射程・運動面・有効タイミングはゲーム入力。 |
| 斧 | [recipe/weapon-axe](../../knowledge/recipes/weapons/weapon-axe.md) | 通常攻撃：扇形120度。 |
| 大剣 | [recipe/weapon-greatsword](../../knowledge/recipes/weapons/weapon-greatsword.md) | 通常攻撃：扇形110度。現在の装備/ActorArchetypeからの参照なし。定義済み候補として保持。 |
| 鎌 | [recipe/weapon-scythe](../../knowledge/recipes/weapons/weapon-scythe.md) | 通常攻撃：円形、判定持続0.35秒。半径はゲーム入力。 |
| 短剣 | [recipe/weapon-dagger](../../knowledge/recipes/weapons/weapon-dagger.md) | 通常攻撃：直接攻撃。射程・予備動作は未提供。 |
| 槍 | [recipe/weapon-spear](../../knowledge/recipes/weapons/weapon-spear.md) | 通常攻撃：直接攻撃。現在の装備/ActorArchetypeから参照なし。定義済み候補として保持。 |
| 棒 | [recipe/weapon-rod](../../knowledge/recipes/weapons/weapon-rod.md) | 通常攻撃：直接攻撃。 |
| 拳 | [recipe/weapon-fist](../../knowledge/recipes/weapons/weapon-fist.md) | 通常攻撃：直接攻撃。 |
| 大盾 | [recipe/weapon-greatshield](../../knowledge/recipes/weapons/weapon-greatshield.md) | 通常攻撃：直接攻撃。現在の装備/ActorArchetypeから参照なし。定義済み候補として保持。 |
| 鉄扇 | [recipe/weapon-ironfan](../../knowledge/recipes/weapons/weapon-ironfan.md) | 通常攻撃：直接攻撃。現在の装備/ActorArchetypeから参照なし。定義済み候補として保持。 |
| 爪 | [recipe/weapon-claw](../../knowledge/recipes/weapons/weapon-claw.md) | 通常攻撃：直接攻撃。モンスター自然武器でも同じ戦闘定義。 |
| 牙 | [recipe/weapon-fang](../../knowledge/recipes/weapons/weapon-fang.md) | 通常攻撃：直接攻撃。モンスター自然武器でも同じ戦闘定義。 |
| 弓 | [recipe/weapon-bow](../../knowledge/recipes/weapons/weapon-bow.md) | 通常攻撃：飛翔18m/s。 |
| クロスボウ | [recipe/weapon-crossbow](../../knowledge/recipes/weapons/weapon-crossbow.md) | 通常攻撃：飛翔22m/s。現在の装備/ActorArchetypeから参照なし。定義済み候補として保持。 |
| 杖 | [recipe/weapon-staff](../../knowledge/recipes/weapons/weapon-staff.md) | 通常攻撃：魔法弾の飛翔10m/s。属性は未指定。 |
| ワンド | [recipe/weapon-wand](../../knowledge/recipes/weapons/weapon-wand.md) | 通常攻撃：小型魔法弾の飛翔12m/s。属性は未指定。 |

## スキル：15件

| 対象 | 採用する共通知識 | このゲームの契約 |
| --- | --- | --- |
| 101 狙い撃ち | [recipe/charged-arrow](../../knowledge/recipes/abilities/charged-arrow.md) | 予備動作0.8秒、飛翔24m/s。 |
| 102 旋風斬 | [recipe/circular-slash](../../knowledge/recipes/abilities/circular-slash.md) | 予備動作0.4秒、半径2.5m。 |
| 103 ファイアボール | [recipe/volumetric-fireball](../../knowledge/recipes/abilities/volumetric-fireball.md) | 詠唱1.2秒＋予備動作0.2秒、飛翔14m/s、着弾半径2m。 |
| 104 ヒール | [recipe/targeted-healing-cast](../../knowledge/recipes/abilities/targeted-healing-cast.md) | 詠唱0.8秒、対象の回復効果1秒。受領表の記載順ではActorEffectId8がヒール。 |
| 105 急所突き | [recipe/weakening-thrust](../../knowledge/recipes/abilities/weakening-thrust.md) | 予備動作0.3秒、弱体10秒。ActorEffectId9/12のどちらかは受領表から確定しない。 |
| 201 号令 | [recipe/sharp-self-buff-cast](../../knowledge/recipes/abilities/sharp-self-buff-cast.md) | 予備動作0.6秒、自分への攻撃強化15秒。ActorEffectId10。 |
| 202 なぎ払い | [recipe/wide-weapon-sweep](../../knowledge/recipes/abilities/wide-weapon-sweep.md) | 予備動作0.6秒、扇形120度、武器射程＋1m。 |
| 203 地響き | [recipe/ground-shockwave](../../knowledge/recipes/abilities/ground-shockwave.md) | 詠唱1秒＋予備動作0.3秒、半径3m、命中と弱体付与。弱体の具体的なActorEffectId・持続はこの行では未提供。 |
| 204 剛腕の一撃 | [recipe/charged-heavy-impact](../../knowledge/recipes/abilities/charged-heavy-impact.md) | 予備動作1秒。 |
| 205 強打 | [recipe/accented-heavy-impact](../../knowledge/recipes/abilities/accented-heavy-impact.md) | 予備動作0.5秒。 |
| 206 呪いの眼光 | [recipe/weakening-gaze](../../knowledge/recipes/abilities/weakening-gaze.md) | 詠唱0.6秒、対象の弱体10秒。具体的なActorEffectId9/12対応は未提供。 |
| 207 再生 | [recipe/self-regeneration-cast](../../knowledge/recipes/abilities/self-regeneration-cast.md) | 予備動作0.5秒、自己回復6秒。ActorEffectId11は1秒ごとの回復。 |
| 208 火炎の息 | [recipe/instant-fire-cone](../../knowledge/recipes/abilities/instant-fire-cone.md) | 予備動作0.8秒、半径5m・90度。瞬間的な範囲攻撃。 |
| 301 鼓舞 | [recipe/soft-self-buff-cast](../../knowledge/recipes/abilities/soft-self-buff-cast.md) | 予備動作0.4秒、自分への強化12秒。ActorEffectId14。 |
| 901 まかない料理 | [recipe/meal-vitality-activation](../../knowledge/recipes/abilities/meal-vitality-activation.md) | 施設サービス、対象への強化300秒。戦闘の詠唱・予備動作は未提供。 |

## 状態効果：14件

| 対象 | 採用する共通知識 | このゲームの契約 |
| --- | --- | --- |
| 1 ポーション | [recipe/periodic-health-restoration](../../knowledge/recipes/states/periodic-health-restoration.md) | ポーション由来、HP回復10秒、1秒ごと。再付与で延長・更新あり。 |
| 2 ハイポーション | [recipe/enhanced-health-restoration](../../knowledge/recipes/states/enhanced-health-restoration.md) | ハイポーション由来、HP回復10秒、1秒ごと。回復量の具体値は未提供。 |
| 3 食事の活力 | [recipe/meal-vitality](../../knowledge/recipes/states/meal-vitality.md) | 食事の活力、攻撃強化300秒。再付与で延長・更新あり。 |
| 4 マナポーション | [recipe/periodic-mana-restoration](../../knowledge/recipes/states/periodic-mana-restoration.md) | マナポーション由来、MP回復10秒、1秒ごと。 |
| 5 エリクサー | [recipe/premium-restoration-burst](../../knowledge/recipes/states/premium-restoration-burst.md) | 受領表の記載順ではエリクサー、短い回復効果1秒。回復するパラメータの詳細は未提供。 |
| 6 食材の栄養 | [recipe/food-health-restoration](../../knowledge/recipes/states/food-health-restoration.md) | 食材の栄養、HP回復5秒。回復刻みの具体値はこの表では未提供。 |
| 7 料理の滋養 | [recipe/restoration-and-vitality](../../knowledge/recipes/states/restoration-and-vitality.md) | 料理の滋養、HP回復5秒、攻撃強化60秒。回復刻みは未提供。 |
| 8 ヒールの回復 | [recipe/targeted-restoration-burst](../../knowledge/recipes/states/targeted-restoration-burst.md) | 受領表の記載順ではヒール、対象の回復効果1秒。 |
| 9 弱体 | [recipe/attack-reduction](../../knowledge/recipes/states/attack-reduction.md) | 弱体、攻撃低下10秒。具体的な付与スキルの対応は未提供。 |
| 10 号令の強化 | [recipe/sharp-self-empowerment](../../knowledge/recipes/states/sharp-self-empowerment.md) | 号令の攻撃強化15秒。SkillId201は自分への強化。 |
| 11 再生の継続 | [recipe/self-regeneration](../../knowledge/recipes/states/self-regeneration.md) | 再生、自己回復6秒、1秒ごと。SkillId207。 |
| 12 弱体（強） | [recipe/strong-attack-reduction](../../knowledge/recipes/states/strong-attack-reduction.md) | 弱体（強）、攻撃低下10秒。効果量と具体的な付与スキル対応は未提供。 |
| 13 休憩 | [recipe/rest-health-and-mana](../../knowledge/recipes/states/rest-health-and-mana.md) | 休憩、HP・MP回復30秒、1秒ごと。休憩モーションの詳細は未提供。 |
| 14 鼓舞の強化 | [recipe/soft-self-empowerment](../../knowledge/recipes/states/soft-self-empowerment.md) | 鼓舞、攻撃強化12秒。SkillId301は自分への強化。 |

## 消費アイテム：16件

| 対象 | 採用する共通知識 | このゲームの契約 |
| --- | --- | --- |
| 2001 ポーション | [recipe/liquid-remedy-use](../../knowledge/recipes/consumption/liquid-remedy-use.md) ＋ [recipe/periodic-health-restoration](../../knowledge/recipes/states/periodic-health-restoration.md) | ポーション → ActorEffectId1。個別対応表はユーザー提供。 |
| 2002 ハイポーション | [recipe/liquid-remedy-use](../../knowledge/recipes/consumption/liquid-remedy-use.md) ＋ [recipe/enhanced-health-restoration](../../knowledge/recipes/states/enhanced-health-restoration.md) | ハイポーション → ActorEffectId2。個別対応表はユーザー提供。 |
| 2003 エリクサー | [recipe/premium-remedy-use](../../knowledge/recipes/consumption/premium-remedy-use.md) ＋ [recipe/premium-restoration-burst](../../knowledge/recipes/states/premium-restoration-burst.md) | エリクサー → ActorEffectId5。個別対応表はユーザー提供。 |
| 2004 マナポーション | [recipe/mana-remedy-use](../../knowledge/recipes/consumption/mana-remedy-use.md) ＋ [recipe/periodic-mana-restoration](../../knowledge/recipes/states/periodic-mana-restoration.md) | マナポーション → ActorEffectId4。個別対応表はユーザー提供。 |
| 2101 ゆでたまご | [recipe/soft-protein-consumption](../../knowledge/recipes/consumption/soft-protein-consumption.md) ＋ [recipe/food-health-restoration](../../knowledge/recipes/states/food-health-restoration.md) | ゆでたまご → ActorEffectId6。個別対応表はユーザー提供。 |
| 2102 おにぎり | [recipe/grain-consumption](../../knowledge/recipes/consumption/grain-consumption.md) ＋ [recipe/food-health-restoration](../../knowledge/recipes/states/food-health-restoration.md) | おにぎり → ActorEffectId6。個別対応表はユーザー提供。 |
| 2103 ビール | [recipe/foamy-beverage-consumption](../../knowledge/recipes/consumption/foamy-beverage-consumption.md) ＋ [recipe/food-health-restoration](../../knowledge/recipes/states/food-health-restoration.md) | ビール → ActorEffectId6。個別対応表はユーザー提供。 |
| 2104 肉 | [recipe/savory-protein-consumption](../../knowledge/recipes/consumption/savory-protein-consumption.md) ＋ [recipe/food-health-restoration](../../knowledge/recipes/states/food-health-restoration.md) | 肉 → ActorEffectId6。個別対応表はユーザー提供。 |
| 2105 謎の肉 | [recipe/savory-protein-consumption](../../knowledge/recipes/consumption/savory-protein-consumption.md) ＋ [recipe/food-health-restoration](../../knowledge/recipes/states/food-health-restoration.md) | 謎の肉 → ActorEffectId6。個別対応表はユーザー提供。 |
| 2106 魚 | [recipe/aquatic-protein-consumption](../../knowledge/recipes/consumption/aquatic-protein-consumption.md) ＋ [recipe/food-health-restoration](../../knowledge/recipes/states/food-health-restoration.md) | 魚 → ActorEffectId6。個別対応表はユーザー提供。 |
| 2107 魚の串焼き | [recipe/warm-meal-consumption](../../knowledge/recipes/consumption/warm-meal-consumption.md) ＋ [recipe/restoration-and-vitality](../../knowledge/recipes/states/restoration-and-vitality.md) | 魚の串焼き → ActorEffectId7。個別対応表はユーザー提供。 |
| 2108 肉の串焼き | [recipe/warm-meal-consumption](../../knowledge/recipes/consumption/warm-meal-consumption.md) ＋ [recipe/restoration-and-vitality](../../knowledge/recipes/states/restoration-and-vitality.md) | 肉の串焼き → ActorEffectId7。個別対応表はユーザー提供。 |
| 2109 ラーメン | [recipe/warm-meal-consumption](../../knowledge/recipes/consumption/warm-meal-consumption.md) ＋ [recipe/restoration-and-vitality](../../knowledge/recipes/states/restoration-and-vitality.md) | ラーメン → ActorEffectId7。個別対応表はユーザー提供。 |
| 2110 コロッケ | [recipe/crispy-food-consumption](../../knowledge/recipes/consumption/crispy-food-consumption.md) ＋ [recipe/food-health-restoration](../../knowledge/recipes/states/food-health-restoration.md) | コロッケ → ActorEffectId6。個別対応表はユーザー提供。 |
| 2111 ポテト | [recipe/starchy-food-consumption](../../knowledge/recipes/consumption/starchy-food-consumption.md) ＋ [recipe/food-health-restoration](../../knowledge/recipes/states/food-health-restoration.md) | ポテト → ActorEffectId6。個別対応表はユーザー提供。 |
| 2112 からあげ | [recipe/crispy-food-consumption](../../knowledge/recipes/consumption/crispy-food-consumption.md) ＋ [recipe/restoration-and-vitality](../../knowledge/recipes/states/restoration-and-vitality.md) | からあげ → ActorEffectId7。個別対応表はユーザー提供。 |

## おにぎりの接続例

Item2102は「米・穀物」の見た目として `recipe/grain-consumption` を採用し、ActorEffect6の回復表示には `recipe/food-health-restoration` を採用する。穀粒表現にHP回復を必須依存として付けない。別のゲームで穀粒表現を使って満腹度だけを変える場合、回復レシピは採用しない。

同じ食品の外観でもゲーム効果は別指定。コロッケ2110とからあげ2112は衣の摂取表現を共有候補とするが、前者はActorEffect6、後者は7。ポテト2111は調理法が未指定なので、衣を必須にせず汎用の芋の表現を選ぶ。魚/肉の串焼きは湯気の形と銀/暖金の小点で差分を付ける。品目ごとの具体値はBINDINGS.jsonに残す。

## 未照合・次の制作

急所突き・地響き・呪いの眼光のActorEffect9/12対応、まかない料理の具体的なActorEffectIdは未照合。ヒール→ActorEffect8は初回表の記載順に基づく。最終EffectIdとPrefab/Material/Variantの共用は試作比較後に決める。

ファイアボール、剣/刺突/打撃、食事の複合状態から試作し、明暗背景・密集・中断・再付与・解除を確認する。別プロジェクトの参照・実装前にはユーザーへ確認する。
