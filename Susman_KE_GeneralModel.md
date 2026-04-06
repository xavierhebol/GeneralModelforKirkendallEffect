# General Kinetic Model for Solid-State Reactions Involving the Nano Kirkendall Effect
**Source:** Susman, Vaskevich & Rubinstein, *J. Phys. Chem. C* 2016, 120, 16140–16152

---

## 1. Parameter Glossary

| Symbol | Name | Units |
|---|---|---|
| $a_0$ | Initial nanoparticle radius | m |
| $a_1$ | Radius of metal–oxide boundary (Interface I) | m |
| $a_2$ | Radius of oxide–air boundary (Interface II) | m |
| $a_v^\text{int}$ | Equivalent internal void radius | m |
| $\delta$ | Conversion fraction (fraction of initial metal volume consumed) | — |
| $Z$ | Pilling–Bedworth ratio (volume expansion coefficient) | — |
| $\phi$ | Core-contraction parameter (fraction of reacted metal that causes core shrinkage) | — |
| $K$ | Ratio of outward-to-inward oxide growth rates | — |
| $V_0$ | Initial particle volume $= \frac{4}{3}\pi a_0^3$ | m³ |
| $V_1$ | Volume enclosed by Interface I (core) | m³ |
| $V_2$ | Total particle volume | m³ |
| $V_\text{Ox}$ | Volume of oxide formed | m³ |
| $V_\text{Cu}$ | Volume of unreacted metal | m³ |
| $V_v^\text{int}$ | Internal void volume | m³ |
| $V_k$ | Kirkendall shift volume | m³ |
| $\eta$ | Stoichiometric coefficient of cations (Cu⁺) | — |
| $\eta'$ | Stoichiometric coefficient of anions (O²⁻) | — |
| $D^*_{\text{Cu}^+}$ | Tracer diffusivity of Cu⁺ in oxide | m²/s |
| $D^*_{\text{O}^{2-}}$ | Tracer diffusivity of O²⁻ in oxide | m²/s |
| $c_{i,1}$ | Equilibrium concentration of species $i$ at Interface I | mol/m³ |
| $c_{i,2}$ | Equilibrium concentration of species $i$ at Interface II | mol/m³ |
| $J_i$ | Molar flow rate of species $i$ across the oxide shell | mol/s |
| $J_v$ | Net molar flow rate of vacancies | mol/s |
| $k_\text{in}$ | Inward (O²⁻) oxidation rate constant | m²/s |
| $k_\text{out}$ | Outward (Cu⁺) oxidation rate constant | m²/s |
| $k_p$ | Parabolic rate constant (measurable from flat-film experiments) | m²/s |
| $\text{FW}_\text{Ox}$ | Formula weight of oxide (Cu₂O) | kg/mol |
| $\text{FW}_{\text{Cu}^0}$ | Formula weight of Cu metal | kg/mol |
| $\rho_\text{Ox}$ | Bulk mass density of oxide | kg/m³ |
| $\rho_{\text{Cu}^0}$ | Bulk mass density of Cu metal | kg/m³ |

---

## 2. Core Assumptions

- Spherical particle geometry throughout the reaction.
- A homogeneous, nonporous, adherent oxide shell forms continuously.
- **Steady-state diffusion** profiles are always maintained in the oxide shell: $\partial c_i / \partial t = 0$.
- Ionic concentrations at both oxide boundaries ($c_{i,1}$, $c_{i,2}$) remain constant.
- Ion diffusion is uncorrelated; no electric-field-enhanced transport (no Cabrera–Mott).
- Bulk densities apply at the nanoscale; $Z$ is constant.
- The Kirkendall shift is suppressed at the nanoscale ($V_k \approx 0$), so $\phi$ is set by diffusivities alone.
- Vacancies are distributed homogeneously throughout the core volume.

---

## 3. Foundational Equations

### 3.1 Oxidation Reaction

$$\eta \,\text{Cu}^0 + \frac{\eta'}{2}\text{O}_2 \rightarrow \text{Cu}_\eta\text{O}_{\eta'} \tag{1}$$

Stoichiometric constraint (for Cu₂O):

$$\eta = 2\eta' \tag{2}$$

---

### 3.2 Pilling–Bedworth Ratio

$$Z = \frac{1}{\eta}\frac{\text{FW}_\text{Ox}\,\rho_{\text{Cu}^0}}{\text{FW}_{\text{Cu}^0}\,\rho_\text{Ox}} \tag{3}$$

