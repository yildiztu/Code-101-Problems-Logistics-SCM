# Execute P85 notebooks
$root = (Get-Location).Path
$py = Join-Path $root ".venv\Scripts\python.exe"

# Create executed directory
$dir = Join-Path $root "Part II - The End-to-End Supply Chain (Problems 47-101)\D. Strategic Network Design & Sourcing (The Blueprint of the Business)\085. The Uncapacitated Facility Location Problem\executed"
New-Item -ItemType Directory -Force -Path $dir | Out-Null

# Execute Tier-1
Write-Host "Executing P85-Tier-1..."
& $py -m jupyter nbconvert --to notebook --execute (Join-Path $root "Part II - The End-to-End Supply Chain (Problems 47-101)\D. Strategic Network Design & Sourcing (The Blueprint of the Business)\085. The Uncapacitated Facility Location Problem\P85-Tier-1.ipynb") --output-dir $dir --ExecutePreprocessor.timeout=1800
if ($LASTEXITCODE -ne 0) { 
    Write-Host "P85-Tier-1 execution failed!" -ForegroundColor Red
    exit 1
} else {
    Write-Host "P85-Tier-1 executed successfully!" -ForegroundColor Green
}
