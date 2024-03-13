#!/usr/bin/env powershell

$msg = "Take a break!"
$reminderTimes = @("08:45", "09:35", "10:35", "11:25", "14:15", "15:05", "16:05", "16:55", "20:05", "20:55", "21:45")

foreach ($time in $reminderTimes) {
    $action = New-ScheduledTaskAction -Execute "msg" -Argument "* `"$msg`""
    $trigger = New-ScheduledTaskTrigger -Daily -At $time
    $taskName = "Reminder_" + $time.Replace(":", "_")
    Register-ScheduledTask -Action $action -Trigger $trigger -TaskName $taskName
}
