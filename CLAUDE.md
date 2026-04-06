# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Context

The repository is an implementation of the general model from the following article

"A General Kinetic-Optical Model for Solid-State Reactions Involving the Nano Kirkendall Effect. The Case of Copper Nanoparticle Oxidation" by Susman et al (2016) - The Journal of Physical Chemistry — source material on solid-state reaction kinetics and the nano-Kirkendall effect applied to copper nanoparticles.

## Principles

- **First principles**: Understand the physics before writing code. Every equation and boundary condition must have a clear physical basis.
- **Occam's razor**: The simplest correct solution wins. Do not add complexity unless it is proven necessary.
- **Consistency, simplicity, and maintainability over features**: Clean, readable code is more valuable than new functionality. Do not sacrifice code quality to ship faster. Refactoring to keep things clean is always justified.

## Code Conventions

- Code should be well-documented with comments.
- The workflow for the code should be apparent from grouping codes for similar functions together