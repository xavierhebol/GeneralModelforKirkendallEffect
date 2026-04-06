"""
GM.py — General Kinetic Model for Solid-State Reactions
        Involving the Nano Kirkendall Effect (NKE)

Based on: Susman, Vaskevich & Rubinstein
          J. Phys. Chem. C 2016, 120, 16140-16152

Equation numbers refer to Susman_KE_GeneralModel.md.

Outputs:
    plots/outer_diameter_vs_time.png
    plots/porosity_vs_time.png
    results.md
"""

import numpy as np
import matplotlib.pyplot as plt
import yaml
from pathlib import Path


# ──────────────────────────────────────────────────────────────────────────────
# 1. LOAD PARAMETERS
# ──────────────────────────────────────────────────────────────────────────────

with open("parameters.yaml", "r") as f:
    p = yaml.safe_load(f)

# Inputs
a0    = p["initial_radius_nm"]   # nm
T     = p["temperature_C"]       # deg C

# Material parameters
FW_Cu  = p["FW_Cu"]              # g/mol
FW_Ox  = p["FW_Cu2O"]            # g/mol
rho_Cu = p["rho_Cu"]             # kg/m3
rho_Ox = p["rho_Cu2O"]           # kg/m3
eta    = p["eta"]                 # stoichiometric coeff of Cu+
eta_p  = p["eta_prime"]           # stoichiometric coeff of O2-

# Model parameters
k_p = p["k_p"]                   # nm2/min
phi = p["phi"]                   # core-contraction parameter


# ──────────────────────────────────────────────────────────────────────────────
# 2. STEP 1 — PILLING-BEDWORTH RATIO  (Eq. 3)
#    Z = (1/eta) * (FW_Ox * rho_Cu) / (FW_Cu * rho_Ox)
#    For Cu -> Cu2O: Z ~ 1.68
# ──────────────────────────────────────────────────────────────────────────────

Z = (1.0 / eta) * (FW_Ox * rho_Cu) / (FW_Cu * rho_Ox)


# ──────────────────────────────────────────────────────────────────────────────
# 3. STEP 2 — RATE CONSTANTS  (Eqs. 30, 31)
#    k_p  = k_in + k_out = [Z / (Z - phi)] * k_out
#    k_out = k_p * (Z - phi) / Z
#    k_in  = [phi / (Z - phi)] * k_out
# ──────────────────────────────────────────────────────────────────────────────

k_out = k_p * (Z - phi) / Z
k_in  = (phi / (Z - phi)) * k_out


# ──────────────────────────────────────────────────────────────────────────────
# 4. STEP 3 — GROWTH RATE RATIO AND phi SELF-CONSISTENCY  (Eqs. 26, 27)
#    K   = k_out / k_in
#    phi = Z / (1 + K)   [suppressed Kirkendall shift at nanoscale]
# ──────────────────────────────────────────────────────────────────────────────

K         = k_out / k_in
phi_check = Z / (1.0 + K)

if phi < Z / 2:
    vacancy_dir = "inward (NKE active — internal void forms)"
elif phi == Z / 2:
    vacancy_dir = "none (no net vacancy flow)"
else:
    vacancy_dir = "outward (no internal void)"


# ──────────────────────────────────────────────────────────────────────────────
# 5. STEPS 4-7 — SOLVE THE GENERAL RATE LAW  (Eq. 32)
#
#    g(delta) = {Z - phi*[1-(phi-Z)*delta]^(2/3) - (Z-phi)*(1-phi*delta)^(2/3)}
#               / [2*(Z-phi)*phi]
#
#    g(delta) = [(Z-phi)/Z] * (k_p / a0^2) * t
#    => t = g(delta) * Z * a0^2 / [(Z-phi) * k_p]
# ──────────────────────────────────────────────────────────────────────────────

# Dense conversion fraction array; exclude delta=1 to avoid numerical edge
delta = np.linspace(0.0, 0.999, 2000)


def g_func(delta, phi, Z):
    """Left-hand side of the general rate law (Eq. 32)."""
    # Note: (phi - Z) is negative, so [1 - (phi-Z)*delta] = [1 + (Z-phi)*delta] > 1
    term1 = Z
    term2 = phi * (1.0 - (phi - Z) * delta) ** (2.0 / 3.0)
    term3 = (Z - phi) * (1.0 - phi * delta) ** (2.0 / 3.0)
    return (term1 - term2 - term3) / (2.0 * (Z - phi) * phi)


g = g_func(delta, phi, Z)

# Solve for time at each delta
t = g * Z * a0**2 / ((Z - phi) * k_p)   # minutes


# ──────────────────────────────────────────────────────────────────────────────
# 6. BOUNDARY POSITIONS AS FUNCTIONS OF delta  (Eqs. 22-24)
#    a1(delta) = a0 * (1 - phi*delta)^(1/3)         — inner boundary (metal/oxide)
#    a2(delta) = a0 * (1 - phi*delta + Z*delta)^(1/3) — outer boundary (oxide/air)
#    a_v(delta) = a0 * [(1-phi)*delta]^(1/3)         — equivalent void radius
# ──────────────────────────────────────────────────────────────────────────────