For Cu → Cu₂O: **Z = 1.68**. Since Z > 1, the oxide shell occupies more volume than the metal it replaces, driving outward expansion of the particle.

---

### 3.3 Conversion Fraction

$$\delta(t) \equiv \frac{V_\text{Ox}(t)}{Z\, V_0} \tag{4}$$

$\delta$ ranges from 0 (unreacted) to 1 (fully converted). $V_\text{Ox}/Z$ is the equivalent volume of metal consumed to form the oxide.

---

### 3.4 Steady-State Concentration Profile in the Oxide Shell

$$c_i(r) = \frac{a_1 c_{i,1}(a_2 - r) + a_2 c_{i,2}(r - a_1)}{r(a_2 - a_1)} \tag{5}$$

This is the solution to Fick's second law in spherical geometry under steady-state. It is linear in $1/r$.

---

### 3.5 Steady-State Ionic Flux

$$J_i = \frac{dQ_i}{dt} = -4\pi D_i^*\,(c_{i,2} - c_{i,1})\,\frac{a_1 a_2}{a_2 - a_1} \tag{6}$$

The geometric factor $a_1 a_2/(a_2 - a_1)$ decreases as the shell thickens, producing parabolic (self-limiting) kinetics. This equation drives all subsequent rate laws.

---

### 3.6 Cu Mass Balance

The total moles of Cu metal and its time derivative:

$$Q_{\text{Cu}^0} = \frac{4}{3}\frac{\rho_{\text{Cu}^0}}{\text{FW}_{\text{Cu}^0}}\pi a_0^3 \tag{7}$$

$$\frac{dQ_{\text{Cu}^0}}{dt} = -\frac{4}{3}\frac{\rho_{\text{Cu}^0}}{\text{FW}_{\text{Cu}^0}}\pi a_0^3\,\frac{d\delta}{dt} \tag{8}$$

By conservation, the rate of Cu⁺ leaving the metal equals the rate of metal consumption:

$$\frac{dQ_{\text{Cu}^+}}{dt} = -\frac{dQ_{\text{Cu}^0}}{dt} = \frac{4}{3}\frac{\rho_{\text{Cu}^0}}{\text{FW}_{\text{Cu}^0}}\pi a_0^3\,\frac{d\delta}{dt} \tag{9}$$

---

## 4. The Two Limiting Models

### 4.1 Valensi–Carter (VC) Model — $\phi = 1$

**Physical picture:** O²⁻ diffuses inward; all oxide forms at Interface I; core shrinks inward; no internal voids.

**Boundary positions:**

$$a_1^3 = a_0^3(1-\delta) \tag{10}$$

$$a_2^3 = a_0^3(1 - \delta + Z\delta) \tag{11}$$

**Rate law** (obtained by equating Eq. 6 for O²⁻ to Eq. 9 and integrating):

$$\frac{Z - [1-(1-Z)\delta]^{2/3} - (Z-1)(1-\delta)^{2/3}}{2(Z-1)} = \frac{k_\text{in}}{a_0^2}\,t \tag{12}$$

**Inward rate constant:**

