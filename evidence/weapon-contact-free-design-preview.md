---
schema_version: 0.1.0
id: evidence/weapon-contact-free-design-preview
kind: evidence
title: 射出・投射体・近接・命中を名称から一から作ったPreview記録
summary: 名称だけから作った射出・投射体・近接・命中・予兆・撃破の21種の版1が10〜100点と評価され、低い評価の原因が「記号的な形」「役割と逆向きの動き」「命中に対して過剰な形」に集中した記録。
status: reviewed
revision: 2
updated_at: '2026-10-08'
aliases: []
tags:
- combat
- evidence
scope: engine-neutral
relations: []
evidence: []
superseded_by: []
evidence_details:
  source_kind: first-party-experiment
  claims:
  - target: recipe/weapon-greatshield
    statement: 盾の面に沿った縦の輪が平面のまま広がる版は80点。攻撃方向と内積0の方向だけへ広がる衝撃波は「敵の攻撃をパリィして衝撃を逃がしている」表現になると指摘された。輪を球面のように内側ほど前へ出すと、盾の前面から衝撃を押し出す表現になる。
  - target: recipe/weapon-bow
    statement: 矢の形のテクスチャ（アイコン）を飛ばす版は40点。矢の長さに伸ばした回転楕円体がよいと指摘された。尾は合格。射出の弦の線は無いほうがよい（90点）。
  - target: recipe/weapon-crossbow
    statement: 矢と同じく、ボルトのアイコンは40点で、伸ばした楕円体へ替える指摘。射出の弦の線は無いほうがよい（90点）。
  - target: recipe/weapon-wand
    statement: 魔法の矢の尾と色は合格だが、丸い芯はダーツに見えず70点。射出は杖との差別化ができていると100点。
  - target: recipe/weapon-staff
    statement: 射出と魔法弾は100点。魔法弾の命中は85点で、再生時間を2/3にする指摘。
  - target: recipe/weapon-spear
    statement: 非対称の穂先と側面の筋を重ねた版は「何を表現しているか分からない」35点。左右対称のシンプルな突きでよいと指摘された。
  - target: recipe/weapon-fang
    statement: 上下の顎の弧と歯の版は25点。狼の牙を上下2本ずつ（計4本）で噛みつく形がよいと指摘された。噛みつきの命中で内へ閉じる表現は10点で、噛みつかれた側のエフェクトなので外へ飛ぶ粒子がよいと指摘された。
  - target: recipe/weapon-fist
    statement: 前へ抜ける輪が3つの版は90点。輪は2つでよく、3つはやりすぎと指摘された。
  - target: recipe/weapon-claw
    statement: 三本の弧の爪は90点。弧を寝かせた角度だけが気になると指摘された。
  - target: recipe/impact-pierce
    statement: 貫く光の針と締まる輪の版は、刺突の命中としては50点（命中に円はやりすぎ、粒子がよい）。レーザー光線の命中としてなら90点と評価された。
  - target: recipe/impact-cut
    statement: 火花に切り線の帯を重ねた版は75点。切り線は無いほうがよいと指摘された。打撃の命中は90点、魔法の矢の命中は100点。
  - target: composition/combat-readability
    statement: 攻撃の予兆（AttackGather）は100点だが、予兆は本来UI/UXの領域（矩形・円・扇の範囲表示）で、エフェクトとしては別の発想が要ると指摘された。撃破（DefeatWisp）は65点で、明確な正解が無いとされた。
  - target: recipe/weapon-spear
    statement: 版2（斬撃の帯を左右対称にした形）は40点で「Swordの手法につられすぎて、切ると突くの違いが出ていない。突くは先が尖りすぎていない円錐状・コーン状でアニメーションすべき」と指摘された。
  - target: recipe/weapon-fang
    statement: 版2（まっすぐの円錐の牙4本）は50点。牙のように曲げる、牙が動いていないのも減点と指摘された。動かなかった原因は速度の曲線の軸のモードが混在していたこと。
  - target: adapter/unity-urp-baseline-sheet-particles
    statement: 全周の輪の中心から継ぎ目に沿う細い線（盾・拳で指摘）は、UV.x が1を越える補助ピクセルで厚みの分岐が飛び、fwidth が巨大になったことが原因だった。UV.x を saturate して消えた。盾は版2で100点。
  - target: recipe/weapon-fang
    statement: 版3（反った牙を平行に動かし、先と先を一点で合わせた形）は「反ってはいるが、牙の配置と角度、噛み合わせが悪い。回転を含めて顎の回転を想定する」と指摘された。
  - target: recipe/weapon-spear
    statement: 版3（伸びる円錐）は、穂先の閃き（Tip）が不要という指摘のほかは合格。
  - target: recipe/weapon-fang
    statement: 版4・5（下の牙を上の牙の前に置き、強く反らせた形）は「上顎の歯が下顎の歯より中にあるのか。人間ですら上顎の歯は外側。閉じた時の牙の角度もおかしい」と指摘された。
  - target: recipe/weapon-fang
    statement: 版7（上の牙が外・前から下の牙にかぶさり、ほぼ垂直に閉じる長い牙を、蝶番まわりの顎の回転で閉じる形）は「まぁいいでしょう」と合格した。直前の版で牙を短くしたことは「長いまま噛み合った状態にする」と戻された。
  conditions: 専用Prefab Preview。暗い背景、45度俯瞰。ユーザーがライブPreviewで評価。前任のアセットは参照していない。名称から推測できないもの（ファイアボールの3種）は質問し、作らないと回答された。
  result: 版1は10〜100点。100点は杖の射出・魔法弾・ワンドの射出・魔法の矢の命中・予兆。版2は盾100点、拳は問題なし（線の修正のみ）、槍40点・牙50点。槍は版3（伸びる円錐）でTip削除のほか合格、牙は版7で合格。
  limitations: 一つのカメラ条件・一つのプロジェクトの例。評価点はユーザーの主観。ゲーム接続・性能は未確認。
  sources: []
  checked_at: '2026-10-08'
  execution:
    engine: unity
    engine_version: 6000.3.14f1
    renderer: URP 17.3.0
    environment: Windows Editor / 専用Prefab Preview
    executed_at: '2026-10-08'
    procedure: 生成スクリプトで面と粒子の層を作り、連番の一覧画像で確認・修正してからユーザーが評価した。
    artifacts:
    - projects/dungeon-inn/runs/weapon-contact-free-design-2026-10-08.md
---

# 射出・投射体・近接・命中を名称から一から作ったPreview記録

## 経緯

剣・斧などの近接の残像に続き、手を付けていない21種を名称だけから作った。ユーザーは制作中に指示をせず、版1の評価を一度にまとめて返した。

## 判定

評価の低い版は三つの型に分かれた。

- **記号的な形**: 矢・ボルトの絵（アイコン）を飛ばす、顎と歯を弧で描く、槍の穂先を非対称の面で描く。実物の立体（伸ばした楕円体、牙）か、対称の単純な形に替える指摘だった。
- **役割と逆向きの動き**: 噛みつかれた命中で光が内へ閉じた（10点）。命中は受けた側から外へ飛ぶ。盾の衝撃波が盾の面に沿って広がると、押すのではなく受け流す（パリィ）表現になる。
- **命中に対して過剰な形**: 刺突の命中の輪、斬撃の命中の切り線、弓の弦の線、拳の3つ目の輪。主役以外の線と輪は削る方向で評価が上がった。

## 限界

一つのカメラ条件・一つのプロジェクトの例。版2の評価は未取得。