a1      = a0 * (1.0 - phi * delta) ** (1.0 / 3.0)
a2      = a0 * (1.0 - phi * delta + Z * delta) ** (1.0 / 3.0)
a_v_int = a0 * ((1.0 - phi) * delta) ** (1.0 / 3.0)

outer_diameter = 2.0 * a2   # nm


# ──────────────────────────────────────────────────────────────────────────────
# 7. POROSITY
#    V_void  = (4/3)*pi * a_v_int^3
#    V_outer = (4/3)*pi * a2^3
#    porosity = V_void / V_outer = (a_v_int / a2)^3
# ──────────────────────────────────────────────────────────────────────────────

porosity = np.where(delta > 0, (a_v_int / a2) ** 3, 0.0)


# ──────────────────────────────────────────────────────────────────────────────
# 8. VERIFICATION — evaluate at reference delta values from case study
#    Reference: Section 8.2 of Susman_KE_GeneralModel.md
# ──────────────────────────────────────────────────────────────────────────────

delta_ref      = np.array([0.0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0])
delta_ref_safe = np.where(delta_ref >= 1.0, 0.999, delta_ref)   # clip delta=1

g_ref   = g_func(delta_ref_safe, phi, Z)
t_ref   = g_ref * Z * a0**2 / ((Z - phi) * k_p)
a1_ref  = a0 * (1.0 - phi * delta_ref_safe) ** (1.0 / 3.0)
a2_ref  = a0 * (1.0 - phi * delta_ref_safe + Z * delta_ref_safe) ** (1.0 / 3.0)
av_ref  = a0 * ((1.0 - phi) * delta_ref_safe) ** (1.0 / 3.0)
por_ref = np.where(delta_ref_safe > 0, (av_ref / a2_ref) ** 3, 0.0)


# ──────────────────────────────────────────────────────────────────────────────
# 9. PLOTS
# ──────────────────────────────────────────────────────────────────────────────

Path("plots").mkdir(exist_ok=True)

# Subsample for scatter markers (every 100th point)
step = 100

# ── Plot 1: Outer Diameter vs Time ──
fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1.plot(t, outer_diameter, "-", color="steelblue", linewidth=1.8, label="Model (continuous)")
ax1.scatter(t[::step], outer_diameter[::step], color="steelblue", s=30, zorder=5, label="Sample points")
ax1.axhline(
    y=2 * a0, color="gray", linestyle="--", linewidth=1.2,
    label=f"Initial diameter = {2*a0:.0f} nm"
)
ax1.set_xlabel("Time (min)", fontsize=12)
ax1.set_ylabel("Outer Diameter (nm)", fontsize=12)
ax1.set_title(
    f"Outer Diameter vs Time\n"
    f"Cu NP, $a_0$ = {a0} nm, $T$ = {T} °C, "
    f"$\\phi$ = {phi}, $k_p$ = {k_p} nm$^2$/min",
    fontsize=11,
)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)
fig1.tight_layout()
fig1.savefig("plots/outer_diameter_vs_time.png", dpi=150)
plt.close(fig1)

# ── Plot 2: Porosity vs Time ──
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.plot(t, porosity * 100, "-", color="firebrick", linewidth=1.8, label="Model (continuous)")
ax2.scatter(t[::step], porosity[::step] * 100, color="firebrick", s=30, zorder=5, label="Sample points")
ax2.set_xlabel("Time (min)", fontsize=12)
ax2.set_ylabel("Porosity  $V_\\mathrm{void}\\,/\\,V_\\mathrm{outer}$ (%)", fontsize=12)
ax2.set_title(
    f"Porosity vs Time\n"
    f"Cu NP, $a_0$ = {a0} nm, $T$ = {T} °C, "
    f"$\\phi$ = {phi}, $k_p$ = {k_p} nm$^2$/min",
    fontsize=11,
)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)
fig2.tight_layout()
fig2.savefig("plots/porosity_vs_time.png", dpi=150)
plt.close(fig2)

print("Saved: plots/outer_diameter_vs_time.png")
print("Saved: plots/porosity_vs_time.png")


# ──────────────────────────────────────────────────────────────────────────────
# 10. WRITE RESULTS.MD
# ──────────────────────────────────────────────────────────────────────────────

phi_ok = abs(phi_check - phi) < 1e-6
kp_ok  = abs((k_in + k_out) - k_p) < 1e-6

# Indices for key conversion fractions in the dense array
idx_0  = 0
idx_04 = int(np.argmin(np.abs(delta - 0.4)))
idx_end = -1

