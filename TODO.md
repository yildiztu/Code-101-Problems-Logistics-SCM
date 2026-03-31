# TODO — 101 Problems folder structure and `.ipynb` generation

## Source of truth (must not change)
- **Source folder**: `D:\Users\Turkay\Desktop\Books\The Logistics & Supply Chain Problem-Solving Playbook (101 Problems Edition)\___LaTeX\___responses-complete\responses-complete-png`
- This folder contains `line1.tex` … `line101.tex`.
- For each problem, the **Python code and Tier information** live inside the corresponding `.tex` file (problem narrative + solution code blocks + Tier count, etc.).

## End goal (output structure)
- Create **101 problem folders** organized into two main categories:
  - `Part I - The Port & Container Terminal (Problems 1-46)/` - Contains problems 1-46
  - `Part II - The End-to-End Supply Chain (Problems 47-101)/` - Contains problems 47-101
- Inside each Part, group problems under TOC-based subfolders (do not use the word "Chapter"):
  - Part I:
    - `A. Foundations of Terminal Operations (The Building Blocks)/` (Problems 1–6)
    - `B. Core Quay-Side Operations (The Ship-to-Shore Interface)/` (Problems 7–15)
    - `C. Core Yard & Land-Side Operations (The Heart of the Terminal)/` (Problems 16–26)
    - `D. Integrated Tactical & Pre-Planning Problems (Connecting the Silos)/` (Problems 27–34)
    - `E. Strategic Design & Long-Term Investment (Shaping the Future)/` (Problems 35–46)
  - Part II:
    - `A. Foundational Analytics & Inventory Control (The Language of Supply Chain)/` (Problems 47–58)
    - `B. Warehouse & Fulfillment Center Operations (Inside the Four Walls)/` (Problems 59–68)
    - `C. Transportation, Routing & Freight Management (The Physical Internet)/` (Problems 69–81)
    - `D. Strategic Network Design & Sourcing (The Blueprint of the Business)/` (Problems 82–91)
    - `E. Integrated, Resilient, & Modern Supply Chains (The Frontier)/` (Problems 92–101)
- Each problem folder name must follow:
  - `NN. <Problem Title>` (two-digit format for 1-46)
  - `NNN. <Problem Title>` (three-digit format for 47-101)
  - Example: `01. The Single Crane Lift Sequence Problem`
  - Example: `047. The Demand Forecasting Problem`
  - Example: `100. The Advanced Supply Chain Analytics Problem`
- Inside each problem folder, generate **one Jupyter notebook per Tier**, based on the content in the `.tex`.
  - Example: Problem 1 `line1.tex` → **4 Tiers** → **4 `.ipynb` files**

## Non-negotiable notebook content requirements
- **[R1] No black-box / proprietary packages**
  - Notebooks must rely on **well-known Python packages** that are commonly used in the Python ecosystem.
  - Prefer **open-source packages**.
  - Avoid company-specific, paid, closed-source, or “black-box” dependencies.
  - If a `.tex` code block references a non-compliant package, replace it with an open-source alternative (and explain the substitution in Markdown).
- **[R2] Tier notebooks must be highly explanatory**
  - Each Tier notebook must include clear, step-by-step **English** explanations.
  - Every major block of code must be explained: purpose, inputs, outputs, assumptions, and interpretation of results.
  - Use Markdown sections to make the notebook readable (not just code dumps).
- **[R2.1] Code must be beginner-friendly and heavily commented**
  - Code cells must include plentiful inline comments that explain:
    - What each section of code is doing
    - Why that step is needed (intuition)
    - What the key variables represent
  - A Python beginner should be able to follow the notebook by reading the comments.
- **[R2.2] Each Tier (k>=2) must justify itself vs previous Tier(s)**
  - Tier 1 should explain the base approach.
  - For Tier 2 and higher, include an explicit comparison section that answers:
    - Why this Tier exists (what limitation of earlier Tiers it addresses)
    - Advantages / disadvantages vs Tier 1..(k-1)
    - When you should prefer this Tier in practice
  - This comparison can be a final Markdown section at the end of the notebook.
- **[R2.3] Pedagogical outputs must make the Tier’s key idea visible**
  - Each Tier notebook must include at least one **explicit output** (table/print/plot) that demonstrates the Tier’s core concept.
  - If the base example can *hide* the concept (e.g., no feasible dual lift, fairness constraint trivially satisfied, GA happens to match optimum, etc.), add a small **what-if / sensitivity** experiment so the concept becomes observable.
  - The what-if section must:
    - Keep the original example intact (do not silently change it)
    - Clearly label which parameter(s) are varied
    - Summarize results in a small table and interpret them in 2–5 sentences
