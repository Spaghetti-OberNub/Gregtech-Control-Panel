local event = require("event")
local component = require("component")

local gpu = component.gpu

local function write_to_file(name, input)
    local file = io.open(name, "w")
    if file then
        file:write(input)
        file:write("\n")
        file:close()
    else
        error("Failed to open file: " .. tostring(name))
    end
end

local function dump(o)
    if type(o) == 'table' then
        local s = '{ '
        for k, v in pairs(o) do
            if type(k) ~= 'number' then k = '"' .. k .. '"' end
            s = s .. '[' .. k .. '] = ' .. dump(v) .. ',\n'
        end
        return s .. '}'
    else
        return tostring(o)
    end
end

local function writePowerInformation()
    local sensorInfo = Supercapacitor.getSensorInformation()
    local sensor_string = ""

    for i = 1, #sensorInfo do
        sensor_string = sensor_string .. sensorInfo[i] .. "\n"
    end

    write_to_file("outputs/energy_sample.txt", sensor_string)
end

local function get_samples()
    for address, ctype in component.list() do
        if ctype == "gt_machine" then
            local machine = component.proxy(address)
            if machine.getName() == "multimachine.supercapacitor" then
                Supercapacitor = machine
            end
        elseif ctype == "reactor" then
            local reactor = component.proxy(address)

            for x = 0, 2 do
                for y = 0, 2 do
                    local slotInfo = reactor.getSlotInfo(x, y)
                    if slotInfo == nil then
                        return
                    end
                end
            end

            local reactor_string =
                tostring(reactor.producesEnergy()) .. "\n" ..
                reactor.getSlotInfo(0, 0)["item"]["label"] .. "\n" ..
                100 - reactor.getSlotInfo(0, 0)["item"]["damage"] .. "\n" ..
                100 - reactor.getSlotInfo(0, 1)["item"]["damage"] .. "\n" ..
                100 - reactor.getSlotInfo(0, 2)["item"]["damage"] .. "\n" ..
                100 - reactor.getSlotInfo(1, 0)["item"]["damage"] .. "\n" ..
                100 - reactor.getSlotInfo(1, 1)["item"]["damage"] .. "\n" ..
                100 - reactor.getSlotInfo(1, 2)["item"]["damage"] .. "\n" ..
                100 - reactor.getSlotInfo(2, 0)["item"]["damage"] .. "\n" ..
                100 - reactor.getSlotInfo(2, 1)["item"]["damage"] .. "\n"

            write_to_file("outputs/reactor_sample.txt", reactor_string)
        end
    end
end


while true do
    get_samples()
    writePowerInformation()
    os.sleep(0.25)
end
