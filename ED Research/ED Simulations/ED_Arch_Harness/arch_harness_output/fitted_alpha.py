import json
import numpy as np

# Load your law-surface results
with open("law_surface_engine_results.json", "r") as f:
    data = json.load(f)

records = data["records"]

print(records[0].keys())
exit()

# Containers for regression
xs = []
ys = []

for rec in records:
    # Only outward sheet
    if rec["gamma"] != -1:
        continue

    chi_emp = float(rec["chi_emp"])
    chi_pred = float(rec["chi_pred"])

    # Δχ
    delta_chi = chi_emp - chi_pred

    # Extract radii
    r_initial = float(rec["r_initial"])
    r_final = float(rec["r_final"])

    # Stretch factor S
    S = (r_final - r_initial) / r_initial

    # Regression variables:
    # x = S * chi_pred
    # y = Δχ
    xs.append(S * chi_pred)
    ys.append(delta_chi)

xs = np.array(xs)
ys = np.array(ys)

# Closed-form least squares slope:
# alpha = (x·y) / (x·x)

alpha = float(np.dot(xs, ys) / np.dot(xs, xs))

print("Fitted alpha:", alpha)
