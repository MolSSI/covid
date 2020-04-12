---
title: "MD Simulations"
description: "Molecular dynamics simulations of relevance to covid-19"
type: "md"
---

<style>
.blur-non-hovered body {
  background: #fafafa;
  color: #444;
  font: 100%/30px 'Helvetica Neue', helvetica, arial, sans-serif;
  text-shadow: 0 1px 0 #fff;
  margin-left: auto;
  margin-right: auto;
  margin: auto;
  text-align: center;
}

.blur-non-hovered strong {
  font-weight: bold;
}

.blur-non-hovered em {
  font-style: italic;
}

.blur-non-hovered table {
  background: #f5f5f5;
  border-collapse: separate;
  box-shadow: inset 0 1px 0 #fff;
  font-size: 15px;
  line-height: 24px;
  margin: auto;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  width: 10%;
}

.blur-non-hovered th {
  background: linear-gradient(#777, #444);
  border-left: 1px solid #555;
  border-right: 1px solid #777;
  border-top: 1px solid #555;
  border-bottom: 1px solid #333;
  box-shadow: inset 0 1px 0 #999;
  color: #fff;
  font-weight: bold;
  padding: 20px 20px 20px 20px;
  position: relative;
  text-shadow: 0 1px 0 #000;
}

.blur-non-hovered th:after {
  background: linear-gradient(rgba(255,255,255,0), rgba(255,255,255,.08));
  content: '';
  display: block;
  margin: auto;
  position: relative;
}

.blur-non-hovered th:first-child {
  border-left: 1px solid #777;
  box-shadow: inset 1px 1px 0 #999;
}

.blur-non-hovered th:last-child {
  box-shadow: inset -1px 1px 0 #999;
}

.blur-non-hovered td {
  border-right: 1px solid #fff;
  border-left: 1px solid #e8e8e8;
  border-top: 1px solid #fff;
  border-bottom: 1px solid #e8e8e8;
  padding: 10px 10px 10px 10px;
  position: relative;
  transition: all 300ms;
}

.blur-non-hovered td:first-child {
  box-shadow: inset 1px 0 0 #fff;
}

.blur-non-hovered td:last-child {
  border-right: 1px solid #e8e8e8;
  box-shadow: inset -1px 0 0 #fff;
}

.blur-non-hovered tr:nth-child(odd) td {
  background: #f1f1f1;
}

.blur-non-hovered tr:last-of-type td {
  box-shadow: inset 0 -1px 0 #fff;
}

.blur-non-hovered tr:last-of-type td:first-child {
  box-shadow: inset 1px -1px 0 #fff;
}

.blur-non-hovered tr:last-of-type td:last-child {
  box-shadow: inset -1px -1px 0 #fff;
}

.blur-non-hovered tbody:hover td {
  color: transparent;
  text-shadow: 0 0 3px #aaa;
}

.blur-non-hovered tbody:hover tr:hover td {
  color: #444;
  text-shadow: 0 1px 0 #fff;
}

.blur-non-hovered center {
    width:100%; 
    margin-left:-30%; 
    margin-right:0%;
}

</style>

<div class="ox-hugo-table blur-non-hovered table-nocaption">
<div></div>

<center>

|     Target          | PDB-IDs | Ensemble | Forcefields       | Solvent  | Salinity (M)          | Temp (K)    | Pressure (atm) | Download          | Author                 | References |
|:-------------------:|:-------:|:--------:|:-----------------:|:--------:|:---------------------:|:-----------:|:--------------:|:-----------------:|:----------------------:|:----------:|
| Viral protease      | [6LU7](https://www.rcsb.org/structure/6LU7)    | NPT      | AMBER99, TIP3P    | Water    | 0.1                   | 300         |    1           | Trajectory, Files | Daniel T. Crawford     | ref [1][2] |
| Viral protease      | [6LU7](https://www.rcsb.org/structure/6LU7)    | NVE      | GROMOS53a6, SPC   | Water    | 0.15                  | N/A         |    N/A         | Trajectory, Files | Levi Naden             |  ref       |
| Viral protease      | [6LU7](https://www.rcsb.org/structure/6LU7)    | NPT      | GAFF              | Implicit | 0.2                   | 300         |    1           | [Trajectory](google.com), [Files](googlg.ecom) | Samuel Ellis           |  ref       |
| Viral protease      | [6LU7](https://www.rcsb.org/structure/6LU7)    | NVT      | CHARMM36, TIP4P   | Water    |0.1                    | 310         |    N/A         | [Files](google.com)             | Andrew Abi-Mansour     | ref [3]    |

</center>

</div>