$$k_\text{in} = \frac{\eta}{\eta'}\frac{\text{FW}_{\text{Cu}^0}}{\rho_{\text{Cu}^0}}\,D^*_{\text{O}^{2-}}\,(c_{\text{O}^{2-},2} - c_{\text{O}^{2-},1}) \tag{13}$$

---

### 4.2 Nano Kirkendall Effect (NKE) Model — $\phi = 0$

**Physical picture:** Cu⁺ diffuses outward; all oxide forms at Interface II; inner boundary stays fixed; vacancies accumulate as an internal void.

**Boundary positions:**

$$a_1^3 = a_0^3 \tag{14}$$

$$a_2^3 = a_0^3(1 + Z\delta) \tag{15}$$

**Equivalent internal void radius:**

$$a_v^3 = a_0^3\,\delta \tag{16}$$

**Rate law** (obtained by equating Eq. 6 for Cu⁺ to Eq. 9 and integrating):

$$\frac{\frac{2}{3}Z\delta - (1+Z\delta)^{2/3} + 1}{2Z} = \frac{k_\text{out}}{a_0^2}\,t \tag{17}$$

**Outward rate constant:**

$$k_\text{out} = -\frac{\text{FW}_{\text{Cu}^0}}{\rho_{\text{Cu}^0}}\,D^*_{\text{Cu}^+}\,(c_{\text{Cu}^+,2} - c_{\text{Cu}^+,1}) \tag{18}$$

---

## 5. The General Model — $0 < \phi \leq 1$

### 5.1 Definition of $\phi$

$$\phi \equiv -Z\,\frac{dV_1}{dV_\text{Ox}} \tag{19}$$

$\phi$ is the fraction of reacted metal volume that results in core contraction. The remainder $(1-\phi)$ becomes internal void.

**Volume relationships:**

$$dV_1 = dV_\text{Cu} + dV_v^\text{int} \tag{20}$$

$$dV_2 = dV_1 + dV_\text{Ox} \tag{21}$$

---

### 5.2 General Boundary Positions

$$a_1^3 = a_0^3(1 - \phi\delta) \tag{22}$$

$$a_2^3 = a_0^3(1 - \phi\delta + Z\delta) \tag{23}$$

These recover Eqs. 10–11 for $\phi=1$ and Eqs. 14–15 for $\phi=0$.

**General internal void radius:**

$$(a_v^\text{int})^3 = a_0^3(1-\phi)\delta \tag{24}$$

Zero for $\phi=1$; equals Eq. 16 for $\phi=0$.

---

### 5.3 Volume Summary Table

| Volume | $\phi = 1$ (VC) | $0 < \phi < 1$ (General) | $\phi = 0$ (NKE) |
|---|---|---|---|
| $V_\text{Cu}$ | $V_0(1-\delta)$ | $V_0(1-\delta)$ | $V_0(1-\delta)$ |
| $V_v^\text{int}$ | $0$ | $V_0(1-\phi)\delta$ | $V_0\delta$ |
| $V_1$ | $V_0(1-\delta)$ | $V_0(1-\phi\delta)$ | $V_0$ |
| $V_\text{Ox}$ | $V_0 Z\delta$ | $V_0 Z\delta$ | $V_0 Z\delta$ |
| $V_2$ | $V_0(1-\delta+Z\delta)$ | $V_0(1-\phi\delta+Z\delta)$ | $V_0(1+Z\delta)$ |

---

### 5.4 General Rate Law

Substitute Eqs. 22–23 into the Cu⁺ flux (Eq. 6), equate to Eq. 9, and integrate from $\delta=0$ to $\delta$:

$$\frac{Z - \phi\left[1-(\phi-Z)\delta\right]^{2/3} - (Z-\phi)(1-\phi\delta)^{2/3}}{2(Z-\phi)\phi} = \frac{k_\text{out}}{a_0^2}\,t \tag{25}$$

This is the **central result of the model**. It reduces to:
- Eq. 17 (NKE) as $\phi \to 0$
- Eq. 12 (VC) as $\phi \to 1$

---

### 5.5 Linking $\phi$ to Diffusivities

**Ratio of oxide growth rates at Interfaces I and II:**

$$K \equiv \frac{dV_\text{Ox}^\text{out}}{dV_\text{Ox}^\text{in}} = \frac{k_\text{out}}{k_\text{in}} = \frac{\eta'\,D^*_{\text{Cu}^+}(c_{\text{Cu}^+,2}-c_{\text{Cu}^+,1})}{\eta\,D^*_{\text{O}^{2-}}(c_{\text{O}^{2-},2}-c_{\text{O}^{2-},1})} \tag{26}$$

**Under suppressed Kirkendall shift** ($V_k \approx 0$, valid at nanoscale):

$$\phi = \frac{Z}{1+K} \tag{27}$$

This is the key constitutive relation. $\phi$ is not a free fitting parameter — it is fixed by the ratio of diffusion driving forces:
- $D^*_{\text{Cu}^+} \gg D^*_{\text{O}^{2-}}$ → $K \gg 1$ → $\phi \to 0$ → NKE dominates
- $D^*_{\text{O}^{2-}} \gg D^*_{\text{Cu}^+}$ → $K \to 0$ → $\phi \to 1$ → VC behavior

---

### 5.6 Vacancy Flux

Conservation of species flow at Interface I:

$$\frac{J_{\text{Cu}^+}}{\eta} + \frac{J_{\text{O}^{2-}}}{\eta'} + \frac{J_v}{\eta} = 0 \tag{28}$$

Using Eq. 27, the vacancy flux simplifies to:

$$\frac{J_v}{\eta} = 4\pi\left(\frac{Z-2\phi}{Z-\phi}\right)\frac{D^*_{\text{Cu}^+}(c_{\text{Cu}^+,2}-c_{\text{Cu}^+,1})}{\eta}\,\frac{a_1 a_2}{a_2-a_1} \tag{29}$$

| $\phi$ range | Vacancy direction | Physical outcome |
|---|---|---|
| $\phi < Z/2$ | Inward | Internal void forms (NKE regime) |
| $\phi = Z/2$ | None | No net vacancy flow |
| $\phi > Z/2$ | Outward | No internal void |

---

### 5.7 Rate Constant Relationships

$$k_\text{in} = \frac{\phi}{Z-\phi}\,k_\text{out} \tag{30}$$

**Parabolic rate constant** (measurable independently from flat-film experiments):

$$k_p = k_\text{in} + k_\text{out} = \frac{Z}{Z-\phi}\,k_\text{out} \tag{31}$$

**General rate law rewritten in terms of $k_p$** (final working form):

$$\frac{Z - \phi\left[1-(\phi-Z)\delta\right]^{2/3} - (Z-\phi)(1-\phi\delta)^{2/3}}{2(Z-\phi)\phi} = \frac{Z-\phi}{Z}\,\frac{k_p}{a_0^2}\,t \tag{32}$$

This is the equation used in practice: $Z$ and $k_p$ come from material data or flat-film measurements, $\phi$ comes from Eq. 27, and $a_0$ is the initial particle size. Solving gives $\delta(t)$.

---

## 6. Equation Solution Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     INPUTS (Material Data)                  │
│  FW_Ox, FW_Cu, ρ_Ox, ρ_Cu, η, η'                           │
│  D*_Cu+, D*_O2-, c_{i,1}, c_{i,2}  (or k_p from literature)│
│  a_0  (initial particle radius)                             │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: Compute Z  (Eq. 3)                                 │
│                                                             │
│  Z = (1/η) · (FW_Ox · ρ_Cu) / (FW_Cu · ρ_Ox)              │
│                                                             │
│  → Describes volume expansion upon oxidation                │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 2: Compute rate constants  (Eqs. 13, 18)              │
│                                                             │
│  k_in  = (η/η') · (FW_Cu/ρ_Cu) · D*_O2- · Δc_O2-          │
│  k_out = −(FW_Cu/ρ_Cu) · D*_Cu+ · Δc_Cu+                   │
│                                                             │
│  → Or use measured k_p directly from flat-film data         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 3: Compute K and φ  (Eqs. 26, 27)                     │
│                                                             │
│  K = k_out / k_in                                           │
│  φ = Z / (1 + K)                                           │
│                                                             │
│  → φ=1: VC model (core shrinks)                             │
│  → φ=0: NKE model (void forms)                              │
│  → 0<φ<1: General model                                     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 4: Express boundary positions as f(δ)  (Eqs. 22, 23) │
│                                                             │
│  a_1³ = a_0³(1 − φδ)                                       │
│  a_2³ = a_0³(1 − φδ + Zδ)                                  │
│  (a_v^int)³ = a_0³(1 − φ)δ      (void radius, Eq. 24)      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 5: Evaluate steady-state ionic flux  (Eq. 6)          │
│                                                             │
│  J_i = −4π D*_i (c_{i,2}−c_{i,1}) · a_1·a_2/(a_2−a_1)     │
│                                                             │
│  → Flux decreases as shell thickens → parabolic kinetics    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 6: Equate flux to Cu mass balance  (Eqs. 6, 9)        │
│                                                             │
│  J_Cu+ = (4/3)(ρ_Cu/FW_Cu)πa_0³ · dδ/dt                   │
│                                                             │
│  → Substituting a_1(δ), a_2(δ) from Step 4                 │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 7: Integrate → General Rate Law  (Eq. 32)             │
│                                                             │
│  g(δ, φ, Z) = [(Z−φ)/Z] · (k_p/a_0²) · t                  │
│                                                             │
│  where:                                                     │
│  g = {Z − φ[1−(φ−Z)δ]^(2/3) − (Z−φ)(1−φδ)^(2/3)}         │
│       ─────────────────────────────────────────             │
│                    2(Z−φ)φ                                  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  OUTPUT: δ(t) for given a_0, φ, k_p                         │
│                                                             │
│  → a_1(t), a_2(t), a_v^int(t)  via Eqs. 22–24              │
│  → Void fraction in core:                                   │
│     δ' = (1−φ)δ / (1−φδ)       (Eq. 59 in paper)          │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Special Cases at a Glance

| Condition | $\phi$ | $K$ | Active boundary | Void? | Rate law |
|---|---|---|---|---|---|
| Only O²⁻ diffuses inward | 1 | 0 | Interface I (a₁) | No | Eq. 12 (VC) |
| Only Cu⁺ diffuses outward | 0 | ∞ | Interface II (a₂) | Yes | Eq. 17 (NKE) |
| Both diffuse equally | Z/2 | 1 | Both | Partial | Eq. 25 |
| General case | Z/(1+K) | K | Both | Partial | Eq. 32 |

> **Note:** At the same rate constant, the NKE model predicts conversion up to **4× faster** than the VC model, because the outer boundary (a₂) is always larger than the inner boundary (a₁), giving a geometrically larger diffusion cross-section.

---

## 8. Case Study: Copper Nanoparticle Oxidation (Cu → Cu₂O)

This case study walks through the complete model for a **90 nm diameter Cu nanoparticle** oxidizing in air at **140 °C**, as reported experimentally by Susman et al.

---

### 8.1 Material Parameters

| Parameter | Symbol | Value | Source |
|---|---|---|---|
| Initial diameter | $2a_0$ | 90 nm → $a_0 = 45$ nm | Experimental |
| Formula weight of Cu | $\text{FW}_{\text{Cu}^0}$ | 63.55 g/mol | — |
| Formula weight of Cu₂O | $\text{FW}_\text{Ox}$ | 143.09 g/mol | — |
| Density of Cu | $\rho_{\text{Cu}^0}$ | 8960 kg/m³ | Bulk |
| Density of Cu₂O | $\rho_\text{Ox}$ | 6000 kg/m³ | Bulk |
| Stoichiometric coefficient (Cu⁺) | $\eta$ | 2 | Cu₂O formula |
| Stoichiometric coefficient (O²⁻) | $\eta'$ | 1 | Cu₂O formula |
| Parabolic rate constant at 140 °C | $k_p$ | 10 nm²/min | Fit to experimental LSPR data |
| Best-fit $\phi$ | $\phi$ | 0.5 | Fit to experimental LSPR data |

---

### 8.2 Step-by-Step Calculation

#### Step 1: Pilling–Bedworth Ratio (Eq. 3)

$$Z = \frac{1}{\eta}\frac{\text{FW}_\text{Ox}\,\rho_{\text{Cu}^0}}{\text{FW}_{\text{Cu}^0}\,\rho_\text{Ox}} = \frac{1}{2}\cdot\frac{143.09 \times 8960}{63.55 \times 6000} = \frac{1}{2}\cdot\frac{1,282,086}{381,300} \approx \mathbf{1.68}$$

Since $Z > 1$, the Cu₂O shell expands outward and the particle grows during oxidation.

---

#### Step 2: Rate Constants (Eqs. 13, 18, 30, 31)

The paper uses $k_p = 10$ nm² min⁻¹ (fitted) and $\phi = 0.5$ (fitted). From Eq. 31:

$$k_\text{out} = k_p \cdot \frac{Z - \phi}{Z} = 10 \cdot \frac{1.68 - 0.5}{1.68} = 10 \cdot \frac{1.18}{1.68} \approx 7 \text{ nm}^2\text{/min}$$

From Eq. 30:

$$k_\text{in} = \frac{\phi}{Z - \phi}\,k_\text{out} = \frac{0.5}{1.18} \times 7 \approx 2.97 \text{ nm}^2\text{/min}$$

Check: $k_p = k_\text{in} + k_\text{out} = 2.97 + 7 \approx 10$ ✓

---

#### Step 3: Growth Rate Ratio and $\phi$ Verification (Eqs. 26, 27)

$$K = \frac{k_\text{out}}{k_\text{in}} = \frac{7}{2.97} \approx 2.36$$

$$\phi = \frac{Z}{1+K} = \frac{1.68}{1 + 2.36} = \frac{1.68}{3.36} = 0.5 \checkmark$$

Since $\phi = 0.5 < Z/2 = 0.84$, vacancies flow **inward** → an internal void forms (NKE active).

---

#### Step 4: Boundary Positions as Functions of $\delta$ (Eqs. 22–24)

With $a_0 = 45$ nm, $\phi = 0.5$, $Z = 1.68$:

$$a_1 = 45\,(1 - 0.5\delta)^{1/3} \text{ nm}$$

$$a_2 = 45\,(1 - 0.5\delta + 1.68\delta)^{1/3} = 45\,(1 + 1.18\delta)^{1/3} \text{ nm}$$

$$(a_v^\text{int}) = 45\,(0.5\delta)^{1/3} \text{ nm}$$

At key conversion fractions:

| $\delta$ | $a_1$ (nm) | $a_2$ (nm) | $a_v^\text{int}$ (nm) | Interpretation |
|---|---|---|---|---|
| 0 | 45.0 | 45.0 | 0 | Pure Cu, no shell |
| 0.2 | 43.5 | 47.6 | 20.5 | Thin shell, small void |
| 0.4 | 41.9 | 49.9 | 25.8 | Shell thickening, void growing |
| 0.6 | 40.1 | 52.0 | 29.4 | Substantial void |
| 0.8 | 38.0 | 53.8 | 32.2 | Large void, thin Cu core |
| 1.0 | 35.7 | 55.5 | 34.7 | Fully converted, hollow shell |

---

#### Step 5: Ionic Flux (Eq. 6)

At $\delta = 0.4$ (as an example), $a_1 = 41.9$ nm, $a_2 = 49.9$ nm:

$$J_{\text{Cu}^+} \propto -4\pi D^*_{\text{Cu}^+}\,\Delta c_{\text{Cu}^+} \cdot \frac{41.9 \times 49.9}{49.9 - 41.9} = -4\pi D^*_{\text{Cu}^+}\,\Delta c_{\text{Cu}^+} \cdot \frac{2090.8}{8.0} \approx -4\pi D^*_{\text{Cu}^+}\,\Delta c_{\text{Cu}^+} \cdot 261 \text{ nm}$$

As $\delta$ increases, the shell thickens ($a_2 - a_1$ grows), so the geometric factor $a_1 a_2/(a_2-a_1)$ decreases and the flux slows — this is the origin of the **parabolic (self-limiting) behavior**.

---

#### Step 6 & 7: Solving the General Rate Law for $\delta(t)$ (Eq. 32)

The left-hand side $g(\delta)$ is evaluated numerically. With $\phi = 0.5$, $Z = 1.68$:

$$g(\delta) = \frac{1.68 - 0.5\left[1 - 1.18\delta\right]^{2/3} - 1.18\,(1-0.5\delta)^{2/3}}{2\,(1.18)\,(0.5)}$$

The right-hand side:

$$\frac{Z-\phi}{Z}\cdot\frac{k_p}{a_0^2}\cdot t = \frac{1.18}{1.68}\cdot\frac{10}{45^2}\cdot t = \frac{1.18}{1.68}\cdot\frac{10}{2025}\cdot t \approx 3.47 \times 10^{-3}\cdot t \text{ min}^{-1}$$

Selected values of $g(\delta)$ and corresponding times:

| $\delta$ | $g(\delta)$ | $t$ (min) |
|---|---|---|
| 0.1 | 0.00127 | 0.37 |
| 0.2 | 0.00514 | 1.48 |
| 0.4 | 0.02097 | 6.05 |
| 0.6 | 0.04883 | 14.1 |
| 0.8 | 0.09151 | 26.4 |
| 1.0 | 0.15323 | 44.2 |

The **extinction maximum** occurs experimentally at ~40% conversion ($\delta \approx 0.4$), corresponding to approximately **6 minutes** at 140 °C for a 90 nm particle — consistent with experimental LSPR observations.

---

### 8.3 Physical Interpretation of $\phi = 0.5$

With $\phi = 0.5$ for Cu → Cu₂O at 140 °C:

- Cu⁺ diffuses outward **~2.4× faster** than O²⁻ diffuses inward ($K \approx 2.36$)
- ~50% of core volume reduction comes from actual metal consumption; the other 50% accumulates as **internal vacancies**
- Vacancies flow **inward** ($\phi < Z/2 = 0.84$), progressively hollowing the core
- The oxidation front sits at $a_\text{of} = a_0 = 45$ nm (no Kirkendall shift)
- Outward oxide growth accounts for $K/(1+K) \approx 70\%$ of total oxide volume; inward growth accounts for $\approx 30\%$

---

### 8.4 Observed vs. Predicted Parabolic Rate

| Source | $k_p$ at 140 °C |
|---|---|
| This model (fitted to LSPR data) | ~10 nm² min⁻¹ |
| Bulk Cu extrapolated from Zhu et al. (700–1050 °C) | ~1.5 × 10⁻⁵ nm² min⁻¹ |
| Thin film data (Matsumura et al.) | Consistent with ~10 nm² min⁻¹ |

The Cu NP oxidation rate is approximately **6 orders of magnitude faster** than bulk Cu at the same temperature. This enhancement is likely due to the large surface-to-volume ratio and the nanoscale geometry of the particles, though the precise mechanism is not yet fully understood.