- **[R2.4] Include a quantitative “quality gap” check when feasible (small instances)**
  - If the instance is small enough, compute an **exact optimum** (Tier 1 style) and report:
    - optimum metric value
    - algorithm’s metric value (heuristic/GA/RL)
    - gap
  - If exact optimum is not feasible, report a principled baseline and explain limitations.
- **[R3] Notebooks must be derived from `lineX.tex` (but must not mention it in the notebook text)**
  - The `.tex` file is the **single source of truth** for each problem.
  - However, the generated `.ipynb` should **not mention** `lineX.tex` directly in the visible notebook text. (The `.tex` remains the source of truth for generation, but notebooks should read like standalone teaching material.)
  - Avoid introducing new scenarios that are unrelated to the `.tex` narrative.
- **[R4] Use the source examples (e.g., “Concrete Example”) to drive notebook outputs**
  - Many Tiers include example sections such as **“Concrete Example”** (or similar wording).
  - The notebook should implement these examples as runnable code cells and aim to produce **comparable outputs/results**.
  - Exact equality is not required, but the notebook should be designed so that it can often reproduce the same results (given the same assumptions/data).
  - If an example cannot be reproduced (missing data/ambiguity), document what is missing and provide the closest reproducible approximation.
- **[R5] Visualize whenever it helps learning**
  - Notebooks should generate strong, student-friendly visual outputs when appropriate (plots, charts, schematic diagrams, timelines, network graphs, etc.).
  - Visualizations must directly support understanding what is happening in the Tier (inputs → process → outputs).
  - Prefer domain-appropriate visuals for logistics / supply chain problems, such as:
    - Time breakdowns (travel vs setup vs handling) as bar or stacked-bar charts
    - Cumulative time curves (how total time grows step-by-step)
    - Timeline / Gantt-like views of operations (sequence of actions)
    - Flow / network plots when the narrative involves routes, hubs, or networks
    - Sensitivity plots (how results change when key parameters change)
  - Visualizations should be driven by the problem narrative and examples in the source, not added randomly.
 - **[R6] Advanced Tier exception: AWS tooling is allowed when the source Tier requires it (e.g., quantum computing)**
  - Default rule remains **open-source-first**.
  - However, if the `.tex` Tier is explicitly about **quantum computing** (e.g., “Quantum Leap”, QAOA, QUBO, Grover’s algorithm, quantum annealing), it is acceptable to base the implementation on **Amazon Web Services**.
  - Preferred AWS option for quantum Tiers: **Amazon Braket** (Python SDK).
  - If AWS is used, the notebook must:
    - Clearly label it as **AWS-based** in the first Markdown cell.
    - Explain required setup (credentials, region, service availability) **without hardcoding secrets**.
    - Offer a best-effort **local/open-source fallback** when feasible (for example: a simplified classical simulation), and clearly state limitations.
 - **[R7] Cloud-scale Tier guidance: AWS may be used as an optional “production track” (non-quantum)**
  - This applies to Tiers that are clearly about **system integration at scale**, such as:
    - Digital twins (IoT sensors, real-time updates, data latency handling)
    - Real-time/streaming data pipelines
    - Deployment/MLOps narratives
  - In these cases, the Tier notebook must still be **fully runnable locally** using open-source tools.
  - AWS content, if included, must be presented as:
    - An optional section (e.g., `### Optional: AWS Production Track`)
    - Architecture guidance + minimal illustrative code (no secrets)
    - Clear mapping from local components to AWS equivalents (e.g., local files → S3, local scheduler → Step Functions) when helpful.
 - **[R8] Dependency strategy: do not install packages inside notebooks**
  - Notebooks must **not** run `pip install ...` as part of normal execution.
  - Instead, dependencies should be preinstalled using the repository's infrastructure setup:
    - `infrastructure/jupyterhub/Dockerfile`
  - Notebooks may include a small **import-only environment check** that fails fast with a clear message if a dependency is missing.

## Local verification workflow (Windows PowerShell + venv)

When you want to validate that notebooks run end-to-end and produce outputs (without relying on Docker), use a local virtual environment and execute notebooks via `nbconvert`.

### 1) Create and activate a virtual environment

Run from the repository root:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 2) Install Jupyter tooling (and common scientific deps)

```powershell
python -m pip install --upgrade pip
python -m pip install jupyterlab nbconvert
python -m pip install numpy pandas matplotlib
```

### 3) Execute notebooks and store executed copies

Important: on Windows, make sure you execute with the venv Python to avoid accidentally using a different Python on PATH.

