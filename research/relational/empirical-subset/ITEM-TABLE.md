| item_id | model | class | layer | contested | confidence | excerpt | lines |
|---|---|---|---|---|---|---|---|
| ES-T1-C2-E01 | T1-C2 | S1 | syntax/parse | no | high | `satisfy greenhouse to moistureControl;` | 41 |
| ES-T1-C3-E01 | T1-C3 | I1 | semantic/behavioural | yes (defect status) | low | `doc /* Soil moisture shall be kept between 35% and 75% ...` | 37-39 |
| ES-T2-C1-E01 | T2-C1 | S1 | syntax/parse | no | high | `transition from idle to lowering on detection.approaching;` | 48-51 |
| ES-T2-C2-E01 | T2-C2 | S2 | constraint/OCL | no | medium | `satisfy lowerBeforeArrival;` | 33 |
| ES-T3-C1-E01 | T3-C1 | N2 | name resolution | no | high | `attribute innerDiameter : Real;` | 4,5,9,10,14,15,19,20,32 |
| ES-T3-C2-E01 | T3-C2 | S1 | syntax/parse | no | high | `port in; / port out; / line.in` | 23,24,33 |
| ES-T3-C2-E02 | T3-C2 | N1 | name resolution | no | high | `satisfy alarmTiming by pump;` | 44 |
| ES-T4-C1-E01 | T4-C1 | T1 | type/typing | no | medium | `first checkCharge; / then checkAvailability; / then assign` | 42-43 |
| ES-T4-C1-E02 | T4-C1 | R1 | type/typing | yes (layer) | medium | `connection powerLink connect controller.fleet.battery.powe` | 51 |
| ES-T4-C2-E01 | T4-C2 | N1 | name resolution | no | high | `satisfy returnToDock by fleet;` | 32 |
| ES-T4-C3-E01 | T4-C3 | R1 | type/typing | yes (layer) | medium | `connection batteryToDock connect fleet.vehicles.battery.po` | 56 |
| ES-T5-C2-E01 | T5-C2 | N1 | name resolution | no | high | `satisfy insideWindow by station;` | 32 |
| ES-T6-C2-E01 | T6-C2 | N1 | name resolution | no | high | `satisfy maintainTemperature by heating;` | 40 |

| control_id | model | tier | second coder covered | note |
|---|---|---|---|---|
| CTRL-T1-C1 | T1-C1 | clean | yes | No coded defect in any population after C12 (the 'first start;' record was withdrawn: Acti |
| CTRL-T2-C3 | T2-C3 | clean | no | No coded defect in any population. |
| CTRL-T3-C3 | T3-C3 | clean | yes | No coded defect in any population; imports SI without writing a unit literal. |
| CTRL-T5-C1 | T5-C1 | clean | yes | No coded defect in any population; imports SI without writing a unit literal. |
| CTRL-T5-C3 | T5-C3 | frozen-clean-only | no | NOT A CONTROL: carries a verified post-inspection defect (attribute window : VisibilityWin |
| CTRL-T6-C1 | T6-C1 | frozen-clean-only | no | NOT A CONTROL: carries a verified post-inspection defect (port return; line 26, reserved k |
| CTRL-T6-C3 | T6-C3 | frozen-clean-only | yes | NOT A CONTROL: carries a verified post-inspection defect (port return; line 26). A diagnos |