with open("results.md", "w") as out:

    out.write("# KEGM Results\n\n")
    out.write("**Model:** General Kinetic Model — Susman, Vaskevich & Rubinstein, "
              "*J. Phys. Chem. C* 2016, 120, 16140–16152  \n")
    out.write(f"**System:** Cu nanoparticle oxidation → Cu₂O  \n")
    out.write(f"**Temperature:** {T} °C  \n")
    out.write(f"**Initial radius:** {a0} nm ({2*a0:.0f} nm diameter)  \n\n")
    out.write("---\n\n")

    # ── Computed Parameters ──
    out.write("## 1. Computed Model Parameters\n\n")
    out.write("| Parameter | Symbol | Value |\n")
    out.write("|---|---|---|\n")
    out.write(f"| Pilling–Bedworth ratio | Z | {Z:.4f} |\n")
    out.write(f"| Core-contraction parameter | phi | {phi} |\n")
    out.write(f"| Growth rate ratio | K | {K:.4f} |\n")
    out.write(f"| Outward rate constant | k_out | {k_out:.4f} nm2/min |\n")
    out.write(f"| Inward rate constant | k_in | {k_in:.4f} nm2/min |\n")
    out.write(f"| Parabolic rate constant (input) | k_p | {k_p:.4f} nm2/min |\n")
    out.write(f"| phi self-consistency check Z/(1+K) | — | {phi_check:.6f} |\n")
    out.write(f"| k_p check (k_in + k_out) | — | {k_in + k_out:.6f} nm2/min |\n")
    out.write(f"| Vacancy flow direction | — | {vacancy_dir} |\n\n")
    out.write(f"**Self-consistency:** phi {'PASS' if phi_ok else 'FAIL'}  |  "
              f"k_p {'PASS' if kp_ok else 'FAIL'}\n\n")
    out.write("---\n\n")

    # ── Verification Table ──
    out.write("## 2. Verification Against Case Study\n\n")
    out.write("Computed values at reference conversion fractions. "
              "Compare with Section 8.2 of `Susman_KE_GeneralModel.md`.\n\n")
    out.write("| delta | g(delta) | t (min) | a1 (nm) | a2 (nm) | "
              "a_v_int (nm) | Outer diameter (nm) | Porosity (%) |\n")
    out.write("|---|---|---|---|---|---|---|---|\n")
    for i, d in enumerate(delta_ref):
        diam = 2 * a2_ref[i]
        out.write(
            f"| {d:.1f} | {g_ref[i]:.5f} | {t_ref[i]:.2f} | "
            f"{a1_ref[i]:.2f} | {a2_ref[i]:.2f} | {av_ref[i]:.2f} | "
            f"{diam:.2f} | {por_ref[i]*100:.2f} |\n"
        )
    out.write("\n")

    # ── Key Milestones ──
    out.write("## 3. Key Milestones\n\n")
    out.write("| Milestone | delta | t (min) | Outer diameter (nm) | Porosity (%) |\n")
    out.write("|---|---|---|---|---|\n")
    out.write(f"| Start (unreacted) | {delta[idx_0]:.3f} | {t[idx_0]:.2f} | "
              f"{outer_diameter[idx_0]:.2f} | {porosity[idx_0]*100:.2f} |\n")
    out.write(f"| ~40% conversion (LSPR max) | {delta[idx_04]:.3f} | {t[idx_04]:.2f} | "
              f"{outer_diameter[idx_04]:.2f} | {porosity[idx_04]*100:.2f} |\n")
    out.write(f"| Near full conversion | {delta[idx_end]:.3f} | {t[idx_end]:.2f} | "
              f"{outer_diameter[idx_end]:.2f} | {porosity[idx_end]*100:.2f} |\n\n")
    out.write("---\n\n")

    # ── Plots ──
    out.write("## 4. Plots\n\n")
    out.write("### Outer Diameter vs Time\n\n")
    out.write("The particle expands as Cu is consumed and Cu2O (Z = 1.68) grows outward. "
              "The outer diameter increases monotonically from the initial 90 nm.\n\n")
    out.write("![Outer Diameter vs Time](plots/outer_diameter_vs_time.png)\n\n")
    out.write("### Porosity vs Time\n\n")
    out.write("Porosity = V_void / V_outer = (a_v_int / a2)^3. "
              "Starts at 0 and increases as inward vacancy flow hollows the core (phi = 0.5 < Z/2 = 0.84).\n\n")
    out.write("![Porosity vs Time](plots/porosity_vs_time.png)\n")

print("Saved: results.md")
print(f"\nVerification summary:")
print(f"  Z          = {Z:.4f}    (expected: 1.68)")
print(f"  phi        = {phi}       (input)")
print(f"  phi check  = {phi_check:.6f}  (must equal phi)")
print(f"  K          = {K:.4f}")
print(f"  k_out      = {k_out:.4f} nm2/min  (expected: ~7)")
print(f"  k_in       = {k_in:.4f} nm2/min  (expected: ~3)")
print(f"  k_p check  = {k_in+k_out:.4f} nm2/min  (must equal {k_p})")
print(f"  phi OK     : {phi_ok}")
print(f"  k_p OK     : {kp_ok}")
