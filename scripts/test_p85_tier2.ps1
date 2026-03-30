# Test P85-Tier-2
$root = (Get-Location).Path
$py = Join-Path $root ".venv\Scripts\python.exe"
$dir = Join-Path $root "Part II - The End-to-End Supply Chain (Problems 47-101)\085. The Uncapacitated Facility Location Problem\executed"
New-Item -ItemType Directory -Force -Path $dir | Out-Null

Write-Host "Testing P85-Tier-2..."
& $py -m jupyter nbconvert --to notebook --execute (Join-Path $root "Part II - The End-to-End Supply Chain (Problems 47-101)\085. The Uncapacitated Facility Location Problem\P85-Tier-2.ipynb") --output-dir $dir --ExecutePreprocessor.timeout=1800
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ P85-Tier-2 executed successfully!" -ForegroundColor Green
} else {
    Write-Host "✗ P85-Tier-2 execution failed!" -ForegroundColor Red
}
