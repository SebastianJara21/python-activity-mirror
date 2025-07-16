$TotalCommits = 60
$StartDate = (Get-Date).AddMonths(-12)
$Messages = @(
    "Refactor logic", "Update module", "Fix async flow", "Improve performance",
    "Add placeholder", "Optimize structure", "Adjust config", "Clean up code"
)

for ($i = 0; $i -lt $TotalCommits; $i++) {
    $DaysOffset = [math]::Floor(($i * 365.0) / $TotalCommits)
    $CommitDate = $StartDate.AddDays($DaysOffset).AddHours((Get-Random -Minimum 8 -Maximum 22)).AddMinutes((Get-Random -Minimum 0 -Maximum 59))
    $FormattedDate = $CommitDate.ToString("ddd MMM dd HH:mm:ss yyyy") + " +0000"

    $env:GIT_AUTHOR_DATE = $FormattedDate
    $env:GIT_COMMITTER_DATE = $FormattedDate

    $Message = $Messages | Get-Random
    git commit --allow-empty -m "$Message #$i"
}