```powershell
$root = (Get-Location).Path
$py = Join-Path $root ".venv\Scripts\python.exe"
```

Problem 1:

```powershell
$dir = Join-Path $root "Part I - The Port & Container Terminal (Problems 1-46)\A. Foundations of Terminal Operations (The Building Blocks)\01. The Single Crane Lift Sequence Problem"
$out = Join-Path $dir "executed"
New-Item -ItemType Directory -Force -Path $out | Out-Null

$files = @("P1-Tier-1.ipynb","P1-Tier-2.ipynb","P1-Tier-3.ipynb","P1-Tier-4.ipynb")
foreach ($f in $files) {
  & $py -m jupyter nbconvert --to notebook --execute (Join-Path $dir $f) --output $f --output-dir $out --ExecutePreprocessor.timeout=1800
  if ($LASTEXITCODE -ne 0) { throw "Execution failed for $f" }
}
```

Problem 2:

```powershell
$dir = Join-Path $root "Part I - The Port & Container Terminal (Problems 1-46)\A. Foundations of Terminal Operations (The Building Blocks)\02. The Container Stacking Rules Problem"
$out = Join-Path $dir "executed"
New-Item -ItemType Directory -Force -Path $out | Out-Null

$files = @("P2-Tier-1.ipynb","P2-Tier-2.ipynb","P2-Tier-3.ipynb","P2-Tier-4.ipynb","P2-Tier-8.ipynb")
foreach ($f in $files) {
  & $py -m jupyter nbconvert --to notebook --execute (Join-Path $dir $f) --output $f --output-dir $out --ExecutePreprocessor.timeout=1800
  if ($LASTEXITCODE -ne 0) { throw "Execution failed for $f" }
}
```

Problem 47 (example for three-digit format):

```powershell
$dir = Join-Path $root "Part II - The End-to-End Supply Chain (Problems 47-101)\A. Foundational Analytics & Inventory Control (The Language of Supply Chain)\047. The Demand Forecasting Problem"
$out = Join-Path $dir "executed"
New-Item -ItemType Directory -Force -Path $out | Out-Null

# Add appropriate notebook files for Problem 47 when available
```

Problem 100 (example for three-digit format):

```powershell
$dir = Join-Path $root "Part II - The End-to-End Supply Chain (Problems 47-101)\E. Integrated, Resilient, & Modern Supply Chains (The Frontier)\100. The Advanced Supply Chain Analytics Problem"
$out = Join-Path $dir "executed"
New-Item -ItemType Directory -Force -Path $out | Out-Null

# Add appropriate notebook files for Problem 100 when available
```

Problem 101 (example for three-digit format):

```powershell
$dir = Join-Path $root "Part II - The End-to-End Supply Chain (Problems 47-101)\E. Integrated, Resilient, & Modern Supply Chains (The Frontier)\101. The Ultimate Supply Chain Challenge Problem"
$out = Join-Path $dir "executed"
New-Item -ItemType Directory -Force -Path $out | Out-Null

# Add appropriate notebook files for Problem 101 when available
```

The executed notebooks (with all outputs captured) will be under each problem folder's `executed/` directory.

## Naming standards (decide once and keep consistent)
- **[K1] Problem folder name**
  - `"{problem_no}. {problem_title}"`
  - Windows-safe: replace `<>:"/\\|?*` with `_`.
  - No leading/trailing whitespace.
  - Two-digit format for Part I (01-46)
  - Three-digit format for Part II (047-101)
- **[K2] Notebook file naming**
  - **Canonical (required):** `P{problem_no}-Tier-1.ipynb`, `P{problem_no}-Tier-2.ipynb`, ...
  - Example for Problem 1: `P1-Tier-1.ipynb` … `P1-Tier-4.ipynb`
  - Do **not** use suffixes such as `.runnable`.
  - If a temporary suffix is used during development (e.g., `P1-Tier-2.runnable.ipynb`), it must be resolved before publishing by renaming it to `P1-Tier-2.ipynb`.
 - **[K2.1] Backup policy during renames (recommended)**
  - Before overwriting `P{problem_no}-Tier-k.ipynb`, move the previous file to:
    - `_backup/P{problem_no}-Tier-k.<timestamp>.ipynb` (or `_backup/P{problem_no}-Tier-k.stub.ipynb`)
  - After verifying `Run All` works, you may delete `_backup/`.
- **[K3] Optional common files per problem folder**
  - `source.tex` (a copy of the corresponding `lineN.tex` or a reference note)
  - `assets/` (images, diagrams, etc. if needed)

## Generation strategy (automation)
This must not be manual work. Since the `.tex` files are the single source of truth, everything should be **reproducible via a script**.

