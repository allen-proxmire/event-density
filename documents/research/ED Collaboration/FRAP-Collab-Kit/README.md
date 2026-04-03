# FRAP Collaboration Kit

## Purpose

This folder contains everything needed to approach an experimental collaborator for the BSA-FRAP void-spreading experiment — the single most important open test in the Event Density research programme.

## The Experiment in Brief

We have a theoretical prediction for how a photobleached spot recovers in concentrated protein solutions. Standard diffusion theory predicts the recovery front expands as R(t) ~ t^0.5. Our theory predicts R(t) ~ t^0.16 at high BSA concentration — three times slower. A standard confocal FRAP experiment at high protein concentration can distinguish these. The experiment takes one afternoon. We provide the protocol and all analysis; the collaborator runs the microscope and sends us the images.

## The Prediction

- **Material:** BSA-FITC at 200-350 mg/mL
- **Geometry:** 2D FRAP (confocal photobleaching + recovery imaging)
- **Predicted front exponent:** alpha_R = 0.160 +/- 0.009
- **Fickian reference:** alpha_R = 0.50
- **Discriminating power:** A measurement with 20% precision distinguishes the two

## Why FRAP?

We have shown computationally that standard concentration-spreading experiments cannot test our prediction. The correct geometry requires a *void* (low-density region) expanding into a *dense background*. FRAP provides exactly this: the bleached spot is the void, the concentrated unbleached solution is the background.

## What We Need from a Collaborator

1. A confocal microscope with FRAP module
2. BSA-FITC conjugate at high concentration (200-350 mg/mL)
3. Temperature control (+/- 0.5C)
4. Willingness to run 4-6 hours of standard FRAP imaging
5. Raw TIFF stacks sent to us for analysis

## How to Use This Folder

| Document | When to use it |
|----------|----------------|
| `One_Page_Pitch.md` | First contact — attach to an email or hand out at a conference |
| `Collaborator_Email_Template.md` | Cold email to a potential collaborator |
| `Lab_Identification_Guide.md` | Before reaching out — identify the right labs |
| `Conversation_Script.md` | Preparing for a first meeting or Zoom call |
| `FRAP_Experiment_Summary.md` | When they ask "what exactly do I need to do?" |
| `What_We_Provide_vs_What_They_Do.md` | When they ask "what's the time commitment?" |

## Full Technical Details

The complete experimental design is in:
`documents/research/ED Physics/ED-Phys-12/ED-Phys-12_FRAP_CollaborationPlan.md`

The synthetic validation (proof that the pipeline works) is in:
`outputs/ED-Phys-11/`
