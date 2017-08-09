-- see if the file exists
function file_exists(file)
  local f = io.open(file, "rb")
  if f then f:close() end
  return f ~= nil
end

-- get all lines from a file, returns an empty 
-- list/table if the file does not exist
function lines_from(file)
  if not file_exists(file) then return {} end
  lines = {}
  for line in io.lines(file) do 
    lines[#lines + 1] = line
  end
  return lines
end

-- tests the functions above
local file = 'A-small-attempt0.in'
local lines = lines_from(file)

-- print all line numbers and their contents
-- for k,v in pairs(lines) do
--   print('line[' .. k .. ']', v)
-- end

getmetatable('').__index = function(str,i) return string.sub(str,i,i) end
local flip = function(str,i,k)
	local r = string.sub(str,1,i-1)
	for j = i,i+k-1 do
		if str[j] == '+' then r = r..'-' else r = r..'+' end
	end
	r = r..string.sub(str,i+k)
	return r
end

local T = lines[1]
-- print('T',T)

for ln = 2,T+1 do
	local S, K = string.match(lines[ln], "([^%s]*) (%d)")
	print(S,K)
	-- print('K',K)

	local outer_count = 0
	local P = #S - K + 1

	if P > 1 then
		repeat
			local inner_count = 0
			for i = 1,P do
				-- print(i)
				left, right = false, false
				if i == 1 then
					left = true
				else
					-- print(S[i-1],S[i],S[i-1] ~= S[i])
					left = S[i-1] ~= S[i]
				end
				if i == P then
					right = true
				else
					right = S[i+K-1] ~= S[i+K]
				end
				if left and right then
					S = flip(S,i,K)
					outer_count = outer_count + 1
					inner_count = inner_count + 1
					print(S)
				end
			end
		until inner_count == 0
	end

	pluses = 0
	for _ in string.gfind(S,"+") do
		pluses = pluses + 1
	end
	minuses = 0
	for _ in string.gfind(S,"-") do
		minuses = minuses + 1
	end

	if pluses == #S or minuses == #S then
		print('Case #'..(ln-1)..' '..outer_count)
	else
		print('Case #'..(ln-1)..' IMPOSSIBLE')
	end
end