### 1) Discovery / inventory
- **[T1]** List `line*.tex` files in the source folder.
  - Expectation: `line1.tex` … `line101.tex` (exactly 101 files)
- **[T2]** For each `lineN.tex`, extract:
  - **Problem number**: `N`
  - **Problem title**: e.g., `The Single Crane Lift Sequence Problem`
  - **Tier count**: e.g., `4`
  - **Python code per Tier**: Tier 1..K

### 2) Parsing rules from `.tex` (parser requirements)
- **[P1] Capture the title**
  - Identify the pattern used for the problem title.
  - Likely candidates:
    - `\section{...}` / `\subsection{...}` / `\title{...}`
    - or plain text like `Problem: ...`
- **[P2] Capture Tier boundaries**
  - Identify how Tier blocks are marked in the `.tex` (e.g., `Tier 1`, `Tier I`, `\textbf{Tier 1}`, etc.).
  - For each Tier, detect:
    - Start
    - End
- **[P3] Capture Python code blocks**
  - Likely environments:
    - `\begin{verbatim} ... \end{verbatim}`
    - `\begin{lstlisting} ... \end{lstlisting}`
    - Markdown-style fences like ```python ... ```
  - Minimal validation that a captured block is Python:
    - Check for `import`, `def`, `print`, `pandas`, `numpy`, etc.
- **[P4] Tier count validation**
  - If the number of captured Tier sections contradicts the Tier count stated in the `.tex`:
    - Fail fast and report clearly.
 - **[P5] Detect “AWS-eligible” advanced Tiers from the source**
  - Mark a Tier as **AWS-eligible** if the `.tex` contains quantum/advanced keywords such as:
    - `Quantum Leap`, `QAOA`, `QUBO`, `Grover`, `Quantum Annealing`, `Quantum Circuit`
  - The generator should record this in extracted metadata so the notebook writer can apply **[R6]**.
 - **[P6] Detect “cloud-scale” (AWS-optional) Tiers from the source**
  - Mark a Tier as **cloud-scale** if the Tier heading or nearby text indicates:
    - Digital twin / IoT sensors / real-time integration / data latency
    - Streaming / event-driven narratives
    - Deployment / MLOps narratives
  - The generator should record this in extracted metadata so the notebook writer can apply **[R7]**.

### 3) Produce the output folder tree
- **[O1]** Choose an output root directory (script parameter):
  - Example: `D:\...\responses-complete-png\_problems_out` (or a separate repo folder)
- **[O2]** For each problem, create a folder in the appropriate category:
  - Problems 1-46: `Part I - The Port & Container Terminal (Problems 1-46)/<A-E heading>/NN. <Problem Title>`
  - Problems 47-101: `Part II - The End-to-End Supply Chain (Problems 47-101)/<A-E heading>/NNN. <Problem Title>`
- **[O3]** For each Tier, create an `.ipynb`:
  - Minimum notebook structure:
    - Markdown cell(s): title + context + Tier overview
    - Code cell(s): the Tier’s Python code (or an open-source equivalent)

### 4) Notebook template (minimum standard)
- **[NB1] Markdown cell content (example)**
  - `# {N}. {Problem Title}`
  - `## Tier {k}`
  - `### Key assumptions`
  - `### Approach (step-by-step)`
  - `### What to look for in the results`
  - `### Concrete example (from the source)`
  - `### Visualization(s)`
  - `### Why this Tier exists vs earlier Tiers (k>=2)`
  - `### Pros / Cons vs Tier 1..(k-1)`
  - `### When to use this Tier`
- **[NB2] Code cells**
  - The extracted Python code from `.tex` (or its open-source replacement).
  - Keep code readable and modular (functions where helpful).
  - Code must be heavily commented so that beginners can follow it.
- **[NB3] Output interpretation**
  - At least one Markdown section explaining:
    - What the computed results mean
    - How to sanity-check them
    - Common pitfalls
 - **[NB4] Example-driven outputs**
  - Include code cells that reproduce the `.tex` example(s) (e.g., “Concrete Example”) and produce outputs that can be compared to the source.
 - **[NB5] Visualization guidance**
  - Prefer open-source plotting libraries such as `matplotlib`, `seaborn`, or `plotly`.
  - For discrete structures (routes, networks, flows), consider open-source tools like `networkx`.

## Current scan results (keywords) — candidates for AWS-based quantum Tiers
Based on an automated keyword scan across `line1.tex` … `line101.tex`, the following files contain **Tier 9 / “Quantum Leap” / QAOA / QUBO / Grover / quantum annealing** indicators and are the strongest candidates for applying **[R6]**:

