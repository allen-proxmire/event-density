# ED Front Door

**This folder is the entry point for anyone encountering Event Density for the first time.**

If you have 3 minutes, open the notebook. If you have 30 seconds, read the 1-pager.

## Contents

| File | Purpose | Audience |
|------|---------|----------|
| **[ED_minimal_demo.ipynb](ED_minimal_demo.ipynb)** | Run the full ED pipeline and see results | Everyone |
| [ED_What_It_Does_1pager.md](ED_What_It_Does_1pager.md) | One-page overview of the framework | Researchers |
| [ED_Falsifiable_Prediction.md](ED_Falsifiable_Prediction.md) | The strongest testable prediction | Observers, experimentalists |
| [ED_Targeted_Hooks.md](ED_Targeted_Hooks.md) | 2-3 sentence hooks for 8 different audiences | Outreach |
| [ED_3min_demo_script.md](ED_3min_demo_script.md) | Script for a video walkthrough | Video production |

## Run the Notebook

**In Google Colab (zero setup):**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Allen-Proxmire/Event-Density/blob/main/ED_FrontDoor/ED_minimal_demo.ipynb)

**Locally:**

```bash
git clone https://github.com/Allen-Proxmire/Event-Density.git
cd Event-Density
pip install -r requirements.txt
jupyter notebook ED_FrontDoor/ED_minimal_demo.ipynb
```

## What You Will See

1. A 2D ED simulation running with canonical parameters
2. The density field evolving from a cosine perturbation toward equilibrium
3. All nine architectural laws verified against the simulation
4. The penalty channel reproducing RC-circuit decay at 0.00% error
5. The participation channel reproducing telegraph oscillation at 0.00% error
6. Monotone energy decay with dissipation channels summing exactly to 1

None of these behaviours were programmed in. They are structural consequences of the constitutive architecture.
