# Task List — KEGM Implementation

**Goal:** Implement the General Kinetic Model (Susman et al. 2016) for solid-state nanoparticle
oxidation involving the nano Kirkendall Effect. Solve for boundary positions, outer diameter,
and porosity as functions of time. Verify against the Cu case study in `Susman_KE_GeneralModel.md`.

---

## Project Structure

```
KE_GeneralModel/
├── CLAUDE.md                        # Claude Code guidance
├── Susman_KE_GeneralModel.md        # Model reference document
├── parameters.yaml                  # All model inputs and parameters
├── GM.py                            # Main solver script
├── task.md                          # This file
├── results.md                       # Generated output — equations results + verification
└── plots/
    ├── outer_diameter_vs_time.png   # Generated plot
    └── porosity_vs_time.png         # Generated plot
```

---

## Tasks

### Setup
- [x] Create `parameters.yaml` with initial radius, temperature, material parameters, and model parameters
- [x] Create `plots/` output directory (created by KEGM.py on first run)

### Implementation — KEGM.py
- [x] **Step 1** — Load parameters from `parameters.yaml`
- [x] **Step 2** — Compute Pilling–Bedworth ratio $Z$ (Eq. 3)
- [x] **Step 3** — Compute rate constants $k_\text{out}$, $k_\text{in}$ from $k_p$ and $\phi$ (Eqs. 30, 31)
- [x] **Step 4** — Compute growth rate ratio $K$ and verify $\phi$ self-consistency (Eqs. 26, 27)
- [x] **Step 5** — Define $g(\delta)$ function — left-hand side of the general rate law (Eq. 32)
- [x] **Step 6** — Solve for time $t(\delta)$ from the rate law over $\delta \in [0, 1)$
- [x] **Step 7** — Compute boundary positions $a_1(\delta)$, $a_2(\delta)$, $a_v^\text{int}(\delta)$ (Eqs. 22–24)
- [x] **Step 8** — Compute outer diameter $= 2a_2$ as a function of time
- [x] **Step 9** — Compute porosity $= V_\text{void} / V_\text{outer} = (a_v^\text{int}/a_2)^3$ as a function of time

### Verification
- [x] Evaluate $g(\delta)$, $t$, $a_1$, $a_2$ at reference $\delta$ values from the case study
- [ ] **Run GM.py** and confirm computed values match the equations in `Susman_KE_GeneralModel.md`
- [ ] Confirm $\phi$ self-consistency check passes ($\phi = Z/(1+K)$)
- [ ] Confirm outer diameter starts at $2a_0 = 90$ nm and increases monotonically
- [ ] Confirm porosity starts at 0 and increases monotonically
- [ ] Confirm $k_p = k_\text{in} + k_\text{out}$

### Outputs
- [ ] **Run GM.py** to generate `plots/outer_diameter_vs_time.png`
- [ ] **Run GM.py** to generate `plots/porosity_vs_time.png`
- [ ] **Run GM.py** to generate `results.md` with computed parameters and verification table

---

## How to Run

```bash
conda activate usam
```
```bash
python GM.py
```