- `line7.tex`
- `line9.tex`
- `line15.tex`
- `line17.tex`
- `line18.tex`
- `line23.tex`
- `line27.tex`
- `line28.tex`
- `line30.tex`
- `line34.tex`
- `line60.tex`
- `line61.tex`
- `line62.tex`
- `line64.tex`
- `line65.tex`
- `line67.tex`
- `line68.tex`
- `line71.tex`
- `line72.tex`
- `line73.tex`
- `line74.tex`
- `line75.tex`
- `line76.tex`
- `line77.tex`
- `line81.tex`
- `line83.tex`
- `line84.tex`
- `line85.tex`
- `line86.tex`
- `line87.tex`
- `line92.tex`
- `line93.tex`
- `line94.tex`
- `line95.tex`
- `line96.tex`
- `line97.tex`
- `line98.tex`
- `line99.tex`

Note: this is a **keyword-based** list. The generator should still parse each file to confirm which **specific Tier number** is quantum-related and mark only that Tier as AWS-eligible.

## Current scan results (headings) — non-quantum cloud-scale Tier candidates
The following files contain an explicit Tier heading for **Tier 5: The Integrated Digital Twin** (or a close variant), which is the clearest non-quantum case where **[R7]** may apply:

- `line7.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line8.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line9.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line80.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line81.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line86.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line87.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line89.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line90.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line92.tex` — `\subsection{Tier 5: The Integrated Digital Twin}`
- `line93.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line94.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line95.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line96.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line97.tex` — `\subsection{Tier 5: The Integrated Digital Twin (System-of-Systems Simulation)}`
- `line98.tex` — `\subsection{Tier 5: The Integrated Digital Twin (Fleet Simulation Engine)}`
- `line99.tex` — `\subsection{Tier 5: The Integrated Digital Twin (Fleet-Wide Energy Simulation)}`

Note: the presence of “Integrated Digital Twin” does **not** force AWS usage. It indicates the Tier is cloud-scale enough that an **optional AWS production track** can be appropriate.

### 5) Reporting / quality checks
- **[Q1]** Produce a summary report at the end:
  - Number of generated problem folders (must be 101)
  - Number of generated notebooks (sum of Tiers)
  - Any files that failed parsing (with reasons)
- **[Q2]** Spot-check example:
  - `line1.tex` → folder `Part I - The Port & Container Terminal (Problems 1-46)/A. Foundations of Terminal Operations (The Building Blocks)/01. The Single Crane Lift Sequence Problem` exists
  - Contains `P1-Tier-1.ipynb` … `P1-Tier-4.ipynb`
  - `line47.tex` → folder `Part II - The End-to-End Supply Chain (Problems 47-101)/A. Foundational Analytics & Inventory Control (The Language of Supply Chain)/047. The Demand Forecasting Problem` exists
  - Contains appropriate Tier notebooks

## Implementation (code tasks) — suggested files
Create a small generator that builds the above structure.

- **[G1]** `scripts/generate_problems.py`
  - Arguments:
    - `--src` (source `.tex` folder)
    - `--out` (output folder)
    - `--dry-run` (optional)
  - Responsibilities:
    - Find `line*.tex`
    - Parse title / tiers / code
    - Generate folders and `.ipynb` notebooks
- **[G2]** `scripts/tex_parser.py`
  - Responsibilities:
    - Extract title, tiers, and Python blocks using regex/heuristics
- **[G3]** `scripts/notebook_writer.py`
  - Responsibilities:
    - Write `.ipynb` using `nbformat`

## Dependencies
- **[D1]** Python package: `nbformat`
- **[D2]** (Optional) `regex` (for more advanced patterns)

## Definition of Done
- **[AC1]** One command generates all 101 problem folders in the appropriate categories.
- **[AC2]** Each problem folder is named `NN. <Title>` (Part I) or `NNN. <Title>` (Part II) and placed in the correct category folder.
- **[AC3]** Each problem contains one `.ipynb` per Tier.
- **[AC4]** Notebook content is faithful to the `.tex` Python logic, **while respecting open-source-only package constraints**.
- **[AC5]** Each Tier notebook includes clear, structured English explanations (not code-only).
- **[AC6]** If a `.tex` file can't be parsed, the script reports it clearly.

## Open decisions (need your confirmation)
- **[C1]** What is the exact output root directory? (Inside the source folder, or a separate repo/output folder?)
- **[C2]** Notebook naming standard: `P{problem_no}-Tier-1.ipynb` or `01 - Tier 1.ipynb`?
- **[C3]** Which exact `.tex` patterns contain the title and Tier markers? (Need 1–2 example `.tex` files to finalize parsing.)
