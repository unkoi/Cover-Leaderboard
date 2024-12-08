---WAITS UNTIL CHARACTER AND GAME IS FULLY LOADED
local lib = loadstring(game:HttpGet("https://raw.githubusercontent.com/Sidhsksjsjsh/VAPE-UI-MODDED/main/.lua"))()

local isrunning,error = pcall(function()
repeat wait() until game:IsLoaded()


local time = os.clock()
COREGUI = game:GetService("CoreGui")
if not game:IsLoaded() then
	game.Loaded:Wait()
end

if game.PlaceId ~= 5712833750 then
    return
end

local breakit = false
while true do
    local success, error = pcall(function()
        print(game.Players.LocalPlayer:FindFirstChild("leaderstats"))
        task.wait()
        if game.Players.LocalPlayer:FindFirstChild("leaderstats") then
            breakit = true
        end
    end)

    if error then
        print(success, error)
    end

    if breakit then
        break
    end
end

Player = game.Players.LocalPlayer
Character = Player.Character or Player.CharacterAdded:Wait()


--[username] = 'webhook'
local Webhook = { -- For Grinding, tells you your leveling speed.
    ["XelXel"] = 'https://discord.com/api/webhooks/1852735481765/3IhmtR2PqI5zaoUGpzrfbfFDu2P0x0pbIs1KY5Zx_ZChzNoQ8LH', -- Example Webhook, doesn't work.
}

if Webhook[game.Players.LocalPlayer.Name] then
    getgenv().LocalWebhookId = Webhook[game.Players.LocalPlayer.Name]
end

Access = true
VIP = true



---SYSTEM TO SEE WHEN A PLAYER IS DEAD OR ALIVE [[START]]
function RemoveGUI()
    local success, error = pcall(function()
        if game.Players.LocalPlayer.PlayerGui:FindFirstChild("newRewardGui") then
            game.Players.LocalPlayer.PlayerGui.newRewardGui:Destroy()
            breakit = true
        end
    end)
end

function RemoveAddedCooldown()
    Character.ChildAdded:connect(function(child)
        if child.Name == "justFound" or child.Name == "Deb" or child.Name == "FireballDeb" then
            wait()
            child:Destroy()
        else
            print(child.Name, "Added")
        end
    end)
end


teleport = false
local CharacterAlive
if Character:FindFirstChild("Humanoid").Health > 0 then
    CharacterAlive = true
    teleport = true

    RemoveAddedCooldown()
    RemoveGUI()

    Character:WaitForChild("Humanoid").Died:Connect(function()
        CharacterAlive = false
    end)
else
    CharacterAlive = false
end

game.Players.LocalPlayer.CharacterAdded:Connect(function(newCharacter)
    Character = newCharacter
    Character:WaitForChild("Humanoid")
    CharacterAlive = true
    teleport = true

    RemoveAddedCooldown()
    RemoveGUI()

    Character:WaitForChild("Humanoid").Died:Connect(function()
        print("Character Dead")
        CharacterAlive = false
    end)
end)

---SYSTEM TO SEE WHEN A PLAYER IS DEAD OR ALIVE [[END]]

-- [[ Comma Function ]]
function commaValue(amount)
    local formatted = amount
    while true do
        formatted, k = string.gsub(formatted, "^(-?%d+)(%d%d%d)", '%1,%2')
        if (k==0) then
            break
        end
    end
    return formatted
end


-- [[ Webhook Setup ]]
local BotUserName = 'ONIxAPI'
local BotPhotoURL = 'https://media.discordapp.net/attachments/856034478408728576/1009394204193067058/oniii.jpg'
local Red = tonumber(tostring("0xFF0000"))
local Green = tonumber(tostring("0x32CD32"))
local Timestamp = os.date("%Y-%m-%dT%X.000Z")
local Request = http_request or request or HttpPost or syn.request




---- KEEP TRACK OF PLAYER'S PING
local fps = 0
local PlayerPing = 0
game:GetService("RunService").RenderStepped:Connect(function(ping)
    PlayerPing = (game:GetService("Stats").Network.ServerStatsItem["Data Ping"]:GetValueString(math.round(2/ping))) -- your ping
    fps = math.round(1/ping)
end)



---- SEND PLAYER'S CURRENT LEVELING DAYA TO THE WEBHOOK

local fireballsTotal = 0

---FOR
local levelaverage = 0
local TotalExpPerMin = 0
local LostExpPerMin = 0
local xseconds = 0
local xmins = 0

if getgenv().LocalWebhookId ~= 'YOUR DISCORD WEBHOOK HERE' then
    local TrackingWebhookSeconds = 0
    local TrackingWebhookMinutes = 0
    local TrackedTime = 0
    local TrackedPlayerLevel = game.Players.LocalPlayer.leaderstats.Level.Value
    local LevelPerMin = 0
    local HoursTilOnLeaderboard = 0
    local leveldiff = 0

    local testSeconds = 0
    local testMins = 0
    local testHours = 0

    local function TotalExp(exp)
        return 500*(exp-1)^2+1500*(exp-1)+1000
    end


    local top100level = 135000
    for i,v in pairs(game:GetService("Workspace").LBFolder.GlobalLeaderboard.LeaderboardGUI.Holder.ScrollingFrame:GetChildren()) do
        if v.Name == "LeaderboardFrame" then
            local rank = tonumber(v.Rank.text)
            local player = v.Player.text
            local level = tonumber(v.Level.text)

            if rank == 100 then
                top100level = level
            end
        end
    end


    local top1level = 165000
    for i,v in pairs(game:GetService("Workspace").LBFolder.GlobalLeaderboard.LeaderboardGUI.Holder.ScrollingFrame:GetChildren()) do
        if v.Name == "LeaderboardFrame" then
            local rank = tonumber(v.Rank.text)
            local player = v.Player.text
            local level = tonumber(v.Level.text)

            if rank == 1 then
                top1level = level
            end
        end
    end

    task.spawn(function()
        while true do

            if testMins ~= 0 and game.Players.LocalPlayer.leaderstats.Level.Value-TrackedPlayerLevel ~= 0 then
                LevelPerMin = (game.Players.LocalPlayer.leaderstats.Level.Value-TrackedPlayerLevel)/testMins
            end

            local expdifftomax100 = TotalExp(top100level) - TotalExp(game.Players.LocalPlayer.leaderstats.Level.Value)
            local expdifftomax1 = TotalExp(top1level) - TotalExp(game.Players.LocalPlayer.leaderstats.Level.Value)
            local TotalExpPerHour = TotalExpPerMin*60

            HoursTilOnLeaderboard100 = expdifftomax100/TotalExpPerHour
            HoursTilOnLeaderboard1 = expdifftomax1/TotalExpPerHour

            if TrackingWebhookSeconds == 0 then
                local msg = {
                    ["username"] = BotUserName,
                    ["avatar_url"] = BotPhotoURL,
                    ["content"] = " ",
                    ["embeds"] = {
                        {
                            ["title"] = "__**Farming Update**__",
                            ["type"] = "rich",
                            ["description"] = Player.Name,
                            ["color"] = Green,
                            ["fields"] = {
                                {
                                    ["name"] = "Current Level",
                                    ["value"] = commaValue(game.Players.LocalPlayer.leaderstats.Level.Value),
                                    ["inline"] = true
                                },
                                {
                                    ["name"] = "Previous Level",
                                    ["value"] = commaValue(TrackedPlayerLevel),
                                    ["inline"] = true
                                },
                                {
                                    ["name"] = "​",
                                    ["value"] = "Data:",
                                },
                                {
                                    ["name"] = "Levels Gained",
                                    ["value"] = commaValue(game.Players.LocalPlayer.leaderstats.Level.Value-TrackedPlayerLevel),
                                    ["inline"] = true
                                },
                                {
                                    ["name"] = "Levels Per Min",
                                    ["value"] = tostring(math.round(LevelPerMin*100)/100),
                                    ["inline"] = true
                                },
                                {
                                    ["name"] = "Levels Per Hour",
                                    ["value"] = tostring(math.round((LevelPerMin*60)*100)/100),
                                    ["inline"] = true
                                },
                                {
                                    ["name"] = "Exp Gained Per Min",
                                    ["value"] = commaValue(TotalExpPerMin),
                                    ["inline"] = false
                                },
                                {
                                    ["name"] = "Exp till #100",
                                    ["value"] = commaValue(expdifftomax100),
                                    ["inline"] = false
                                },
                                {
                                    ["name"] = "Hours till #100",
                                    ["value"] = tostring(math.round(HoursTilOnLeaderboard100*100)/100),
                                    ["inline"] = true
                                },
                                {
                                    ["name"] = "Exp till #1",
                                    ["value"] = commaValue(expdifftomax1),
                                    ["inline"] = false
                                },
                                {
                                    ["name"] = "Hours till #1",
                                    ["value"] = tostring(math.round(HoursTilOnLeaderboard1*100)/100),
                                    ["inline"] = true
                                },
                                {
                                    ["name"] = "Fireballs",
                                    ["value"] = fireballsTotal,
                                    ["inline"] = true
                                },
                            },
                            ['timestamp'] = Timestamp,
                            ["footer"] = {
                                ["text"]  = "Time Farming: ".. TrackedTime.. "\n" .. "FPS: "..fps.."\n" .. "Ping: ".. PlayerPing .. "\n" .."​"
                            }
                        },
                    }
                }
                pcall(function()
                    Request({Url = getgenv().LocalWebhookId, Method = "POST", Headers = {["Content-Type"] = "application/json"}, Body = game.HttpService:JSONEncode(msg)})
                end)
                --print("Sending Request")


                xseconds = 0
                xmins = 0
                TotalExpPerMin = 0
                LostExpPerMin = 0
                levelaverage = 0
            end


            testSeconds += 1
            testMins = testSeconds / 60
            testHours = testMins / 60

            --print("SECONDS: ",TrackingWebhookSeconds)

            TrackingWebhookSeconds = TrackingWebhookSeconds + 1
            if TrackingWebhookSeconds >= 300 then
                TrackingWebhookMinutes = (TrackingWebhookSeconds + (TrackingWebhookMinutes * 60)) / 60
                TrackedTime = math.floor(TrackingWebhookMinutes) .. ' Minutes'

                if TrackingWebhookMinutes >= 60 then
                    TrackingWebhookHours = TrackingWebhookMinutes / 60
                    TrackingWebhookLeftoverMinutes = (TrackingWebhookHours%1) * 60
                    TrackingWebhookHours = math.floor(TrackingWebhookHours)
                    TrackedTime = TrackingWebhookHours .. ' Hours ' .. math.floor(TrackingWebhookLeftoverMinutes) .. ' Minutes'
                end
                TrackingWebhookSeconds = 0
            end
            wait(1)
        end
    end)
end

-- [[ Anti AFK ]]
if not game:IsLoaded() then game.Loaded:Wait(); end

local idledEvent = game:GetService("Players").LocalPlayer.Idled
local function disable()
    for _, cn in ipairs(getconnections(idledEvent)) do
        cn:Disable()
    end
end

oldConnect = hookfunction(idledEvent.Connect, function(self, ...)
    local cn = oldConnect(self, ...); disable()
    return cn
end)

namecall = hookmetamethod(game, "__namecall", function(self, ...)
    if self == idledEvent and getnamecallmethod() == "Connect" then
        local cn = oldConnect(self, ...); disable()
        return cn
    end
    return namecall(self, ...)
end)

disable()







---- KEEPS TRACK OF ALL THE EXP GAINED FROM THE USE OF THE CHANGED SIGNAL. THIS IS USED TO PREDICT WHAT LEVEL YOU WILL BE BASED ON THE GIVEN EXP PER MIN


local tickstart = os.clock()
local expgained = 0
local lostexp = 0
local totalexp = 0
local level = 0
local exp = 0
local expreset = 0
local leveluptrack = 0
local FireballOrHittrack = 0


local currentexp
local previousexp
local previouslevel
function Exp()
    local ExperienceBar = game:GetService("Players").LocalPlayer:WaitForChild("PlayerGui"):WaitForChild("LevelBar"):WaitForChild("Experience")
    currentexp = tonumber(ExperienceBar.text:split("/")[1])
    previousexp = tonumber(ExperienceBar.text:split("/")[1])
    previouslevel = tonumber(ExperienceBar.text:split("/")[2]:sub(1, -4))
    warn(currentexp, previousexp, previouslevel)

    getgenv().ExpTracker = ExperienceBar:GetPropertyChangedSignal("Text"):Connect(function(text)
        a, b = pcall(function()
            if CharacterAlive == false then
                getgenv().ExpTracker:Disconnect()
                return
            end

            if game:GetService("Players").LocalPlayer.Character:FindFirstChild("Humanoid").Health == 0 then
                getgenv().ExpTracker:Disconnect()
                return
            end

            if text == "0/100" then
                return
            end

            exp = tonumber(ExperienceBar.text:split("/")[1])
            level = tonumber(ExperienceBar.text:split("/")[2]:sub(1, -4))



            if currentexp < previousexp then
                wait(.2)
                print("[Current exp] " .. currentexp .." is less than [Previous Exp] "..previousexp)
                print(level, previouslevel, CharacterAlive)
                if level < previouslevel then
                    print("Level Down: ".. level - previouslevel)
                    leveldown = true
                else
                    leveldown = false
                end

                if level > previouslevel then
                    levelup = true
                else
                    levelup = false
                end

                if level == previouslevel then
                    expsame = true
                else
                    expsame = false
                end

                if levelup then
                    leveluptrack += 1
                    print("Level up: " .. level - previouslevel)
                    previouslevel = level

                    currentexp = tonumber(ExperienceBar.text:split("/")[1])
                    previousexp = tonumber(ExperienceBar.text:split("/")[1])


                end

                if expsame and not levelup or leveldown then
                    print("Exp decreased")
                    expreset += 1
                    lostexp += previousexp - currentexp
                    currentexp = tonumber(ExperienceBar.text:split("/")[1])
                    previousexp = currentexp
                end
            end

            previousexp = currentexp
            currentexp = tonumber(ExperienceBar.text:split("/")[1])
            if currentexp > previousexp then
                totalexp += currentexp - previousexp
            end
        end)
        if b then
            print(a, b)
        end
    end)
end

task.spawn(function()
    getgenv().Player = game.Players.LocalPlayer.CharacterAdded:Connect(function(Character)
        Exp()
    end)
    Exp()
end)


task.spawn(function()
    while wait(1) do
        xseconds += 1
        xmins = xseconds/60
    end
end)


task.spawn(function()
    while wait(10) do
        TotalExpPerMin = totalexp/xmins
        LostExpPerMin = lostexp/xmins
        levelaverage = level/xmins

        --print"[-------"
        --warn("Level: " .. level .. " Current: ".. currentexp .." Previous: " .. previousexp .. " Total Exp: " .. totalexp)
        --warn("Gained: ".. currentexp - previousexp)
        --warn("Lost Exp: ", lostexp)
        --print"-------"
        --warn("Exp Per Min: ", TotalExpPerMin)
        --warn("Times exp was lowered: ", expreset)
        --warn("Level Ups: ", leveluptrack)
        --print"-------]"
        --print(xmins)
    end
end)






----END TRACKER









-- [[ UI Library Setup ]]
local wndw = lib:Window("VIP Turtle Hub V4")
local T1 = wndw:Tab("Main")

-- [[ TIMER ]]
local timeSecondsDummy = 0
local timeMinsDummy = timeSecondsDummy / 60
local timeHoursDummy = timeMinsDummy / 60
local timeDaysDummy = timeHoursDummy / 60
task.spawn(function()
    pcall(function()
        while wait(1) do
            ----print(timeSecondsDummy)
            timeSecondsDummy += 1
            timeMinsDummy = timeSecondsDummy / 60
            timeHoursDummy = timeMinsDummy / 60
            timeDaysDummy = timeHoursDummy / 60
        end
    end)
end)

local savedpos
T1:Toggle("Dummy hit",false,function(value)
    NewLoop = value
    
    timeSecondsDummy = 0
    local dummytarget = nil
    local success, error = pcall(function()
        if NewLoop then
            savedpos = Character.HumanoidRootPart.CFrame
            TrackingWebhookSeconds = 0
            timeSecondsDummy = 0
            local search
            local dummyLevel
            if game.Players.LocalPlayer.leaderstats.Level.Value > 5000 then
                dummyLevel = "Dummy2"
                search = game:GetService("Workspace").MAP.waterfall1
            else
                dummyLevel = "Training Dummy"
                search = game:GetService("Workspace").MAP.dummies
            end

            dummytarget = search:FindFirstChild(dummyLevel)

            Character.HumanoidRootPart.CFrame = dummytarget.HumanoidRootPart.CFrame + Vector3.new(3,0,0)
        else
            Character.HumanoidRootPart.CFrame = savedpos
        end

        local FireLoop = 0
        local Fire = 0
        while NewLoop do
            task.wait()
            Fire += 1
            if Fire >= 2 then
                Fire = 0
                FireLoop += 1
                if FireLoop > 60 then
                    FireLoop = 1
                end
                game:GetService("ReplicatedStorage").jdskhfsIIIllliiIIIdchgdIiIIIlIlIli:FireServer(dummytarget.Humanoid, FireLoop)
            end

            task.spawn(function()
                if timeMinsDummy > 5 then
                    timeSecondsDummy = 0
                    if Character:FindFirstChild("Humanoid") then
                        Character.Humanoid.Health = 0
                    end
                    repeat
                        wait()
                    until CharacterAlive == true

                    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = dummytarget.HumanoidRootPart.CFrame
                end
            end)
        end
    end)
end)


local savedpos
T1:Toggle("Dummy single fireball + hit",false,function(value)
    NewLoop = value
    
    timeSecondsDummy = 0
    local dummytarget = nil
    local success, error = pcall(function()
        if NewLoop then
            savedpos = Character.HumanoidRootPart.CFrame
            TrackingWebhookSeconds = 0
            timeSecondsDummy = 0
            local search
            local dummyLevel
            if game.Players.LocalPlayer.leaderstats.Level.Value > 5000 then
                dummyLevel = "Dummy2"
                search = game:GetService("Workspace").MAP.waterfall1
            else
                dummyLevel = "Training Dummy"
                search = game:GetService("Workspace").MAP.dummies
            end

            dummytarget = search:FindFirstChild(dummyLevel)

            Character.HumanoidRootPart.CFrame = dummytarget.HumanoidRootPart.CFrame + Vector3.new(3,0,0)
        else
            Character.HumanoidRootPart.CFrame = savedpos
        end


        task.spawn(function()

            local Delay = 0
            local runningFireball = false
            local waittime = 0.1
            while NewLoop do
                task.wait()


                game:GetService("ReplicatedStorage").jdskhfsIIIllliiIIIdchgdIiIIIlIlIli:FireServer(dummytarget.Humanoid, 1)



                task.spawn(function()
                    pcall(function()
                        if game.Players.LocalPlayer.Backpack:FindFirstChild("Fireball") then
                            game.Players.LocalPlayer.Backpack:FindFirstChild("Fireball").FireballEvent:FireServer(dummytarget.HumanoidRootPart.Position)
                        end

                        if game.Players.LocalPlayer.Character:FindFirstChild("Fireball") then
                            game.Players.LocalPlayer.Character:FindFirstChild("Fireball").FireballEvent:FireServer(dummytarget.HumanoidRootPart.Position)
                        end
                        fireballsTotal = 1
                    end)
                end)



                task.spawn(function()
                    if timeMinsDummy > 5 then
                        timeSecondsDummy = 0
                        if Character:FindFirstChild("Humanoid") then
                            Character.Humanoid.Health = 0
                        end
                        repeat
                            wait()
                        until CharacterAlive == true

                        game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = dummytarget.HumanoidRootPart.CFrame
                    end
                end)
            end
        end)
    end)
end)


local savedpos
T1:Toggle("Dummy all fireballs + hit - multitoggle",false,function(value)
    NewLoop = value
    
    timeSecondsDummy = 0
    local dummytarget = nil
    local success, error = pcall(function()
        if NewLoop then
            savedpos = Character.HumanoidRootPart.CFrame
            TrackingWebhookSeconds = 0
            timeSecondsDummy = 0
            local search
            local dummyLevel
            if game.Players.LocalPlayer.leaderstats.Level.Value > 5000 then
                dummyLevel = "Dummy2"
                search = game:GetService("Workspace").MAP.waterfall1
            else
                dummyLevel = "Training Dummy"
                search = game:GetService("Workspace").MAP.dummies
            end

            dummytarget = search:FindFirstChild(dummyLevel)

            Character.HumanoidRootPart.CFrame = dummytarget.HumanoidRootPart.CFrame + Vector3.new(3,0,0)
        else
            Character.HumanoidRootPart.CFrame = savedpos
        end


        task.spawn(function()

            local runningFireball = false
            while NewLoop do
                task.wait()

                game:GetService("ReplicatedStorage").jdskhfsIIIllliiIIIdchgdIiIIIlIlIli:FireServer(dummytarget.Humanoid, 1)


                local Fireballs = 0
                if runningFireball == false then
                    runningFireball = true
                    task.spawn(function()
                        a, b = pcall(function()

                            local Balls = {"Fireball", "Lightningball"}
                            local Locations = {"Backpack", "Character"}
                            for i, player in pairs(game.Players:GetChildren()) do
                                local earlyreturn = false
                                for _,Ball in pairs(Balls) do
                                    for i,Location in pairs(Locations) do
                                        local CheckBall = player[Location]:FindFirstChild(Ball)
                                        if CheckBall then
                                            Fireballs += 1
                                            CheckBall:FindFirstChild("FireballEvent"):FireServer(dummytarget.HumanoidRootPart.Position)
                                            earlyreturn = true
                                            wait()
                                            break
                                        end
                                    end

                                    if earlyreturn then
                                        break
                                    end
                                end
                            end

                            fireballsTotal = Fireballs
                            Fireballs = 0
                            runningFireball = false
                        end)
                        if b then
                            runningFireball = false
                        end
                    end)
                end


                task.spawn(function()
                    if timeMinsDummy > 5 then
                        timeSecondsDummy = 0
                        if Character:FindFirstChild("Humanoid") then
                            Character.Humanoid.Health = 0
                        end
                        repeat
                            wait()
                        until CharacterAlive == true

                        game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = dummytarget.HumanoidRootPart.CFrame
                    end
                end)
            end
        end)
    end)

    if error then
        print(error)
    end
end)



local savedpos
T1:Toggle("Coin gain",false,function(value)
    Coins = value
    
    while Coins do
        wait(.1)
        game:GetService("ReplicatedStorage").Events.CoinEvent:FireServer()

        if CharacterAlive and game.Players.LocalPlayer:FindFirstChild("otherstats").Coin.Value >= 500 then
            game:GetService("ReplicatedStorage").Events.unlockEvent:FireServer()
        end
    end
end)

-- [[ XEN SETTINGS ]]


local T2 = wndw:Tab("Name features")

--[[local Animation
Page_2:CreateToggle("ONI Text [Animation]", false, function(Value)
    if Value == true then
        Animation = true
    else
        Animation = false
    end

    Animate = {}
    loadstring(game:HttpGet("https://raw.githubusercontent.com/Xen101/Roblox/main/Animal%20Simulator/Animations/Animation%20Oni%20Logo.lua",true))()

    while Animation do
        wait()
            --Forward
        for i=1, #Animate, 1 do
            print(Animate)
            game:GetService("Players").LocalPlayer.PlayerGui.RolePlayName.Frame.bodyFrame.submitBtn.nameEvent:FireServer(Animate[i].Text)
            wait(0.5)
        end

        --Reverse
        for i= #Animate, 1, -1 do
            game:GetService("Players").LocalPlayer.PlayerGui.RolePlayName.Frame.bodyFrame.submitBtn.nameEvent:FireServer(Animate[i].Text)
            wait(0.5)
        end
    end
end)
]]

local Animation
T2:Toggle("TeaSip [ Animation ]",false,function(value)
    Animation = value
    loadstring(game:HttpGet("https://raw.githubusercontent.com/Xen101/Roblox/main/Animal%20Simulator/Animations/Animation%20Tea%20Sip.lua",true))()

    while Animation do
        wait()
        for i,v in pairs(Animate) do
            game:GetService("Players").LocalPlayer.PlayerGui.RolePlayName.Frame.bodyFrame.submitBtn.nameEvent:FireServer(v.Text)
            wait(0.3)
        end
        wait(0.5)
    end
end)

local Animation
T2:Toggle("Girl kiss [ Animation ]",false,function(value)
    Animation = value
    loadstring(game:HttpGet("https://raw.githubusercontent.com/Xen101/Roblox/main/Animal%20Simulator/Animations/Animation%20Kiss%20GIrl%202.lua",true))()

    while Animation do
        wait()
        for i,v in pairs(Animate) do
            game:GetService("Players").LocalPlayer.PlayerGui.RolePlayName.Frame.bodyFrame.submitBtn.nameEvent:FireServer(v.Text)
            wait(0.3)
        end
        wait(0.5)
    end
end)

local Animation
T2:Toggle("Nezuko run [ Animation ]",false,function(value)
    Animation = value
    loadstring(game:HttpGet("https://raw.githubusercontent.com/Xen101/Roblox/main/Animal%20Simulator/Animations/Animation%20Nezuko.lua",true))()

    while Animation do
        wait()
        for i,v in pairs(Animate) do
            game:GetService("Players").LocalPlayer.PlayerGui.RolePlayName.Frame.bodyFrame.submitBtn.nameEvent:FireServer(v.Text)
            wait(0.3)
        end
    end
end)


T2:Button("Bug everyone's HUD",function()
    local string = "####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################"
    local fullstring = ""
    for i = 1, 100 do
        fullstring = fullstring .. string
    end
    game:GetService("Players").LocalPlayer.PlayerGui.RolePlayName.Frame.bodyFrame.submitBtn.nameEvent:FireServer(fullstring)
end)

T2:Button("Cover the leaderboard with RAIDER",function()
    local string = "\r\n RAIDER"
    local fullstring = ""
    for i = 1, 75 do
        fullstring = fullstring .. string
    end
    game:GetService("Players").LocalPlayer.PlayerGui.RolePlayName.Frame.bodyFrame.submitBtn.nameEvent:FireServer(fullstring)
    
end)




local T3 = wndw:Tab("Misc features")



local Fireworks
T3:Toggle("Firework spam",false,function(value)
    Fireworks = value
    
    local windowFrame = game.Players.LocalPlayer.PlayerGui.ToolsGUI.windowFrame
    local toolsFrame = windowFrame.bodyFrame.body2Frame.toolsFrame
    local firework = toolsFrame.fireworks
    local fireworkFrame = firework.Frame



    if Fireworks then
        windowFrame.Visible = true
        for i,v in pairs(toolsFrame:GetChildren()) do
            if not v:IsA("Frame") then
                continue
            end
            if v.Name ~= "fireworks" then
                v.Visible = false
            end
        end
        
    else
        windowFrame.Visible = false
        for i,v in pairs(toolsFrame:GetChildren()) do
            if not v:IsA("Frame") then
                continue
            end

            if v.Name ~= "fireworks" then
                v.Visible = true
            end
        end
    end
    if Fireworks then
        while Fireworks do
            wait()

            pcall(function()
                game:GetService("VirtualInputManager"):SendMouseButtonEvent(fireworkFrame.AbsolutePosition.X+fireworkFrame.AbsoluteSize.X/2,fireworkFrame.AbsolutePosition.Y+50,0,true,fireworkFrame,1)
                game:GetService("VirtualInputManager"):SendMouseButtonEvent(fireworkFrame.AbsolutePosition.X+fireworkFrame.AbsoluteSize.X/2,fireworkFrame.AbsolutePosition.Y+50,0,false,fireworkFrame,1)
                task.wait()
                game.Players.LocalPlayer.Character.Humanoid:EquipTool(Player.Backpack:WaitForChild("Fireworks"))
                wait()
                game.Players.LocalPlayer.Character.Fireworks:Activate()
                task.wait()
                game:GetService("VirtualInputManager"):SendMouseButtonEvent(fireworkFrame.AbsolutePosition.X+fireworkFrame.AbsoluteSize.X/2,fireworkFrame.AbsolutePosition.Y+50,0,true,fireworkFrame,1)
                game:GetService("VirtualInputManager"):SendMouseButtonEvent(fireworkFrame.AbsolutePosition.X+fireworkFrame.AbsoluteSize.X/2,fireworkFrame.AbsolutePosition.Y+50,0,false,fireworkFrame,1)
            end)

        end
    end
end)


local MEgg = 0
local WorkspaceSound
local EGGWorkspaceSound
T3:Toggle("Mute all annoying audio",false,function(value)
    Mute = value
    
    --Yes this could be rewritten to be more effective, am just too lazy to do so.

    if not Mute then
        for i, connection in pairs(getconnections(workspace.DescendantAdded)) do
            connection:Disable()
        end
    end

    if Mute then
        MEgg += 1
        warn(MEgg)
    end

    pcall(function()
        if game.ReplicatedStorage:FindFirstChild("Soundtracks") then
            game.ReplicatedStorage:FindFirstChild("Soundtracks"):Destroy()
        end
    end)

    if Mute and MEgg == 5 then
        game.Workspace.DescendantAdded:connect(function(child)
            if child:IsA("Sound") then
                child.Pitch = 0.2
            end
        end)
    end

    if Mute and MEgg ~= 5 then
        game.Workspace.DescendantAdded:connect(function(child)
            if child:IsA("Sound") then
                child.Playing = false
                child.Volume = 0
            end
        end)
    end



    while Mute do
        local success, error = pcall(function()
            for i,v in pairs(game.Players:GetPlayers()) do
                ----print(i,v)
                if v.Name ~= game.Players.LocalPlayer.Name and v.Character and v.Character:FindFirstChild("HumanoidRootPart") and v.Character.HumanoidRootPart:FindFirstChild("Sound") then
                ----print(i,v)
                    v.Character.HumanoidRootPart:FindFirstChild("Sound").Volume = 0
                end
            end

            game:GetService("SoundService"):FindFirstChild("BGMusic").Volume = 0
            game:GetService("Players").LocalPlayer.PlayerScripts:FindFirstChild("coinSpawner").Sound.Volume = 0
        end)

        if not success then
            --warn(error)
        end

        wait(1)
    end

    local success, error = pcall(function()
        for i,v in pairs(game.Players:GetPlayers()) do
            if v.Name ~= game.Players.LocalPlayer.Name and v.Character and v.Character:FindFirstChild("HumanoidRootPart") and v.Character.HumanoidRootPart:FindFirstChild("Sound") then
                v.Character.HumanoidRootPart:FindFirstChild("Sound").Volume = 1.3
            end
        end
        game:GetService("SoundService"):FindFirstChild("BGMusic").Volume = 1
        game.GetService("Players").LocalPlayer:FindFirstChild("coinSpawner").Sound.Volume = 0.1
    end)
end)

T3:Toggle("Grab lighting",false,function(value)
    Light = value
    pcall(function()
        --print(Lightn)
        if Light then
            for i,v in pairs(game.Workspace.MAP.waterfall1.cave:GetChildren()) do
                if v.Name == "Model" then
                    for i,v in pairs(v:GetChildren()) do
                        if v.Name == "rock" then
                            v.CanCollide = false
                        end
                    end
                end
            end

            getgenv().Lightning = game.Players.LocalPlayer.CharacterAdded:Connect(function(newCharacter)
                wait(2)
                local savedpos = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame
                local Camera = game.Workspace.CurrentCamera
                Camera.CameraType = Enum.CameraType.Scriptable
                Camera.CFrame = game.Workspace.PickFolder.rock.CFrame * CFrame.new(0,2,10)
                Camera.CFrame = CFrame.lookAt(Camera.CFrame.p, game.Workspace.PickFolder.rock.Position)

                game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame * CFrame.new(0,-60,0)
                wait(.1)
                game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = game.Workspace.PickFolder.rock.CFrame * CFrame.new(0,-60,0)
                wait(.1)
                game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = game.Workspace.PickFolder.rock.CFrame * CFrame.new(0,0-11.5,0)
                task.wait()
                repeat
                wait(.3)
                game:GetService('VirtualInputManager'):SendKeyEvent(true, "E", false, game)
                until game.Players.LocalPlayer.Character:FindFirstChild("Lightningball") or game.Players.LocalPlayer.Backpack:FindFirstChild("Lightningball") or a

                wait()
                game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame * CFrame.new(0,-60,0)
                wait(.1)
                game.Workspace.CurrentCamera.CameraType = Enum.CameraType.Custom
                game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = savedpos
            end)
        else
            getgenv().Lightning:Disconnect()
        end
    end)
end)

T3:Toggle("Character reset - Avatar editor",false,function(value)
    CharacterReset = value
    
    if not CharacterReset then
        return
    end

    game:GetService("ReplicatedStorage").AvatarEditor.RemoteEvent:FireServer("reset")


    game.Players.LocalPlayer.CharacterAdded:Connect(function(newCharacter)
        wait(1)
        game:GetService("ReplicatedStorage").AvatarEditor.RemoteEvent:FireServer("reset")
        wait(1)
        game:GetService("ReplicatedStorage").AvatarEditor.RemoteEvent:FireServer("reset")
    end)
end)


local Connection
function InviteConnection(GUI)
    Connection = GUI:GetPropertyChangedSignal("Enabled"):Connect(function(state)
        --print("changed", state)
        GUI.Enabled = false
    end)
end

function GetInviteConnection()
    return Connection
end

T3:Toggle("Ride invite GUI",false,function(value)
    InviteDisabled = value
    
    local GUI = game:GetService("Players").LocalPlayer.PlayerGui.Ride.RideInviteGUI

    if InviteDisabled then
        InviteConnection(GUI)
    end

    if not InviteDisabled then
        GetInviteConnection():Disconnect()
        GUI.Enabled = false
    end
end)




--[[Page_3:CreateToggle("Anti-Fling", false, function(Value)
    if Value == true then
        InviteDisabled = true
    else
        InviteDisabled = false
    end

    local GUI = game:GetService("Players").LocalPlayer.PlayerGui.Ride.RideInviteGUI

    if InviteDisabled then
        getgenv().AntiFlingConfig = {
            disable_rotation = true;

            limit_velocity = true;
            limit_velocity_sensitivity = 150; 
            limit_velocity_slow = 0;

            anti_ragdoll = true;

            anchor = false;
            smart_anchor = true; 
            anchor_dist = 30;

            teleport = false;
            smart_teleport = true;
            teleport_dist = 30;
        }
        loadstring(game:HttpGet('https://raw.githubusercontent.com/topitbopit/rblx/main/extra/better_antifling.lua'))()
    end

    if not InviteDisabled then
        getgenv().disable()
    end
end)
]]




T1:Toggle("Auto eat",false,function(value)
    Tog = value
    
    while Tog do
        local success, error = pcall(function()
            if Character.Humanoid.Health >= Character.Humanoid.MaxHealth then
                repeat
                    ----print("Waiting")
                    wait(.1)
                until Character.Humanoid.Health < Character.Humanoid.MaxHealth

                break
            end
        end)
        if not success then
            --warn(error)
        end

        if Character:FindFirstChild("Food") ~= false and game.Players.LocalPlayer.Backpack:FindFirstChild("Food") then
            Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Food"))
        end

        wait()

        if Character:FindFirstChild("Food") then
            Character:FindFirstChild("Food"):Activate()
            wait()
            Character:FindFirstChild("Humanoid"):UnequipTools()
        end
    end
end)


-- [[ UI Section FPS ]] --
local T4 = wndw:Tab("UI Section")

T4:Button("FPS + Ping counter",function()
    loadstring(game:HttpGet('https://raw.githubusercontent.com/1201for/littlegui/main/FPS-Counter'))()
end)

T4:Toggle("Render Toggle",false,function(value)
    game:GetService("RunService"):Set3dRenderingEnabled(value)
end)


local function getDir(v)
	return (
		((v.Y == 0) and Vector3.new()) or
		((v.Y > 0) and -v) or
		v
	)
end

local function computeLowestPoint(part)
	local cf = part.CFrame
	local dist = part.Size/2
	local xVec = getDir(cf.RightVector) * dist.X
	local yVec = getDir(cf.UpVector) * dist.Y
	local zVec = getDir(cf.LookVector) * dist.Z
	return (cf + xVec + yVec + zVec).p
end

local folder = Instance.new("Folder")
folder.Name = "Platforms"
folder.Parent = workspace


function createBaseplate(Part, Size, Offset)
    local baseplate = Instance.new("Part")
    baseplate.Name = "Platform"
    baseplate.Anchored = true
    baseplate.Size = Vector3.new(Size, 0.5, Size)
    baseplate.TopSurface = "Smooth"
    baseplate.BottomSurface = "Smooth"
    baseplate.Material = "Glass"
    baseplate.Transparency = 0.75

    baseplate.CFrame = CFrame.new(computeLowestPoint(Part)) * Offset

    baseplate.Parent = folder
end

T4:Button("Delete map V2",function()

    local success, error = pcall(function()
        local keepListDirect = {
            game:GetService("Workspace").Camera,
            game:GetService("Players").LocalPlayer.Character,
            game:GetService("Workspace").LBFolder,
            game:GetService("Workspace").SpawnPoints
        }


        local keepListName = {
            "Terrain",
            "Platform"
        }

        local listSearch = {
            "Dummy2",
            "Training Dummy",
            "spawnPoint",
        }


        local SpawnList = game:GetService("Workspace"):FindFirstChild("SpawnPoints")
        local SpawnLocation = game:GetService("Workspace"):FindFirstChild("SpawnLocation")
        local Dummy0kList = game:GetService("Workspace"):FindFirstChild("MAP"):FindFirstChild("dummies")
        local Dummy5kList = game:GetService("Workspace"):FindFirstChild("MAP"):FindFirstChild("waterfall1")

        local addTable = {SpawnList, Dummy0kList, Dummy5kList}


        for _,Players in pairs(game.Players:GetPlayers()) do
            table.insert(keepListDirect, Players.Character)
        end



        local Part
        for _,List in pairs(addTable) do
            for i,v in pairs(List:GetChildren()) do
                if not table.find(listSearch, v.Name) then
                    continue
                end


                if v:FindFirstChild("HumanoidRootPart") then
                    table.insert(keepListDirect, v)
                    Part = v:FindFirstChild("HumanoidRootPart")
                elseif v:IsA("Part") then
                    table.insert(keepListDirect, v)
                    Part = v
                else
                    --print("Something went wrong -- [Map Delete]")
                    continue
                end

                print(List.Name, Part)
                if List.Name == "SpawnPoints" then
                    print("HERE", List, Part)
                    createBaseplate(Part, 20, CFrame.new(0,-5.655,0))
                    -- NORMAL == (-89)
                    -- -10 == (-84)
                else
                    --print(List)
                    createBaseplate(Part, 20, CFrame.new(0,0,0))
                end

            end
            game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = SpawnList:FindFirstChild("spawnPoint").CFrame * CFrame.new(0,3,0)
        end

        for i,v in pairs(keepListDirect) do
            --print(v)
            if not table.find(keepListName, v.Name) then
                table.insert(keepListName, v.Name)
            end
        end




        for _, object in pairs(game.Workspace:GetDescendants()) do

            if object:IsA("Folder") then
                continue
            end

            if table.find(keepListName, object.Name) then
                continue
            end

            local skip = false
            for i,v in pairs(keepListDirect) do
                if object:IsDescendantOf(v) then
                    --[[if v.Name == "Dummy2" or v.Name == "Training Dummy" then
                        if object.Name == "HumanoidRootPart" or object.Name == "Humanoid" then
                            ----print("IN: ",object.Name)
                            skip = true
                            continue
                        else
                            object:Destroy()
                        end
                   end

                    if v.Name == game:GetService("Players").LocalPlayer.Name then
                        if object:IsA("Accessory") then
                            object:Destroy()
                        end
                        pcall(function()
                            object.Transparency = 1
                        end)
                    end]]

                   skip = true
                end
            end

            if skip == true then
                continue
            end
            object:Destroy()
        end
    end)

    if not success then
        --print(success, error)
    end
end)

-- [[ UI Section Misc ]]
local T5 = wndw:Tab("Pack settings")


T5:Button("Create IND pack",function()
    game:GetService("Players").LocalPlayer.PlayerGui.TeamGUI.createFrame.bodyFrame.createButton.createTeamEvent:FireServer('🇮🇩')
end)

T5:Button("Create Raider pack",function()
    game:GetService("Players").LocalPlayer.PlayerGui.TeamGUI.createFrame.bodyFrame.createButton.createTeamEvent:FireServer('RAIDER')
end)

local Invitedelay = 0.3
T5:Toggle("Spam invite",false,function(value)
    Spam = value
    

    local Player = game.Players.LocalPlayer
    local TeamGUI = Player.PlayerGui.TeamGUI
    local playersFrame = TeamGUI.playersFrame
    local clanFrame = TeamGUI.clanFrame
    local playerInfo = playersFrame.bodyFrame


    if Spam == false then
        warn("Spam Off")
        Value = false

        playerInfo.Position = UDim2.new(0, 0, 0, 0)
        TeamGUI.Enabled = false
        clanFrame.Visible = true
        playersFrame.Visible = false
        playerInfo.Visible = false
    end

    leader = false
    for i,v in pairs(game.Workspace.Teams:GetChildren()) do
        if v.leader.Value == Player.Name then
            leader = true
        end
    end

    if leader and Spam then
        warn("Enabled GUI")

        TeamGUI.Enabled = true
        clanFrame.Visible = false
        playersFrame.Visible = true
        playerInfo.Visible = true
    else
        print("Spam is off or you are not leader")
        Value = false
        return
    end

    local function click(a)
        game:GetService("VirtualInputManager"):SendMouseButtonEvent(a.AbsolutePosition.X+a.AbsoluteSize.X/2,a.AbsolutePosition.Y+50,0,true,a,1)
        game:GetService("VirtualInputManager"):SendMouseButtonEvent(a.AbsolutePosition.X+a.AbsoluteSize.X/2,a.AbsolutePosition.Y+50,0,false,a,1)
    end

    a = 0
    --playerInfo.Position = UDim2.new(1, 0, 0, 0)


    print("HERE")
    while Spam do
        if not Character and not Character:FindFirstChild("HumanoidRootPart") then
            break
        end
        print("HERE", a)
        wait()

        a += 1

         --print(a)

        for i,v in pairs(playerInfo.body2Frame.scrollingFrame:GetChildren()) do
            if v.Name == "playerFrame" then
                if v:FindFirstChild("invite") then
                    click(v.invite)

                    wait(Invitedelay)

                    v:Destroy()
                end

            end
        end

        wait()

        click(playerInfo.refreshButton)

        wait(.3)
    end
end)
end)
if not isrunning then
	lib:notify(lib:ColorFonts(error,"Red"),10)
end
