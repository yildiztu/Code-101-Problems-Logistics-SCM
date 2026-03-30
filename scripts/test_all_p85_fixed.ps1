# Test all P85 notebooks
$root = (Get-Location).Path
$py = Join-Path $root ".venv\Scripts\python.exe"

# Create executed directory
$dir = Join-Path $root "Part II - The End-to-End Supply Chain (Problems 47-101)\D. Strategic Network Design & Sourcing (The Blueprint of the Business)\085. The Uncapacitated Facility Location Problem\executed"
New-Item -ItemType Directory -Force -Path $dir | Out-Null

# Test each notebook
$notebooks = @("P85-Tier-1", "P85-Tier-2", "P85-Tier-3", "P85-Tier-4", "P85-Tier-9")
$success = @()

foreach ($notebook in $notebooks) {
    Write-Host "Testing $notebook..."
    $output = Join-Path $dir "$notebook.ipynb"
    
    & $py -m jupyter nbconvert --to notebook --execute (Join-Path $root "Part II - The End-to-End Supply Chain (Problems 47-101)\D. Strategic Network Design & Sourcing (The Blueprint of the Business)\085. The Uncapacitated Facility Location Problem\$notebook.ipynb") --output-dir $dir --ExecutePreprocessor.timeout=1800 2>&1
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ $notebook executed successfully!" -ForegroundColor Green
        $success += "$notebook"
    } else {
        Write-Host "✗ $notebook execution failed!" -ForegroundColor Red
    }
    Write-Host ""
}

Write-Host "=== EXECUTION SUMMARY ==="
Write-Host "Successful: $($success.Count)/$($notebooks.Count) notebooks"
Write-Host "Failed: $($($notebooks.Count - $success.Count))/$($notebooks.Count) notebooks"
