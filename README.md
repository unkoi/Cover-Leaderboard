# Cover-Leaderboard
T2:Button("Cover the leaderboard with RAIDER",function()
    local string = "\r\n RAIDER"
    local fullstring = ""
    for i = 1, 75 do
        fullstring = fullstring .. string
    end
    game:GetService("Players").LocalPlayer.PlayerGui.RolePlayName.Frame.bodyFrame.submitBtn.nameEvent:FireServer(fullstring)
    
end)
